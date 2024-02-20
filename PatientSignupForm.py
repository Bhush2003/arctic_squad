import customtkinter

class PatientSignupApp:
    def __init__(self):
        self.window = customtkinter.CTk(fg_color="#21f63d")
        self.window.title("Patient Signup")
        self.window.geometry('1000x1000')

        self.root = customtkinter.CTkFrame(master=self.window, width=1100, height=1000)
        self.root.pack_propagate(False)
        self.root.pack(padx=200,pady=200)

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

        self.signup_button = customtkinter.CTkButton(self.root, text="Signup")
        self.signup_button.grid(row=6, column=0, columnspan=2, pady=10)
    
    # def check_Data(self):
    #     fields=[(self.entry_Fname,)]

if __name__ == "__main__":
    app = PatientSignupApp()
    app.window.mainloop()
