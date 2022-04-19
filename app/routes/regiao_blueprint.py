from flask import Blueprint
from app.controllers.regiao_controller import create_regiao


bp = Blueprint("bp_regioes", __name__)

# Associamos nosso controlador com a rota POST para /regioes
bp.post("/regioes")(create_regiao)