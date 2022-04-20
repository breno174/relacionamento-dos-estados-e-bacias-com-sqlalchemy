from flask import request, current_app, jsonify
from app.models.regiao_model import RegiaoModel
from app.models.estado_model import EstadoModel
from app.models.bacia_hidro_model import BaciaHidroModel

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


    # Retiramos o nome da bacia do nosso JSON
    nome_bacia = data.pop('bacia')

    # Buscar pela bacia existente
    bacia = BaciaHidroModel.query.filter_by(nome=nome_bacia).first()

    estado = EstadoModel(**data)

    # Utilizamos o relationship criado em BaciaHidroModel para relacionar
    # facilmente um objeto do tipo BaciaHidroModel a um objeto do tipo EstadoModel
    estado.bacias.append(bacia)

    session.add(estado)
    session.commit()

    return jsonify({
        "id": estado.id,
        "nome": estado.nome,
        "sigla": estado.sigla,
        "populacao": estado.populacao,
        "area": float(estado.area),
        "regiao": estado.regiao.nome,
        "bacia": estado.bacias
    }), 201