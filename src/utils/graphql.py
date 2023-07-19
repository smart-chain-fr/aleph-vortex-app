import uvicorn
import asyncio
from tartiflette import Resolver, Engine
from tartiflette_asgi import TartifletteApp
from src.utils.env import initEnvDatabase
from src.utils.database import connectDatabase

def startGraphqlServer() :
    # Specify the database connection details
    db_info : dict = initEnvDatabase()

    # Connect to the database
    dbConnection = connectDatabase(db_info["host"][0], db_info["port"][0], db_info["database"][0], db_info["user"][0], db_info["password"])

    # @Resolver("Query.contract_dex_storage")
    # async def contract_dex_storage(parent, args, ctx, info = None):
    #     id = args["id"]
    #     result = []
    #     rows = await dbConnection.fetch('SELECT * FROM contract_dex_storage WHERE id = $1', id)
    #     for row in rows:
    #         result.append(dict(row))
    #     await dbConnection.close()
    #     return result

    @Resolver("Query.hello")
    async def hello(parent, args, context, info):
        name = args["name"]
        return f"Hello, {name}!"

    sdl = '''
    type Query {
        hello(name: String): String
    }
    '''

    # sdl = '''
    # type Query {
    #     hello(name: String): String
    #     contract_dex_storage(id : Int) : dex_storage
    # }
    # type ContractDexStorage {
    #     id: Int!
    #     history: BigInt
    #     manager: String
    #     reserve: String
    #     xtzpool: String
    #     lqttotal: String
    #     tokenpool: String
    #     lqtaddress: String
    #     freezebaker: Boolean
    #     tokenaddress: String
    #     user_investments: BigInt
    #     selfisupdatingtokenpool: Boolean
    # }
    # '''

    # Create a Tartiflette engine with the defined schema and resolvers
    print("Starting the GraphQL Server...")
    engine = Engine(sdl=sdl)
    app = TartifletteApp(engine=engine, sdl=sdl, path="/api")
    return app