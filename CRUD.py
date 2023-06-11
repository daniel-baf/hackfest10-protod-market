import firebase_admin
import json

from firebase_admin import credentials, db

# /////////////////////////////////////
# ///////////// FIREBASE /////////////
# /////////////////////////////////////
cred = credentials.Certificate("./clave.json")
firebase_admin.initialize_app(cred)


# path = market, keyindex = col, valueIndex = value
def delete(path: str, key_index: str, value_index):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    doc = ref.get()
    for k, v in doc.items():
        if v[key_index] == value_index:
            ref.child(k).set({})


# key index = product, path = market, keyAIm=price, valueIndex = product, valueAim = price
def update(path: str, key_index: str, key_aim: str, value_index, value_aim):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    doc = ref.get()
    for k, v in doc.items():
        if v[key_index] == value_index:
            obj = {key_aim: value_aim}
            ref.child(k).update(obj)


def read(path: str):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    data = ref.get().items()
    return data


def create(path: str, obj: dict):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    ref.push().set(obj)


# /////////////////////////////////////
# ///////////// REQUESTS //////////////
# /////////////////////////////////////
def request_market_prod_list(market):
    data = {"market": market, "items": {}}

    try:
        if market is not None:
            path = f'/{market}'
            _iter = 0
            for _item in read(path):
                try:
                    data["items"][f'item-{_iter}'] = {"product": _item[1]["product"], "price": _item[1]["price"]}
                    _iter += 1
                except Exception:  # do nothing
                    print("error on loop")
        return data
    except Exception:
        return "unable to connect to firebase"


def request_basic_market():
    try:
        file = open('./basket.json')
        data = json.load(file)
        file.close()
        return data
    except:
        print("ERROR on JSON")
        return "ERROR"