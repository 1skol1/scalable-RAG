from fastapi import FastAPI

from api.api_v1.api import router as api_router
from core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION

from mangum import Mangum


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    handler = Mangum(app)

    return application


app = get_application()
