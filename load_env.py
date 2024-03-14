from dotenv import load_dotenv
import os
path = os.path.dirname(os.path.realpath(__file__))

env_path = f"{os.path.dirname(os.path.realpath(__file__))}/.env"
load_dotenv(dotenv_path= env_path)

api_url = os.getenv("API_URL")
api_key = os.getenv("APIKEY")


e_host=os.getenv("DB_HOST")
e_user= os.getenv("DB_USER")
e_password=os.getenv("DB_PASSWORD")
e_database=os.getenv("DATABASE_NAME")

e_msg_broker = os.getenv("MSG_BROKER")