import json

class ContractOperation:
    def __init__(self, type, id, level, timestamp, block, hash, counter, sender,
                 gasLimit, gasUsed, storageLimit, storageUsed, bakerFee, storageFee,
                 allocationFee, target, amount, status, hasInternals,
                 initiator = None, nonce = None, parameter = None, senderCodeHash = None, targetCodeHash = None, tokenTransfersCount = None, errors = None, eventsCount = None):
        self.type = type
        self.id = id
        self.level = level
        self.timestamp = timestamp
        self.block = block
        self.hash = hash
        self.counter = counter
        self.sender = json.dumps(sender)
        self.gasLimit = gasLimit
        self.gasUsed = gasUsed
        self.storageLimit = storageLimit
        self.storageUsed = storageUsed
        self.bakerFee = bakerFee
        self.storageFee = storageFee
        self.allocationFee = allocationFee
        self.target = json.dumps(target)
        self.amount = amount
        self.status = status
        self.hasInternals = hasInternals
        self.initiator =  getattr(self, 'initiator', None)
        self.nonce = getattr(self, 'nonce', None)
        self.parameter = getattr(self, 'parameter', None)
        self.senderCodeHash = getattr(self, 'senderCodeHash', None)
        self.targetCodeHash = getattr(self, 'targetCodeHash', None)
        self.tokenTransfersCount = getattr(self, 'tokenTransfersCount', None)
        self.errors = getattr(self, 'errors', None)
        self.eventsCount = getattr(self, 'eventsCount', None)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    async def insert_into_db(cls, connection, table_name):
        query = '''
            INSERT INTO '''+ table_name +''' (
                type, level, timestamp, block, hash, counter, sender,
                gasLimit, gasUsed, storageLimit, storageUsed, bakerFee, storageFee,
                allocationFee, target, amount, status, hasInternals, initiator,
                nonce, parameter, senderCodeHash, targetCodeHash, tokenTransfersCount,
                errors, eventsCount
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        '''

        cursor = connection.cursor()
        cursor.execute(query, (
            cls.type, cls.level, cls.timestamp, cls.block, cls.hash,
            cls.counter, cls.sender, cls.gasLimit, cls.gasUsed,
            cls.storageLimit, cls.storageUsed, cls.bakerFee, cls.storageFee,
            cls.allocationFee, cls.target, cls.amount, cls.status,
            cls.hasInternals, cls.initiator, cls.nonce, cls.parameter,
            cls.senderCodeHash, cls.targetCodeHash, cls.tokenTransfersCount,
            cls.errors, cls.eventsCount
        ))
        # print("[ContractOperation] inserted_id : ", cursor.fetchone()[0])
        connection.commit()
        cursor.close()

    def printObject(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} :', value)
