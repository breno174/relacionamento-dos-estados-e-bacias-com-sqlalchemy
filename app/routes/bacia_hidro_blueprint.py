from flask import Blueprint
from app.controllers.bacia_hidro_controller import create_bacia_hidro

bp = Blueprint("bp_bacias_hidro", __name__)

# Associando o controller create_bacia_hidro a rota POST em /bacias
bp.post("/bacias")(create_bacia_hidro)