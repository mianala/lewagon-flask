from flask import Flask, jsonify
import os

sentry_dsn = os.getenv('SENTRY_DSN', None)
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(
        sentry_dsn,
        integrationsb= [FlaskIntegration()]
    )

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'roll':4})

@app.route('/error')
def error():
    return "hei!"