from Services import Services
from app import app, request, jsonify

@app.route("/", methods=["GET"])
def olaMundo():
    return ("Testando Hello, World!")


@app.route("/relatorio", methods=["GET"])
def relatorio():
    desejoUsuario = request.args.get("desejo")
    novoServico = Services().gerarRelatorio(desejoUsuario)
    resultado = novoServico
    return (resultado)