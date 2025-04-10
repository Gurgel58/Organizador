# Projeto organizador de arquivos baseado em extensão
# Esta versão pergunta qual a pasta de origem dos arquivos e também o caminho das novas pastas a serem criadas.
# Também pergunta se os arquivos vão ser Copiados ou Movidos para as novas pastas.

# Este código foi feito a partir do código original, postado no Linkedin, por Felipe Torres. O código original pode ser visto neste link: https://shre.ink/MLHq

import customtkinter
import os
import shutil
import time

# Define tema da interface
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Help do Organizador
ajuda = 'Ajuda do Organizador\n\nEste programa verifica os tipos de arquivos presentes em uma pasta e classifica os mesmos pelo tipo de arquivo, em pastas separadas.\n\nCaminho de Origem: O caminho completo da pasta a ser organizada.\n   P.Ex: /home/<usuário>/Downloads\n\nCaminho de Destino: O caminho completo onde as pastas organizadas vão ser criadas.\n   P.Ex: /home/<usuário>/Documents" (deixar em branco se o local for o mesmo do Caminho de Origem)'


# Definição dos Radio Button
class MyRadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(
            self, text=self.title, fg_color="gray30", corner_radius=6
        )
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(
                self, text=value, value=value, variable=self.variable
            )
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


# Aplicação Organizador
class App(customtkinter.CTk):
    # Definição visual da interface
    def __init__(self):
        super().__init__()

        self.title("Organizador")
        self.geometry("620x360")
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.organizador = self

        self.radiobutton_frame = MyRadiobuttonFrame(
            self, "Options", values=["Copiar", "Mover"]
        )
        self.radiobutton_frame.grid(
            row=2, column=0, padx=(0, 10), pady=(10, 0), sticky="nsew", columnspan=2
        )

        self.button_1 = customtkinter.CTkButton(
            self, text="Executar", command=self.buttom_callback
        )
        self.button_1.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.entry_1 = customtkinter.CTkEntry(
            self, placeholder_text="Caminho de origem"
        )
        self.entry_1.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew", rowspan=1
        )

        self.entry_2 = customtkinter.CTkEntry(
            self, placeholder_text="Caminho de destino"
        )
        self.entry_2.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew", rowspan=1
        )
        self.button_2 = customtkinter.CTkButton(
            self, text="Sair", command=self.buttom_end
        )
        self.button_2.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.button_3 = customtkinter.CTkButton(
            self, text="Ajuda", command=self.buttom_ajuda
        )
        self.button_3.grid(row=4, column=2, padx=10, pady=10, sticky="ew", columnspan=2)

        self.textbox = customtkinter.CTkTextbox(self, width=100)
        self.textbox.grid(
            row=0, column=2, padx=10, pady=(10, 0), sticky="nsew", columnspan=1
        )

        self.textbox_2 = customtkinter.CTkTextbox(self, width=100)
        self.textbox_2.grid(row=2, column=2, padx=10, pady=(10, 0), sticky="nsew", columnspan=1, rowspan=2,
        )

    # Define as ações quando o botão Executar é clicado
    def buttom_callback(self):
        acao = self.radiobutton_frame.get()
        entrada = self.entry_1.get()
        saida = self.entry_2.get()
        if saida == "":
            saida = entrada

        # Trecho responsável pela organização dos arquivos
        categorias = {
            "imagens": (".jpg", ".png", ".jpeg", ".gif", ".bmp"),
            "documentos": (".pdf", ".docx", ".txt", ".epub", ".xlsx", ".xls", ".doc"),
            "audios": (".mp3", ".mp4", ".wav"),
            "programas": (".rpm", ".deb", ".exe", ".tar.gz", ".tgz"),
            "scripts": (".py", ".ipynb", ".sh"),
        }
        arquivos = os.listdir(entrada)

        for pasta in ["imagens", "documentos", "audios", "programas", "scripts"]:
            pasta1 = saida + "/" + pasta
            os.makedirs(pasta1, exist_ok=True)

        for arquivo in arquivos:
            caminho_origem = os.path.join(entrada, arquivo)

            for pasta, extensoes in categorias.items():
                if acao == "copiar":
                    if arquivo.lower().endswith(extensoes):
                        pasta1 = saida + "/" + pasta
                        shutil.copy(caminho_origem, os.path.join(pasta1, arquivo))

                else:
                    if arquivo.lower().endswith(extensoes):
                        pasta1 = saida + "/" + pasta
                        shutil.move(caminho_origem, os.path.join(pasta1, arquivo))
        time.sleep(5)
        self.textbox.insert("0.0", "Ação solicitada executada com sucesso")

    # Define a ação correspondente ao botão Sair
    def buttom_end(self):
        self.organizador.quit()
        self.organizador.destroy()

    def buttom_ajuda(self):
        self.textbox_2.insert("0.0", ajuda)


app = App()
app.mainloop()
