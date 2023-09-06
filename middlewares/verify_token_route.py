from fastapi import Request
from helpers.jwt_helper import validate_token
from fastapi.routing import APIRoute
from fastapi import HTTPException

class VerifyTokenRoutes(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()
        
        async def verify_token_middleware(request: Request):
            if(request.headers.get("Authorization") is None):
                raise HTTPException(status_code=401, detail="Bearer Token is empty")
            token = request.headers["Authorization"].split(" ")[1]
            print(token)
            validation_response = validate_token(token, output=False)

            if validation_response == None:
                return await original_route(request)
            else:
                return validation_response
        
        return verify_token_middleware