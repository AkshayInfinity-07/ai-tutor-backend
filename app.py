from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Tutoring Chatbot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName')
    
    if intent == 'Greet':
        return jsonify({'fulfillmentText': 'Hey there! Ready to learn something new today? 😊'})
    elif intent == 'StudyTips':
        return jsonify({'fulfillmentText': 'Tip: Break your study into 25-minute chunks with 5-minute breaks!'})
    else:
        return jsonify({'fulfillmentText': "Sorry, I didn’t get that. Try asking me about study tips or greetings!"})

if __name__ == '__main__':
    app.run(debug=True)
