from fastapi import APIRouter, Depends, Form, Response, status, HTTPException
from controllers.depends.usuarios_depends import get_usuario_logado
from schemas import UsuarioCreate, UsuarioPatch, UsuarioResponse
from models.usuario import Usuario
from security import verificacao, criar_jwt_token
from typing import List
import ormar


router = APIRouter()

@router.post("/login",tags=["Usuario"])
async def login_user(username: str = Form(...), password: str = Form(...)):
    usuario = await Usuario.objects.get_or_none(email=username)
    if not usuario or not verificacao(password, usuario.hash_password):
        raise HTTPException(
            status_code=403,
            detail="Usuario ou senha incorretos"
        )

    return {
        "access_token": criar_jwt_token(usuario.id),
        "token_type": "bearer"
    }



@router.post("/", response_model=UsuarioResponse,tags=["Usuario"])
async def create_user(criando_usuario: UsuarioCreate):
    dados = criando_usuario.dict(exclude_unset=True)
    usuario = Usuario(**dados)
    return await usuario.save()

@router.get("/", response_model=List[UsuarioResponse],tags=["Usuario"])
async def listview_user():
    return await Usuario.objects.all()

@router.get("/{id}", response_model=UsuarioResponse,tags=["Usuario"])
async def listview_user(id: int):
    return await Usuario.objects.get(id=id)

@router.patch("/{id}",response_model=UsuarioResponse,tags=["Usuario"])
async def update_user(id: int, dados_usuario: UsuarioPatch, response: Response):
    dados = await Usuario.objects.get(id=id)
    update = dados_usuario.dict(exclude_unset=True)
    await dados.update(**update)
    dados.save()
    return dados


@router.delete("/{id}",tags=["Usuario"])
async def delete_user(id: int,response: Response,usuariologado: Usuario = Depends(get_usuario_logado)):
    try:
        usuario = await Usuario.objects.get(id=id)
        response.status_code = status.HTTP_204_NO_CONTENT
        return await usuario.delete()
    except ormar.NoMatch:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error":"Usuario Não encontrado"}

@router.post("/{id}/cargos/{cargo}",response_model=UsuarioResponse,tags=["Usuario"])
async def add_cargos(id:int , cargo: str,response:Response):
    try:
        usuario = await Usuario.objects.get(id=id)
        usuario.cargos += [cargo]
        await usuario.update()
        return usuario
    except ormar.NoMatch:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error":"Usuario Não encontrado"}


@router.delete("/{id}/cargos/{cargo}",response_model=UsuarioResponse ,tags=["Usuario"])
async def delete_cargos(id:int , cargo: str,response:Response):
    try:
        usuario = await Usuario.objects.get(id=id)
        usuario.cargos.remove(cargo)
        await usuario.update()
        return usuario
    except ormar.NoMatch:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error":"Usuario Não encontrado"}
    


    
    