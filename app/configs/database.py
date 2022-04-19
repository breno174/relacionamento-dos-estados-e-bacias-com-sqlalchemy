from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Usaremos essa instância para declarar nossas models
# e anexar nosso app com o banco
db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    # Estamos criando um atributo db em app, que armazenará nossa instância
    # de db para que tenhamos uma maior facilidade no desenvolvimento
    app.db = db

    from app.models.estado_model import EstadoModel
    from app.models.capital_model import CapitalModel
