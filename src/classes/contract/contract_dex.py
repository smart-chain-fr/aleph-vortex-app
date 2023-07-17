from classes.operations import ContractOperation
from utils.tzkt import getContractStorage, getContractOperationCount, getContractOperations


class ContractDex:
    storage_table_name = "contract_dex_storage"
    operations_table_name = "contract_dex_operations"

    def __init__(self, history, manager, reserve, xtzPool, lqtTotal, tokenPool, lqtAddress, freezeBaker, tokenAddress, user_investments, selfIsUpdatingTokenPool):
        self.history = history
        self.manager = manager
        self.reserve = reserve
        self.xtzPool = xtzPool
        self.lqtTotal = lqtTotal
        self.tokenPool = tokenPool
        self.lqtAddress = lqtAddress
        self.freezeBaker = freezeBaker
        self.tokenAddress = tokenAddress
        self.user_investments = user_investments
        self.selfIsUpdatingTokenPool = selfIsUpdatingTokenPool

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    async def insert_into_db(cls, connection, table_name=storage_table_name):
        query = '''
            INSERT INTO ''' + table_name + ''' (
                history, manager, reserve, xtzpool, lqttotal,
                tokenpool, lqtaddress, freezebaker, tokenaddress,
                user_investments, selfisupdatingtokenpool
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        '''

        cursor = connection.cursor()
        cursor.execute(query, (
            cls.history, cls.manager, cls.reserve, cls.xtzPool, cls.lqtTotal,
            cls.tokenPool, cls.lqtAddress, cls.freezeBaker, cls.tokenAddress,
            cls.user_investments, cls.selfIsUpdatingTokenPool
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
        contractStorage = ContractDex(**storageResponse)
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