import tkinter
import customtkinter
from PIL import ImageTk, Image
import Signup,update_profile,update_records

import re
from datetime import datetime
from tkinter import ttk,messagebox
class MainWindow:
  
    def __init__(self):
        self.app = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark-blue")
        self.winWidth = self.app.winfo_screenwidth()
        self.height = self.app.winfo_screenheight()
        self.app.geometry(f"{self.winWidth}x{self.height}")
            
        frame1 = customtkinter.CTkFrame(master=self.app, width=self.winWidth, height=80, fg_color='#00157c',corner_radius=0)
        frame1.pack()

        l4=customtkinter.CTkLabel(frame1,text=" MedVault",font=('Roboto',22),text_color='white')
        l4.place(x=1,y=20,anchor="nw")

        img1=customtkinter.CTkImage(Image.open('resources\h1.png'))
        b1=customtkinter.CTkButton(master=frame1,fg_color='#191970',text='',width=0.1,image=img1,hover=True)
        b1.place(x=self.winWidth-60,y=5,anchor="nw")

        img2=customtkinter.CTkImage(Image.open('resources\h1.png'))
        b2=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.8,text='Login',font=('Roboto',18),text_color='#3498DB',hover=True,image=img2,hover_color='#FDFEFE')
        b2.place(x=self.winWidth-160,y=5,anchor="nw")

        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.7,text='History',font=('Roboto',18),text_color='blue',hover=True,hover_color='white')
        b3.place(x=self.winWidth-235,y=5,anchor="nw")
        
        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.7,text='Profile',font=('Roboto',18),text_color='blue',hover=True,hover_color='white',command=self.update_profile)
        b3.place(x=self.winWidth-335,y=5,anchor="nw")
        
        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.7,text='Records',font=('Roboto',18),text_color='blue',hover=True,hover_color='white',command=self.update_records)
        b3.place(x=self.winWidth-435,y=5,anchor="nw")

        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.6,text='Find Doctor',font=('Roboto',18),text_color='blue',hover=True,hover_color='white')
        b3.place(x=self.winWidth-560,y=5,anchor="nw")

        frame2= customtkinter.CTkScrollableFrame(master=self.app, width=1600, height=800, fg_color='white',border_width=2,border_color='#76D7C4')
        #frame2.pack_propagate(False)
        frame2.pack(pady=70)

        f2label=customtkinter.CTkLabel(frame2,text="TODAY'S TOP STORIES..",font=('Aerial',20),text_color='#191970')
        f2label.pack(padx=100,side=customtkinter.TOP,anchor=customtkinter.NW)

        image_path = 'D:/PYTHONX/mainproject/assets/image.jpg'  # Adjust the path to your image
        image = Image.open('resources\h1.png')
        tk_image = ImageTk.PhotoImage(image)
        image_label1 = customtkinter.CTkLabel(frame2, image=tk_image,text='')
        image_label1.pack(padx=20, pady=30, anchor='n')

        text_label = customtkinter.CTkLabel(frame2, text='Healthy Diet', font=('Aerial', 30), text_color='black')
        text_label.place(relx=0.5, rely=0.56,  anchor='s')

        paragraph_text = ("""Whether it's the lycopene – the pigment that gives tomatoes their red color – or 
                          Chances are you already know that eating too much sugar isn’t good for you. Yet you’re probably still overdoing it. 
                           Americans average about 270 calories of added sugars each day. That’s about 17  teaspoons a day,
                           compared to the recommended limits of about 12 teaspoon per day or 200 calories.

                         Sugary drinks, candy, baked goods, and sweetened dairy are the main sources of added sugar. But even some savory foods,
                           like breads, tomato sauce, and protein bars, can have sugar, making it all too easy to end up with a 
                          surplus of the sweet stuff. Added sugars may be hard to spot on nutrition labels since they can be listed
                           under a number of names, such as corn syrup, agave nectar, palm sugar, cane juice, or sucrose. """)
        paragraph_label = customtkinter.CTkLabel(frame2, text=paragraph_text, font=('Arial', 20), text_color='blue')
        paragraph_label.pack(padx=0,pady=40,anchor='se')
        cont_read1=customtkinter.CTkButton(master=frame2,text="Continue Reading",hover=True,fg_color='white',hover_color='gray',command=self.login)
        cont_read1.place(relx=0.5, rely=0.8,  anchor='s')
        self.app.mainloop()
        
    def login(self):
       run3= PatientSignupApp()
       run3.run()
       
    def update_profile(self):
      run1=Window()
      run1.run()
      
      
    def update_records(self):
      run2=App()  
      run2.run()
      

class PatientSignupApp:
    def __init__(self):
        self.window = customtkinter.CTk(fg_color="#21f63d")
        self.window.title("Patient Signup")
        self.window.geometry('600x400x200x200')

        self.root = customtkinter.CTkFrame(master=self.window, width=600, height=600)
        self.root.pack_propagate(False)
        self.root.pack()

        self.create_widgets()

    def create_widgets(self):
        self.label_Fname = customtkinter.CTkLabel(self.root, text="First Name:")
        self.label_Fname.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_Fname = customtkinter.CTkEntry(self.root)
        self.entry_Fname.grid(row=0, column=1, padx=10, pady=10)

        self.label_Lname = customtkinter.CTkLabel(self.root, text="Last Name:")
        self.label_Lname.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.entry_Lname = customtkinter.CTkEntry(self.root)
        self.entry_Lname.grid(row=0, column=3, padx=10, pady=10)

        self.label_Mname = customtkinter.CTkLabel(self.root, text="Last Name:")
        self.label_Mname.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_Mname = customtkinter.CTkEntry(self.root)
        self.entry_Mname.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_age = customtkinter.CTkLabel(self.root, text="Age:")
        self.label_age.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.entry_age = customtkinter.CTkEntry(self.root)
        self.entry_age.grid(row=1, column=3, padx=10, pady=10)

        self.label_phone = customtkinter.CTkLabel(self.root, text="Phone NO.:")
        self.label_phone.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_phone = customtkinter.CTkEntry(self.root)
        self.entry_phone.grid(row=3, column=1, padx=10, pady=10)

        self.label_email = customtkinter.CTkLabel(self.root, text="email")
        self.label_email.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.entry_email = customtkinter.CTkEntry(self.root)
        self.entry_email.grid(row=3, column=3, padx=10, pady=10)

        self.label_abha = customtkinter.CTkLabel(self.root, text="Abha Id:")
        self.label_abha.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.entry_abha = customtkinter.CTkEntry(self.root)
        self.entry_abha.grid(row=4, column=1, padx=10, pady=10)

        self.label_Username = customtkinter.CTkLabel(self.root, text="User Name:")
        self.label_Username.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        self.entry_Username = customtkinter.CTkEntry(self.root)
        self.entry_Username.grid(row=4, column=3, padx=10, pady=10)

        self.label_passward = customtkinter.CTkLabel(self.root, text="Password:")
        self.label_passward.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.entry_passward = customtkinter.CTkEntry(self.root)
        self.entry_passward.grid(row=5, column=1, padx=10, pady=10)

        self.label_cpassward = customtkinter.CTkLabel(self.root, text="Confirm Password:")
        self.label_cpassward.grid(row=5, column=2, padx=10, pady=10, sticky="w")

        self.entry_cpassward = customtkinter.CTkEntry(self.root)
        self.entry_cpassward.grid(row=5, column=3, padx=10, pady=10)

        self.signup_button = customtkinter.CTkButton(self.root, text="Signup",command=self.window.destroy)
        self.signup_button.grid(row=6, column=0, columnspan=2, pady=10)
    
    # def check_Data(self):
    #     fields=[(self.entry_Fname,)]
    def run(self):
        self.window.mainloop() 

  
