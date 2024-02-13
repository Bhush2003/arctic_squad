import customtkinter

class Window:
    def __init__(self):
        self.root=customtkinter.CTk()
        self.windowColor=customtkinter.set_appearance_mode("light")
        self.theme=customtkinter.set_default_color_theme("green")
        self.window_width=self.root.winfo_screenwidth()
        self.window_height=self.root.winfo_screenheight()
        self.root.geometry(f"{self.window_width}x{self.window_height}")
                
        self.setUp()

    def setUp(self):
        self.profileLabel=customtkinter.CTkLabel(self.root,text="Your Profile",font=("Roboto",28))
        self.profileLabel.pack(pady=20)
    
        self.mainFrame=customtkinter.CTkFrame(self.root,width=1200,height=800,border_width=2,border_color="#76D7C4")
        self.mainFrame.pack_propagate(False)
        self.mainFrame.pack(pady=50)

        self.personalInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Personal Information",font=("Roboto",20),text_color="blue")
        self.personalInfoLabel.place(x=70,y=20,anchor="nw")

        self.pInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=150,border_width=2,border_color="#A3E4D7")
        self.pInfoFrame.pack(pady=50)

        self.fNameLabel=customtkinter.CTkLabel(self.pInfoFrame,text="First Name ",font=("Roboto",18))
        self.fNameLabel.place(x=20,y=10,anchor="nw")
        self.fNameEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Enter First Name",font=("Roboto",18),corner_radius=3)
        self.fNameEntry.place(x=120,y=10,anchor="nw")

        self.mNameLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Middle Name ",font=("Roboto",18))
        self.mNameLabel.place(x=400,y=10,anchor="nw")
        self.mNameEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Enter Middle Name",font=("Roboto",18),corner_radius=3)
        self.mNameEntry.place(x=520,y=10,anchor="nw")

        self.lNameLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Last Name ",font=("Roboto",18))
        self.lNameLabel.place(x=770,y=10,anchor="nw")
        self.lNameEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Enter Last Name",font=("Roboto",18),corner_radius=3)
        self.lNameEntry.place(x=870,y=10,anchor="nw")

        self.dobLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Date of Birth ",font=("Roboto",18))
        self.dobLabel.place(x=20,y=70,anchor="nw")
        self.dobEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="dd/mm/yy",font=("Roboto",18),corner_radius=3)
        self.dobEntry.place(x=130,y=70,anchor="nw")

        self.ageLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Age ",font=("Roboto",18))
        self.ageLabel.place(x=400,y=70,anchor="nw")
        self.ageEntry=customtkinter.CTkEntry(self.pInfoFrame,width=150,height=2,placeholder_text="Your Age",font=("Roboto",18),corner_radius=3)
        self.ageEntry.place(x=450,y=70,anchor="nw")

        self.genderLabel=customtkinter.CTkLabel(self.pInfoFrame,text="Date of Birth ",font=("Roboto",18))
        self.genderLabel.place(x=670,y=70,anchor="nw")
        genders=['Select Your Gender','Male','Female']
        self.genderOption=customtkinter.CTkOptionMenu(self.pInfoFrame,width=150,height=3,font=("Roboto",18),corner_radius=3,values=genders,fg_color="white",text_color="black",dropdown_font=("Roboto",18))
        self.genderOption.pack_propagate(False)
        self.genderOption.place(x=780,y=70,anchor="nw")

        
        



        

    












    def run(self):
        self.root.mainloop()


if __name__=="__main__":
    app=Window()
    app.run()












