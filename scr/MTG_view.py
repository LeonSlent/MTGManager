import tkinter as tk
from PIL import ImageTk, Image
import sys
from tkinter import ttk
from tkinter import messagebox, Toplevel


class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("MTG Manager")
        self.root.geometry("1200x720")
        self.root.config(bg="#F5F5DC")
        self.frame_atual = None
        self.exibir_menu()
        self.root.mainloop()

    # Função para trocar de tela
    def trocar_tela(self, tela_nova):
        if self.frame_atual:
            self.frame_atual.destroy()
        tela_nova()

    # Função para exibir o menu
    def exibir_menu(self):

        self.root.resizable(False, False) #proibe aumentar a tela
        self.root.title("MTG Manager - Menu") #Titulo da tela
        self.root.geometry("1200x720") #Tamanho da tela
        self.root.config(bg="#F5F5DC") #Cor de fundo da tela

        # Criando o fundo da tela de cor preta
        self.frame_fundo = tk.Frame(self.root, width=1160, height=680, bg="black", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo de cor bege
        self.frame_titulo = tk.Frame(self.root, bg="#F5F5DC", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # criando o Título dentro do Frame
        self.titulo = tk.Label(self.frame_titulo, text="Bem-vindo ao MTG Manager", font=("Arial", 32, "bold"),bg="#F5F5DC", fg="black")
        self.titulo.pack(pady=5)

        # Criando frame de fundo do menu
        self.frame_botoes = tk.Frame(self.root, width=800, height=500, bg="#F5F5DC", relief="solid")
        self.frame_botoes.place(relx=0.5, rely=0.5, anchor="center")

        # criando imagem
        imagem = Image.open("img\mana.jpg") #diretório da imagem
        imagem = imagem.resize((402, 200), Image.Resampling.LANCZOS) #redimencionando a imagem
        self.imagem_tk = ImageTk.PhotoImage(imagem) #convertendo a imagem para o formato do tkinter
        label_imagem = tk.Label(self.root, image=self.imagem_tk) # Adicionando a imagem ao label
        label_imagem.place(relx=0.5, rely=0.2, anchor="n") # Adicionando a imagem ao frame
        self.label_imagem = label_imagem

        # Criando o botão de cadastro de cartas
        self.btn_cadastro = tk.Button(self.root, text="Cadastro de cartas", font=("Arial", 18, "bold"),bg="black", fg="#F5F5DC", width=26, height=1, command=lambda: self.trocar_tela(self.exibir_cadastro))
        self.btn_cadastro.place(relx=0.5, rely=0.5, anchor="n")

        # Criando o botão de listagem de cartas
        self.btn_listagem = tk.Button(self.root, text="Listagem de cartas", font=("Arial", 18, "bold"),bg="black", fg="#F5F5DC", width=26, height=1, command=lambda: self.trocar_tela(self.exibir_lista))
        self.btn_listagem.place(relx=0.5, rely=0.6, anchor="n")

        # Criando o botão de sair
        self.btn_listagem = tk.Button(self.root, text="Sair", font=("Arial", 18, "bold"), bg="black",fg="#F5F5DC", width=26, height=1, command=self.close)
        self.btn_listagem.place(relx=0.5, rely=0.7, anchor="n")

    # Funçao para fechar no botão sair
    def close(self):
        sys.exit()

    # Função para adicionar carta
    def exibir_cadastro(self):
    
        self.cores_vars = {}  #Dicionário: chave = id_cor, valor = BooleanVar()
        self.root.resizable(False, False)  # proibe aumentar a tela
        self.root.title("MTG Manager - Cadastro")  # Titulo da tela
        self.root.geometry("1200x720")  # Tamanho da tela
        self.root.config(bg="#F5F5DC")  # Cor de fundo da tela

        # Criando o fundo da tela de cor preta
        self.frame_fundo = tk.Frame(self.root, width=1160, height=680, bg="black", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo de cor bege
        self.frame_titulo = tk.Frame(self.root, bg="#F5F5DC", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # Criando o Título dentro do Frame
        self.titulo = tk.Label(self.frame_titulo, text="Cadastro de Cartas", font=("Arial", 32, "bold"),bg="#F5F5DC", fg="black")
        self.titulo.pack(pady=5)

        # Criando frame de fundo do cadastro
        self.frame_cadastro = tk.Frame(self.root, width=800, height=500, bg="#F5F5DC", relief="solid")
        self.frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")

        # Criando imagem
        imagem = Image.open("img/mana2.png")  # diretório da imagem
        imagem = imagem.resize((220, 125), Image.Resampling.LANCZOS)  # redimencionando a imagem
        self.imagem_tk = ImageTk.PhotoImage(imagem)  # convertendo a imagem para o formato do tkinter
        label_imagem = tk.Label(self.root, image=self.imagem_tk, bg="#F5F5DC")  # Adicionando a imagem ao label
        label_imagem.place(relx=0.71, rely=0.23, anchor="n")  # Adicionando a imagem ao frame
        self.label_imagem = label_imagem

        # Criando nome
        label_nome = tk.Label(self.root, text='Nome', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_nome.place(relx=0.22, rely=0.2, anchor="n")

        # Criando o campo de texto do nome
        self.entryNome = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryNome.place(relx=0.43, rely=0.2, anchor="n")

        # Criando tipo
        label_tipo = tk.Label(self.root, text='Tipo', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_tipo.place(relx=0.22, rely=0.3, anchor="n")

        # Criando o campo de texto do tipo
        self.entryTipo = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryTipo.place(relx=0.43, rely=0.3, anchor="n")

        # Criando custo de mana
        label_custo = tk.Label(self.root, text='Custo', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_custo.place(relx=0.22, rely=0.4, anchor="n")

        # Criando o campo de texto do custo de mana
        self.entryCusto = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryCusto.place(relx=0.43, rely=0.4, anchor="n")

        # Criando quantidade
        label_quantidade = tk.Label(self.root, text='Quantidade', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_quantidade.place(relx=0.22, rely=0.5, anchor="n")

        # Criando o campo de texto dda quantidade
        self.entryQuantidade = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryQuantidade.place(relx=0.43, rely=0.5, anchor="n")

        # Criando cor de mana
        label_cor = tk.Label(self.root, text='Cor', font=("Arial", 15, "bold"), bg="#F5F5DC")
        label_cor.place(relx=0.22, rely=0.6, anchor="n")

        # Criando variavel para botões
        self.azul = tk.BooleanVar()
        self.branco = tk.BooleanVar()
        self.preto = tk.BooleanVar()
        self.vermelho = tk.BooleanVar()
        self.verde = tk.BooleanVar()
        self.incolor = tk.BooleanVar()


        # Criando as opções de cores de mana
        chkBttn = tk.Checkbutton(text='Azul', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.azul,anchor=tk.W)
        chkBttn.place(relx=0.29, rely=0.606, anchor="n")

        chkBttn = tk.Checkbutton(text='Branco', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.branco,anchor=tk.W)
        chkBttn.place(relx=0.36, rely=0.606, anchor="n")

        chkBttn = tk.Checkbutton(text='Preto', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.preto,anchor=tk.W)
        chkBttn.place(relx=0.43, rely=0.606, anchor="n")

        chkBttn = tk.Checkbutton(text='Vermelho', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.vermelho,anchor=tk.W)
        chkBttn.place(relx=0.50, rely=0.606, anchor="n")

        chkBttn = tk.Checkbutton(text='Verde', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.verde,anchor=tk.W)
        chkBttn.place(relx=0.57, rely=0.606, anchor="n")

        chkBttn = tk.Checkbutton(text='Incolor', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.incolor,anchor=tk.W)
        chkBttn.place(relx=0.64, rely=0.606, anchor="n")

        # Criando o botão voltar
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 18, "bold"), bg="black", fg="#F5F5DC",width=10, height=1,command=lambda: self.trocar_tela(self.exibir_menu))
        self.btn_voltar.place(relx=0.4, rely=0.7, anchor="n")

        # Criando o botão cadastrar
        self.btn_cadastrar = tk.Button(self.root, text="Cadastrar", font=("Arial", 18, "bold"), bg="black",fg="#F5F5DC", width=10, height=1, command=lambda: self.adicionar_carta())
        self.btn_cadastrar.place(relx=0.6, rely=0.7, anchor="n")

    # Função para editar carta
    def exibir_edit(self, carta):

        self.root.resizable(False, False)  # proibe aumentar a tela
        self.root.title("MTG Manager - Editar")  # Titulo da tela
        self.root.geometry("1200x720")  # Tamanho da tela
        self.root.config(bg="#F5F5DC")  # Cor de fundo da tela

        # Criando o fundo da tela de cor preta
        self.frame_fundo = tk.Frame(self.root, width=1160, height=680, bg="black", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo de cor bege
        self.frame_titulo = tk.Frame(self.root, bg="#F5F5DC", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # Criando o Título dentro do Frame
        self.titulo = tk.Label(self.frame_titulo, text="Editar Cartas", font=("Arial", 32, "bold"),bg="#F5F5DC", fg="black")
        self.titulo.pack(pady=5)

        # Criando frame de fundo do cadastro
        self.frame_cadastro = tk.Frame(self.root, width=800, height=500, bg="#F5F5DC", relief="solid")
        self.frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")

        # Criando imagem
        imagem = Image.open("img/mana2.png")  # diretório da imagem
        imagem = imagem.resize((220, 125), Image.Resampling.LANCZOS)  # redimencionando a imagem
        self.imagem_tk = ImageTk.PhotoImage(imagem)  # convertendo a imagem para o formato do tkinter
        label_imagem = tk.Label(self.root, image=self.imagem_tk, bg="#F5F5DC")  # Adicionando a imagem ao label
        label_imagem.place(relx=0.71, rely=0.23, anchor="n")  # Adicionando a imagem ao frame
        self.label_imagem = label_imagem

        # Criando nome
        label_nome = tk.Label(self.root, text='Nome', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_nome.place(relx=0.22, rely=0.2, anchor="n")

        # Criando o campo de texto do nome
        self.entryNome = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryNome.place(relx=0.43, rely=0.2, anchor="n")

        # Atualiza campo com valores
        self.entryNome.delete(0, tk.END)
        self.entryNome.insert(0, carta[1])  

        # Criando tipo
        label_tipo = tk.Label(self.root, text='Tipo', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_tipo.place(relx=0.22, rely=0.3, anchor="n")

        # Criando o campo de texto do tipo
        self.entryTipo = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryTipo.place(relx=0.43, rely=0.3, anchor="n")

        # Atualiza campo com valores
        self.entryTipo.delete(0, tk.END)
        self.entryTipo.insert(0, carta[2])  # indice 2 = tipo

        # Criando custo de mana
        label_custo = tk.Label(self.root, text='Custo', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_custo.place(relx=0.22, rely=0.4, anchor="n")

        # Criando o campo de texto do custo de mana
        self.entryCusto = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryCusto.place(relx=0.43, rely=0.4, anchor="n")

        # Atualiza campo com valores
        self.entryCusto.delete(0, tk.END)
        self.entryCusto.insert(0, str(carta[3]))  # indice 3 = custo

        # Criando quantidade
        label_quantidade = tk.Label(self.root, text='Quantidade', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_quantidade.place(relx=0.22, rely=0.5, anchor="n")

        # Criando o campo de texto dda quantidade
        self.entryQuantidade = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryQuantidade.place(relx=0.43, rely=0.5, anchor="n")

        # Atualiza campo com valores
        self.entryQuantidade.delete(0, tk.END)
        self.entryQuantidade.insert(0, str(carta[4]))

        # Criando cor de mana
        label_cor = tk.Label(self.root, text='Cor', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_cor.place(relx=0.22, rely=0.6, anchor="n")

        # Campos de cores (Checkboxes)
        cores_da_carta = carta[5]  # indice 5 = string com as cores, ex: "Branco, Azul"
        cores_lista = cores_da_carta.split(", ") if cores_da_carta else []

        # Criando variavel para botões
        self.azul = tk.BooleanVar(value="Azul" in cores_lista)
        self.branco = tk.BooleanVar(value="Branco" in cores_lista)
        self.preto = tk.BooleanVar(value="Preto" in cores_lista)
        self.vermelho = tk.BooleanVar(value="Vermelho" in cores_lista)
        self.verde = tk.BooleanVar(value="Verde" in cores_lista)
        self.incolor = tk.BooleanVar(value="Incolor" in cores_lista)

        # Criando as opções de cores de mana
        chkBttn2 = tk.Checkbutton(text='Azul', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.azul,anchor=tk.W)
        chkBttn2.place(relx=0.29, rely=0.606, anchor="n")

        chkBttn2 = tk.Checkbutton(text='Branco', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.branco,anchor=tk.W)
        chkBttn2.place(relx=0.36, rely=0.606, anchor="n")

        chkBttn2 = tk.Checkbutton(text='Preto', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.preto,anchor=tk.W)
        chkBttn2.place(relx=0.43, rely=0.606, anchor="n")

        chkBttn2 = tk.Checkbutton(text='Vermelho', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.vermelho,anchor=tk.W)
        chkBttn2.place(relx=0.50, rely=0.606, anchor="n")

        chkBttn2 = tk.Checkbutton(text='Verde', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.verde,anchor=tk.W)
        chkBttn2.place(relx=0.57, rely=0.606, anchor="n")

        chkBttn2 = tk.Checkbutton(text='Incolor', font=("Arial", 12, "bold"), bg="#F5F5DC", variable=self.incolor,anchor=tk.W)
        chkBttn2.place(relx=0.64, rely=0.606, anchor="n")

        # Criando o botão voltar
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 18, "bold"), bg="black", fg="#F5F5DC",width=10, height=1, command=lambda: self.trocar_tela(self.exibir_lista))
        self.btn_voltar.place(relx=0.4, rely=0.7, anchor="n")

        # Criando o botão editar
        self.btn_editar = tk.Button(self.root, text="Editar", font=("Arial", 18, "bold"), bg="black",fg="#F5F5DC", width=10, height=1, command=lambda: self.salvar_edicao_carta(carta[0]))
        self.btn_editar.place(relx=0.6, rely=0.7, anchor="n")

    # Obter os valores dos campos de entrada
    def exibir_lista(self):

        self.root.resizable(False, False)  # proibe aumentar a tela
        self.root.title("MTG Manager - Lista")  # Titulo da tela
        self.root.geometry("1200x720")  # Tamanho da tela
        self.root.config(bg="#F5F5DC")  # Cor de fundo da tela

        # Criando o fundo da tela de cor preta
        self.frame_fundo = tk.Frame(self.root, width=1160, height=680, bg="black", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo de cor bege
        self.frame_titulo = tk.Frame(self.root, bg="#F5F5DC", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # Criando o Título dentro do Frame
        self.titulo = tk.Label(self.frame_titulo, text="Lista de Cartas", font=("Arial", 32, "bold"), bg="#F5F5DC",fg="black")
        self.titulo.pack(pady=5)

        # Criando frame de fundo
        self.frame_cadastro = tk.Frame(self.root, width=800, height=500, bg="#F5F5DC", relief="solid")
        self.frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")

        # Criando pesquisa
        self.entry_pesquisa = tk.Entry(self.root, font=("Arial", 11), width=50)
        self.entry_pesquisa.place(relx=0.35, rely=0.18, anchor="n")
        self.entry_pesquisa.insert(0, "Pesquisar carta...")
        

        # Criando o botão filtrar por cores
        self.btn_filtrar = tk.Button(self.root, text="Filtrar por cores", font=("Arial", 8, "bold"), bg="black", fg="#F5F5DC", width=12, height=1, command=self.filtrar_por_cores)
        self.btn_filtrar.place(relx=0.22, rely=0.25, anchor="n")

        # Criando um combobox com opções de cores para filrar
        self.combo_cor = ttk.Combobox(self.root, width=30, font=("Arial", 12, "bold"), values=['Mono-Red', 'Mono-Green', 'Mono-Blue', 'Mono-White', 'Mono-Green', 'Mono-Black', 'Azorius', 'Dimir', 'Rakdos', 'Gruul', 'Selesnya', 'Orzho'
                                                                                                , 'Izzet', 'Golgari', 'Boros', 'Simic', 'Abzan', 'Bant', 'Esper', 'Grixis', 'Jeskai'
                                                                                                , 'Jund', 'Mardu', 'Naya', 'Sultai', 'Temur', 'Yore', 'Dune', 'Witch', 'Ink', 'Glint', 'Multicolor'])
        self.combo_cor.place(relx=0.397, rely=0.25, anchor="n")

        # Criando o botão limpar filtros
        self.btn_limpar = tk.Button(self.root, text="Limpar filtros", font=("Arial", 8, "bold"), bg="black", fg="#F5F5DC", width=12, height=1, command=self.limpar_filtros)
        self.btn_limpar.place(relx=0.22, rely=0.30, anchor="n")

        # Criando a tabela onde a lista vai aparecer, aqui usamos treeview, que é uma tabela do tkinter
        self.tree = ttk.Treeview(self.root, columns=("ID","Nome", "Cor", "Tipo", "Custo", "Quantidade"), show="headings", height=13)
        self.tree.place(relx=0.5, rely=0.38, anchor="n")

        # Definindo nome das colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome", command=lambda _col="Nome": self.treeview_ordenacao(self.tree, _col, False))
        self.tree.heading("Cor", text="Cor")
        self.tree.heading("Tipo", text="Tipo", command=lambda _col="Tipo": self.treeview_ordenacao(self.tree, _col, False))
        self.tree.heading("Custo", text="Custo", command=lambda _col="Custo": self.treeview_ordenacao(self.tree, _col, False))
        self.tree.heading("Quantidade", text="Quantidade", command=lambda _col="Quantidade": self.treeview_ordenacao(self.tree, _col, False))

        # Ajustando a largura das colunas
        self.tree.column("ID", width=0, anchor="w", stretch=False)
        self.tree.column("Nome", width=300, anchor="c")
        self.tree.column("Cor", width=140, anchor="c")
        self.tree.column("Tipo", width=190, anchor="c")
        self.tree.column("Custo", width=50, anchor="c")
        self.tree.column("Quantidade", width=85, anchor="c")

        cartas = self.controller.obter_cartas_com_cores()
        for id_carta, nome, tipo, custo, quantidade, cores in cartas:
            self.tree.insert("", "end",values=(id_carta, nome, cores or "Nenhuma", tipo, custo, quantidade))

            
        # Criando o botão voltar
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 12, "bold"), bg="black", fg="#F5F5DC", width=10, height=1, command=lambda: self.trocar_tela(self.exibir_menu))
        self.btn_voltar.place(relx=0.227, rely=0.79, anchor="n")

        # Criado o botão de editar
        self.btn_editar = tk.Button(self.root, text="Editar", font=("Arial", 12, "bold"), bg="black", fg="#F5F5DC", width=10, height=1, command=self.editar_carta_selecionada)
        self.btn_editar.place(relx=0.33, rely=0.79, anchor="n")
        
        # Criado o botão de excluir
        self.btn_editar = tk.Button(self.root, text="Excluir", font=("Arial", 12, "bold"), bg="black", fg="#F5F5DC", width=10, height=1, command=lambda: self.excluir_carta_selecionada())
        self.btn_editar.place(relx=0.774, rely=0.79, anchor="n")

        # Criado o botão de pesquisa
        self.btn_editar = tk.Button(self.root, text="Pesquisar", font=("Arial", 8, "bold"), bg="black", fg="#F5F5DC", width=12, height=1, command=self.pesquisar_cartas)
        self.btn_editar.place(relx=0.57, rely=0.177, anchor="n")

    # Função para adicionar cartas
    def adicionar_carta(self, ):

        # Pega os valores da carta
        nome = self.entryNome.get()
        tipo = self.entryTipo.get()
        custo = self.entryCusto.get()
        quantidade = int(self.entryQuantidade.get())

        # Dicionario que vincula as cores as suas respectivas chaves no banco de dados
        mapa_cores = {
            "Branco": (1, self.branco),
            "Azul": (2, self.azul),
            "Preto": (3, self.preto),
            "Vermelho": (4, self.vermelho),
            "Verde": (5, self.verde),
            "Incolor": (6, self.incolor),
            }
        
        cores_ids = [id_cor for (id_cor, var) in mapa_cores.values() if var.get()] #Faz uma varredura no checkbox para saber quais cores foram  selecionadas
        self.controller.adicionar_carta(nome, tipo, custo, quantidade, cores_ids)

        self.confirmar_cadastro()

        # Limpar os campos após o cadastro
        self.entryNome.delete(0, tk.END)
        self.entryTipo.delete(0, tk.END)
        self.entryCusto.delete(0, tk.END)
        self.entryQuantidade.delete(0, tk.END)
        for _, var in mapa_cores.values():
            var.set(False)

        

    def confirmar_exclusao(self, callback):
        # Cria uma nova janela acima da principal
        janela = tk.Toplevel(self.root)
        janela.title("Confirmar exclusão")
        janela.geometry("300x150")
        janela.resizable(False, False)
        janela.grab_set()  # Impede interações fora da janela

        # Centralizar em relação ao root
        self.root.update_idletasks()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        win_width = 300
        win_height = 150
        pos_x = root_x + (root_width - win_width) // 2
        pos_y = root_y + (root_height - win_height) // 2
        janela.geometry(f"+{pos_x}+{pos_y}")

        # Texto
        tk.Label(janela, text="Tem certeza que deseja excluir esta carta?", font=("Arial", 10)).pack(pady=20)

        # Botões
        frame_botoes = tk.Frame(janela)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="Sim", width=10, command=lambda: [janela.destroy(), callback(True)]).pack(side="left", padx=10)
        tk.Button(frame_botoes, text="Não", width=10, command=lambda: [janela.destroy(), callback(False)]).pack(side="right", padx=10)

    def excluir_carta_selecionada(self):
        item_selecionado = self.tree.selection()
        if item_selecionado:
            def ao_confirmar(resposta):
                if resposta:
                    valores = self.tree.item(item_selecionado)["values"]
                    id_carta = valores[0]
                    self.controller.excluir_carta(id_carta)
                    self.tree.delete(item_selecionado)

            self.confirmar_exclusao(ao_confirmar)

    def treeview_ordenacao(self, tv, col, reverse):
        # tv: o widget Treeview que será ordenado.
        # col: o nome da coluna que deve ser usada para ordenar.
        # Pega todos os itens da treeview. tv.get_children('') pega todos os IDs dos itens da árvore.
        # tv.set(k, col) obtém o valor da coluna col do item k.
        # Então l é uma lista do tipo: [(valor_coluna, id_item), ...]
        l = [(tv.set(k, col), k) for k in tv.get_children('')]

        # Tenta ordenar numericamente se possível
        try:
            l.sort(key=lambda t: int(t[0]), reverse=reverse) 
        except ValueError:
            l.sort(key=lambda t: t[0].lower(), reverse=reverse)  # se ordenação falhou com numeros inteiros (no caso de nome) ordena o texto em ordem alfabetica

        # Reorganiza os itens agora ja ordenados
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # Atualiza o comando do cabeçalho para alternar a ordem na próxima vez
        tv.heading(col, command=lambda: self.treeview_ordenacao(tv, col, not reverse))

    def filtrar_por_cores(self):
        cores_selecionadas = self.combo_cor.get() #pega o valor selecionado no combobox
        
    
        grupos_cores = {
        # Mono-color (1 cor)
        "Mono-Red": ["Vermelho"],
        "Mono-Green": ["Verde"],
        "Mono-Blue": ["Azul"],
        "Mono-White": ["Branco"],
        "Mono-Black": ["Preto"],
        "Colorless": ["Incolor"],

        # Duas cores (guildas de Ravnica)
        "Azorius": ["Branco", "Azul"],
        "Dimir": ["Azul", "Preto"],
        "Rakdos": ["Preto", "Vermelho"],
        "Gruul": ["Vermelho", "Verde"],
        "Selesnya": ["Branco", "Verde"],
        "Orzhov": ["Branco", "Preto"],
        "Izzet": ["Azul", "Vermelho"],
        "Golgari": ["Preto", "Verde"],
        "Boros": ["Branco", "Vermelho"],
        "Simic": ["Azul", "Verde"],

        # Três cores (shards e wedges)
        "Abzan": ["Branco", "Preto", "Verde"],      # Wedge (white, black, green)
        "Bant": ["Branco", "Azul", "Verde"],       # Wedge (white, blue, green)
        "Esper": ["Branco", "Azul", "Preto"],      # Wedge (white, blue, black)
        "Grixis": ["Azul", "Preto", "Vermelho"],   # Shard (blue, black, red)
        "Jeskai": ["Branco", "Azul", "Vermelho"],  # Wedge (white, blue, red)
        "Jund": ["Preto", "Vermelho", "Verde"],    # Shard (black, red, green)
        "Mardu": ["Branco", "Preto", "Vermelho"],  # Wedge (white, black, red)
        "Naya": ["Branco", "Vermelho", "Verde"],   # Shard (white, red, green)
        "Sultai": ["Azul", "Preto", "Verde"],      # Wedge (blue, black, green)
        "Temur": ["Azul", "Vermelho", "Verde"],    # Shard (blue, red, green)

        # Quatro cores (4-color combos)
        "Yore": ["Azul", "Preto", "Vermelho", "Verde"],    # Sem branco
        "Dune": ["Branco", "Preto", "Vermelho", "Verde"],  # Sem azul
        "Witch": ["Branco", "Azul", "Vermelho", "Verde"],  # Sem preto
        "Ink": ["Branco", "Azul", "Preto", "Verde"],       # Sem vermelho
        "Glint": ["Branco", "Azul", "Preto", "Vermelho"],  # Sem verde

        # Cinco cores (todos)
        "Multicolor": ["Branco", "Azul", "Preto", "Vermelho", "Verde"]
        }
        
        if not cores_selecionadas:
            # Limpa filtro, pega todas cartas
            cartas_filtradas = self.controller.obter_cartas_com_cores()
        else:
            cores_desejadas = grupos_cores.get(cores_selecionadas, [])
            cartas_filtradas = self.controller.obter_cartas_por_cores(cores_desejadas)

        cores_desejadas = grupos_cores.get(cores_selecionadas, [])
        cartas_filtradas = self.controller.obter_cartas_por_cores(cores_desejadas) #Pede ao controller para buscar as cartas que tenham pelo menos uma dessas cores

        # Limpa a treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insere as cartas filtradas na treeview
        for id_carta, nome, tipo, custo, quantidade, cores in cartas_filtradas:
            self.tree.insert("", "end", values=(id_carta, nome, cores or "Nenhuma", tipo, custo, quantidade))

    def limpar_filtros(self):
        # Limpa a seleção do combobox
        self.combo_cor.set('')  
        
        # Recarrega a lista sem filtro (mostra todas as cartas)
        self.filtrar_por_cores()

    def pesquisar_cartas(self):
        texto = self.entry_pesquisa.get() # pega o texto digitado no campo de pesquisa
        cartas_filtradas = self.controller.buscar_cartas_por_nome(texto) # chama o controller para buscar as cartas
        self.atualizar_treeview(cartas_filtradas) # atualiza a lista exibida 

    def atualizar_treeview(self, cartas):
        self.tree.delete(*self.tree.get_children())  # limpa todos os itens da tabela/treeview
        for id_carta, nome, tipo, custo, quantidade, cores in cartas:
           self.tree.insert("", "end", values=(id_carta, nome, cores or "Nenhuma", tipo, custo, quantidade)) # insere cada carta filtrada no treeview, preenchendo as colunas

    def editar_carta_selecionada(self):
        # Pega o item selecionado na Treeview
        selecionado = self.tree.selection()
        if not selecionado:
            # Se nada estiver selecionado, mostra um alerta e sai da função
            self.aviso_edição()
            return

        # Pega os valores da linha selecionada (tupla com os campos)
        valores = self.tree.item(selecionado)["values"]
        id_carta = valores[0]  # normalmente o ID está na primeira coluna

        # Chama o controller para buscar a carta completa pelo id
        carta = self.controller.obter_carta_por_id(id_carta)

        # Chama a tela de edição, passando a carta para preencher os campos
        self.exibir_edit(carta)

    def salvar_edicao_carta(self, id_carta):
        # Pega os valores atualizados dos campos de entrada
        nome = self.entryNome.get()
        tipo = self.entryTipo.get()
        custo = int(self.entryCusto.get())
        quantidade = int(self.entryQuantidade.get())
        
        # Mapeamento das cores selecionadas, igual no cadastro
        mapa_cores = {
            "Branco": (1, self.branco),
            "Azul": (2, self.azul),
            "Preto": (3, self.preto),
            "Vermelho": (4, self.vermelho),
            "Verde": (5, self.verde),
            "Incolor": (6, self.incolor),
        }
        cores_ids = [id_cor for (id_cor, var) in mapa_cores.values() if var.get()]

        # Chama o controller para atualizar os dados da carta e cores
        self.controller.atualizar_carta(id_carta, nome, tipo, custo, quantidade, cores_ids)

        # Exibe mensagem de sucesso
        self.confirmar_edicao()

    def confirmar_cadastro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Confirmar exclusão")
        janela.geometry("300x150")
        janela.resizable(False, False)
        janela.grab_set()  # Impede interações fora da janela

        # Centralizar em relação ao root
        self.root.update_idletasks()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        win_width = 300
        win_height = 150
        pos_x = root_x + (root_width - win_width) // 2
        pos_y = root_y + (root_height - win_height) // 2
        janela.geometry(f"+{pos_x}+{pos_y}")

        # Texto
        tk.Label(janela, text="Carta cadastrada", font=("Arial", 10)).pack(pady=20)

        # Botões
        frame_botoes = tk.Frame(janela)
        frame_botoes.pack()

    def confirmar_cadastro(self):
        # Cria janela modal para avisar que cadastro foi realizado
        janela = tk.Toplevel(self.root)
        janela.title("Cadastro concluído")
        janela.geometry("300x150")
        janela.resizable(False, False)
        janela.grab_set()  # impede interação com a janela principal

        # Centraliza a janela em relação à principal
        self.root.update_idletasks()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        win_width, win_height = 300, 150
        pos_x = root_x + (root_width - win_width) // 2
        pos_y = root_y + (root_height - win_height) // 2
        janela.geometry(f"+{pos_x}+{pos_y}")

        # Mensagem de confirmação
        tk.Label(janela, text="Carta cadastrada com sucesso!", font=("Arial", 12)).pack(pady=30)

        # Botão OK que fecha a janela
        tk.Button(janela, text="OK", width=10, command=janela.destroy).pack()

    def confirmar_edicao(self):
        # Cria janela modal para avisar que edição foi realizada
        janela = tk.Toplevel(self.root)
        janela.title("Edição concluída")
        janela.geometry("300x150")
        janela.resizable(False, False)
        janela.grab_set()

        # Centraliza a janela
        self.root.update_idletasks()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        win_width, win_height = 300, 150
        pos_x = root_x + (root_width - win_width) // 2
        pos_y = root_y + (root_height - win_height) // 2
        janela.geometry(f"+{pos_x}+{pos_y}")

        # Mensagem de confirmação
        tk.Label(janela, text="Carta editada com sucesso!", font=("Arial", 12)).pack(pady=30)

        # Botão OK que fecha a janela
        tk.Button(janela, text="OK", width=10, command=janela.destroy).pack()

    def aviso_edição(self):
        # Cria janela modal para avisar que edição foi realizada
        janela = tk.Toplevel(self.root)
        janela.title("Selecione uma carta")
        janela.geometry("300x150")
        janela.resizable(False, False)
        janela.grab_set()

        # Centraliza a janela
        self.root.update_idletasks()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        win_width, win_height = 300, 150
        pos_x = root_x + (root_width - win_width) // 2
        pos_y = root_y + (root_height - win_height) // 2
        janela.geometry(f"+{pos_x}+{pos_y}")

        # Mensagem de confirmação
        tk.Label(janela, text="Selecione uma carta!", font=("Arial", 12)).pack(pady=30)

        # Botão OK que fecha a janela
        tk.Button(janela, text="OK", width=10, command=janela.destroy).pack()