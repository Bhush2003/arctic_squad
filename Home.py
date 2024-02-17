import customtkinter

class App:
    def __init__(self):
        
        self.root=customtkinter.CTk(fg_color='#58D68D')
        self.root.geometry(f'{self.root.winfo_screenheight()}x{self.root.winfo_screenwidth()}')
        self.root._set_appearance_mode('white')
        
        self.frame1=customtkinter.CTkLabel(self.root,
                                           text='RECORDS',
                                           font=('Roboto',40),
                                           width=500
                                           
                                           )
        self.frame1.pack_propagate(False)
        self.frame1.pack()
        
        self.header_text=customtkinter.CTkLabel(self.frame1,
                                                text='RECORDS',
                                                font=('Roboto',50)
                                                )
        self.header_text.pack()
        
        self.base_Frame=customtkinter.CTkFrame(self.root,height=650,width=800)
        self.base_Frame.pack(side=customtkinter.TOP, anchor=customtkinter.CENTER,pady=50,padx=50)
        
        self.addButton=customtkinter.CTkButton(self.base_Frame,width=70,height=50,text='Add',command=self.fill_Info)
        self.addButton.pack(side=customtkinter.RIGHT, anchor=customtkinter.NE,pady=50,padx=50)
        
        self.profile_Info()
            
    def profile_Info(self):
        self.info_storing_frame=customtkinter.CTkScrollableFrame(self.base_Frame,height=500,width=800,border_color='cyan',border_width=1)   
        self.info_storing_frame.pack(side=customtkinter.TOP,anchor=customtkinter.CENTER,padx=60,pady=100)
        
        self.hospital=customtkinter.CTkLabel(self.info_storing_frame,text='Hospital : ',font=('Roboto',20))
        self.hospital.place(x=20,y=20,anchor='nw')
        
        self.doctor=customtkinter.CTkLabel(self.info_storing_frame,text='Doctor : ',font=('Roboto',20))
        self.doctor.place(x=20,y=80,anchor='nw')
        
        self.diagnosis=customtkinter.CTkLabel(self.info_storing_frame,text='Diagnosis : ',font=('Roboto',20))
        self.diagnosis.place(x=20,y=140,anchor='nw')
        
        self.symptoms=customtkinter.CTkLabel(self.info_storing_frame,text='Symptoms : ',font=('Roboto',20))
        self.symptoms.place(x=20,y=200,anchor='nw')
        
    def fill_Info(self):    
        
        self.imput_Taking_frame=customtkinter.CTkFrame(self.info_storing_frame,height=350,width=350,border_color='cyan',border_width=1)
        self.imput_Taking_frame.pack(side=customtkinter.TOP,anchor=customtkinter.CENTER,padx=30,pady=50)
        
        self.hospital=customtkinter.CTkLabel(self.imput_Taking_frame,text='Hospital : ',font=('Roboto',20))
        self.hospital.place(x=20,y=20,anchor='nw')
        
        self.hospital_Entry=customtkinter.CTkOptionMenu(self.imput_Taking_frame,values=[
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
        
        
        self.doctor=customtkinter.CTkLabel(self.imput_Taking_frame,text='Doctor : ',font=('Roboto',20))
        self.doctor.place(x=20,y=80,anchor='nw')
        
        self.doctor_Entry=customtkinter.CTkEntry(self.imput_Taking_frame,height=30,width=140,placeholder_text='Enter Doctor Name')
        self.doctor_Entry.place(x=150,y=80,anchor='nw')
        
        self.diagnosis=customtkinter.CTkLabel(self.imput_Taking_frame,text='Diagnosis : ',font=('Roboto',20))
        self.diagnosis.place(x=20,y=140,anchor='nw')
        
        self.diagnosis_Entry=customtkinter.CTkOptionMenu(self.imput_Taking_frame,values=["Hypertension","Diabetes mellitus",
    "Hyperlipidemia","Coronary artery disease","Osteoarthritis","Rheumatoid arthritis","Chronic obstructive pulmonary disease (COPD)",
    "Asthma","Depression","Anxiety","Gastroesophageal reflux disease (GERD)","Migraine","Obesity","Thyroid disorders",
    "Peptic ulcer disease","Osteoporosis","Chronic kidney disease","Anemia","Stroke","Heart failure","Chronic liver disease",
    "Chronic sinusitis","Allergic rhinitis","Irritable bowel syndrome (IBS)","Inflammatory bowel disease (IBD)","Celiac disease",
    "Epilepsy","Chronic fatigue syndrome","HIV/AIDS","Sleep apnea","Urinary tract infection (UTI)","Gout",
    "Cancer","Polycystic ovary syndrome (PCOS)","Endometriosis","Hypothyroidism","Hyperthyroidism","Psoriasis","Eczema",
    "Chronic bronchitis","Post-traumatic stress disorder (PTSD)","Attention-deficit/hyperactivity disorder (ADHD)",
    "Autism spectrum disorder (ASD)","Schizophrenia","Bipolar disorder","Alzheimer's disease","Parkinson's disease","Others"])
        self.diagnosis_Entry.place(x=150,y=140,anchor='nw')
        
        self.symptoms=customtkinter.CTkLabel(self.imput_Taking_frame,text='Symptoms : ',font=('Roboto',20))
        self.symptoms.place(x=20,y=200,anchor='nw')
        
        self.diagnosis_Entry=customtkinter.CTkOptionMenu(self.imput_Taking_frame,values=["Fever","Fatigue","Headache",
    "Cough","Shortness of breath","Chest pain","Abdominal pain","Nausea","Vomiting","Diarrhea","Constipation",
    "Joint pain","Muscle aches","Dizziness","Lightheadedness","Rash","Itching","Sore throat","Congestion",
    "Runny nose","Sneezing","Watery eyes","Difficulty swallowing","Changes in vision","Numbness or tingling","Weakness",
    "Difficulty sleeping","Weight loss","Weight gain","Frequent urination","Increased thirst","Difficulty concentrating",
    "Memory loss","Irritability","Anxiety","Depression","Mood swings","Hallucinations","Seizures","Tremors",
    "Balance problems","Speech difficulties","Fainting","Confusion","Trouble speaking or understanding speech",
    "Sweating","Chills","Swelling","Bruising easily","Abnormal bleeding","Chest tightness"])
        self.diagnosis_Entry.place(x=150,y=200,anchor='nw')
        
        
        self.submit_button=customtkinter.CTkButton(self.imput_Taking_frame,text='Save',height=30,width=50,command=self.imput_Taking_frame.destroy)
        self.submit_button.place(x=100,y=250,anchor='nw')
            
    def function(self):
       pass  
        
             
        
        
    def run(self):
        self.root.mainloop()        

if __name__=='__main__':
    app=App()
    app.run()
    
    
   #medicines,hospital name,doctor name,symptoms, 