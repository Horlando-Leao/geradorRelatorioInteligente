from Services import Services
from app import app, request, jsonify, make_response

@app.route("/", methods=["GET"])
def olaMundo():
    #minhaResp = make_response({"respoata":"Testando Hello World!"})
    #minhaResp.headers["warning"] = "warning"
    #minhaResp.status_code = 200
    minhaResp = ({"resposta":"Testando Hello World!"})
    return jsonify(minhaResp)


@app.route("/relatorio", methods=["GET"])
def relatorio():
    intencao_usuario = request.args.get("intencao_usuario")
    resultado = Services().gerarRelatorio(desejoUsuario=intencao_usuario)

    return (resultado)