import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyC8syT4_Lykgkqu_nfZ7mBL-i5fPedwK7E",
  "authDomain": "user-profile-fa7a7.firebaseapp.com",
  "projectId": "user-profile-fa7a7",
  "storageBucket": "user-profile-fa7a7.appspot.com",
  "messagingSenderId": "1006259943723",
  "appId": "1:1006259943723:web:2762207bdeed829c946d6e",
  "measurementId": "G-FRE6J6412C",
  "databaseURL":"https://user-profile-fa7a7-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()

#Authentication

# email=input('Enter your email:-')
# password=input('enter your password:-')


# # auth.sign_in_with_email_and_password(email,password)
# # print("Successfully loged in ")

# auth.create_user_with_email_and_password(email,password)
# print('SignedIn successfully')

data={'age':'21','name':'Harshal','course':'Computer'}

