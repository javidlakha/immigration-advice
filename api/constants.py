import pathlib

from starlette.config import Config


config = Config(pathlib.Path(__file__).parent.parent.resolve() / ".env")
ANTHROPIC_API_KEY = config("ANTHROPIC_API_KEY")
OPENAI_API_KEY = config("OPENAI_API_KEY")
MONGO_USERNAME = config("MONGO_USERNAME")
MONGO_PASSWORD = config("MONGO_PASSWORD")
MONGO_HOST = config("MONGO_HOST")
TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = config("TWILIO_PHONE_NUMBER")
WEBHOOK_DOMAIN = config("WEBHOOK_DOMAIN")

MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/?retryWrites=true&w=majority"
VECTOR_SEARCH_INDEX = 'semantic-search'
EMBEDDINGS_FIELD = 'embedding'