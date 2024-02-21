import tkinter
import customtkinter
from PIL import ImageTk, Image

class LoginApp:
    def __init__(self):
        self.app = customtkinter.CTk()
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        self.winWidth = self.app.winfo_screenwidth()
        self.height = self.app.winfo_screenheight()
        self.app.geometry(f"{self.winWidth}x{self.height}")
        self.app.title("Login")

        self.main_page()

    def create_login_frame(self):
        # self.app.destroy()
        # self.loginform=customtkinter.CTk()
        # self.loginform.geometry(f"{self.winWidth}x{self.height}")
        # self.loginform.title("loginform")
        self.frame = customtkinter.CTkFrame(master=self.app, width=340, height=360, fg_color='#76D7C4')
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Log into your Account", font=("Garamond", 20))
        self.l2.place(x=50, y=45)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text="username")
        self.entry1.place(x=50, y=110)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text="password",show="*")
        self.entry2.place(x=50, y=150)

        self.l3 = customtkinter.CTkButton(master=self.frame, text="Forgot password ?", font=("Helventica", 10), text_color='blue',
                                     fg_color='white', hover=True, hover_color='#E5E7E9', width=0.3)
        self.l3.place(x=175, y=185)

        self.button1 = customtkinter.CTkButton(master=self.frame, text="LOGIN", fg_color='green', hover=True, command=self.login_button,
                                          hover_color=['black', 'blue'])
        self.button1.place(x=90, y=220)

        self.l4 = customtkinter.CTkLabel(master=self.frame, text="New Register", font=("Helventica", 10), text_color='blue')
        self.l4.place(x=110, y=250)

        self.button2 = customtkinter.CTkButton(master=self.frame, text="Signup", font=('Shink', 10), text_color='blue',
                                          fg_color='white', hover=True, width=0.5, height=0.3, hover_color='#E5E7E9',command=self.button2_func)
        self.button2.place(x=174, y=254)
        # self.loginform.mainloop()

    def login_button(self):
        self.loginform.destroy()
        self.mainframe2 = customtkinter.CTk()
        self.mainframe2.geometry(f"{self.winWidth}x{self.height}")
        self.mainframe2.title("After login")

        frame1 = customtkinter.CTkFrame(master=self.mainframe2, width=self.winWidth, height=80, fg_color='#00157c',corner_radius=0)
        frame1.pack()

        l4=customtkinter.CTkLabel(frame1,text=" MedVault",font=('Roboto',22),text_color='white')
        l4.place(x=1,y=20,anchor="nw")

        img1=customtkinter.CTkImage(Image.open('D:/PYTHONX/mainproject/assets/pro.png'))
        b1=customtkinter.CTkButton(master=frame1,fg_color='#191970',text='',width=0.1,image=img1,hover=True)
        b1.place(x=self.winWidth-60,y=5,anchor="nw")

        b2=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.8,text='Logout',font=('Roboto',18),text_color='blue',hover=True,hover_color='white')
        b2.place(x=self.winWidth-160,y=5,anchor="nw")

        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.7,text='History',font=('Roboto',18),text_color='blue',hover=True,hover_color='white')
        b3.place(x=self.winWidth-235,y=5,anchor="nw")

        img3=customtkinter.CTkImage(Image.open('D:/PYTHONX/mainproject/assets/stata3.png'))
        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.6,text='Find Doctor',font=('Roboto',18),text_color='blue',hover=True,hover_color='white')
        b3.place(x=self.winWidth-360,y=5,anchor="nw")

        frame2= customtkinter.CTkScrollableFrame(master=self.mainframe2, width=1600, height=800, fg_color='white',border_width=2,border_color='#76D7C4')
        #frame2.pack_propagate(False)
        frame2.pack(pady=70)

        f2label=customtkinter.CTkLabel(frame2,text="TODAY'S TOP STORIES..",font=('Aerial',20),text_color='#191970')
        f2label.pack(padx=100,side=customtkinter.TOP,anchor=customtkinter.NW)

        #image_path = 'D:/PYTHONX/mainproject/assets/image.jpg'  # Adjust the path to your image
        image = Image.open('D:/PYTHONX/mainproject/assets/h1.png')
        tk_image = ImageTk.PhotoImage(image)
        image_label1 = customtkinter.CTkLabel(frame2, image=tk_image,text='')
        image_label1.pack(padx=20, pady=30, anchor='n')

        text_label = customtkinter.CTkLabel(frame2, text='Healthy Diet', font=('Aerial', 30), text_color='black')
        text_label.place(relx=0.5, rely=0.52,  anchor='s')

        paragraph_text = ("""Whether it's the lycopene – the pigment that gives tomatoes their red color – or 
                          Chances are you already know that eating too much sugar isn’t good for you. Yet you’re probably still overdoing it. 
                           Americans average about 270 calories of added sugars each day. That’s about 17  teaspoons a day,
                           compared to the recommended limits of about 12 teaspoon per day or 200 calories.

                         Sugary drinks, candy, baked goods, and sweetened dairy are the main sources of added sugar. But even some savory foods,
                           like breads, tomato sauce, and protein bars, can have sugar, making it all too easy to end up with a 
                          surplus of the sweet stuff. Added sugars may be hard to spot on nutrition labels since they can be listed
                           under a number of names, such as corn syrup, agave nectar, palm sugar, cane juice, or sucrose. 

                        No matter what it’s called, sugar is sugar, and in excess, it can negatively affect your body in many ways. Here’s a closer look at how sugar can
                           mess with your health, from head to toe.something else isn't clear. But some studies have linked eating tomatoes to reduced 
                risk of several types of cancer, including prostate cancer. Studies also suggest that processed tomato products such as juice, sauce, or 
                paste increase the cancer-fighting potential.""")
        paragraph_label = customtkinter.CTkLabel(frame2, text=paragraph_text, font=('Arial', 20), text_color='blue')
        paragraph_label.pack(padx=0,pady=40,anchor='se')
        self.mainframe2.mainloop()

    def button2_func(self):
        self.app.destroy()
        self.signup = customtkinter.CTk()
        self.signup.geometry(f"{self.winWidth}x{self.height}")
        self.signup.title("signup")
        self.signup.mainloop()


    def main_page(self):
        frame1 = customtkinter.CTkFrame(master=self.app, width=self.winWidth, height=80, fg_color='#00157c',corner_radius=0)
        frame1.pack()

        l4=customtkinter.CTkLabel(frame1,text=" MedVault",font=('Roboto',22),text_color='white')
        l4.place(x=1,y=20,anchor="nw")

        img1=customtkinter.CTkImage(Image.open('D:/PYTHONX/mainproject/assets/pro.png'))
        b1=customtkinter.CTkButton(master=frame1,fg_color='#191970',text='',width=0.1,image=img1,hover=True)
        b1.place(x=self.winWidth-60,y=5,anchor="nw")

        img2=customtkinter.CTkImage(Image.open('D:/PYTHONX\mainproject/assets/log4.png'))
        b2=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.8,text='Login',font=('Roboto',18),text_color='#3498DB',hover=True,image=img2,hover_color='#FDFEFE',command=self.create_login_frame)
        b2.place(x=self.winWidth-160,y=5,anchor="nw")

        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.7,text='History',font=('Roboto',18),text_color='blue',hover=True,hover_color='white')
        b3.place(x=self.winWidth-235,y=5,anchor="nw")

        b3=customtkinter.CTkButton(master=frame1,fg_color='#191970',width=0.6,text='Find Doctor',font=('Roboto',18),text_color='blue',hover=True,hover_color='white')
        b3.place(x=self.winWidth-360,y=5,anchor="nw")

        frame2= customtkinter.CTkScrollableFrame(master=self.app, width=1600, height=800, fg_color='white',border_width=2,border_color='#76D7C4')
        #frame2.pack_propagate(False)
        frame2.pack(pady=70)

        f2label=customtkinter.CTkLabel(frame2,text="TODAY'S TOP STORIES..",font=('Aerial',20),text_color='#191970')
        f2label.pack(padx=100,side=customtkinter.TOP,anchor=customtkinter.NW)

        #image_path = 'D:/PYTHONX/mainproject/assets/image.jpg'  # Adjust the path to your image
        image = Image.open('D:/PYTHONX/mainproject/assets/h1.png')
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
        paragraph_label.pack(padx=0,pady=40,anchor='s')
        cont_read1=customtkinter.CTkButton(master=frame2,text="Continue Reading",hover=True,fg_color='gray',hover_color='gray',command=self.create_login_frame)
        cont_read1.place(relx=0.5, rely=0.9,  anchor='s')
        self.app.mainloop()


if __name__ == "__main__":
    app = LoginApp()
    app.app.mainloop()
