from sqlalchemy import Column, Integer, String, Float
from app.configs.database import db

class EstadoModel(db.Model):
    __tablename__ = 'estados'

    # Atributos que representam colunas da nossa tabela estados
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    sigla = Column(String(2), nullable=False, unique=True)
    populacao = Column(Integer)
    area = Column(Float)
