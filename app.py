import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/index1")
def main_func():
    return "This is a main page!!!"


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
