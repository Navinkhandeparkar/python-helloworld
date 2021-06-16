import json
import logging
import datetime
from flask import Flask
app = Flask(__name__)


# FORMAT = '{{TIMESTAMP}}, {{ ENDPOINT_NAME}}'
FORMAT = '%(asctime)s, %(message)s endpoint was reached'


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    app.logger.info('/status')
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/metrics")
def metrics():
    app.logger.info('/metrics')
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    app.logger.info('/__main__')
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format=FORMAT)

    app.run(host='0.0.0.0')
