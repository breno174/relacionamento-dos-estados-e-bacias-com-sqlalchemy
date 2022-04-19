from flask import request, current_app, jsonify
from app.models.capital_model import CapitalModel
from app.models.estado_model import EstadoModel

def create_capital():
    session = current_app.db.session

    data = request.get_json()
    # Retirando a chave estado da requisição
    nome_estado = data.pop("estado")
    # Procuramos por um estado com o nome retirado
    estado = EstadoModel.query.filter_by(nome=nome_estado).first()

    # Anexamos o id desse estado ao nosso payload data
    data["estado_id"] = estado.id

    # Conseguimos criar corretamente um objeto de CapitalModel, agora com
    # estado_id contendo o id do estado invés do estado contendo o nome.
    capital = CapitalModel(**data)

    session.add(capital)
    session.commit()

    return jsonify({
        "id": capital.id,
        "nome": capital.nome,
        "bairros": capital.bairros,
        "populacao": capital.populacao,
        "estado_nome": capital.estado.nome,
    }), 201