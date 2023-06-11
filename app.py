from flask import Flask, render_template
from flask_cors import CORS
import CRUD

app = Flask(__name__, static_folder='static')
crud = CRUD

CORS(app)


@app.route('/')
def main():  # put application's code here
    return render_template("index.html")\

@app.route('/colab')
def redirect_to_aporte():  # put application's code here
    return render_template("aporte.html")


@app.route("/market/<market_name>")
def redirect_to_market_page(market_name):
    # request data to FIREBASE AND DISPLAY IT
    data = crud.request_market_prod_list(market_name)
    return render_template("market.html", data_struct=data)


if __name__ == '__main__':
    app.run()
