from fastapi import APIRouter, Response, status
from schemas import UsuarioCreate, UsuarioPatch, UsuarioResponse
from models.usuario import Usuario
from typing import List
import ormar

from security import criacao


router = APIRouter()

@router.post("/", response_model=UsuarioResponse)
async def create_user(criando_usuario: UsuarioCreate):
    dados = criando_usuario.dict(exclude_unset=True)
    usuario = Usuario(**dados)
    return await usuario.save()

@router.get("/", response_model=List[UsuarioResponse])
async def listview_user():
    return await Usuario.objects.all()

@router.get("/{id}", response_model=UsuarioResponse)
async def listview_user(id: int):
    return await Usuario.objects.get(id=id)

@router.patch("/{id}",response_model=UsuarioResponse)
async def update_user(id: int, dados_usuario: UsuarioPatch, response: Response):
    dados = await Usuario.objects.get(id=id)
    update = dados_usuario.dict(exclude_unset=True)
    await dados.update(**update)
    dados.save()
    return dados 


@router.delete("/{id}")
async def delete_user(id: int,response: Response):
    try:
        response.status_code = status.HTTP_204_NO_CONTENT
        usuario = await Usuario.objects.get(id=id)
        return await usuario.delete()
    except ormar.NoMatch:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error":"Usuario Não encontrado"}
    
    