# from fastapi import Request, HTTPException
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from jose import jwt, JWTError
# from security import auth_handler
#
# class JWTBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super(JWTBearer, self).__init__(auto_error=auto_error)
#
#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
#         if credentials:
#             if credentials.scheme != "Bearer":
#                 raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
#             if not self.verify_jwt(credentials.credentials):
#                 raise HTTPException(status_code=403, detail="Invalid or expired token.")
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")
#
#     def verify_jwt(self, jwtoken: str):
#         try:
#             payload = jwt.decode(jwtoken, auth_handler.SECRET_KEY, algorithms=[auth_handler.ALGORITHM])
#             return payload
#         except JWTError:
#             return False
