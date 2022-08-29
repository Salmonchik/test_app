from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException

from app.api.errors.http_exception import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes.api import router as api_router

app = FastAPI()


app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)
app.add_exception_handler(ValueError, http422_error_handler)

app.include_router(api_router, prefix='/api')
