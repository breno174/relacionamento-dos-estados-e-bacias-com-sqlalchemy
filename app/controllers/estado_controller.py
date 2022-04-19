from flask import request, current_app, jsonify
from app.models.regiao_model import RegiaoModel
from app.models.estado_model import EstadoModel


def create_estado():
    # Aqui, utilizamos do artifício criado em nosso app/configs/database.py.
    # O método current_app nos disponibiliza o contexto do app atual,
    # e, a partir dele, conseguimos acessar o db que atribuímos lá
    # no database.py. Precisamos do db para acessar o session
    # e executar comandos de persistência do SQLAlchemy.
    session = current_app.db.session

    data = request.get_json()

    # Retiramos o nome da regiao do nosso JSON
    nome_regiao = data.pop('regiao')

    # Buscar pela região existente
    regiao = RegiaoModel.query.filter_by(nome=nome_regiao).first()

    # Adicionando o id da região para fazer a criação do estado
    data['regiao_id'] = regiao.id

    estado = EstadoModel(**data)

    session.add(estado)
    session.commit()

    return jsonify({
        "id": estado.id,
        "nome": estado.nome,
        "sigla": estado.sigla,
        "populacao": estado.populacao,
        "area": float(estado.area),
        "regiao": estado.regiao.nome,
    }), 201
