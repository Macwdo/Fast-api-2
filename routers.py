from controllers import prod_controllers, usuario_controllers
from fastapi import APIRouter

router = APIRouter()
router.include_router(prod_controllers.router,prefix="/produtos")
router.include_router(usuario_controllers.router,prefix="/usuarios")