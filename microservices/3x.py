# Should remove opinions only keeping facts

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "API is working!"

if __name__ == '__main__':
    app.run(debug=True)
