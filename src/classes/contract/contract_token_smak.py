from classes.operations import ContractOperation
from utils.tzkt import getContractStorage, getContractOperationCount, getContractOperations


class ContractTokenSmak:
    storage_table_name = "contract_token_smak_storage"
    operations_table_name = "contract_token_smak_operations"

    def __init__(self, freezer, balances, metadata, totalSupply, administrator, token_metadata, frozen_accounts):
        self.freezer = freezer
        self.balances = balances
        self.metadata = metadata
        self.totalSupply = totalSupply
        self.administrator = administrator
        self.token_metadata = token_metadata
        self.frozen_accounts = frozen_accounts

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    async def insert_into_db(cls, connection, table_name=storage_table_name):
        query = '''
            INSERT INTO ''' + table_name + ''' (
                freezer, balances, metadata, totalSupply, administrator, token_metadata, frozen_accounts
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s
            ) RETURNING id
        '''

        cursor = connection.cursor()
        cursor.execute(query, (
            cls.freezer, cls.balances, cls.metadata, cls.totalSupply, cls.administrator, cls.token_metadata, cls.frozen_accounts
        ))
        # print("[ContractStorage] inserted_id : ", cursor.fetchone()[0])
        connection.commit()
        cursor.close()

    def printObject(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} :', value)

    @staticmethod
    async def processContract(rpcEndpoint, dbConnection, contractAddress, table_name=operations_table_name):
        ## Get storage of contract
        storageResponse = await getContractStorage(rpcEndpoint, contractAddress)
        contractStorage = ContractTokenSmak(**storageResponse)
        try:
            await contractStorage.insert_into_db(dbConnection)
        except Exception as e:
            dbConnection.rollback()
            raise Exception(
                f"[contractStorage.insert_into_db ]Error inserting contract into DB : {e}")

        ## Get operations of contract
        operationCount = await getContractOperationCount(rpcEndpoint, contractAddress)
        print(f"[getContractOperations] Operation count : {operationCount}")
        for i in range(0, operationCount + 1, 1000):
            start = i
            ## Ensure the end value does not exceed N
            end = min(i + 999, operationCount)
            print(f"[getContractOperations] Range : {start} --> {end}")

            try:
                operationsResponse = await getContractOperations(
                    rpcEndpoint, contractAddress, i)
                if operationsResponse is None:
                    continue
            except (Exception, ValueError) as e:
                raise Exception("Exception occurred: " + str(e))

            for operationData in operationsResponse:
                try:
                    contractOperations = ContractOperation.from_dict(
                        operationData)
                except (KeyError, TypeError) as e:
                    raise Exception('Could not parse operation data: {}'.format(e))
                except Exception as e:
                    # contractOperations.printObject()
                    raise Exception('Something went wrong: {}'.format(e))
                try:
                    await contractOperations.insert_into_db(dbConnection, table_name)
                except Exception as e:
                    dbConnection.rollback()
                    raise Exception(
                        f"[contractOperations.insert_into_db ]Error inserting contract into DB : {e}")