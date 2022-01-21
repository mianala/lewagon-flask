from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from models import Product
from flask_migrate import Migrate

migrate = Migrate(app, db)

@app.route('/')
def home():
    return jsonify({'roll':0})
# push