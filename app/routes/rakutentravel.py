from fastapi import APIRouter, HTTPException, Response
from dotenv import load_dotenv
import requests
import logging
import os

load_dotenv(os.path.join(os.path.abspath(os.curdir), ".env"))
RAKUTEN_API_KEY = os.getenv("RAKUTEN_API_KEY")

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/rakutentravel")
def search_hotel():
    RAKUTEN_TRAVEL_API_ENDPOINT = "https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426"

    params = {
        "format": "json",
        "applicationId": RAKUTEN_API_KEY,
        "keyword": "福岡"
    }
    
    response = requests.get(RAKUTEN_TRAVEL_API_ENDPOINT, params=params)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Rakuten API")
    
    return response.json()