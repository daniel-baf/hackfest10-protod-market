from flask import *
from flask_cors import CORS

import CRUD
from lib import HANDLER

app = Flask(__name__)
CORS(app)

crud = CRUD
handler = HANDLER


@app.route('/')
def start_method():  # put application's lib here
    return render_template("index.html")


@app.route("/market/<name>")
def redirect_to_market_page(name):
    # request data to FIREBASE AND DISPLAY IT
    data = handler.request_market_prod_list(name)

    # for _item_key, _item_data in data["items"].items():
    #     price = _item_data["price"]
    #     name = _item_data["product"]
    #     print(f"Item: {_item_key}, Name: {name}, Price: {price}")
    # return data
    return render_template("market.html", data_struct=data)


@app.route("/insert", methods=['POST'])
def insert_price():
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


@app.route("/update", methods=["POST"])
def update_product():
    try:
        market = request.values.get("market")
        if market is not None:
            path = f'/{market}'
            # get values and temporally insert
            crud.update(path, 'product', 'price', request.values.get('product'), request.values.get('price'))
            return 'ACTUALIZADO'
        return abort(404)
    except:
        return abort(404)


@app.route('/delete', methods=["GET"])
def delete_product():
    try:
        market = request.values.get("market")
        if market is not None:
            path = f'/{market}'
            # get values and temporally insert
            crud.delete(path, 'product', request.values.get('product'))
            return 'BORRADO'
        return abort(404)
    except:
        return abort(404)


@app.route('/read', methods=["GET"])
def read_products():
    return handler.request_market_prod_list(request.args.get("market"))


if __name__ == "__main__":
    app.run()
