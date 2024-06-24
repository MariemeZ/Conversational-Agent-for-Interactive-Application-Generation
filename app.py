from flask import Flask, request, jsonify
from gerer_aide import gerer_aide  
from actions_intents import process_app
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200']) 

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('user_input')
    chatbot_response = process_app(user_input)
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)