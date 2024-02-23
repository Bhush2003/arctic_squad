import customtkinter
from google.cloud import firestore
import json

credentials_path="C:/Users/bhushan chaudhari/Downloads/patientsignuppage-firebase-adminsdk-z4pcd-7708f0747a.json"

with open(credentials_path)as json_file:
    credential_info=json.load(json_file)
db=firestore.Client.from_service_account_info(credential_info)
class PatientSignupApp:
    def __init__(self):
        self.window = customtkinter.CTk(fg_color="#21f63d")
        self.windowColor = customtkinter.set_appearance_mode("light")
        self.theme = customtkinter.set_default_color_theme("green")
        self.window.title("Patient Signup")
        self.window.geometry('1000x700')

        self.patientSinupFrame = customtkinter.CTkFrame(master=self.window, width=1100, height=1000, fg_color="#CAD9F8")
        # self.patientSinupFrame.pack_propagate(False)
        self.patientSinupFrame.pack(padx=200, pady=200)

        self.patientSignup()

    def patientSignup(self):
        self.label_Fname = customtkinter.CTkLabel(self.patientSinupFrame, text="First Name:")
        self.entry_Fname = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_Lname = customtkinter.CTkLabel(self.patientSinupFrame, text="Last Name:")
        self.entry_Lname = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_Mname = customtkinter.CTkLabel(self.patientSinupFrame, text="Middle Name:")
        self.entry_Mname = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_age = customtkinter.CTkLabel(self.patientSinupFrame, text="Age:")
        self.entry_age = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_phone = customtkinter.CTkLabel(self.patientSinupFrame, text="Phone NO.:")
        self.entry_phone = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_email = customtkinter.CTkLabel(self.patientSinupFrame, text="Email:")
        self.entry_email = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_abha = customtkinter.CTkLabel(self.patientSinupFrame, text="Abha Id:")
        self.entry_abha = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_Username = customtkinter.CTkLabel(self.patientSinupFrame, text="User Name:")
        self.entry_Username = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_passward = customtkinter.CTkLabel(self.patientSinupFrame, text="Password:")
        self.entry_passward = customtkinter.CTkEntry(self.patientSinupFrame)

        self.label_cpassward = customtkinter.CTkLabel(self.patientSinupFrame, text="Confirm Password:")
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

        self.signup_button = customtkinter.CTkButton(self.patientSinupFrame, text="Signup")
        self.signup_button.place(x=220,y=220,anchor="nw")

    def get_patient_information(self):
        self.getFname=self.entry_Fname.get()
        self.getLname=self.entry_Lname.get()
        self.getMname=self.entry_Mname.get()
        self.getAge=self.entry_age.get()
        self.getPhone=self.entry_phone.get()
        self.getemail=self.entry_email.get()
        self.getabha=self.entry_abha.get()
        self.getusername=self.entry_Username.get()
        self.getpassward=self.entry_passward.get()
        self.getcpassward=self.entry_cpassward.get()

        self.user_profile_ref=db.collection('user_profile')
        self.user1={'Fname':self.getFname}

if __name__ == "__main__":
    app = PatientSignupApp()
    app.window.mainloop()
