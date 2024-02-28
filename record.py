import customtkinter
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate(r"C:/Users/Harshal/Downloads/user-profile-fa7a7-firebase-adminsdk-3vt6t-b13404fe9f.json")
firebase_admin.initialize_app(cred)
        
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
class App:
   
    def __init__(self,root,historyFrame): 
        self.root=root
        self.recordFrame = historyFrame
        # self.root.geometry(f'{self.recordFrame.winfo_screenheight()}x{self.root.winfo_screenwidth()}')
        # customtkinter.set_appearance_mode('light')
        # customtkinter.set_default_color_theme('green')

       
        self.header_text=customtkinter.CTkLabel(self.recordFrame,text='RECORDS',pady=30,font=('Algerian',50),text_color='#00157c')
        self.header_text.pack()
        
        self.addButton=customtkinter.CTkButton(self.recordFrame,width=70,height=50,text='Previous',command=self.display_data)
        self.addButton.pack(side=customtkinter.TOP, anchor=customtkinter.NW,padx=500)
        
        self.addButton=customtkinter.CTkButton(self.recordFrame,width=70,height=50,text='Add',command=self.fill_Info)
        self.addButton.pack(side=customtkinter.TOP, anchor=customtkinter.NW,padx=500)
        
        self.base_Frame=customtkinter.CTkScrollableFrame(self.recordFrame,height=500,width=400,scrollbar_button_color='white')
        self.base_Frame.pack(side=customtkinter.LEFT, anchor=customtkinter.NW,padx=150)

        
        
        # self.info_storing_frame=customtkinter.CTkScrollableFrame(self.base_Frame,height=500,orientation='vertical',width=950,border_color='cyan',border_width=1)   
        # self.info_storing_frame.pack(side=customtkinter.TOP,anchor=customtkinter.CENTER,padx=60,pady=100)
        
        
    def fill_Info(self):    
        
        self.input_Taking_frame=customtkinter.CTkFrame(self.recordFrame,height=500,width=400,border_color='cyan',border_width=2)
        self.input_Taking_frame.pack(side=customtkinter.TOP,anchor=customtkinter.CENTER,padx=30)
        
        self.hospital=customtkinter.CTkLabel(self.input_Taking_frame,text='Hospital : ',font=('Roboto',20))
        self.hospital.place(x=20,y=20,anchor='nw')
        
        self.hospital_Entry=customtkinter.CTkOptionMenu(self.input_Taking_frame,values=[
    "Ruby Hall Clinic","Jehangir Hospital","Deenanath Mangeshkar Hospital","Sancheti Hospital","Poona Hospital and Research Centre","KEM Hospital",
    "Columbia Asia Hospital","Sahyadri Hospital","Inamdar Multispeciality Hospital","Aditya Birla Memorial Hospital","Noble Hospital",
    "Medipoint Hospital","Criticare Hospital","Hardikar Hospital","Apollo Jehangir Hospital","Ratna Memorial Hospital","Lokmanya Hospital",
    "Kotbagi Hospital","Sanjeevan Hospital","Cedar Hospitals","Joshi Hospital","Vinayak Hospital","Kulkarni Hospital","Gokhale Hospital",
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
    def display_data(self):
        
        db=firestore.client()
        
        result = db.collection("RecordsCollection").get()
        try:
            for i in range(9):
                hospitalName=result[i].to_dict().get('Hospital')
                doctorName=result[i].to_dict().get('Doctor')
                diagnosisName=result[i].to_dict().get('Diagnosis')
                symptomsName=result[i].to_dict().get('Symptoms')
                
                self.hospital=customtkinter.CTkLabel(self.base_Frame,text_color='#00157c',text=f'Hospital : {hospitalName}\n \n Doctor : {doctorName}\n \n Diagnosis : {diagnosisName}\n \n Symptoms : {symptomsName}',font=('Roboto',20))
                self.hospital.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
                
                self.symptoms=customtkinter.CTkLabel(self.base_Frame,text=f'-------------------------------------------------------------------\n',font=('Roboto',20))
                self.symptoms.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        except:
            print('index out of range')        
            
    def function(self):
        
        db=firestore.client()
        
        doc_ref=db.collection('RecordsCollection').add({
        'Hospital':f'{self.hospital_Entry.get()}',
        'Doctor':f'{self.doctor_Entry.get()}',
        'Diagnosis':f'{self.diagnosis_Entry.get()}',
        'Symptoms':f'{self.symptoms_Entry.get()}',
        })
        
        
        
        
        
        
        
        # self.doctor=customtkinter.CTkLabel(self.base_Frame,text=f'Doctor : {doctorName}',font=('Roboto',20))
        # self.doctor.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        # self.diagnosis=customtkinter.CTkLabel(self.base_Frame,text=f'Diagnosis : {diagnosisName}',font=('Roboto',20))
        # self.diagnosis.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        # self.symptoms=customtkinter.CTkLabel(self.base_Frame,text=f'Symptoms : {symptomsName}',font=('Roboto',20))
        # self.symptoms.pack(padx=20,pady=20,side=customtkinter.TOP,anchor=customtkinter.NW)
        
        
        
        self.input_Taking_frame.destroy()
        
       
        
        
    def run(self):
        self.recordFrame.mainloop()        

if __name__=='__main__':
    app=App()
    app.run()