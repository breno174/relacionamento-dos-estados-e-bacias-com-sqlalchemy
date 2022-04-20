from app.configs.database import db

bacias_estados = db.Table('bacias_estados',
    # Coluna que cria um id autoincrementavel em bacias_estados (opcional)
    db.Column('id', db.Integer, primary_key=True),
    # Coluna de referencia entre a tabela pivo e o id da tabela bacias_hidro
    db.Column('bacia_id', db.Integer, db.ForeignKey('bacias_hidrograficas.id')),
    # Coluna de referencia entre a tabela pivo e o id da tabela estados
    db.Column('estado_id', db.Integer, db.ForeignKey('estados.id'))
)