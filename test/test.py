import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

#環境変数読み込み
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
URL = os.environ.get("URL")

def main():
    original_data  = get_Api_Parameter(API_KEY)
    print(result.text)

def get_Api_Parameter(API_KEY: str,) -> str:
    parameter = URL + API_KEY + "&keyword=東京都"
    print(parameter)
    response = requests.get(parameter)
    return response

def pop_Store_data(original_data: str,) -> str:
    for store_name in original_data:
        pass

if __name__ == '__main__':
    main()