from flask import Flask, jsonify
app = Flask(__name__)

# this comment is for a conflict form master
# this comment is for a from branch for conflict
@app.route('/')
def home():
    return jsonify({'roll':0})