from django.shortcuts import render
from django.shortcuts import redirect

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

    teste = []
    for doc in docs:
        teste.append((doc.id, doc.get('nome')))
        # print(doc.id, doc, doc.get('nome'), doc.to_dict())

    context = {
        'teste':teste
    }

    return render(request, 'index.html', context)

def create_view(request):

    nome = request.POST.get("nome", "")

    doc_ref = db.collection("cliente")

    doc_ref.add({
        "nome":nome
    })

    return redirect('/')

def delete(request):

    id = request.POST.get("id", "")

    doc_ref = db.collection("cliente")

    doc_ref.document(id).delete()

    return redirect('/')

def edit(request):

    id = request.POST.get("id", "")

    doc_ref = db.collection("cliente").document(id).get()

    docs = db.collection("cliente").stream()

    teste = []
    for doc in docs:
        teste.append((doc.id, doc.get('nome')))
        # print(doc.id, doc, doc.get('nome'), doc.to_dict())

    context = {
        'teste':teste,
         'editNome': doc_ref.get('nome'),
         'editId': request.POST.get("id", ""),
    }

    return render(request, 'index.html', context)

def salvar(request):

    id = request.POST.get("id", "")
    alteracao = request.POST.get("nome", "")

    doc_ref = db.collection("cliente")

    doc_ref.document(id).update({"nome":alteracao})

    return redirect('/')