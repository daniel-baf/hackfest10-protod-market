from flask import Flask, render_template, request, abort
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
    # request basic data for select
    basket_list = crud.request_basic_market()
    return render_template("aporte.html", market_produts=basket_list)


@app.route("/market/<market_name>")
def redirect_to_market_page(market_name):
    # request data to FIREBASE AND DISPLAY IT
    data = crud.request_market_prod_list(market_name)
    return render_template("market.html", data_struct=data)

@app.route("/new-item", methods=["POST"])
def insert_product():
    try:
        _market = request.values.get("market-select")
        
        # return(_market + "<br>" + request.values.get("product-select") + "<br>" + request.values.get("input-price"))

        if _market is not None:
            path = f'/{_market}'
            data = {
                'product': request.values.get("product-select"),
                'price': request.values.get("input-price"),
            }
            crud.create(path, data)
            return "insertado"
        print("hola")
        return abort(404)
    except Exception as e:
        print("adios")
        print(e)
        return abort(404)



if __name__ == '__main__':
    app.run()
