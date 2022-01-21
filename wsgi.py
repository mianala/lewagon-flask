from flask import Flask, jsonify
app = Flask(__name__)

# this comment is for a conflict form master
# this comment is for a from branch for conflict
# unrelated in master
@app.route('/')
def home():
    return jsonify({'roll':4})

# from unrelated