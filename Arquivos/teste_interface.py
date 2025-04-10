import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("blue")


class MyRadiobuttonFrame(customtkinter.CTkFrame):
            
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Organizador')
        self.geometry('500x320')
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.organizador = self

        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", values=["Copiar", "Mover"])
        self.radiobutton_frame.grid(row=2, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew", columnspan=2)
               
        self.button = customtkinter.CTkButton(self, text='Executar', command=self.buttom_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=2)

        self.button_2 = customtkinter.CTkButton(self, text="Sair", command=self.buttom_end)        
        self.button_2.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        
        self.entry_1 = customtkinter.CTkEntry(self, placeholder_text="Caminho de origem")
        self.entry_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew", rowspan=1)

        self.entry_2 = customtkinter.CTkEntry(self, placeholder_text="Caminho de destino")
        self.entry_2.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew", rowspan=1)

        self.textbox = customtkinter.CTkTextbox(self, width=100)
        self.textbox.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew", columnspan=1)

        

    def buttom_callback(self):
        acao = self.radiobutton_frame.get()
        entrada = self.entry_1.get()
        saida = self.entry_2.get()
        if saida == '':
            saida = entrada

    def buttom_end(self):
        self.organizador.destroy()
        self.organizador.quit()
            
app = App()
app.mainloop()

#CustomTKinter
