from django.shortcuts import render

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# docs = db.collection("cliente").stream()

# for doc in docs:
#     print(doc.id, doc.reference, doc.get('nome'), doc.to_dict())


# print(context)

# doc_ref = db.collection("cliente")

# doc_ref.add({
#     "nome":"Atila3"
# })


def index(request):
    docs = db.collection("cliente").stream()

    id = []
    nome = []
    teste = []
    for doc in docs:
        id.append(doc.id)
        nome.append(doc.get('nome'))
        teste.append((doc.id, doc.get('nome')))
        # print(doc.id, doc, doc.get('nome'), doc.to_dict())

    context = {
        'id': id,
        'nome': nome,
        'teste':teste
    }

    return render(request, 'index.html', context)
