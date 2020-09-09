from flask import Flask 

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def homepage():
    return {"Message" : "Helloeeeee world!"}

if __name__ == "__main__":
    app.run(port=8000, debug=True) #5000