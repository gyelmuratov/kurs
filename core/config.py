from environs import Env
env = Env()
env.read_env()


BOT_TOKEN = env.str('BOT_TOKEN')
DEVELOPER_ID = env.int('DEVELOPER_ID')

DB_USER = env.str('DB_USER')
DB_PASSWORD = env.str('DB_PASSWORD')
DB_HOST = env.str('DB_HOST')
DB_NAME = env.str('DB_NAME')
DB_PORT = env.int('DB_PORT')

DB_CONFIG = {
    "user": DB_USER,
    "password": DB_PASSWORD,
    "host": DB_HOST,
    "port": DB_PORT,
    "database": DB_NAME
}
