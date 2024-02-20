import customtkinter


class DoctorSignupForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Signup Form")

        self.main_Frame=customtkinter.CTkScrollableFrame(root,width=600,height=650,border_width=2,bg_color="grey")
        self.main_Frame.grid(padx=500,pady=80)
        self
        # main_Frame=customtkinter.CTkFrame()
        
        self.label_personal_info = customtkinter.CTkLabel(self.main_Frame, text="Personal Information", font=("Helvetica", 14, "bold"))
        self.label_personal_info.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_full_name = customtkinter.CTkLabel(self.main_Frame, text="Full Name:")
        self.entry_full_name = customtkinter.CTkEntry(self.main_Frame)

        self.label_gender = customtkinter.CTkLabel(self.main_Frame, text="Gender:")
        self.entry_gender = customtkinter.CTkEntry(self.main_Frame)

        self.label_dob = customtkinter.CTkLabel(self.main_Frame, text="Date of Birth:")
        self.entry_dob = customtkinter.CTkEntry(self.main_Frame)

        self.label_contact_info = customtkinter.CTkLabel(self.main_Frame, text="Contact Information:")
        self.entry_contact_info = customtkinter.CTkEntry(self.main_Frame)

        self.label_full_name.grid(row=1, column=0, padx=10, pady=5, sticky='N')
        self.entry_full_name.grid(row=1, column=1, padx=10, pady=5)

        self.label_gender.grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.entry_gender.grid(row=2, column=1, padx=10, pady=5)

        self.label_dob.grid(row=3, column=0, padx=10, pady=5, sticky='W')
        self.entry_dob.grid(row=3, column=1, padx=10, pady=5)

        self.label_contact_info.grid(row=4, column=0, padx=10, pady=5, sticky='W')
        self.entry_contact_info.grid(row=4, column=1, padx=10, pady=5)

        self.label_professional_info = customtkinter.CTkLabel(self.main_Frame, text="Professional Information", font=("Helvetica", 14, "bold"))
        self.label_professional_info.grid(row=5, column=0, columnspan=2, pady=10)

        self.label_license_number = customtkinter.CTkLabel(self.main_Frame, text="Medical License Number:")
        self.entry_license_number = customtkinter.CTkEntry(self.main_Frame)

        self.label_specialty = customtkinter.CTkLabel(self.main_Frame, text="Medical Specialty or Specializations:")
        self.entry_specialty = customtkinter.CTkEntry(self.main_Frame)

        self.label_certifications = customtkinter.CTkLabel(self.main_Frame, text="Board Certification(s):")
        self.entry_certifications = customtkinter.CTkEntry(self.main_Frame)

        self.label_education = customtkinter.CTkLabel(self.main_Frame, text="Educational Background:")
        self.entry_education = customtkinter.CTkEntry(self.main_Frame)

        self.label_experience = customtkinter.CTkLabel(self.main_Frame, text="Years of Experience:")
        self.entry_experience = customtkinter.CTkEntry(self.main_Frame)

        self.label_employment = customtkinter.CTkLabel(self.main_Frame, text="Current Employment:")
        self.entry_employment = customtkinter.CTkEntry(self.main_Frame)

        self.label_license_number.grid(row=6, column=0, padx=10, pady=5, sticky='W')
        self.entry_license_number.grid(row=6, column=1, padx=10, pady=5)

        self.label_specialty.grid(row=7, column=0, padx=10, pady=5, sticky='W')
        self.entry_specialty.grid(row=7, column=1, padx=10, pady=5)

        self.label_certifications.grid(row=8, column=0, padx=10, pady=5, sticky='W')
        self.entry_certifications.grid(row=8, column=1, padx=10, pady=5)

        self.label_education.grid(row=9, column=0, padx=10, pady=5, sticky='W')
        self.entry_education.grid(row=9, column=1, padx=10, pady=5)

        self.label_experience.grid(row=10, column=0, padx=10, pady=5, sticky='W')
        self.entry_experience.grid(row=10, column=1, padx=10, pady=5)

        self.label_employment.grid(row=11, column=0, padx=10, pady=5, sticky='W')
        self.entry_employment.grid(row=11, column=1, padx=10, pady=5)

        self.label_credential_verification = customtkinter.CTkLabel(self.main_Frame, text="Credential Verification", font=("Helvetica", 14, "bold"))
        self.label_credential_verification.grid(row=12, column=0, columnspan=2, pady=10)

        self.label_attachments = customtkinter.CTkLabel(self.main_Frame, text="Attachments for Credential Documents:")
        self.entry_attachments = customtkinter.CTkEntry(self.main_Frame)

        self.label_npi_number = customtkinter.CTkLabel(self.main_Frame, text="National Provider Identifier (NPI) Number:")
        self.entry_npi_number = customtkinter.CTkEntry(self.main_Frame)

        self.label_dea_registration = customtkinter.CTkLabel(self.main_Frame, text="Drug Enforcement Administration (DEA) Registration:")
        self.entry_dea_registration = customtkinter.CTkEntry(self.main_Frame)

        self.label_attachments.grid(row=13, column=0, padx=10, pady=5, sticky='W')
        self.entry_attachments.grid(row=13, column=1, padx=10, pady=5)

        self.label_npi_number.grid(row=14, column=0, padx=10, pady=5, sticky='W')
        self.entry_npi_number.grid(row=14, column=1, padx=10, pady=5)

        self.label_dea_registration.grid(row=15, column=0, padx=10, pady=5, sticky='W')
        self.entry_dea_registration.grid(row=15, column=1, padx=10, pady=5)

        self.label_work_history = customtkinter.CTkLabel(self.main_Frame, text="Work History", font=("Helvetica", 14, "bold"))
        self.label_work_history.grid(row=16, column=0, columnspan=2, pady=10)

        self.label_previous_employers = customtkinter.CTkLabel(self.main_Frame, text="Previous Employers:")
        self.entry_previous_employers = customtkinter.CTkEntry(self.main_Frame)

        self.label_positions_held = customtkinter.CTkLabel(self.main_Frame, text="Positions Held:")
        self.entry_positions_held = customtkinter.CTkEntry(self.main_Frame)

        self.label_dates_employment = customtkinter.CTkLabel(self.main_Frame, text="Dates of Employment:")
        self.entry_dates_employment = customtkinter.CTkEntry(self.main_Frame)

        self.label_previous_employers.grid(row=17, column=0, padx=10, pady=5, sticky='W')
        self.entry_previous_employers.grid(row=17, column=1, padx=10, pady=5)

        self.label_professional_memberships = customtkinter.CTkLabel(self.main_Frame, text="Professional Memberships", font=("Helvetica", 14, "bold"))
        self.label_professional_memberships.grid(row=20, column=0, columnspan=2, pady=10)

        self.label_medical_associations = customtkinter.CTkLabel(self.main_Frame, text="Memberships in Medical Associations or Societies:")
        self.entry_medical_associations = customtkinter.CTkEntry(self.main_Frame)

        self.label_medical_associations.grid(row=21, column=0, padx=10, pady=5, sticky='W')
        self.entry_medical_associations.grid(row=21, column=1, padx=10, pady=5)

        self.label_references = customtkinter.CTkLabel(self.main_Frame, text="References", font=("Helvetica", 14, "bold"))
        self.label_references.grid(row=22, column=0, columnspan=2, pady=10)

        self.label_professional_references = customtkinter.CTkLabel(self.main_Frame, text="Professional References (Colleagues, Supervisors):")
        self.entry_professional_references = customtkinter.CTkEntry(self.main_Frame)

        self.label_professional_references.grid(row=23, column=0, padx=10, pady=5, sticky='W')
        self.entry_professional_references.grid(row=23, column=1, padx=10, pady=5)

        self.label_background_check = customtkinter.CTkLabel(self.main_Frame, text="Background Check", font=("Helvetica", 14, "bold"))
        self.label_background_check.grid(row=24, column=0, columnspan=2, pady=10)

        self.label_authorization_check = customtkinter.CTkLabel(self.main_Frame, text="Authorization for Background Check (if required by the institution):")
        self.entry_authorization_check = customtkinter.CTkEntry(self.main_Frame)

        self.label_authorization_check.grid(row=25, column=0, padx=10, pady=5, sticky='W')
        self.entry_authorization_check.grid(row=25, column=1, padx=10, pady=5)

        self.label_username_password = customtkinter.CTkLabel(self.main_Frame, text="Username and Password", font=("Helvetica", 14, "bold"))
        self.label_username_password.grid(row=26, column=0, columnspan=2, pady=10)

        self.label_username = customtkinter.CTkLabel(self.main_Frame, text="Username:")
        self.entry_username = customtkinter.CTkEntry(self.main_Frame)

        self.label_password = customtkinter.CTkLabel(self.main_Frame, text="Password:")
        self.entry_password = customtkinter.CTkEntry(self.main_Frame, show="*")

        self.label_username.grid(row=27, column=0, padx=10, pady=5, sticky='W')
        self.entry_username.grid(row=27, column=1, padx=10, pady=5)

        self.label_password.grid(row=28, column=0, padx=10, pady=5, sticky='W')
        self.entry_password.grid(row=28, column=1, padx=10, pady=5)

        
        self.button_signup = customtkinter.CTkButton(self.main_Frame, text="Signup", command=self.perform_signup)
        self.button_signup.grid(row=29, column=0, columnspan=2, pady=20)

    def perform_signup(self):
        
        pass

if __name__ == "__main__":
    root = customtkinter.CTk()
   
    signup_form = DoctorSignupForm(root)

    root.mainloop()
