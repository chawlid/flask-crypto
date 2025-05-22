from flask import Flask, request
import Sendpush as sp

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask Crypto!"
@app.route('/send', methods=['POST'])
def send():
    token = request.form.get('token')
    sp.send_data(token)
    return f"Received: {token}"

if __name__ == '__main__':
    app.run(host='192.168.1.48', port=5000, debug=True)