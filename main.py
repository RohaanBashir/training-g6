from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask is running inside a Docker container!'

if __name__ == '__main__':
    # We set host to 0.0.0.0 so it's accessible outside the container
    app.run(debug=True, host='0.0.0.0', port=5000)
