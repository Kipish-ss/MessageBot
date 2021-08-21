from enum import Enum
from environs import Env

env = Env()
env.read_env()
API_TOKEN = env.str("API_TOKEN")
PATH = '/Users/kyryl/Desktop/Кирилл Сидак/Glinobot/data/users.db'


class States(Enum):
    S_START = 0  # Start
    S_ENTER_NAME = 1  # User enters his name
    S_TYPE_MESSAGE = 2  # User types a message
    S_UPDATE_NAME = 3  # User updates his name
