import json
from typing import Union
from fastapi.exceptions import RequestValidationError, ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST


def http422_error_handler(
    _: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    exc_json = json.loads(exc.json())
    errors = [f'{error["loc"][-1]}: {error["msg"]}' for error in exc_json]

    return JSONResponse(
        {'error': {
            'message': ','.join(errors),
            'code': 1,
        }},
        status_code=HTTP_400_BAD_REQUEST,
    )
