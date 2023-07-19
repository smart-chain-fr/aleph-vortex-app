from datetime import datetime
from src.utils.tzkt import getIndexerStats

class Indexer:
    def __init__(self, timestamp, level, totalSupply, circulatingSupply, totalBootstrapped, totalCommitments, totalActivated, totalCreated, totalBurned, totalBanished, totalFrozen, totalRollupBonds, totalSmartRollupBonds, totalVested):
        self.timestamp = timestamp
        self.level = level
        self.totalSupply = totalSupply
        self.circulatingSupply = circulatingSupply
        self.totalBootstrapped = totalBootstrapped
        self.totalCommitments = totalCommitments
        self.totalActivated = totalActivated
        self.totalCreated = totalCreated
        self.totalBurned = totalBurned
        self.totalBanished = totalBanished
        self.totalFrozen = totalFrozen
        self.totalRollupBonds = totalRollupBonds
        self.totalSmartRollupBonds = totalSmartRollupBonds
        self.totalVested = totalVested

    @classmethod
    def from_dict(self, data) :
        return self(**data)

    # @staticmethod
    # def createTable(connection):
    #     query = '''
    #         CREATE TABLE IF NOT EXISTS indexer (
    #             level INTEGER,
    #             totalSupply INTEGER,
    #             circulatingSupply INTEGER,
    #             totalBootstrapped INTEGER,
    #             totalCommitments INTEGER,
    #             totalActivated INTEGER,
    #             totalCreated INTEGER,
    #             totalBurned INTEGER,
    #             totalBanished INTEGER,
    #             totalFrozen INTEGER,
    #             totalRollupBonds INTEGER,
    #             totalSmartRollupBonds INTEGER,
    #             totalVested INTEGER,
    #             CONSTRAINT indexer_pkey PRIMARY KEY (timestamp)
    #         );
    #     '''
    #     cursor = connection.cursor()
    #     cursor.execute(query)
    #     connection.commit()
    #     cursor.close()

    async def insert_into_db(self, connection):
        query = '''
            INSERT INTO indexer (
                timestamp,
                level,
                totalSupply,
                circulatingSupply,
                totalBootstrapped,
                totalCommitments,
                totalActivated,
                totalCreated,
                totalBurned,
                totalBanished,
                totalFrozen,
                totalRollupBonds,
                totalSmartRollupBonds,
                totalVested
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        '''

        cursor = connection.cursor()
        cursor.execute(query, (self.timestamp,
                               self.level,
                               self.totalSupply,
                               self.circulatingSupply,
                               self.totalBootstrapped,
                               self.totalCommitments,
                               self.totalActivated,
                               self.totalCreated,
                               self.totalBurned,
                               self.totalBanished,
                               self.totalFrozen,
                               self.totalRollupBonds,
                               self.totalSmartRollupBonds,
                               self.totalVested))
        # print("[Indexer] inserted_id : ", cursor.fetchone()[0])
        connection.commit()
        cursor.close()

    def printObject(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} :', value)

    @staticmethod
    async def processIndexer(rpcEndpoint, dbConnection):
        indexerStats = await getIndexerStats(rpcEndpoint)
        indexerStats = Indexer.from_dict(indexerStats)
        indexerStats.timestamp = datetime.fromisoformat(indexerStats.timestamp)
        await indexerStats.insert_into_db(dbConnection)