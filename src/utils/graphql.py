from tartiflette import Resolver, Engine
from tartiflette_asgi import TartifletteApp
from utils.database import connectDatabase
import uvicorn

def startGraphqlServer(dbConnection) :

    # # Define the GraphQL schema
    # sdl = """
    # type User {
    #     id: Int!
    #     name: String!
    # }

    # type Query {
    #     users: [User]
    # }
    # """

    # # Create a Tartiflette engine with the defined schema and resolvers
    # engine = Engine(sdl=sdl)

    # # Create a TartifletteApp instance with the engine
    # app = TartifletteApp(engine=engine)

    @Resolver("Query.contract_dex_storage")
    async def contract_dex_storage(parent, args, ctx, info = None):
        id = args["id"]
        result = []
        rows = await dbConnection.fetch('SELECT * FROM contract_dex_storage WHERE id = $1', id)
        for row in rows:
            result.append(dict(row))
        await dbConnection.close()
        return result

    @Resolver("Query.hello")
    async def hello(parent, args, context, info):
        name = args["name"]
        return f"Hello, {name}!"

    sdl = '''
    type Query {
        hello(name: String): String
        contract_dex_storage(id : Int) : dex_storage
    }
    type ContractDexStorage {
        id: Int!
        history: BigInt
        manager: String
        reserve: String
        xtzpool: String
        lqttotal: String
        tokenpool: String
        lqtaddress: String
        freezebaker: Boolean
        tokenaddress: String
        user_investments: BigInt
        selfisupdatingtokenpool: Boolean
    }
    '''

    # Create a Tartiflette engine with the defined schema and resolvers
    engine = Engine(sdl=sdl)
    app = TartifletteApp(engine=engine, sdl=sdl, path="/api")

    uvicorn.run(app)