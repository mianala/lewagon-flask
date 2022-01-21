from flask import Flask, jsonify
app = Flask(__name__)

# this comment is for a conflict form master
@app.route('/')
def home():
    return jsonify({'roll':0})