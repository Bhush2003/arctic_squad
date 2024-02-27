import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate(r"C:\Users\Harshal\Downloads\user-profile-fa7a7-firebase-adminsdk-3vt6t-b13404fe9f.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

data={
    'tasks':'making food',
    'status':'in progress'
}

doc_ref=db.collection('taskcollection').document()
doc_ref.set(data)

print('document id',doc_ref.id)
