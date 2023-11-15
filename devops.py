from flask import Flask, jsonify, request
import random 

app = Flask(__name__)

@app.route('/shuffle', methods=['POST'])
def shuffle_list():
    inputList = request.json.get('list_of_ints') 
    shuffled_list = random.sample(inputList, len(inputList))
    return jsonify({"shuffled_list": shuffled_list})

if __name__ == '__main__':
    app.run(debug=True)