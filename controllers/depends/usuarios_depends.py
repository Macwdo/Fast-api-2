from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel, ValidationError
from security import SECRET_KEY, JWT_ALGORITHM
from models.usuario import Usuario

class TokenSCHEMA(BaseModel):
    sub: Optional[int] = None

key = OAuth2PasswordBearer(tokenUrl="api/usuarios/login")

async def get_usuario_logado(token: str = Depends(key)) -> Usuario:
    try:
        decode = jwt.decode(token=token,key=SECRET_KEY, algorithms=[JWT_ALGORITHM])
        token_data = TokenSCHEMA(**decode)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail="Não foi possivel validar as credenciais"
        )
    user = await Usuario.objects.get_or_none(id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404,detail="Usuario não encontrado")
    return user
        