import asyncio
from utils.env import initEnvRpc, initEnvDatabase, initEnvContracts
from utils.database import connectDatabase, disconnectDatabase, initDatabase
from utils.graphql import startGraphqlServer
from classes.indexer import Indexer
from classes.contract.contract_dex import ContractDex
from classes.contract.contract_token_smak import ContractTokenSmak
from classes.contract.contract_token_anti import ContractTokenAnti
from classes.contract.contract_factory_fa12 import ContractFactoryFA12
from classes.contract.contract_factory_fa2 import ContractFactoryFA2
from classes.contract.contract_factory_doga import ContractFactoryDoga
from classes.contract.contract_staking_smak import ContractStakingSmak
from classes.contract.contract_farms_v1 import ContractFarmsV1
from classes.contract.contract_farms_v2 import ContractFarmsV2

async def main() :
    print("Starting the app...")

    # Specify the Tezos node RPC endpoint
    rpcEndpoint : str = await initEnvRpc()

    # Specify the contract addresses
    contractsAddr : dict = await initEnvContracts()

    # Specify the database connection details
    db_info : dict = await initEnvDatabase()

    # Connect to the database
    dbConnection = connectDatabase(db_info["host"][0], db_info["port"][0], db_info["database"][0], db_info["user"][0], db_info["password"])

    # Initialize the database
    initDatabase(dbConnection)

    # # Insert Indexer state into the database
    # await Indexer.processIndexer(rpcEndpoint, dbConnection)

    # # Get DEX contract storage and operations
    # await ContractDex.processContract(rpcEndpoint, dbConnection, contractsAddr["VORTEX"])

    # # Get SMAK TOKEN contract storage and operations
    # await ContractTokenSmak.processContract(rpcEndpoint, dbConnection, contractsAddr["TOKEN_SMAK"])

    # # Get ANTI TOKEN contract storage and operations
    # await ContractTokenAnti.processContract(rpcEndpoint, dbConnection, contractsAddr["TOKEN_ANTI"])

    # # Get FA12 FACTORY contract storage and operations
    # await ContractFactoryFA12.processContract(rpcEndpoint, dbConnection, contractsAddr["FACTORY_FA12"])

    # # Get FA2 FACTORY contract storage and operations
    # await ContractFactoryFA2.processContract(rpcEndpoint, dbConnection, contractsAddr["FACTORY_FA2"])

    # # Get DOGA FACTORY contract storage and operations
    # await ContractFactoryDoga.processContract(rpcEndpoint, dbConnection, contractsAddr["FACTORY_DOGA"])

    # # Get SMAK STAKING contract storage and operations
    # await ContractStakingSmak.processContract(rpcEndpoint, dbConnection, contractsAddr["STAKING_SMAK"])

    # # Get FARMS V1 contract storage and operations
    # await ContractFarmsV1.processContract(rpcEndpoint, dbConnection, contractsAddr["FARMS_V1"])

    # # Get FARMS V2 contract storage and operations
    # await ContractFarmsV2.processContract(rpcEndpoint, dbConnection, contractsAddr["FARMS_V2"])

    # await startGraphqlServer(dbConnection)

    # Disconnect from the database
    disconnectDatabase(dbConnection)

    print("Exiting the app...")

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.run_until_complete(startGraphqlServer())