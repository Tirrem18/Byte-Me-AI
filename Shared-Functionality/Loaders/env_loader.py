import os
from dotenv import load_dotenv

# Load .env as soon as this module is imported
load_dotenv()

def load_env():
    print("✅ Environment variables loaded.")
