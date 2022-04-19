from flask import Blueprint
from app.controllers.estado_controller import create_estado

bp = Blueprint("bp_estados", __name__)

# Associando o controller create_estado a rota POST em /estados
bp.post("/estados")(create_estado)
