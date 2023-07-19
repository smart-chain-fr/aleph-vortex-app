from environs import Env

env = Env()
env.read_env()

async def initEnv() -> tuple[str, dict, dict] :
    return await initEnvRpc(), await initEnvDatabase(), await initEnvContracts()

async def initEnvRpc() -> str:
    try:
        rpcEndpoint = env.str("RPC_ENDPOINT")
    except Exception as e:
        raise Exception(f"Error reading RPC_ENDPOINT from .env file : {e}")
    print(f"rpcEndpoint : {rpcEndpoint}")
    return rpcEndpoint


async def initEnvDatabase() -> dict :
    db_info = {}
    try:
        db_info["host"] = env.str("PG_HOST"),
        db_info["port"] = env.int("PG_PORT"),
        db_info["database"] = env.str("PG_DATABASE"),
        db_info["user"] = env.str("PG_USERNAME"),
        db_info["password"] = env.str("PG_PASSWORD")
    except Exception as e:
        raise Exception(
            f"Error reading database connection details from .env file : {e}")
    return db_info


async def initEnvContracts() -> dict:
    contractsAddr = {}
    try:
        contractsAddr["VORTEX"] = env.str("VORTEX")
        contractsAddr["TOKEN_SMAK"] = env.str("TOKEN_SMAK")
        contractsAddr["TOKEN_ANTI"] = env.str("TOKEN_ANTI")
        contractsAddr["FACTORY_FA12"] = env.str("FACTORY_FA12")
        contractsAddr["FACTORY_FA2"] = env.str("FACTORY_FA2")
        contractsAddr["FACTORY_DOGA"] = env.str("FACTORY_DOGA")
        contractsAddr["STAKING_SMAK"] = env.str("STAKING_SMAK")
        contractsAddr["FARMS_V1"] = env.str("FARMS_V1")
        contractsAddr["FARMS_V2"] = env.str("FARMS_V2")
    except Exception as e:
        raise Exception(
            f"Error reading contract addresses from .env file : {e}")
    return contractsAddr
