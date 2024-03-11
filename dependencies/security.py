from fastapi import Depends, FastAPI, HTTPException, Request, Security
from fastapi.security.api_key import APIKeyHeader

from ..settings import Settings

API_KEY_NAME = "x-access-token"

api_key_header_object = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def init_app(app: FastAPI, sets: Settings) -> None:
    app.router.dependencies.append(Depends(verifier_factory(sets.API_KEY)))


def verifier_factory(api_key):
    def verify_key(req: Request, api_key_header: str = Security(api_key_header_object)):
        if req.method == "GET" and req.scope.get("path") == "/":
            return None

        if api_key_header == api_key:
            return api_key_header

        raise HTTPException(status_code=403, detail="Invalid api key provided")

    return verify_key