class App:
    def __init__(self):
        
        self.root=customtkinter.CTk(fg_color='#58D68D')
        self.root.geometry(f'{self.root.winfo_screenheight()}x{self.root.winfo_screenwidth()}')
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')
       
        self.header_text=customtkinter.CTkLabel(self.root,text='RECORDS',pady=30,font=('Roboto',50))
        self.header_text.pack()
        
        self.addButton=customtkinter.CTkButton(self.root,width=70,height=50,text='Add',command=self.fill_Info)
        self.addButton.pack(side=customtkinter.TOP, anchor=customtkinter.NW,padx=700)
        
        self.base_Frame=customtkinter.CTkScrollableFrame(self.root,height=500,width=400,scrollbar_button_color='white')
        self.base_Frame.pack(side=customtkinter.LEFT, anchor=customtkinter.NW,padx=150)
        
        
        # self.info_storing_frame=customtkinter.CTkScrollableFrame(self.base_Frame,height=500,orientation='vertical',width=950,border_color='cyan',border_width=1)   
        # self.info_storing_frame.pack(side=customtkinter.TOP,anchor=customtkinter.CENTER,padx=60,pady=100)
        
        
    def fill_Info(self):    
        
        self.input_Taking_frame=customtkinter.CTkFrame(self.root,height=500,width=400,border_color='cyan',border_width=1)
        self.input_Taking_frame.pack(side=customtkinter.TOP,anchor=customtkinter.CENTER,padx=30)
        
        self.hospital=customtkinter.CTkLabel(self.input_Taking_frame,text='Hospital : ',font=('Roboto',20))
        self.hospital.place(x=20,y=20,anchor='nw')
        
        self.hospital_Entry=customtkinter.CTkOptionMenu(self.input_Taking_frame,values=[
    "Ruby Hall Clinic","Jehangir Hospital","Deenanath Mangeshkar Hospital","Sancheti Hospital","Poona Hospital and Research Centre","KEM Hospital",
    "Columbia Asia Hospital","Sahyadri Hospital","Inamdar Multispeciality Hospital","Aditya Birla Memorial Hospital","Noble Hospital",
    "Medipoint Hospital","Criticare Hospital","Hardikar Hospital","Apollo Jehangir Hospital","Ratna Memorial Hospital","Lokmanya Hospital",
    "Kotbagi Hospital","Sanjeevani Hospital","Cedar Hospitals","Joshi Hospital","Vinayak Hospital","Kulkarni Hospital","Gokhale Hospital",
    "Shashwat Hospital","Bharati Hospital","Ranka Multispeciality Hospital","Niramaya Hospital","Poona Surgical and Maternity Hospital","Rising Medicare Hospital",
    "Lifeline Hospital","Noble Institute of Medical Sciences","Vinayak Netralaya","Kataria Multispeciality Hospital","Silver Star Hallmark Hospital",
    "Lakshya Hospital","Siddharth Hospital","Sathe Hospital","Dr. Parakh Hospital","Pandit Clinic","Deoyani Multispeciality Hospital",
    "Vasan Eye Care","Horizon Hospital","Surya Mother and Child Super Speciality Hospital","Mediplus Clinic","Chellaram Diabetes Institute",
    "Sant Dnyaneshwar Hospital","Others"])
        self.hospital_Entry.place(x=150,y=20,anchor='nw')
        
        
        self.doctor=customtkinter.CTkLabel(self.input_Taking_frame,text='Doctor : ',font=('Roboto',20))
        self.doctor.place(x=20,y=80,anchor='nw')
        
        
        self.doctor_Entry=customtkinter.CTkEntry(self.input_Taking_frame,height=30,width=140,placeholder_text='Enter Doctor Name')
        self.doctor_Entry.place(x=150,y=80,anchor='nw')
        
        
        self.diagnosis=customtkinter.CTkLabel(self.input_Taking_frame,text='Diagnosis : ',font=('Roboto',20))
        self.diagnosis.place(x=20,y=140,anchor='nw')
        
        self.diagnosis_Entry=customtkinter.CTkOptionMenu(self.input_Taking_frame,values=["Hypertension","Diabetes mellitus",
    "Hyperlipidemia","Coronary artery disease","Osteoarthritis","Rheumatoid arthritis","Chronic obstructive pulmonary disease (COPD)",
    "Asthma","Depression","Anxiety","Gastroesophageal reflux disease (GERD)","Migraine","Obesity","Thyroid disorders",
    "Peptic ulcer disease","Osteoporosis","Chronic kidney disease","Anemia","Stroke","Heart failure","Chronic liver disease",
    "Chronic sinusitis","Allergic rhinitis","Irritable bowel syndrome (IBS)","Inflammatory bowel disease (IBD)","Celiac disease",
    "Epilepsy","Chronic fatigue syndrome","HIV/AIDS","Sleep apnea","Urinary tract infection (UTI)","Gout",
    "Cancer","Polycystic ovary syndrome (PCOS)","Endometriosis","Hypothyroidism","Hyperthyroidism","Psoriasis","Eczema",
    "Chronic bronchitis","Post-traumatic stress disorder (PTSD)","Attention-deficit/hyperactivity disorder (ADHD)",
    "Autism spectrum disorder (ASD)","Schizophrenia","Bipolar disorder","Alzheimer's disease","Parkinson's disease","Others"])
        self.diagnosis_Entry.place(x=150,y=140,anchor='nw')
        
        self.symptoms=customtkinter.CTkLabel(self.input_Taking_frame,text='Symptoms : ',font=('Roboto',20))
        self.symptoms.place(x=20,y=200,anchor='nw')
        
        self.symptoms_Entry=customtkinter.CTkOptionMenu(self.input_Taking_frame,values=["Fever","Fatigue","Headache",
    "Cough","Shortness of breath","Chest pain","Abdominal pain","Nausea","Vomiting","Diarrhea","Constipation",
    "Joint pain","Muscle aches","Dizziness","Lightheadedness","Rash","Itching","Sore throat","Congestion",
    "Runny nose","Sneezing","Watery eyes","Difficulty swallowing","Changes in vision","Numbness or tingling","Weakness",
    "Difficulty sleeping","Weight loss","Weight gain","Frequent urination","Increased thirst","Difficulty concentrating",
    "Memory loss","Irritability","Anxiety","Depression","Mood swings","Hallucinations","Seizures","Tremors",
    "Balance problems","Speech difficulties","Fainting","Confusion","Trouble speaking or understanding speech",
    "Sweating","Chills","Swelling","Bruising easily","Abnormal bleeding","Chest tightness"])
        self.symptoms_Entry.place(x=150,y=200,anchor='nw')
        
        self.rating=customtkinter.CTk
        
        
        self.submit_button=customtkinter.CTkButton(self.input_Taking_frame,text='Save',height=30,width=50,command=self.function)
        self.submit_button.place(x=100,y=250,anchor='nw')
        
        
            
    def function(self):
        self.hospital=customtkinter.CTkLabel(self.base_Frame,text=f'Hospital : {self.hospital_Entry.get()}',font=('Roboto',20))
        self.hospital.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        self.doctor=customtkinter.CTkLabel(self.base_Frame,text=f'Doctor : {self.doctor_Entry.get()}',font=('Roboto',20))
        self.doctor.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        self.diagnosis=customtkinter.CTkLabel(self.base_Frame,text=f'Diagnosis : {self.diagnosis_Entry.get()}',font=('Roboto',20))
        self.diagnosis.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        self.symptoms=customtkinter.CTkLabel(self.base_Frame,text=f'Symptoms : {self.symptoms_Entry.get()}',font=('Roboto',20))
        self.symptoms.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        self.symptoms=customtkinter.CTkLabel(self.base_Frame,text=f'-------------------------------------------------------------------\n',font=('Roboto',20))
        self.symptoms.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        self.input_Taking_frame.destroy()
        
       
        
        
    def run(self):
        self.root.mainloop()     
        
