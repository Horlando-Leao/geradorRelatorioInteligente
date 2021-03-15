from flask import Flask, request, abort, jsonify

app = Flask(__name__)
import routes

if __name__ == "__main__":
    app.run()
