import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate(r"C:/Users/Harshal/Downloads/user-profile-fa7a7-firebase-adminsdk-3vt6t-b13404fe9f.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

# data={
#     'tasks':'making food',
#     'status':'in progress'
# }

#doc_ref=db.collection('RecordsCollection').add({'Hospital':'Harshal','Doctor':'Dr.Wadekar'})
# doc_ref.set(data)
result = db.collection("RecordsCollection").get()

#print('document id',doc_ref.id)
for i in range(2):
    x=result[i].to_dict().get('Diagnosis')
    y=result[i].to_dict().get('Doctor')
    z=result[i].to_dict().get('Hospital')
    a=result[i].to_dict().get('Symptoms')
    print(f'Diagnosis : {x}')
    print(f'Doctor : {y}')
    print(f'Hospital : {z}')
    print(f'Symptoms : {a}')
    print('----------------------------------------')