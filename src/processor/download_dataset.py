from dotenv import load_dotenv
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Explicitly load the .env file
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

# Force-set the environment variables for Kaggle
os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

# Debug: Print environment variables to ensure they're set
print(f"KAGGLE_USERNAME: {os.getenv('KAGGLE_USERNAME')}")
print(f"KAGGLE_KEY: {os.getenv('KAGGLE_KEY')}")

# Test Kaggle API Authentication
try:
    api = KaggleApi()
    api.authenticate()
    print("Kaggle API authenticated successfully!")
except Exception as e:
    print(f"Error during Kaggle API authentication: {e}")
