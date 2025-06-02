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
    
        cores_disponiveis = self.controller.obter_cores_disponiveis() #Buscando as cores disponíveis do banco via Controller
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
    def exibir_edit(self):

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
        label_custo = tk.Label(self.root, text='Quantidade', font=("Arial", 16, "bold"), bg="#F5F5DC")
        label_custo.place(relx=0.22, rely=0.5, anchor="n")

        # Criando o campo de texto dda quantidade
        self.entryCusto = tk.Entry(self.root, width=30, font=("Arial", 16, "bold"), bg="black", fg="white")
        self.entryCusto.place(relx=0.43, rely=0.5, anchor="n")

        # Criando cor de mana
        label_cor = tk.Label(self.root, text='Cor', font=("Arial", 16, "bold"), bg="#F5F5DC")
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
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 18, "bold"), bg="black", fg="#F5F5DC",width=10, height=1, command=lambda: self.trocar_tela(self.exibir_lista))
        self.btn_voltar.place(relx=0.4, rely=0.7, anchor="n")

        # Criando o botão editar
        self.btn_cadastrar = tk.Button(self.root, text="Editar", font=("Arial", 18, "bold"), bg="black",fg="#F5F5DC", width=10, height=1)
        self.btn_cadastrar.place(relx=0.6, rely=0.7, anchor="n")

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
        #Deselvolver pesquisa com tecla enter AQUI

        # Criando o botão filtrar por cores
        self.btn_filtrar = tk.Button(self.root, text="Filtrar por cores", font=("Arial", 8, "bold"), bg="black", fg="#F5F5DC", width=12, height=1)
        self.btn_filtrar.place(relx=0.22, rely=0.25, anchor="n")

        # Criando um combobox com opções de cores para filrar
        self.combo_cor = ttk.Combobox(self.root, width=30, font=("Arial", 12, "bold"), values=['Mono-Red', 'Mono-Green', 'Mono-Blue', 'Mono-White', 'Mono-Green', 'Colorless'
                                                                                                , 'Mono-Black', 'Azorius', 'Dimir', 'Rakdos', 'Gruul', 'Selesnya', 'Orzho'
                                                                                                , 'Izzet', 'Golgari', 'Boros', 'Simic', 'Abzan', 'Bant', 'Esper', 'Grixis', 'Jeskai'
                                                                                                , 'Jund', 'Mardu', 'Naya', 'Sultai', 'Temur', 'Yore', 'Dune', 'Witch', 'Ink', 'Glint', 'Multicolor'])
        self.combo_cor.place(relx=0.397, rely=0.25, anchor="n")

        # Criando o botão limpar filtros
        self.btn_limpar = tk.Button(self.root, text="Limpar filtros", font=("Arial", 8, "bold"), bg="black", fg="#F5F5DC", width=12, height=1)
        self.btn_limpar.place(relx=0.22, rely=0.30, anchor="n")

        # Criando a tabela onde a lista vai aparecer, aqui usamos treeview, que é uma tabela do tkinter
        self.tree = ttk.Treeview(self.root, columns=("ID","Nome", "Cor", "Tipo", "Custo", "Quantidade"), show="headings", height=13)
        self.tree.place(relx=0.5, rely=0.38, anchor="n")

        # Definindo nome das colunas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Cor", text="Cor")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Custo", text="Custo")
        self.tree.heading("Quantidade", text="Quantidade")

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
        self.btn_editar = tk.Button(self.root, text="Editar", font=("Arial", 12, "bold"), bg="black", fg="#F5F5DC", width=10, height=1, command=lambda: self.trocar_tela(self.exibir_edit))
        self.btn_editar.place(relx=0.33, rely=0.79, anchor="n")
        
        # Criado o botão de excluir
        self.btn_editar = tk.Button(self.root, text="Excluir", font=("Arial", 12, "bold"), bg="black", fg="#F5F5DC", width=10, height=1, command=lambda: self.excluir_carta_selecionada())
        self.btn_editar.place(relx=0.774, rely=0.79, anchor="n")

        # Criado o botão de pesquisa
        self.btn_editar = tk.Button(self.root, text="Pesquisar", font=("Arial", 8, "bold"), bg="black", fg="#F5F5DC", width=12, height=1)
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
