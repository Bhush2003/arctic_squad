import customtkinter


class DoctorSignupForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Signup Form")
        self.windowColor = customtkinter.set_appearance_mode("light")
        self.theme = customtkinter.set_default_color_theme("green")
        self.main_Frame = customtkinter.CTkScrollableFrame(root, width=600, height=650, border_width=2, fg_color="#CAD9F8")
        self.main_Frame.pack(padx=500, pady=80)

        self.label_personal_info = customtkinter.CTkLabel(self.main_Frame, text="Personal Information", font=("Helvetica", 14, "bold"))
        self.label_personal_info.pack(side="top", fill="x", pady=10)

        self.label_full_name = customtkinter.CTkLabel(self.main_Frame, text="Full Name:")
        self.entry_full_name = customtkinter.CTkEntry(self.main_Frame)

        self.label_gender = customtkinter.CTkLabel(self.main_Frame, text="Gender:")
        self.entry_gender = customtkinter.CTkEntry(self.main_Frame)

        self.label_dob = customtkinter.CTkLabel(self.main_Frame, text="Date of Birth:")
        self.entry_dob = customtkinter.CTkEntry(self.main_Frame)

        self.label_contact_info = customtkinter.CTkLabel(self.main_Frame, text="Contact Information:")
        self.entry_contact_info = customtkinter.CTkEntry(self.main_Frame)

        self.label_full_name.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_full_name.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_gender.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_gender.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_dob.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_dob.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_contact_info.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_contact_info.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_professional_info = customtkinter.CTkLabel(self.main_Frame, text="Professional Information", font=("Helvetica", 14, "bold"))
        self.label_professional_info.pack(side="top", fill="x", pady=10)

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

        self.label_license_number.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_license_number.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_specialty.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_specialty.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_certifications.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_certifications.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_education.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_education.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_experience.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_experience.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_employment.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_employment.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_credential_verification = customtkinter.CTkLabel(self.main_Frame, text="Credential Verification", font=("Helvetica", 14, "bold"))
        self.label_credential_verification.pack(side="top", fill="x", pady=10)

        self.label_attachments = customtkinter.CTkLabel(self.main_Frame, text="Attachments for Credential Documents:")
        self.entry_attachments = customtkinter.CTkEntry(self.main_Frame)

        self.label_npi_number = customtkinter.CTkLabel(self.main_Frame, text="National Provider Identifier (NPI) Number:")
        self.entry_npi_number = customtkinter.CTkEntry(self.main_Frame)

        self.label_dea_registration = customtkinter.CTkLabel(self.main_Frame, text="Drug Enforcement Administration (DEA) Registration:")
        self.entry_dea_registration = customtkinter.CTkEntry(self.main_Frame)

        self.label_attachments.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_attachments.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_npi_number.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_npi_number.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_dea_registration.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_dea_registration.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_work_history = customtkinter.CTkLabel(self.main_Frame, text="Work History", font=("Helvetica", 14, "bold"))
        self.label_work_history.pack(side="top", fill="x", pady=10)

        self.label_previous_employers = customtkinter.CTkLabel(self.main_Frame, text="Previous Employers:")
        self.entry_previous_employers = customtkinter.CTkEntry(self.main_Frame)

        self.label_positions_held = customtkinter.CTkLabel(self.main_Frame, text="Positions Held:")
        self.entry_positions_held = customtkinter.CTkEntry(self.main_Frame)

        self.label_dates_employment = customtkinter.CTkLabel(self.main_Frame, text="Dates of Employment:")
        self.entry_dates_employment = customtkinter.CTkEntry(self.main_Frame)

        self.label_previous_employers.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_previous_employers.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_professional_memberships = customtkinter.CTkLabel(self.main_Frame, text="Professional Memberships", font=("Helvetica", 14, "bold"))
        self.label_professional_memberships.pack(side="top", fill="x", pady=10)

        self.label_medical_associations = customtkinter.CTkLabel(self.main_Frame, text="Memberships in Medical Associations or Societies:")
        self.entry_medical_associations = customtkinter.CTkEntry(self.main_Frame)

        self.label_medical_associations.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_medical_associations.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_references = customtkinter.CTkLabel(self.main_Frame, text="References", font=("Helvetica", 14, "bold"))
        self.label_references.pack(side="top", fill="x", pady=10)

        self.label_professional_references = customtkinter.CTkLabel(self.main_Frame, text="Professional References (Colleagues, Supervisors):")
        self.entry_professional_references = customtkinter.CTkEntry(self.main_Frame)

        self.label_professional_references.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_professional_references.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_background_check = customtkinter.CTkLabel(self.main_Frame, text="Background Check", font=("Helvetica", 14, "bold"))
        self.label_background_check.pack(side="top", fill="x", pady=10)

        self.label_authorization_check = customtkinter.CTkLabel(self.main_Frame, text="Authorization for Background Check (if required by the institution):")
        self.entry_authorization_check = customtkinter.CTkEntry(self.main_Frame)

        self.label_authorization_check.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_authorization_check.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_username_password = customtkinter.CTkLabel(self.main_Frame, text="Username and Password", font=("Helvetica", 14, "bold"))
        self.label_username_password.pack(side="top", fill="x", pady=10)

        self.label_username = customtkinter.CTkLabel(self.main_Frame, text="Username:")
        self.entry_username = customtkinter.CTkEntry(self.main_Frame)

        self.label_password = customtkinter.CTkLabel(self.main_Frame, text="Password:")
        self.entry_password = customtkinter.CTkEntry(self.main_Frame, show="*")

        self.label_username.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_username.pack(side="top", anchor="w", padx=10, pady=5)

        self.label_password.pack(side="top", anchor="w", padx=10, pady=5)
        self.entry_password.pack(side="top", anchor="w", padx=10, pady=5)

        self.button_signup = customtkinter.CTkButton(self.main_Frame, text="Signup", command=self.perform_signup)
        self.button_signup.pack(side="top", fill="x", pady=20)

    def perform_signup(self):
        pass

if __name__ == "__main__":
    root = customtkinter.CTk()
    signup_form = DoctorSignupForm(root)
    root.mainloop()
