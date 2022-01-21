from flask import Flask, jsonify
app = Flask(__name__)

# this comment is for a conflict
@app.route('/')
def home():
    return jsonify({'roll':0})