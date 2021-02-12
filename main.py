from flask import Flask, jsonify, request

app = Flask(__name__)
seed = {"num":100}

@app.route('/', methods=['GET'])
def fetch():
    #return jsonify({'num':seed["num"]})
    return str(seed['num'])

@app.route('/', methods=['POST'])
def addnum():
    number= {'num' : request.json['num']}
    seed.update(number)
    return jsonify({'num':seed['num']})
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
