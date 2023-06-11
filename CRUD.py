import firebase_admin
import json

from firebase_admin import credentials, db

# /////////////////////////////////////
# ///////////// FIREBASE /////////////
# /////////////////////////////////////
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "prueba-cf26f",
  "private_key_id": "8ac134b614f7758618ea8a340ed9ca7851361e89",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDU15w7a0exiazV\n1qB75B9RPztEf2UsmuwtBs7n+c3L4uYVb/8eNYEHUDX3woUH1lxcEkfOljtAHL9f\n3nWpkYSSjT5404zRDHMhSYKaL11gT4MgpvG6a4XmpGqtN6xTywtbCHDCgbluemeN\nxMuEDcaw7JPL2Hb40ZeAIxFzv3dGuxKQFj5dzd3ICKOpMH8WuArROKtqBfHXy+dq\n8WKLe9hluJSOwTJRzu2Cn0RxyQFIIYC1eobW8DTjhnDP0DfPUSAY9ifRAoT2Xe/r\n2Urf031KPzRcgFDZyjEb4ujwIoIUNH70rEGUaIRzphuEAHBzDNxPp/Hw0+vBRD2X\nFUKR5t+JAgMBAAECggEAEjr5AmRjFsdzbrn0U0RD8/Ax7gEo6/AFlmo4vukYOdRQ\nj4nBHOfpijQyOStXvGb9kHPO43id8NT9hdM+ugRRKgHP1ebNzwqNUm6y0WzI51LM\nKRfviL+Er6+JxRYpjCBOM9EGYnycwsQYek2+vkv1Rqpu0tUSxKdkHfky+Zpu15eO\nm4ziZkYEnN9V1gF11Si7gL+vocAxt2iA4v45bfFqMt/gGwQhRkVu38zpPm51Hwqt\nh/tMCxEadotitTf4Yn2JAExvE1ZIuF+HiLS+jdnSys4PlrIX/I5tirmF5yHTYCOk\np3ZcB7OqH1iNg43xiWgqCrgEQGb4U78o2lZwO58rEQKBgQD1JHGoHObwrwmX4B40\nloOMLysOiimvrO5nhw6Wrcb0XzQXSOc25jYN8JHgAE8TD88LGUGxIuzGW20UZhP5\naEXdrYKD1UqMAXE7Ub1dQOU6QYnGWbym+on5nhzx4auqvZE+ipILms/JE3rj/2SW\nl0LkvarLbF9Y6aJML47nFHPsUQKBgQDeRO4WhGEC3igExnD7FzloLc7R1LNhZZEA\nDvpZbz8BfBcprW7u3cFI0SmuyYUIddGWNIGS/pPCjYKcw11SqKaknCZZ1W2NpswF\npiorA0BA9ur8lwfKJ2EvWXftsF0+q53io6rJL7Fa/nOKvi6KzYLQStMh1cytq9LT\nz/WQFl5JuQKBgQCsKjM0eU/sG1Jmer1b+5VZv8rChGAwhAhPZzfktRk0iSRhcg8I\nrHesJJeetTjTz1d+mPdc+4VE7fLWz7YZhJUE0hYGlqarW1v16DtRIgGbf2nOhzmK\nIA0E5Xm4muBgopA+Vz2orspdkrPNKpGvfX46fcZU5cC1Bii4zvHS8rdTcQKBgQC0\nVHJiPGbEv97x+NojLTV7K2cX4JzkkVWyGXTN6K7Sko3sV3SgQbQWUvShhYf0VDqF\nxfW2f+r7tnnYm7x0WrZQ6QtIaRtoCIKQtr6RhSK1Ul9WLWa5gXecxdbCNguA1BXV\nkfn3HkWjULwHPcNfA9t1CLABTIeyA6yaAqf1jeBTqQKBgQC1wgc6RxKSXLix//Qn\nx3vD9jmE9/X+TQCMDFC4QglACA6FoY3sl2CtkDFmw9MDiuH4Ntj+tLutJ7pnCAEs\nZSCNbKrlAlZDXj7SwtLIJ6un65AaETh/8/jE3FdHkaR29IwD1pKUJB1r9qwseHmO\nivD7Fa+DIdcp4NMbWa7CKHA9KQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-cc2z5@prueba-cf26f.iam.gserviceaccount.com",
  "client_id": "112909101333845904866",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cc2z5%40prueba-cf26f.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})

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
    except Exception as e:
        print("ERROR on JSON")
        print(e)
        return "ERROR"