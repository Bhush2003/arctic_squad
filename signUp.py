import customtkinter
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# cred = credentials.Certificate(r"C:\Users\Harshal\Downloads\user-profile-fa7a7-firebase-adminsdk-3vt6t-b13404fe9f.json")
# firebase_admin.initialize_app(cred)
# db=firestore.client()



#Authentication

# email=input('Enter your email:-')
# password=input('enter your password:-')


# auth.sign_in_with_email_and_password(email,password)
# print("Successfully loged in ")

# auth.create_user_with_email_and_password(email,password)
# print('SignedIn successfully')


# credentials_path="C:/Users/bhushan chaudhari/Downloads/patientsignuppage-firebase-adminsdk-z4pcd-7708f0747a.json"

# with open(credentials_path)as json_file:
#     credential_info=json.load(json_file)
# db=firestore.Client.from_service_account_info(credential_info)
class PatientSignupApp:
    
    def __init__(self,root,frame,create_login_frame):

        self.window = root
        self.patientSinupFrame = frame
        self.create_login_frame = create_login_frame
        # self.windowColor = customtkinter.set_appearance_mode("light")
        # self.theme = customtkinter.set_default_color_theme("green")
        # self.window.title("Patient Signup")
        # self.window.geometry(f'{self.window.winfo_screenwidth()} x {self.window.winfo_screenheight()}')

        self.patientSignup()

    def patientSignup(self):
        self.label_Fname = customtkinter.CTkLabel(self.patientSinupFrame, text="First Name : ")
        self.entry_Fname = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_Lname = customtkinter.CTkLabel(self.patientSinupFrame, text="Last Name : ")
        self.entry_Lname = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_Mname = customtkinter.CTkLabel(self.patientSinupFrame, text="Middle Name : ")
        self.entry_Mname = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_age = customtkinter.CTkLabel(self.patientSinupFrame, text="Age : ")
        self.entry_age = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_phone = customtkinter.CTkLabel(self.patientSinupFrame, text="Phone NO. : ")
        self.entry_phone = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_email = customtkinter.CTkLabel(self.patientSinupFrame, text="Email : ")
        self.entry_email = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_abha = customtkinter.CTkLabel(self.patientSinupFrame, text="Abha Id : ")
        self.entry_abha = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_Username = customtkinter.CTkLabel(self.patientSinupFrame, text="User Name : ")
        self.entry_Username = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_passward = customtkinter.CTkLabel(self.patientSinupFrame, text="Password : ")
        self.entry_passward = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_cpassward = customtkinter.CTkLabel(self.patientSinupFrame, text="Confirm Password : ")
        self.entry_cpassward = customtkinter.CTkEntry(self.patientSinupFrame)

        

        # Packing labels and entries
        self.label_Fname.place(x=10,y=10,anchor="nw")
        self.entry_Fname.place(x=100,y=10,anchor="nw")

        self.label_Lname.place(x=280,y=10,anchor="nw")
        self.entry_Lname.place(x=400,y=10,anchor="nw")

        self.label_Mname.place(x=10,y=50,anchor="nw")
        self.entry_Mname.place(x=100,y=50,anchor="nw")

        self.label_age.place(x=280,y=50,anchor="nw")
        self.entry_age.place(x=400,y=50,anchor="nw")

        self.label_phone.place(x=10,y=90,anchor="nw")
        self.entry_phone.place(x=100,y=90,anchor="nw")

        self.label_email.place(x=280,y=90,anchor="nw")
        self.entry_email.place(x=400,y=90,anchor="nw")

        self.label_abha.place(x=10,y=130,anchor="nw")
        self.entry_abha.place(x=100,y=130,anchor="nw")

        self.label_Username.place(x=280,y=130,anchor="nw")
        self.entry_Username.place(x=400,y=130,anchor="nw")

        self.label_passward.place(x=10,y=170,anchor="nw")
        self.entry_passward.place(x=100,y=170,anchor="nw")

        self.label_cpassward.place(x=280,y=170,anchor="nw")
        self.entry_cpassward.place(x=400,y=170,anchor="nw")

        self.signup_button = customtkinter.CTkButton(self.patientSinupFrame, text="Signup",command=self.create_User())
        self.signup_button.place(x=220,y=250,anchor="nw")

    # def function1(self):
    #     self.create_User
    #     self.create_login_frame.destroy()
   
    def create_User(self):
        
        data={
        'FirstName':f'{self.entry_Fname.get()}',
        'LastName':f'{self.entry_Lname.get()}',
        'MiddleName':f'{self.entry_Mname.get()}',
        'Age':f'{self.entry_age.get()}',
        'Phone':f'{self.entry_phone.get()}',
        'Email':f'{self.entry_email.get()}',
        'abha_Id':f'{self.entry_abha.get()}',
        'username':f'{self.entry_Username.get()}',
        'password':f'{self.entry_passward.get()}',
        }
        del self.patientSinupFrame
        # doc_ref=db.collection('UserInfoCollection').document()
        # doc_ref.set(data)
        
        
if __name__ == "__main__":
    app = PatientSignupApp()
    app.window.mainloop()