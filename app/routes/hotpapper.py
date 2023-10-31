
from fastapi import APIRouter
from dotenv import load_dotenv
import requests
import os

load_dotenv(os.path.join(os.path.abspath(os.curdir), ".env"))
API_KEY = os.getenv("HOT_PAPPER_API_KEY")

router = APIRouter()

@router.get("/hotpapper")
def get_opensky_data():
     # ホットペッパーAPIのエンドポイント
    url = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    
    # パラメータの設定
    params = {
        "key": API_KEY,
        "keyword": "ラーメン",
        "format": "json"
    }
    
    # APIリクエストの実行
    response = requests.get(url, params=params)
    data = response.json()

    return data["results"]["shop"]