class Window:
    
    def __init__(self):
        
        self.root=customtkinter.CTk(fg_color="#EAE2B7")
        self.windowColor=customtkinter.set_appearance_mode("light")
        self.theme=customtkinter.set_default_color_theme("green")
        self.window_width=self.root.winfo_screenwidth()
        self.window_height=self.root.winfo_screenheight()
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        
        self.profileLabel=customtkinter.CTkLabel(self.root,text="Your Profile",font=("Roboto",28))
        self.profileLabel.pack(pady=20)
        self.updateButton=customtkinter.CTkButton(self.root,text="Update Profile",font=("Roboto",20),command=self.setUp,fg_color="#4C72B0",hover_color="#78C2F0")
        self.updateButton.pack(side=customtkinter.TOP,anchor=customtkinter.NW,padx=700)  
        
        self.profile()

    def profile(self):

        self.profileFrame = customtkinter.CTkScrollableFrame(self.root, width=1200, height=1000, border_width=2, border_color="#76D7C4")
        self.profileFrame.pack(pady=50)

        self.personalILabel = customtkinter.CTkLabel(self.profileFrame, text="Personal Information", font=("Roboto", 20), text_color="blue")
        self.personalILabel.pack(side=customtkinter.TOP, anchor=customtkinter.NW,pady=10)

        self.displayNameLabel = customtkinter.CTkLabel(self.profileFrame, text="Full Name: " , font=("Roboto", 18) )
        self.displayNameLabel.pack(anchor="nw")

        self.displayDOBLabel = customtkinter.CTkLabel(self.profileFrame, text="Date of Birth: ", font=("Roboto", 18))
        self.displayDOBLabel.pack(anchor="nw")

        self.displayAgeLabel = customtkinter.CTkLabel(self.profileFrame, text="Age: ", font=("Roboto", 18))
        self.displayAgeLabel.pack(anchor="nw")

        self.displayGenderLabel = customtkinter.CTkLabel(self.profileFrame, text="Gender: ", font=("Roboto", 18))
        self.displayGenderLabel.pack(anchor="nw")

        self.displayContactInfoLabel = customtkinter.CTkLabel(self.profileFrame, text="Contact Information", font=("Roboto", 20), text_color="blue")
        self.displayContactInfoLabel.pack(anchor="nw",pady=10)

        self.displayMobileNoLabel = customtkinter.CTkLabel(self.profileFrame, text="Mobile No: ", font=("Roboto", 18))
        self.displayMobileNoLabel.pack(anchor="nw")
        
        self.displayeEmailLabel = customtkinter.CTkLabel(self.profileFrame, text="Email: ", font=("Roboto", 18))
        self.displayeEmailLabel.pack(anchor="nw")

        self.displayFullAddressLabel = customtkinter.CTkLabel(self.profileFrame, text="Address: ", font=("Roboto", 18))
        self.displayFullAddressLabel.pack(anchor="nw")

        self.displayPhysicalCharInfoLabel = customtkinter.CTkLabel(self.profileFrame, text="Physical Characteristics", font=("Roboto", 20), text_color="blue")
        self.displayPhysicalCharInfoLabel.pack(anchor="nw",pady=10)

        self.displayHeightLabel = customtkinter.CTkLabel(self.profileFrame, text="Height (cm): ", font=("Roboto", 18))
        self.displayHeightLabel.pack(anchor="nw")

        self.displayWeightLabel = customtkinter.CTkLabel(self.profileFrame, text="Weight (kg): ", font=("Roboto", 18))
        self.displayWeightLabel.pack(anchor="nw")

        self.displayDisablityLabel = customtkinter.CTkLabel(self.profileFrame, text="Disability: ", font=("Roboto", 18))
        self.displayDisablityLabel.pack(anchor="nw")

        self.displayVitalSignsInfoLabel = customtkinter.CTkLabel(self.profileFrame, text="Vital Signs ", font=("Roboto", 20), text_color="blue")
        self.displayVitalSignsInfoLabel.pack(anchor="nw",pady=10)

        self.displayHeartRateLabel = customtkinter.CTkLabel(self.profileFrame, text="Heart rate (BPM): ", font=("Roboto", 18))
        self.displayHeartRateLabel.pack(anchor="nw")
        
        self.displayBloodPressureLabel = customtkinter.CTkLabel(self.profileFrame, text="Blood pressure (mmHg): ", font=("Roboto", 18))
        self.displayBloodPressureLabel.pack(anchor="nw")

        self.displayTemperatureLabel=customtkinter.CTkLabel(self.profileFrame,text="Temperature (°F): ",font=("Roboto",18))
        self.displayTemperatureLabel.pack(anchor="nw")
        
        self.displayOxygenSaturationLabel=customtkinter.CTkLabel(self.profileFrame,text="Oxygen Saturation (%): ",font=("Roboto",18))
        self.displayOxygenSaturationLabel.pack(anchor="nw")
        
        self.displayCholesterolLevelLabel=customtkinter.CTkLabel(self.profileFrame,text="Cholesterol Level (mg/dL): ",font=("Roboto",18))
        self.displayCholesterolLevelLabel.pack(anchor="nw")
        
        self.displayRBCLabel=customtkinter.CTkLabel(self.profileFrame,text="Red Blood Cell Count (T/L): ",font=("Roboto",18))
        self.displayRBCLabel.pack(anchor="nw")
        
        self.displayWBCLabel=customtkinter.CTkLabel(self.profileFrame,text="White Blood Cell Count (B/L): ",font=("Roboto",18))
        self.displayWBCLabel.pack(anchor="nw")

        self.displayLifestyleInfoLabel=customtkinter.CTkLabel(self.profileFrame,text="Lifestyle and Behavioral Factors ",font=("Roboto",20),text_color="blue")
        self.displayLifestyleInfoLabel.pack(anchor="nw",pady=10)

        self.displaySmokingStatusLabel=customtkinter.CTkLabel(self.profileFrame,text="Smoking Status:",font=("Roboto",18))
        self.displaySmokingStatusLabel.pack(anchor="nw")
        
        self.displayAlcoholConsumptionLabel=customtkinter.CTkLabel(self.profileFrame,text="Alcohol Consumption:",font=("Roboto",18))
        self.displayAlcoholConsumptionLabel.pack(anchor="nw")
        
        self.displayPhysicalExerciseLevelLabel=customtkinter.CTkLabel(self.profileFrame,text="Physical Exercise Level:",font=("Roboto",18))
        self.displayPhysicalExerciseLevelLabel.pack(anchor="nw")
        
        self.displayDietaryHabitsLabel=customtkinter.CTkLabel(self.profileFrame,text="Dietary Habits:",font=("Roboto",18))
        self.displayDietaryHabitsLabel.pack(anchor="nw")

    def setUp(self):
        
        self.profileFrame.pack_forget()
        self.updateButton.pack_forget()

        self.progressBar = ttk.Progressbar(self.root,orient="vertical",length=1000)
        self.progressBar.pack(side=customtkinter.RIGHT,anchor=customtkinter.NW,padx=30,pady=60)

        self.mainFrame=customtkinter.CTkScrollableFrame(self.root,width=1200,height=800,border_width=2,border_color="#76D7C4")
        #self.mainFrame.pack_propagate(False)
        self.mainFrame.pack(pady=50)

        self.personalInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Personal Information",font=("Roboto",20),text_color="blue")
        self.personalInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW)

        self.pInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=170,border_width=2,border_color="#A3E4D7",fg_color="#c3efea")
        self.pInfoFrame.pack_propagate(False)
        self.pInfoFrame.pack(side=customtkinter.TOP,anchor=customtkinter.NW,padx=20,pady=20)

        self.fNameLabel=customtkinter.CTkLabel(self.pInfoFrame,text="First Name ",font=("Roboto",18))
        self.fNameLabel.place(x=20,y=10,anchor="nw")
        self.fNameEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Enter First Name",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.fNameEntry.place(x=120,y=10,anchor="nw")

        self.mNameLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Middle Name ",font=("Roboto",18))
        self.mNameLabel.place(x=400,y=10,anchor="nw")
        self.mNameEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Enter Middle Name",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.mNameEntry.place(x=520,y=10,anchor="nw")

        self.lNameLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Last Name ",font=("Roboto",18))
        self.lNameLabel.place(x=770,y=10,anchor="nw")
        self.lNameEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Enter Last Name",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.lNameEntry.place(x=870,y=10,anchor="nw")

        self.dobLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Date of Birth ",font=("Roboto",18))
        self.dobLabel.place(x=20,y=70,anchor="nw")
        self.dobEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="DD/MM/YYYY",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        #self.dobEntry=tb.DateEntry(self.pInfoFrame,bootstyle="danger")
        self.dobEntry.place(x=130,y=70,anchor="nw")

        self.ageLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Age ",font=("Roboto",18))
        self.ageLabel.place(x=400,y=70,anchor="nw")
        self.ageEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Your Age",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.ageEntry.place(x=450,y=70,anchor="nw")

        self.genderLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Gender ",font=("Roboto",18))
        self.genderLabel.place(x=670,y=70,anchor="nw")
        genders=['Select Option','Male','Female']
        self.genderOption=customtkinter.CTkOptionMenu(self.pInfoFrame,values=genders,fg_color="white",font=("Roboto",18),text_color="black")
        self.genderOption.pack_propagate(False)
        self.genderOption.place(x=780,y=70,anchor="nw")

        self.nextbutton=customtkinter.CTkButton(self.pInfoFrame,text="Next",command=self.contact,fg_color="#4C72B0",hover_color="#78C2F0",font=("Roboto",18))
        self.nextbutton.place(x=900,y=118,anchor="nw")

    def check_pInfoFields_filled(self):
    # List of entry widgets and their corresponding labels
        fields = [(self.fNameEntry, "First Name"),(self.mNameEntry, "Middle Name"),(self.lNameEntry, "Last Name"),
            (self.dobEntry, "Date of Birth"),(self.ageEntry, "Age"),(self.genderOption, "Gender")]

    # Check if any field is empty
        for field, label in fields:
            if isinstance(field, customtkinter.CTkEntry) and not field.get():
                raise ValueError(f"Please fill in {label}")

            if isinstance(field, customtkinter.CTkOptionMenu) and field.get() == 'Select Option':
                raise ValueError(f"Please select a valid option for {label}")
            
        fName = self.fNameEntry.get()
        mName = self.mNameEntry.get()
        lName = self.lNameEntry.get()
        dob = self.dobEntry.get()

        if not re.match(r"^[A-Za-z]+$",fName):
            raise ValueError("First Name\n Name should have alphabets")
        
        if not re.match(r"^[a-zA-Z]+$",mName):
            raise ValueError("Middle Name\n Name should have alphabets")
        
        if not re.match(r"^[a-zA-Z]+$",lName):
            raise ValueError("Last Name\n Name should have alphabets")
        
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', dob):
            raise ValueError("Enter valid Date\nThe format should be DD/MM/YYYY")        
        

    def contact(self):

        try:
            self.check_pInfoFields_filled()  # Check if all fields are filled
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Display error message
            return
        
        dob_str = self.dobEntry.get()

    # Check if the date format is valid
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', dob_str):
            messagebox.showerror("Error", "Invalid Date\nThe format should be DD/MM/YYYY")
            return

        try:
            # Parse DOB string to a datetime object
            dob_date = datetime.strptime(dob_str, '%d/%m/%Y')

            # Calculate age till current date
            today = datetime.today()
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

            # Update ageEntry with the calculated age
            self.ageEntry.delete(0, 'end')  # Clear any previous value
            self.ageEntry.insert(0, str(age))
        except ValueError:
            messagebox.showerror("Error", "Invalid Date\nPlease enter a valid date")
            return

        if hasattr(self, 'contact_clicked') and self.contact_clicked:
            return
        self.contact_clicked = True

        self.progressBar["value"]+=20

        self.contactInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Contact Information",font=("Roboto",20),text_color="blue")
        self.contactInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.contactInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=400,border_width=2,border_color="#A3E4D7",fg_color="#c3efea")
        self.contactInfoFrame.pack(side=customtkinter.TOP,anchor=customtkinter.NW,padx=20,pady=20)

        self.countryCodeLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="Country Code ",font=("Roboto",18))
        self.countryCodeLabel.place(x=20,y=10,anchor="nw")
        self.codeFrame=customtkinter.CTkScrollableFrame(self.contactInfoFrame,)
        self.codes = [
    "Select Option","United States 1","Canada 1","Russia 7","Kazakhstan 7","Egypt 20","South Africa 27","Greece 30","Netherlands 31","Belgium 32","France 33","Spain 34",
    "Hungary 36","Italy 39","Romania 40","Switzerland 41","Austria 43","United Kingdom 44","Denmark 45","Sweden 46","Norway 47","Poland 48","Germany 49","Peru 51",
    "Mexico 52","Cuba 53","Argentina 54","Brazil 55","Chile 56","Colombia 57","Venezuela 58","Malaysia 60","Australia 61","Indonesia 62","Philippines 63","New Zealand 64",
    "Singapore 65","Thailand 66","Japan 81","South Korea 82","Vietnam 84","China 86","Turkey 90","India 91","Pakistan 92","Afghanistan 93","Sri Lanka 94","Myanmar  95","Iran 98","Morocco 212",
    "Algeria 213","Tunisia 216","Libya 218","Gambia 220","Senegal 221","Mauritania 222","Mali 223","Guinea 224","Ivory Coast 225","Burkina Faso 226","Niger 227","Togo 228",
    "Benin 229","Mauritius 230","Liberia 231","Sierra Leone 232","Ghana 233","Nigeria 234","Chad 235","Cameroon 237","Cape Verde 238","Equatorial Guinea 240","Gabon 241",
    "Congo 243","Angola 244","Guinea-Bissau 245","Seychelles 248","Sudan 249","Rwanda 250","Ethiopia 251","Somalia 252","Djibouti 253","Kenya 254","Tanzania 255","Uganda 256",
    "Burundi 257","Mozambique 258","Zambia 260","Madagascar 261","Reunion Island 262","Zimbabwe 263","Namibia 264","Malawi 265","Lesotho 266","Botswana 267","Swaziland 268",
    "Comoros 269","Saint Helena 290""Eritrea 291","Aruba 297","Faroe Islands 298","Greenland 299","Gibraltar 350","Portugal 351""Luxembourg 352","Ireland 353","Iceland 354",
    "Albania 355","Malta 356","Cyprus 357","Finland 358","Bulgaria 359","Lithuania 370","Latvia 371","Estonia 372","Moldova 373","Armenia 374","Belarus 375""Andorra 376","Monaco 377","San Marino 378",
    "Vatican City 379","Ukraine 380","Serbia 381","Montenegro 382","Croatia 385","Slovenia 386","North Macedonia 389","Czech Republic 420","Slovakia 421","Liechtenstein 423","Falkland Islands 500",
    "Belize 501","Guatemala 502","El Salvador 503","Honduras 504","Nicaragua 505","Costa Rica 506","Panama 507","Haiti 509","Guadeloupe 590","Bolivia 591","Guyana 592","Ecuador 593","French Guiana 594",
    "Paraguay 595","Martinique 596","Suriname 597","Uruguay 598","East Timor 670","Brunei 673","Nauru 674","Papua New Guinea 675","Tonga 676","Solomon Islands 677",
    "Vanuatu 678","Fiji 679","Palau 680","Wallis and Futuna 681","Cook Islands 682","Niue 683","Samoa 685""Kiribati 686","New Caledonia 687","Tuvalu 688","French Polynesia 689",
    "Tokelau 690","Micronesia 691","Marshall Islands 692""North Korea 850","Hong Kong 852","Macao 853","Cambodia 855","Laos 856","Bangladesh 880","Taiwan 886","Maldives 960",
    "Lebanon 961","Jordan 962""Syria 963","Iraq 964","Kuwait 965","Saudi Arabia 966","Yemen 966","Oman 967","UAE 971","Israel 972","Bahrain 973","Qatar 974","Bhutan 975","Mongolia 976",
    "Nepal 977","Tajikistan 992","Turkmenistan 993","Azerbaijan 994","Georgia 995","Kyrgyzstan 996","Uzbekistan 998"
]

        self.codeOption=customtkinter.CTkOptionMenu(self.contactInfoFrame,values=self.codes,fg_color="white",font=("Roboto",18),text_color="black")
        self.codeOption.pack_propagate(False)
        self.codeOption.place(x=150,y=10,anchor="nw")

        self.mobileNoLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="Mobile No: ",font=("Roboto",18))
        self.mobileNoLabel.place(x=400,y=10,anchor="nw")
        self.mobileNoEntry=customtkinter.CTkEntry(self.contactInfoFrame,width=150,height=2,placeholder_text="Enter email",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.mobileNoEntry.place(x=510,y=10,anchor="nw")

        self.emailLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="Email ",font=("Roboto",18))
        self.emailLabel.place(x=750,y=10,anchor="nw")
        self.emailEntry=customtkinter.CTkEntry(self.contactInfoFrame,width=150,height=2,placeholder_text="Enter email",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.emailEntry.place(x=800,y=10,anchor="nw")

        self.addressLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="Address",font=("Roboto",20),text_color="#5DADE2")
        self.addressLabel.place(x=20,y=70)

        self.streetAddressLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="Street Address:",font=("Roboto",20))
        self.streetAddressLabel.place(x=20,y=100)
        self.streetAddressEntry=customtkinter.CTkEntry(self.contactInfoFrame,width=550,height=2,placeholder_text="",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.streetAddressEntry.place(x=170,y=100,anchor="nw")

        self.cityTownLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="City or Town:",font=("Roboto",20))
        self.cityTownLabel.place(x=20,y=150)
        self.cityTownEntry=customtkinter.CTkEntry(self.contactInfoFrame,width=550,height=2,placeholder_text="",font=("Roboto",18),corner_radius=3)
        self.cityTownEntry.place(x=170,y=150,anchor="nw")

        self.stateProvinceLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="State/Province:",font=("Roboto",20))
        self.stateProvinceLabel.place(x=20,y=200)
        self.stateProvinceEntry=customtkinter.CTkEntry(self.contactInfoFrame,width=550,height=2,placeholder_text="",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.stateProvinceEntry.place(x=170,y=200,anchor="nw")

        self.postalCodeLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="Postal Code/ZIP Code:",font=("Roboto",20))
        self.postalCodeLabel.place(x=20,y=250)
        self.postalCodeEntry=customtkinter.CTkEntry(self.contactInfoFrame,width=130,height=2,placeholder_text="",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.postalCodeEntry.place(x=230,y=250,anchor="nw")

        self.countryLabel=customtkinter.CTkLabel(self.contactInfoFrame,text="Country:",font=("Roboto",20))
        self.countryLabel.place(x=20,y=300)
        self.countryEntry=customtkinter.CTkEntry(self.contactInfoFrame,width=250,height=2,placeholder_text="",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.countryEntry.place(x=120,y=300,anchor="nw")

        self.nextbutton2=customtkinter.CTkButton(self.contactInfoFrame,text="Next",command=self.physicalChar,fg_color="#4C72B0",hover_color="#78C2F0",font=("Roboto",18))
        self.nextbutton2.place(x=900,y=350,anchor="nw")

    def check_contact_filled(self):
        self.contactFields = [(self.codeOption,"Country Code"),(self.mobileNoEntry,"Mobile Number"),(self.emailEntry,"Email Address"),(self.streetAddressEntry,"Street Address"),(self.cityTownEntry,"City/Town"),(self.stateProvinceEntry,"State/Province"),(self.postalCodeEntry,"Postal Code"),(self.countryEntry,"Country")]
        for field2,label2 in self.contactFields:
            if isinstance(field2, customtkinter.CTkEntry) and not field2.get():
                raise ValueError(f"Please Fill in {label2}")
            
            if isinstance(field2, customtkinter.CTkOptionMenu) and field2.get() == "Select Option":
                raise ValueError(f"Please Select a Valid Option for {label2}")

            if label2 == "Mobile Number":
                mobileNumber = field2.get()
                india_regex = r"^\+91[6-9]\d{9}$"
                uk_regex = r"^\+44\d{10}$"
                usa_regex = r"^\+1\d{10}$"
            
                if not re.match(india_regex, mobileNumber) and not re.match(uk_regex, mobileNumber) and not re.match(usa_regex, mobileNumber):
                    raise ValueError("Please Enter a Valid Mobile Number along with Country Code")
                

        self.email = self.emailEntry.get()
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.email):
            raise ValueError("Please enter a valid email address")
        
        postalCode = self.postalCodeEntry.get()
        if not re.match(r"^[0-9]+$",postalCode):
            raise ValueError("Enter Correct Postal Code")
        

    def physicalChar(self):

        try:
            self.check_contact_filled()
        except ValueError as e:
            messagebox.showerror("Error",str(e))
            return

        if hasattr(self, 'physical_char_clicked') and self.physical_char_clicked:
            return
        self.physical_char_clicked = True

        self.progressBar["value"]+=20

        self.physicalCharInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Physical Characteristics",font=("Roboto",20),text_color="blue")
        self.physicalCharInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.physicalCharFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=100,border_width=2,border_color="#A3E4D7",fg_color="#c3efea")
        self.physicalCharFrame.pack(side=customtkinter.TOP,anchor=customtkinter.NW,padx=20,pady=20)

        self.heightLabel=customtkinter.CTkLabel(self.physicalCharFrame,text="Height (cm): ",font=("Roboto",18))
        self.heightLabel.place(x=20,y=10,anchor="nw")
        self.heightEntry=customtkinter.CTkEntry(self.physicalCharFrame,width=150,height=2,placeholder_text="Height in cm",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.heightEntry.place(x=120,y=10,anchor="nw")

        self.weightLabel=customtkinter.CTkLabel(self.physicalCharFrame,text="Weight (kg): ",font=("Roboto",18))
        self.weightLabel.place(x=400,y=10,anchor="nw")
        self.weightEntry=customtkinter.CTkEntry(self.physicalCharFrame,width=150,height=2,placeholder_text="Weigth in kg",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.weightEntry.place(x=520,y=10,anchor="nw")

        self.disablityLabel=customtkinter.CTkLabel(self.physicalCharFrame,text="Disability: ",font=("Roboto",18))
        self.disablityLabel.place(x=770,y=10,anchor="nw")
        options=["Select Option",'No','Yes']
        self.disabilityOption=customtkinter.CTkOptionMenu(self.physicalCharFrame,values=options,fg_color="white",font=("Roboto",18),text_color="black")
        self.disabilityOption.pack_propagate(False)
        self.disabilityOption.place(x=870,y=10,anchor="nw")

        self.nextbutton3=customtkinter.CTkButton(self.physicalCharFrame,text="Next",command=self.vitalSigns,fg_color="#4C72B0",hover_color="#78C2F0",font=("Roboto",18))
        self.nextbutton3.place(x=900,y=50,anchor="nw")

    def check_physicalChar(self):
        self.physicalCharFields = [(self.heightEntry,"Height"),(self.weightEntry,"Weight"),(self.disabilityOption,"Disability Option")]
        for field3,label3 in self.physicalCharFields:
            if isinstance(field3,customtkinter.CTkEntry) and not field3.get():
                raise ValueError(f"Please Fill in {label3}")
            
            if isinstance(field3,customtkinter.CTkOptionMenu) and field3.get() == "Select Option":
                raise ValueError(f"Please Select a Valid Option for {label3}")
            
        height=self.heightEntry.get()
        weight=self.weightEntry.get()

        if not re.match(r"^[0-9]+$",height):
            raise ValueError("Height should be Numeric")
        
        if not re.match(r"^[0-9]+$",weight):
            raise ValueError("Weight should be Numeric")


    def vitalSigns(self):

        try:
            self.check_physicalChar()
        except ValueError as e:
            messagebox.showerror("Error",str(e))

        if hasattr(self, 'vital_Signs_clicked') and self.vital_Signs_clicked:
            return
        self.vital_Signs_clicked = True

        self.progressBar["value"]+=20

        self.vitalSignsInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Vital Signs ",font=("Roboto",20),text_color="blue")
        self.vitalSignsInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.vitalSignsInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=410,border_width=2,border_color="#A3E4D7",fg_color="#c3efea")
        self.vitalSignsInfoFrame.pack(side=customtkinter.TOP,anchor=customtkinter.NW,padx=20,pady=20)

        self.heartRateLabel=customtkinter.CTkLabel(self.vitalSignsInfoFrame,text="Heart rate (BPM): ",font=("Roboto",18))
        self.heartRateLabel.place(x=20,y=10,anchor="nw")
        self.heartRateEntry=customtkinter.CTkEntry(self.vitalSignsInfoFrame,width=150,height=2,placeholder_text="Current Heart rate in (Beats Per Minute)",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.heartRateEntry.place(x=250,y=10,anchor="nw")

        self.bloodPressureLabel=customtkinter.CTkLabel(self.vitalSignsInfoFrame,text="Blood pressure (mmHg): ",font=("Roboto",18))
        self.bloodPressureLabel.place(x=20,y=60,anchor="nw")
        self.bloodPressureEntry=customtkinter.CTkEntry(self.vitalSignsInfoFrame,width=150,height=2,placeholder_text="Current Blood pressure in (mmHg)",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.bloodPressureEntry.place(x=250,y=60,anchor="nw")

        self.temperatureLabel=customtkinter.CTkLabel(self.vitalSignsInfoFrame,text="Temperature (°F): ",font=("Roboto",18))
        self.temperatureLabel.place(x=20,y=110,anchor="nw")
        self.temperatureEntry=customtkinter.CTkEntry(self.vitalSignsInfoFrame,width=150,height=2,placeholder_text="Temperature in (°F)",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.temperatureEntry.place(x=250,y=110,anchor="nw")

        self.oxygenSaturationLabel=customtkinter.CTkLabel(self.vitalSignsInfoFrame,text="Oxygen Saturation (%): ",font=("Roboto",18))
        self.oxygenSaturationLabel.place(x=20,y=160,anchor="nw")
        self.oxygenSaturationEntry=customtkinter.CTkEntry(self.vitalSignsInfoFrame,width=150,height=2,placeholder_text="Oxygen Saturation in  Percentage",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.oxygenSaturationEntry.place(x=250,y=160,anchor="nw")

        self.cholesterolLevelLabel=customtkinter.CTkLabel(self.vitalSignsInfoFrame,text="Cholesterol Level (mg/dL): ",font=("Roboto",18))
        self.cholesterolLevelLabel.place(x=20,y=210,anchor="nw")
        self.cholesterolLevelEntry=customtkinter.CTkEntry(self.vitalSignsInfoFrame,width=150,height=2,placeholder_text="Milligrams per Deciliter",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.cholesterolLevelEntry.place(x=250,y=210,anchor="nw")

        self.RBCLabel=customtkinter.CTkLabel(self.vitalSignsInfoFrame,text="Red Blood Cell Count (T/L): ",font=("Roboto",18))
        self.RBCLabel.place(x=20,y=260,anchor="nw")
        self.RBCEntry=customtkinter.CTkEntry(self.vitalSignsInfoFrame,width=150,height=2,placeholder_text="Trillion per liter",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.RBCEntry.place(x=250,y=260,anchor="nw")

        self.WBCLabel=customtkinter.CTkLabel(self.vitalSignsInfoFrame,text="White Blood Cell Count (B/L): ",font=("Roboto",18))
        self.WBCLabel.place(x=20,y=310,anchor="nw")
        self.WBCEntry=customtkinter.CTkEntry(self.vitalSignsInfoFrame,width=150,height=2,placeholder_text="Billions per liter",placeholder_text_color="#D5DBDB",font=("Roboto",18),corner_radius=3)
        self.WBCEntry.place(x=250,y=310,anchor="nw")

        self.nextbutton4=customtkinter.CTkButton(self.vitalSignsInfoFrame,text="Next",command=self.lifestyle,fg_color="#4C72B0",hover_color="#78C2F0",font=("Roboto",18))
        self.nextbutton4.place(x=900,y=360,anchor="nw")

    def check_vitalSignsFields(self):
        self.vitalSignsFields = [(self.heartRateEntry, "Heart rate"),(self.bloodPressureEntry, "Blood pressure"),(self.temperatureEntry, "Temperature"),
            (self.oxygenSaturationEntry, "Oxygen Saturation"),(self.cholesterolLevelEntry, "Cholesterol Level"),(self.RBCEntry, "Red Blood Cell Count"),(self.WBCEntry, "White Blood Cell Count")]

        for field4, label4 in self.vitalSignsFields:
            if not field4.get():
                raise ValueError(f"Please fill in {label4}")
            
        heartRate = self.heartRateEntry.get()
        bloodPressure = self.bloodPressureEntry.get()
        temperature = self.temperatureEntry.get()
        oxygenSaturation = self.oxygenSaturationEntry.get()
        cholesterolLevel = self.cholesterolLevelEntry.get()
        rbc = self.RBCEntry.get()
        wbc = self.WBCEntry.get()

        if not re.match(r"^[0-9]+$",heartRate):
            raise ValueError("Heart Rate should be Numeric")
        
        if not re.match(r"^\d+\s*/\s*\d+$", bloodPressure):
            raise ValueError("Blood Pressure\nPlease enter blood pressure in proper format (mm/Hg)")
        
        if not re.match(r"^\d+(\.\d{1,2})?$", temperature):
            raise ValueError("Temperature should be in proper format (e.g., 98.6)")

        if not re.match(r"^[0-9]+$", oxygenSaturation):
            raise ValueError("Oxygen Saturation should be Numeric")

        if not re.match(r"^[0-9]+$", cholesterolLevel):
            raise ValueError("Cholesterol Level should be Numeric")

        if not re.match(r"^[0-9]+$", rbc):
            raise ValueError("Red Blood Cell Count should be Numeric")

        if not re.match(r"^[0-9]+$", wbc):
            raise ValueError("White Blood Cell Count should be Numeric")

    def lifestyle(self):

        try:
            self.check_vitalSignsFields()
        except ValueError as e:
            messagebox.showerror("Error",str(e))
            return

        if hasattr(self, 'lifestyle_clicked') and self.lifestyle_clicked:
            return
        self.lifestyle_clicked = True

        self.progressBar["value"]+=20

        self.lifestyleInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Lifestyle and Behavioral Factors ",font=("Roboto",20),text_color="blue")
        self.lifestyleInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.lifestyleInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=150,border_width=2,border_color="#4A235A",fg_color="#c3efea")
        self.lifestyleInfoFrame.pack(side=customtkinter.TOP,anchor=customtkinter.NW,padx=20,pady=20)

        self.smokingStatusLabel=customtkinter.CTkLabel(self.lifestyleInfoFrame,text="Smoking Status:",font=("Roboto",18))
        self.smokingStatusLabel.place(x=20,y=10,anchor="nw")
        smokingOptions=['Select Option','Non-smoker','Current smoker','Former smoker','Occasional smoker','Social smoker']
        self.smokingAnswer=customtkinter.CTkOptionMenu(self.lifestyleInfoFrame,values=smokingOptions,font=("Roboto",18),fg_color="white",text_color="black")
        self.smokingAnswer.place(x=250,y=10,anchor="nw")

        self.alcoholConsumptionLabel=customtkinter.CTkLabel(self.lifestyleInfoFrame,text="Alcohol Consumption:",font=("Roboto",18))
        self.alcoholConsumptionLabel.place(x=550,y=10,anchor="nw")
        self.consumptionOptions=['Select Option','Non-Alcoholic','Occasional/Event Drinker','Moderate Drinker','Heavy Drinker','Binge Drinker']
        self.consumptionAnswer=customtkinter.CTkOptionMenu(self.lifestyleInfoFrame,values=self.consumptionOptions,font=("Roboto",18),fg_color="white",text_color="black")
        self.consumptionAnswer.place(x=750,y=10,anchor="nw")

        self.physicalExerciseLevelLabel=customtkinter.CTkLabel(self.lifestyleInfoFrame,text="Physical Exercise Level:",font=("Roboto",18))
        self.physicalExerciseLevelLabel.place(x=20,y=60,anchor="nw")
        self.exerciseOptions=["Select Option","Sedentary","Lightly active","Moderately active","Very active","Extremely active"]
        self.exerciesAnswer=customtkinter.CTkOptionMenu(self.lifestyleInfoFrame,values=self.exerciseOptions,font=("Roboto",18),fg_color="white",text_color="black")
        self.exerciesAnswer.place(x=250,y=60,anchor="nw")

        self.dietaryHabitsLabel=customtkinter.CTkLabel(self.lifestyleInfoFrame,text="Dietary Habits:",font=("Roboto",18))
        self.dietaryHabitsLabel.place(x=550,y=60,anchor="nw")
        self.dietOption=["Select Option","Three Meals a Day","Intermittent Fasting","Two Meals a Day","One Meal a Day"]
        self.dietAnswer=customtkinter.CTkOptionMenu(self.lifestyleInfoFrame,values=self.dietOption,font=("Roboto",18),fg_color="white",text_color="black")
        self.dietAnswer.place(x=750,y=60,anchor="nw")

        self.submitbutton=customtkinter.CTkButton(self.lifestyleInfoFrame,text="Submit",font=("Roboto",18),command=self.submit,fg_color="#198C19",hover_color="#5EAE5E")
        self.submitbutton.place(x=900,y=100,anchor="nw")

    def check_lifestyleFields(self):
        self.lifeStyleFieldsfields = [(self.smokingAnswer, "Smoking Status"),(self.consumptionAnswer, "Alcohol Consumption"),(self.exerciesAnswer, "Physical Exercise Level"),(self.dietAnswer, "Dietary Habits")]

        for field5, label5 in self.lifeStyleFieldsfields:
            if field5.get() == "Select Option":
                raise ValueError(f"Please select an option for {label5}")

    def submit(self):

        try:
            self.check_lifestyleFields()
        except ValueError as e:
            messagebox.showerror("Error",str(e))
            return

        if hasattr(self,'submit_clicked') and self.submit_clicked:
            return
        self.submit_clicked=True

        self.progressBar["value"]+=20

        self.profile()
        self.mainFrame.pack_forget()

    def run(self):
        self.root.mainloop()           

if __name__ == "__main__":
    app = MainWindow()
    app.app.mainloop()        