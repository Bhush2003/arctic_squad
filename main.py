import customtkinter
from login import MainWindow


class Main:
    def __init__(self):
        self.root=customtkinter.CTk(fg_color="#caf0f8")
        self.windowColor=customtkinter.set_appearance_mode("light")
        self.theme=customtkinter.set_default_color_theme("blue")
        self.root.title('MedVault')
        self.window_width=self.root.winfo_screenwidth()
        self.window_height=self.root.winfo_screenheight()
        self.root.geometry(f"{self.window_width}x{self.window_height}")

        windowObj = MainWindow(self.root,self.window_width)

    def run(self):
        self.root.mainloop()

if __name__=="__main__":
    app=Main()
    app.run()








