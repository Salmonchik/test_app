from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        {'error': {
            'message': ','.join([exc.detail]),
            'code': 1,
        }}, status_code=exc.status_code)
