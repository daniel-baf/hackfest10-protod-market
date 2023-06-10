import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("clave.json")
firebase_admin.initialize_app(cred)

# path = market, keyindex = col, valueIndex = value
def delete( path: str, keyIndex: str, valueIndex):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    doc = ref.get()
    for k, v in doc.items():
        if (v[keyIndex] == valueIndex):
            ref.child(k).set({})


#key index = product, path = market, keyAIm=price, valueIndex = product, valueAim = price
def update(path: str, keyIndex: str, keyAim: str, valueIndex, valueAim):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    doc = ref.get()
    for k, v in doc.items():
        if (v[keyIndex] == valueIndex):
            obj = {keyAim: valueAim}
            ref.child(k).update(obj)


def read(path: str):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    data = ref.get().items()
    return data


def create(path: str, obj: dict):
    ref = db.reference(path, None, "https://prueba-cf26f-default-rtdb.firebaseio.com/")
    ref.push().set(obj)


data = {
    'nombre': 'Jua',
    'correo': 'Juan@goole.com',
    'comentario': 'Hol'
}

# create(path='/comments', obj=data)

# datos = read(path='/comments')
# for _, comment in datos:
#    print(f'{comment["correo"]}')
#update(path='/comments', keyIndex="nombre", keyAim="correo", valueIndex="Juan", valueAim="Lopez@gmail.com")
#delete(path='/comments', keyIndex="correo", valueIndex="Lopez@gmail.com")