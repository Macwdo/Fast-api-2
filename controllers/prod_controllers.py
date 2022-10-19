from typing import List, Optional
from models.prod import Produto
from fastapi import APIRouter, status, Response,HTTPException
import ormar.exceptions
from models.usuario import Usuario
from schemas import ProdutoSCHM, ProdutoSCHMPatch

router = APIRouter()


@router.get("/",tags=["Produtos"])
async def view_list():
    return {"Produtos":await Produto.objects.all()}

@router.get("/{id}",tags=["Produtos"])
async def view(id: int,response:Response):
    try:
        return await Produto.objects.get(id=id)
    except ormar.exceptions.NoMatch :
        response.status_code = 404
        return {"Error":"Produto Não encontrado"}


@router.patch("/{id}",tags=["Produtos"])
async def update(id: int,produto:ProdutoSCHMPatch,response:Response):
    try:
        produto_get = await Produto.objects.get(id=id)
        produto_dict = produto.dict(exclude_unset=True)
        await produto_get.update(**produto_dict)
        produto_get.save()
        return produto_get
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"Error":"Produto Não encontrado"}
    

@router.post("/",tags=["Produtos"])
async def create(produto:ProdutoSCHM):
    prod = produto.dict()
    print(prod)
    criar = Produto.objects.create(**prod)
    last = await Produto.objects.all()
    user = await Usuario.objects.get_or_none(id=prod.get('vendedor'))
    user.vendas += [int(last[-1].id)]
    await user.update()
    return ProdutoSCHM


@router.delete("/{id}",tags=["Produtos"])
async def view(id: int,response: Response):
    try:
        response.status_code = status.HTTP_204_NO_CONTENT
        produto = await Produto.objects.get(id=id)
        return await produto.delete()
    except ormar.NoMatch:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error":"Produto Não encontrado"}
