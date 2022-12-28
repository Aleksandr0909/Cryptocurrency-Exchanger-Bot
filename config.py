import environ


env = environ.Env()
environ.Env.read_env('.env')

TELEGRAM_TOKEN = env('TELEGRAM_TOKEN')
EXCHANGE_API_KEY = env('EXCHANGE_API_KEY')
