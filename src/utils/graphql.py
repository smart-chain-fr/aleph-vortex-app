from tartiflette import Resolver, Engine
from tartiflette_asgi import TartifletteApp
import asyncpg

# Define a resolver to fetch data from the Postgres database
@Resolver("Query.users")
async def resolve_users(dbConnection, parent, args, ctx, info):
    result = []
    rows = await dbConnection.fetch('SELECT * FROM users')
    for row in rows:
        result.append(dict(row))
    await dbConnection.close()
    return result

# Define the GraphQL schema
sdl = """
type User {
    id: Int!
    name: String!
}

type Query {
    users: [User]
}
"""

# Create a Tartiflette engine with the defined schema and resolvers
engine = Engine(sdl=sdl)

# Create a TartifletteApp instance with the engine
app = TartifletteApp(engine=engine)
