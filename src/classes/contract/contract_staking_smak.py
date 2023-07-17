from classes.operations import ContractOperation
from utils.tzkt import getContractStorage, getContractOperationCount, getContractOperations


class ContractStakingSmak:
    storage_table_name = "contract_staking_smak_storage"
    operations_table_name = "contract_staking_smak_operations"

    def __init__(self, admin, reserve, metadata, addressId, maxValuesNb, stakingHistory, stakingOptions, votingContract, can_set_storage, numberOfStakers, redeemedRewards, stakeFlexLength, FA12TokenContract, userStakeFlexPack, userStakeLockPack, totalRedeemedRewards):
        self.admin = admin
        self.reserve = reserve
        self.metadata = metadata
        self.addressId = addressId
        self.maxValuesNb = maxValuesNb
        self.stakingHistory = stakingHistory
        self.stakingOptions = stakingOptions
        self.votingContract = votingContract
        self.can_set_storage = can_set_storage
        self.numberOfStakers = numberOfStakers
        self.redeemedRewards = redeemedRewards
        self.stakeFlexLength = stakeFlexLength
        self.FA12TokenContract = FA12TokenContract
        self.userStakeFlexPack = userStakeFlexPack
        self.userStakeLockPack = userStakeLockPack
        self.totalRedeemedRewards = totalRedeemedRewards

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    async def insert_into_db(cls, connection, table_name=storage_table_name):
        query = '''
            INSERT INTO ''' + table_name + ''' (
                admin, reserve, metadata, addressId, maxValuesNb, stakingHistory, votingContract, can_set_storage, numberOfStakers, redeemedRewards, stakeFlexLength, FA12TokenContract, userStakeFlexPack, userStakeLockPack, totalRedeemedRewards
            ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s
            ) RETURNING id;
        '''
        cursor = connection.cursor()
        cursor.execute(query, (
            cls.admin, cls.reserve, cls.metadata, cls.addressId, cls.maxValuesNb, cls.stakingHistory, cls.votingContract, cls.can_set_storage, cls.numberOfStakers, cls.redeemedRewards, cls.stakeFlexLength, cls.FA12TokenContract, cls.userStakeFlexPack, cls.userStakeLockPack, cls.totalRedeemedRewards
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
        contractStorage = ContractStakingSmak(**storageResponse)
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