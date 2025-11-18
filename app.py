from flask import Flask
from supporters.test_utils import test_bp

app = Flask(__name__)

# register supporters
app.register_blueprint(test_bp)

@app.route('/')
def hello():
    return "Hello, World from Raspberry Pi!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # "flask run --debug" in terminal
    # proxy change added