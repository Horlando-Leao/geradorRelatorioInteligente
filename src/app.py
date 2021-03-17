from flask import Flask, request, abort, jsonify, make_response

app = Flask(__name__)
import routes

if __name__ == "app":
    app.run(debug=True)
else:
    app.logger.debug("__name__ é diferente de app")


