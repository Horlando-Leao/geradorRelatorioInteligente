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
    resultado = ""
    if(isinstance(intencao_usuario, str) and len(intencao_usuario) > 1):
        resultado = Services().gerarRelatorio(desejoUsuario=intencao_usuario)
        resultado = resultado
    else:
        rs = {"response":"Falta paramêtros", "parametros":["intencao_usuario"] }
        resultado = make_response(rs)
        resultado.status_code = 422
    return (resultado)

@app.route("/relatorio/nomes", methods=["GET"])
def relatorioNomes():
    todoNomesRelatorio = Services().retornarTodosNomesRelatorios()
    rs = make_response(todoNomesRelatorio)
    rs.headers.add('Access-Control-Allow-Origin', '*')
    rs.headers["dataType"] = "jsonp"


    return rs