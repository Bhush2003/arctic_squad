import customtkinter
import tkinter
from  tkinter import messagebox 
from PIL import ImageTk, Image
import webbrowser
from record import App
from profile import Progress
from signUp import PatientSignupApp
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

class MainWindow():
    
    def __init__(self,root,window_width):
        self.root=root
        self.window_width=window_width
        # self.windowColor=customtkinter.set_appearance_mode("light")
        # self.theme=customtkinter.set_default_color_theme("green")
        # self.window_width=self.root.winfo_screenwidth()
        # self.window_height=self.root.winfo_screenheight()
        # self.root.geometry(f"{self.window_width}x{self.window_height}")

        
        self.dashbord()

    def mainLogin(self):
        self.loginbutton2 = customtkinter.CTkButton(self.introFrame, text="LogIn", font=("Roboto",25), corner_radius=2, fg_color="#00157c", hover_color="#00b4d8", command=self.create_login_frame)
        self.loginbutton2.place(relx=0.2, rely=0.2, anchor="nw")


    def dashbord(self):

        self.dashbordFrame = customtkinter.CTkFrame(self.root, width=self.window_width, height=60, fg_color='#00157c',corner_radius=0)
        self.dashbordFrame.pack()

        self.nameLabel=customtkinter.CTkLabel(self.dashbordFrame,text=" MedVault",font=('Roboto',22),text_color='white')
        self.nameLabel.place(x=1,y=20,anchor="nw")

        self.img2=customtkinter.CTkImage(Image.open('C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/log4.png'))
        self.b2=customtkinter.CTkButton(master=self.dashbordFrame,fg_color='#191970',width=0.8,text='Login',font=('Roboto',18),text_color='white',hover=True,image=self.img2,hover_color='#008b8b',command=self.create_login_frame)
        self.b2.place(x=self.window_width-160,y=20,anchor="nw")

        self.intro()

    def dashbordLabels(self):
        self.logoutButton = customtkinter.CTkButton(self.dashbordFrame,fg_color="#191970",width=0.8,text='LogOut',font=('Roboto',18),text_color='white',hover=True,image=self.img2,hover_color='#008b8b',command=self.logout)
        self.logoutButton.place(x=self.window_width-160,y=20,anchor="nw")

        # self.healthButton=customtkinter.CTkButton(self.dashbordFrame,fg_color="#191970",width=0.8,text='Health',font=('Roboto',18),text_color='white',hover=True,hover_color='#008b8b',command=self.health)
        # self.healthButton.place(x=self.window_width-230,y=20,anchor="nw")

        self.profileButton=customtkinter.CTkButton(self.dashbordFrame,fg_color="#191970",width=0.8,text='Profile',font=('Roboto',18),text_color='white',hover=True,hover_color='#008b8b',command=self.profile)
        self.profileButton.place(x=self.window_width-300,y=20,anchor="nw")

        self.historyButton = customtkinter.CTkButton(self.dashbordFrame,fg_color="#191970",width=0.8,text='History',font=('Roboto',18),text_color='white',hover=True,hover_color='#008b8b',command=self.history)
        self.historyButton.place(x=self.window_width-370,y=20,anchor="nw")

        self.homeButton = customtkinter.CTkButton(self.dashbordFrame,fg_color="#191970",width=0.8,text='Home',font=('Roboto',18),text_color='white',hover=True,hover_color='#008b8b',command=self.home)
        self.homeButton.place(x=self.window_width-430,y=20,anchor="nw")

    

        

    def intro(self):

        self.introFrame= customtkinter.CTkScrollableFrame(self.root, width=1600, height=1000, fg_color='#caf0f8',border_width=2,border_color='#76D7C4')
        self.introFrame.pack()

        self.sloganLabel=customtkinter.CTkLabel(self.introFrame,text="Your Care. Your Way.",text_color="#00157c",font=("Algerian",55))
        self.sloganLabel.place(relx=0.03,rely=0.1,anchor="w")

        self.mainLogin()

        image = Image.open('C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/doc.png')
        tk_image = ImageTk.PhotoImage(image)
        image_label1 = customtkinter.CTkLabel(self.introFrame, image=tk_image,text='')
        image_label1.pack(padx=20, pady=30, anchor='ne')

        self.messageFrame=customtkinter.CTkFrame(self.introFrame,width=1000,height=100,fg_color="#caf0f8")
        self.messageFrame.pack(padx=300,pady=20,anchor="nw")

        self.missionStatement = "Our Vision at MedVault is to empower individuals through user-friendly \nmonitoring tools and personalized insights, fostering a supportive community\n to promote healthier lifestyles and improve overall well-being."
        self.statementLabel =customtkinter.CTkLabel(self.messageFrame,text=self.missionStatement,text_color="#00157c",font=("Georgia",22))
        self.statementLabel.place(anchor="nw")
        self.patners()

    def patners(self):

        self.patnersLabel = customtkinter.CTkLabel(self.introFrame,text="Our Major Patners",font=("Roboto",24),text_color="#03045e").pack(padx=180,anchor="nw")

        self.patnersFrame=customtkinter.CTkFrame(self.introFrame,width=1200,height=360,fg_color="#caf0f8",border_width=0,border_color="#6464ff")
        self.patnersFrame.pack(padx=180,anchor="nw")

        self.hospitallogo1 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h1.png")
        self.hospitallogo2 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h2.png")
        self.hospitallogo3 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h3.png")
        self.hospitallogo4 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h4.png")
        self.hospitallogo5 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h5.png")
        self.hospitallogo6 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h6.png")
        self.hospitallogo7 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h7.png")
        self.hospitallogo8 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h8.png")
        self.hospitallogo9 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h9.png")
        self.hospitallogo10 = Image.open("C:/Users/Harshal/OneDrive/Desktop/PythonXProject/PythonXProject/resources/h1.png")

        self.logo1Image = ImageTk.PhotoImage(self.hospitallogo1)
        self.logo2Image = ImageTk.PhotoImage(self.hospitallogo2)
        self.logo1ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo1Image,text="",fg_color="#caf0f8",command=self.open_url1)
        self.logo1ImageButton.grid(column=0,row=0)
        self.logo2ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo2Image,text="",fg_color="#caf0f8",command=self.open_url2) 
        self.logo2ImageButton.grid(column=1,row=0)
        self.logo3Image = ImageTk.PhotoImage(self.hospitallogo3)
        self.logo4Image = ImageTk.PhotoImage(self.hospitallogo4)
        self.logo3ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo3Image,text="",fg_color="#caf0f8",command=self.open_url3) 
        self.logo3ImageButton.grid(column=2,row=0)
        self.logo4ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo4Image,text="",fg_color="#caf0f8",command=self.open_url4) 
        self.logo4ImageButton.grid(column=3,row=0)
        self.logo5Image = ImageTk.PhotoImage(self.hospitallogo5)
        self.logo6Image = ImageTk.PhotoImage(self.hospitallogo6)
        self.logo5ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo5Image,text="",fg_color="#caf0f8",command=self.open_url5) 
        self.logo5ImageButton.grid(column=4,row=0)
        self.logo6ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo6Image,text="",fg_color="#caf0f8",command=self.open_url6) 
        self.logo6ImageButton.grid(column=0,row=1)
        self.logo7Image = ImageTk.PhotoImage(self.hospitallogo7)
        self.logo8Image = ImageTk.PhotoImage(self.hospitallogo8)
        self.logo7ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo7Image,text="",fg_color="#caf0f8",command=self.open_url7) 
        self.logo7ImageButton.grid(column=1,row=1)
        self.logo8ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo8Image,text="",fg_color="#caf0f8",command=self.open_url8) 
        self.logo8ImageButton.grid(column=2,row=1)
        self.logo9Image = ImageTk.PhotoImage(self.hospitallogo9)
        self.logo10Image = ImageTk.PhotoImage(self.hospitallogo10)
        self.logo9ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo9Image,text="",fg_color="#caf0f8",command=self.open_url9) 
        self.logo9ImageButton.grid(column=3,row=1)
        self.logo10ImageButton = customtkinter.CTkButton(self.patnersFrame,image=self.logo10Image,text="",fg_color="#caf0f8",command=self.open_url10) 
        self.logo10ImageButton.grid(column=4,row=1)

        self.aboutUsFrame = customtkinter.CTkFrame(self.introFrame,width=1550,height=650,fg_color="#caf0f8",border_color="#6464ff",border_width=1)
        self.aboutUsFrame.pack(padx=400,pady=20,anchor="nw")

        self.aboutMedVault = "ABOUT MEDVAULT"
        self.aboutMedVaultLabel = customtkinter.CTkLabel(self.aboutUsFrame,text=self.aboutMedVault,text_color="#00157c",font=("Algerian",25))
        self.aboutMedVaultLabel.pack(pady=20)

        self.ourMissionText = "Our mission:"
        self.ourMissionLabel = customtkinter.CTkLabel(self.aboutUsFrame,text=self.ourMissionText,text_color="#00157c",font=("Algerian",23))
        self.ourMissionLabel.pack(padx=5,anchor="nw")

        self.MissionText = "Provide services that focus healthcare resources on existing and emergent \nthreats to community health."
        self.MissionLabel = customtkinter.CTkLabel(self.aboutUsFrame,text=self.MissionText,text_color="#00157c",font=("Georgia",21))
        self.MissionLabel.pack(padx=10)

        self.ourCustomersText = "Our customers:"
        self.ourCustomersLabel = customtkinter.CTkLabel(self.aboutUsFrame,text=self.ourCustomersText,text_color="#00157c",font=("Algerian",23))
        self.ourCustomersLabel.pack(padx=5,anchor="nw")

        self.ourCustomersText = "State and local public health departments and health systems.\n We currently serve Pune,  Nagpur, and several counties in India, \ncovering a total of more than 40 million people."
        self.ourCustomersLabel = customtkinter.CTkLabel(self.aboutUsFrame,text=self.ourCustomersText,text_color="#00157c",font=("Georgia",21))
        self.ourCustomersLabel.pack(padx=10)

        self.whatWeDoText = "What we do"
        self.whatWeDoLabel = customtkinter.CTkLabel(self.aboutUsFrame,text=self.whatWeDoText,text_color="#00157c",font=("Algerian",23))
        self.whatWeDoLabel.pack(padx=5,anchor="nw")

        self.whatWeDoStatementText = "Monitor real-time health-related data for community health indicators. \nWe collect data from nearly 600 hospitals and \n3,600 ambulatory systems."
        self.whatWeDoStatementLabel = customtkinter.CTkLabel(self.aboutUsFrame,text=self.whatWeDoStatementText,text_color="#00157c",font=("Georgia",21))
        self.whatWeDoStatementLabel.pack(padx=10)

    def open_url1(self):
        webbrowser.open("http://www.wadiahospitals.org/")

    def open_url2(self):
        webbrowser.open("https://rubyhall.com/")

    def open_url3(self):
        webbrowser.open("https://sahyadrihospital.com/")

    def open_url4(self):
        webbrowser.open("https://www.narayanahealth.org/hospitals")

    def open_url5(self):
        webbrowser.open("https://www.medanta.org/hospitals-near-me/gurugram-hospital")

    def open_url6(self):
        webbrowser.open("https://www.apollohospitals.com/delhi/")

    def open_url7(self):
        webbrowser.open("https://mgmhealthcare.in/")

    def open_url8(self):
        webbrowser.open("https://www.maxhealthcare.in/")

    def open_url9(self):
        webbrowser.open("https://www.amrihospitals.in/")

    def open_url10(self):
        webbrowser.open("https://www.hindujahospital.com/")   
        
    def patientSignUp(self):
        
        self.frame.destroy()

        self.patientSinupFrame = customtkinter.CTkFrame(master=self.introFrame, width=600, height=350, fg_color="#CAD9F8",border_color='blue',border_width=1)
        self.patientSinupFrame.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.signUpObj = PatientSignupApp(self.root,self.patientSinupFrame,self.create_login_frame)



    

    def create_login_frame(self):

        self.loginbutton2.destroy()
        try:
            self.patientSinupFrame.destroy()
        except:
            pass

        self.frame = customtkinter.CTkFrame(self.root, width=340, height=360, fg_color='#cad9f8')
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Log into your Account", font=("Roboto", 20))
        self.l2.place(x=50, y=45)

        self.entry1 = customtkinter.CTkEntry(self.frame, width=220, placeholder_text="Username")
        self.entry1.place(x=50, y=110)

        self.entry2 = customtkinter.CTkEntry(self.frame, width=220, placeholder_text="Password",show="*")
        self.entry2.place(x=50, y=150)

        self.l3 = customtkinter.CTkButton(self.frame, text="Forgot password ?", font=("Roboto", 10), text_color='white',
                                     fg_color='#00458B', hover=True, hover_color='#3FD2C7', width=0.3)
        self.l3.place(x=175, y=185)

        self.button1 = customtkinter.CTkButton(self.frame, text="LOGIN", fg_color='green', hover=True, command=self.login_button,
                                          hover_color=['black', 'blue'])
        self.button1.place(x=90, y=220)

        self.l4 = customtkinter.CTkLabel(master=self.frame, text="New Register", font=("Roboto", 10), text_color='black')
        self.l4.place(x=100, y=250)

        self.button2 = customtkinter.CTkButton(self.frame, text="SignUp", font=('Roboto', 10), text_color='white',
                                          fg_color='#00458B', hover=True, width=0.5, height=0.3, hover_color='#3FD2C7',corner_radius=5,command=self.patientSignUp)
        self.button2.place(x=170, y=255)


    def loginCreditionalsCheck(self):
        self.loginFields = [(self.entry1,"Username"),(self.entry2,"Password")]

        for loginField, loginLabel in self.loginFields:
            if isinstance(loginField, customtkinter.CTkEntry) and not loginField.get():
                raise ValueError(f"Please fill in {loginLabel}")


    def login_button(self):
        
        email=f'{self.entry1.get()}'
        password=f'{self.entry2.get}'
        auth.create_user_with_email_and_password(email,password)

        try:
            self.loginCreditionalsCheck()  # Check if all fields are filled
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Display error message
            return

        self.welcome()
        self.b2.destroy()
        self.dashbordLabels()
        self.frame.destroy()

    def welcome(self):

        self.welcomeLabel = customtkinter.CTkLabel(self.introFrame,text="Welcome To MedVault",font=("Algerian",50),text_color="#00157c")
        self.welcomeLabel.place(relx=0.1, rely=0.15, anchor="nw")

    def home(self):

        try:
            self.healthFrame.pack_forget()
        except:
            pass

        try:
            self.profileFrame.pack_forget()
        except:
            pass

        try:
            self.historyFrame.pack_forget()
        except:
            pass


        


        self.introFrame.pack()


    # def patientSignUp(self):
        
    #     self.frame.pack_forget()

    #     self.patientSinupFrame = customtkinter.CTkFrame(master=self.root, width=600, height=600, fg_color="#CAD9F8")
    #     self.patientSinupFrame.pack(padx=200, pady=200)

    #     self.signUpObj = PatientSignupApp(self.root,self.patientSinupFrame,self.create_login_frame)


    def logout(self):

        self.loginbutton2.place(relx=0.2, rely=0.2, anchor="nw")
        self.b2.place(x=self.window_width-160,y=20,anchor="nw")

        self.historyButton.destroy()
        self.profileButton.destroy()
        self.homeButton.destroy()
        self.logoutButton.destroy()




    def health(self):

        self.introFrame.pack_forget()

        self.healthFrame =customtkinter.CTkScrollableFrame(self.root, width=1600, height=1000, fg_color='#caf0f8',border_width=2,border_color='#76D7C4')
        self.healthFrame.pack()

        self.bmiFrame = customtkinter.CTkFrame(self.healthFrame,width=500)
        
        

    def profile(self):
        self.introFrame.pack_forget()
        try:
            self.healthFrame.pack_forget()
        except:
            pass      

        self.profileFrame = customtkinter.CTkScrollableFrame(self.root, width=1200, height=1000, border_width=2, border_color="#76D7C4")
        self.profileFrame.pack(pady=50)
        self.profileObj = Progress(self.root,self.window_width,self.profileFrame)

    def history(self):

        try:
            self.healthFrame.pack_forget()
        except:
            pass
        
        self.historyFrame = customtkinter.CTkScrollableFrame(self.root, width=1200, height=1000, border_width=2, border_color="#76D7C4")
        self.historyFrame.pack(pady=50)

        self.introFrame.pack_forget()
       
        self.historyObj = App(self.root,self.historyFrame)




    def run(self):
        self.root.mainloop()

if __name__=="__main__":
    app=MainWindow()
    app.run()












