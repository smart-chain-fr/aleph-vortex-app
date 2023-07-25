import asyncio
from src.utils.env import initEnvRpc, initEnvDatabase, initEnvContracts
from src.utils.database import connectDatabase, disconnectDatabase, initDatabase
from src.utils.graphql import startGraphqlServer
from src.classes.indexer import Indexer
from src.classes.contract.contract_dex import ContractDex
from src.classes.contract.contract_token_smak import ContractTokenSmak
from src.classes.contract.contract_token_anti import ContractTokenAnti
from src.classes.contract.contract_factory_fa12 import ContractFactoryFA12
from src.classes.contract.contract_factory_fa2 import ContractFactoryFA2
from src.classes.contract.contract_factory_doga import ContractFactoryDoga
from src.classes.contract.contract_staking_smak import ContractStakingSmak
from src.classes.contract.contract_farms_v1 import ContractFarmsV1
from src.classes.contract.contract_farms_v2 import ContractFarmsV2

async def main() :
    print("Starting the app...")

    # Specify the Tezos node RPC endpoint
    rpcEndpoint : str = initEnvRpc()

    # Specify the contract addresses
    contractsAddr : dict = initEnvContracts()

    # Specify the database connection details
    db_info : dict = initEnvDatabase()

    # Connect to the database
    dbConnection = connectDatabase(db_info["host"][0], db_info["port"][0], db_info["database"][0], db_info["user"][0], db_info["password"])

    # Initialize the database
    initDatabase(dbConnection)

    # Insert Indexer state into the database
    await Indexer.processIndexer(rpcEndpoint, dbConnection)
    print("[Indexer.processIndexer] Indexer state inserted into the database")

    # Get DEX contract storage and operations
    await ContractDex.processContract(rpcEndpoint, dbConnection, contractsAddr["VORTEX"])
    print("[ContractDex.processContract] DEX contract storage and operations inserted into the database")

    # Get SMAK TOKEN contract storage and operations
    await ContractTokenSmak.processContract(rpcEndpoint, dbConnection, contractsAddr["TOKEN_SMAK"])
    print("[ContractTokenSmak.processContract] SMAK TOKEN contract storage and operations inserted into the database")

    # Get ANTI TOKEN contract storage and operations
    await ContractTokenAnti.processContract(rpcEndpoint, dbConnection, contractsAddr["TOKEN_ANTI"])
    print("[ContractTokenAnti.processContract] ANTI TOKEN contract storage and operations inserted into the database")

    # Get FA12 FACTORY contract storage and operations
    await ContractFactoryFA12.processContract(rpcEndpoint, dbConnection, contractsAddr["FACTORY_FA12"])
    print("[ContractFactoryFA12.processContract] FA12 FACTORY contract storage and operations inserted into the database")

    # Get FA2 FACTORY contract storage and operations
    await ContractFactoryFA2.processContract(rpcEndpoint, dbConnection, contractsAddr["FACTORY_FA2"])
    print("[ContractFactoryFA2.processContract] FA2 FACTORY contract storage and operations inserted into the database")

    # Get DOGA FACTORY contract storage and operations
    await ContractFactoryDoga.processContract(rpcEndpoint, dbConnection, contractsAddr["FACTORY_DOGA"])
    print("[ContractFactoryDoga.processContract] DOGA FACTORY contract storage and operations inserted into the database")

    # Get SMAK STAKING contract storage and operations
    await ContractStakingSmak.processContract(rpcEndpoint, dbConnection, contractsAddr["STAKING_SMAK"])
    print("[ContractStakingSmak.processContract] SMAK STAKING contract storage and operations inserted into the database")

    # Get FARMS V1 contract storage and operations
    await ContractFarmsV1.processContract(rpcEndpoint, dbConnection, contractsAddr["FARMS_V1"])
    print("[ContractFarmsV1.processContract] FARMS V1 contract storage and operations inserted into the database")

    # Get FARMS V2 contract storage and operations
    await ContractFarmsV2.processContract(rpcEndpoint, dbConnection, contractsAddr["FARMS_V2"])
    print("[ContractFarmsV2.processContract] FARMS V2 contract storage and operations inserted into the database")

    # Disconnect from the database
    disconnectDatabase(dbConnection)
    print("Exiting the app...")

# start with uvicorn commandline
if __name__ == "main":
    asyncio.gather(main())

    global app
    app = startGraphqlServer()