from src.classes.operations import ContractOperation
from src.utils.tzkt import getContractStorage, getContractOperationCount, getContractOperations


class ContractFactoryDoga:
    storage_table_name = "contract_factory_doga_storage"
    operations_table_name = "contract_factory_doga_operations"

    def __init__(self, swaps, counter, empty_tokens, empty_history, token_to_swaps, default_reserve, default_metadata, empty_allowances, default_token_metadata, empty_user_investments):
        self.swaps = swaps
        self.counter = counter
        self.empty_tokens = empty_tokens
        self.empty_history = empty_history
        self.token_to_swaps = token_to_swaps
        self.default_reserve = default_reserve
        self.default_metadata = default_metadata
        self.empty_allowances = empty_allowances
        self.default_token_metadata = default_token_metadata
        self.empty_user_investments = empty_user_investments

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    async def insert_into_db(cls, connection, table_name=storage_table_name):
        query = '''
            INSERT INTO ''' + table_name + ''' (
                swaps, counter, empty_tokens, empty_history, token_to_swaps, default_reserve, default_metadata, empty_allowances, default_token_metadata, empty_user_investments
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            RETURNING id;
        '''

        cursor = connection.cursor()
        cursor.execute(query, (
            cls.swaps, cls.counter, cls.empty_tokens, cls.empty_history, cls.token_to_swaps, cls.default_reserve, cls.default_metadata, cls.empty_allowances, cls.default_token_metadata, cls.empty_user_investments
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
        contractStorage = ContractFactoryDoga(**storageResponse)
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