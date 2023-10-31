from fastapi import FastAPI
from .routes import hotpapper, rakutentravel

app = FastAPI()

app.include_router(hotpapper.router)
app.include_router(rakutentravel.router)