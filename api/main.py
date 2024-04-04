from fastapi import FastAPI
from mangum import Mangum

from api.routes import router as api_router


app = FastAPI()
app.include_router(api_router)

handler = Mangum(app)