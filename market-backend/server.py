from flask import *
import CRUD

app = Flask(__name__)
crud = CRUD

@app.route('/')
def start_method():  # put application's code here
    return 'main'


@app.route("/insert", methods=['POST'])
def insert_price():
    try:
        market = request.values.get("market")
        if(market is not None):
            path = f'/{market}'
            # check stock
            data = {
                'product': request.values.get('product'),
                'price': request.values.get('price'),
            }
            # get values and temporally insert
            crud.create(path,data)
            return data
        return abort(404)
    except:
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
    try:
        market = request.values.get("market")
        if market is not None:
            path = f'/{market}'
            # get values and temporally insert
            response = {}
            iter = 0
            for _item in crud.read(path):
                response.update({f'item-{iter}': f'{_item[1]}'})
                iter+=1
            return response
        return abort(404)
    except:
        return abort(404)