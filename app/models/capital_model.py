from sqlalchemy import Column, Integer, String, ForeignKey
from app.configs.database import db

class CapitalModel(db.Model):
    __tablename__ = 'capitais'

    # Atributos que representam colunas da nossa tabela capitais
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)
    bairros = Column(Integer)
    populacao = Column(Integer)
    # Chave Estrangeira para relacionamento com a tabela estados
    estado_id = Column(
      Integer,
      ForeignKey("estados.id"),
      nullable=False,
      unique=True
      )

    # Variável criada para auxiliar no desenvolvimento, não
    # faz parte da criação das tabelas no banco.
    estado = db.relationship(
      "EstadoModel",
      backref=db.backref("capital", uselist=False),
      uselist=False
    )