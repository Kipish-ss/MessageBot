from environs import Env

env = Env()
env.read_env()
API_TOKEN = env.str("API_TOKEN")
PATH = '/Users/kyryl/Desktop/users.db'
ADMINS = env.list("ADMINS")

