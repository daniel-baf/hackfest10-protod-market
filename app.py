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
    # request basic data for select
    basket_list = crud.request_basic_market()
    for _item in basket_list.items():
        # for _item_key, _item_data in _item.items():
        _item_key = _item[0]
        _item_value = _item[1]["value"]
        _item_price = _item[1]["price"]

        # print(f'key {_item_key} value {_item_value} price {_item_price}')
    return render_template("aporte.html", market_produts=basket_list)


@app.route("/market/<market_name>")
def redirect_to_market_page(market_name):
    # request data to FIREBASE AND DISPLAY IT
    data = crud.request_market_prod_list(market_name)
    return render_template("market.html", data_struct=data)

@app.route("/new-item/", methods=["POST"])
def insert_product():
    try:
        market = request.values.get("market")
        if market is not None:
            path = f'/{market}'
            data = {
                'product': request.values.get('product'),
                'price': request.values.get('price'),
            }
            # get values and temporally insert
            crud.create(path, data)
            return data
        return abort(404)
    except Exception:
        return abort(404)


if __name__ == '__main__':
    app.run()
