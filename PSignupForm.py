import customtkinter

class PatientSignupApp:
    def __init__(self):
        self.window = customtkinter.CTk(fg_color="#21f63d")
        self.windowColor = customtkinter.set_appearance_mode("light")
        self.theme = customtkinter.set_default_color_theme("green")
        self.window.title("Patient Signup")
        self.window.geometry('1000x1000')

        self.root = customtkinter.CTkScrollableFrame(master=self.window, width=1100, height=1000, fg_color="#CAD9F8")
        # self.root.pack_propagate(False)
        self.root.pack(padx=200, pady=200)

        self.create_widgets()

    def create_widgets(self):
        self.label_Fname = customtkinter.CTkLabel(self.root, text="First Name:")
        self.entry_Fname = customtkinter.CTkEntry(self.root)

        self.label_Lname = customtkinter.CTkLabel(self.root, text="Last Name:")
        self.entry_Lname = customtkinter.CTkEntry(self.root)

        self.label_Mname = customtkinter.CTkLabel(self.root, text="Middle Name:")
        self.entry_Mname = customtkinter.CTkEntry(self.root)

        self.label_age = customtkinter.CTkLabel(self.root, text="Age:")
        self.entry_age = customtkinter.CTkEntry(self.root)

        self.label_phone = customtkinter.CTkLabel(self.root, text="Phone NO.:")
        self.entry_phone = customtkinter.CTkEntry(self.root)

        self.label_email = customtkinter.CTkLabel(self.root, text="Email:")
        self.entry_email = customtkinter.CTkEntry(self.root)

        self.label_abha = customtkinter.CTkLabel(self.root, text="Abha Id:")
        self.entry_abha = customtkinter.CTkEntry(self.root)

        self.label_Username = customtkinter.CTkLabel(self.root, text="User Name:")
        self.entry_Username = customtkinter.CTkEntry(self.root)

        self.label_passward = customtkinter.CTkLabel(self.root, text="Password:")
        self.entry_passward = customtkinter.CTkEntry(self.root)

        self.label_cpassward = customtkinter.CTkLabel(self.root, text="Confirm Password:")
        self.entry_cpassward = customtkinter.CTkEntry(self.root)

        self.signup_button = customtkinter.CTkButton(self.root, text="Signup")
        self.signup_button.pack(side="top", fill="x", pady=10)

        # Packing labels and entries
        self.label_Fname.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_Fname.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_Lname.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_Lname.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_Mname.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_Mname.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_age.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_age.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_phone.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_phone.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_email.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_email.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_abha.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_abha.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_Username.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_Username.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_passward.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_passward.pack(side="top", anchor="w", padx=10, pady=10)

        self.label_cpassward.pack(side="top", anchor="w", padx=10, pady=10)
        self.entry_cpassward.pack(side="top", anchor="w", padx=10, pady=10)

if __name__ == "__main__":
    app = PatientSignupApp()
    app.window.mainloop()
