import tkinter as tk
from PIL import ImageTk, Image


class Menu():
    def __init__(self):
        self.root = tk.Tk()
        self.titulo()
        self.menu()
        self.root.mainloop()

    def titulo(self):
        self.root.resizable(False, False) #proibe aumentar a tela
        self.root.title("MTG Manager") #Titulo da tela
        self.root.geometry("600x400") #Tamanho da tela
        self.root.config(bg="#F5F5DC") #Cor de fundo da tela

        # Criando o fundo da tela de cor preta
        self.frame_fundo = tk.Frame(self.root, width=580, height=384, bg="black", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo de cor bege
        self.frame_titulo = tk.Frame(self.root, bg="#F5F5DC", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # Adicionando o Título dentro do Frame
        self.titulo = tk.Label(self.frame_titulo, text="Bem-vindo ao MTG Manager", font=("Arial", 16, "bold"),bg="#F5F5DC", fg="black")
        self.titulo.pack(pady=5)

    def menu(self):
        # Criando frame de fundo do menu
        self.frame_botoes = tk.Frame(self.root, width=400, height=250, bg="#F5F5DC", relief="solid")
        self.frame_botoes.place(relx=0.5, rely=0.5, anchor="center")

        # Adicionando imagem
        imagem = Image.open("../img/mana.jpg") #diretório da imagem
        imagem = imagem.resize((201, 100), Image.Resampling.LANCZOS) #redimencionando a imagem
        self.imagem_tk = ImageTk.PhotoImage(imagem) #convertendo a imagem para o formato do tkinter
        label_imagem = tk.Label(self.root, image=self.imagem_tk) # Adicionando a imagem ao label
        label_imagem.place(relx=0.5, rely=0.2, anchor="n") # Adicionando a imagem ao frame
        self.label_imagem = label_imagem

        # Criando o botão de cadastro de cartas
        self.btn_cadastro = tk.Button(self.root, text="Cadastro de cartas", font=("Arial", 10, "bold"),bg="black", fg="white", width=24, height=1)
        self.btn_cadastro.place(relx=0.5, rely=0.5, anchor="n")

        # Criando o botão de listagem de cartas
        self.btn_listagem = tk.Button(self.root, text="Listagem de cartas", font=("Arial", 10, "bold"),bg="black", fg="white", width=24, height=1)
        self.btn_listagem.place(relx=0.5, rely=0.6, anchor="n")

        # Criando o botão de sair
        self.btn_listagem = tk.Button(self.root, text="Sair", font=("Arial", 10, "bold"), bg="black",fg="white", width=24, height=1)
        self.btn_listagem.place(relx=0.5, rely=0.7, anchor="n")

Menu()