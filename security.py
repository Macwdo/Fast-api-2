from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Union, Any
from jose import jwt

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

SECRET_KEY = 'secret'
JWT_ALGORITHM = 'HS512'
ACESS_TOKEN_EXPIRE_HOURS = 24

def criar_jwt_token(subject:Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        hours=ACESS_TOKEN_EXPIRE_HOURS
    )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm='HS512')
    return encoded_jwt



def verificacao(senha_plana: str, senha_hashed: str) -> bool:
    return pwd_context.verify(senha_plana, senha_hashed)

def criacao(password: str) -> str:
    return pwd_context.hash(password)