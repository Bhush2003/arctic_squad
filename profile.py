import customtkinter

class Window:
    def __init__(self):
        self.root=customtkinter.CTk(fg_color="#58D68D")
        self.windowColor=customtkinter.set_appearance_mode("light")
        self.theme=customtkinter.set_default_color_theme("green")
        self.window_width=self.root.winfo_screenwidth()
        self.window_height=self.root.winfo_screenheight()
        self.root.geometry(f"{self.window_width}x{self.window_height}")
                
        
        self.profileLabel=customtkinter.CTkLabel(self.root,text="Your Profile",font=("Roboto",28))
        self.profileLabel.pack(pady=20)
        self.updateButton=customtkinter.CTkButton(self.root,text="Update Profile",font=("Roboto",20),command=self.setUp)
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

        self.mainFrame=customtkinter.CTkScrollableFrame(self.root,width=1200,height=800,border_width=2,border_color="#76D7C4")
        #self.mainFrame.pack_propagate(False)
        self.mainFrame.pack(pady=50)


        self.personalInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Personal Information",font=("Roboto",20),text_color="blue")
        self.personalInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW)

        self.pInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=170,border_width=2,border_color="#A3E4D7")
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

        self.nextbutton=customtkinter.CTkButton(self.pInfoFrame,text="Next",command=self.contact,fg_color="#7FB3D5",font=("Roboto",18))
        self.nextbutton.place(x=900,y=118,anchor="nw")

    def contact(self):

        if hasattr(self, 'contact_clicked') and self.contact_clicked:
            return
        self.contact_clicked = True

        self.contactInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Contact Information",font=("Roboto",20),text_color="blue")
        self.contactInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.contactInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=400,border_width=2,border_color="#A3E4D7")
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

        self.nextbutton2=customtkinter.CTkButton(self.contactInfoFrame,text="Next",command=self.physicalChar,fg_color="#7FB3D5",font=("Roboto",18))
        self.nextbutton2.place(x=900,y=350,anchor="nw")

    def physicalChar(self):

        if hasattr(self, 'physical_char_clicked') and self.physical_char_clicked:
            return
        self.physical_char_clicked = True

        self.physicalCharInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Physical Characteristics",font=("Roboto",20),text_color="blue")
        self.physicalCharInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.physicalCharFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=100,border_width=2,border_color="#A3E4D7")
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

        self.nextbutton3=customtkinter.CTkButton(self.physicalCharFrame,text="Next",command=self.vitalSigns,fg_color="#7FB3D5",font=("Roboto",18))
        self.nextbutton3.place(x=900,y=50,anchor="nw")


    def vitalSigns(self):

        if hasattr(self, 'vital_Signs_clicked') and self.vital_Signs_clicked:
            return
        self.vital_Signs_clicked = True

        self.vitalSignsInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Vital Signs ",font=("Roboto",20),text_color="blue")
        self.vitalSignsInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.vitalSignsInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=410,border_width=2,border_color="#A3E4D7")
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

        self.nextbutton4=customtkinter.CTkButton(self.vitalSignsInfoFrame,text="Next",command=self.lifestyle,fg_color="#7FB3D5",font=("Roboto",18))
        self.nextbutton4.place(x=900,y=360,anchor="nw")

    def lifestyle(self):

        if hasattr(self, 'lifestyle_clicked') and self.lifestyle_clicked:
            return
        self.lifestyle_clicked = True

        self.lifestyleInfoLabel=customtkinter.CTkLabel(self.mainFrame,text="Lifestyle and Behavioral Factors ",font=("Roboto",20),text_color="blue")
        self.lifestyleInfoLabel.pack(side=customtkinter.TOP,anchor=customtkinter.NW,pady=10)

        self.lifestyleInfoFrame=customtkinter.CTkFrame(self.mainFrame,width=1100,height=150,border_width=2,border_color="#A3E4D7")
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

        self.nextbutton5=customtkinter.CTkButton(self.lifestyleInfoFrame,text="Submit",font=("Roboto",18),command=self.submit,fg_color="#7FB3D5")
        self.nextbutton5.place(x=900,y=100,anchor="nw")


    def submit(self):
        if hasattr(self,'submit_clicked') and self.submit_clicked:
            return
        self.submit_clicked=True

        self.profile()
        self.mainFrame.pack_forget()
        

        
        



    def run(self):
        self.root.mainloop()


if __name__=="__main__":
    app=Window()
    app.run()












