from sqlalchemy import Column, Integer, String
from app.configs.database import db

class RegiaoModel(db.Model):
    __tablename__ = 'regioes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    numero_estados = Column(Integer)
    
    estados = db.relationship("EstadoModel", backref="regiao",uselist=True)