import sqlite3

class Model:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path
        self.criar_tabelas()

    def criar_tabelas(Self):
        #Cria tabelas do banco de dados caso ainda nao existam   
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Crando tabelas 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cartas(
                id_carta integer primary key autoincrement,
                nome text not null,
                tipo text not null,
                custo int not null,
                quantidade int not null
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cores(
            id_cor integer primary key autoincrement,
            nome text not null           
            );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cartas_cores (
            id_carta INTEGER NOT NULL,
            id_cor INTEGER NOT NULL,
            PRIMARY KEY (id_carta, id_cor),
            FOREIGN KEY (id_carta) REFERENCES cartas(id_carta) ON DELETE CASCADE,
            FOREIGN KEY (id_cor) REFERENCES cores(id_cor) ON DELETE CASCADE
        );
        ''')

        #cursor.execute('''INSERT OR IGNORE INTO cores (nome) VALUES ('Branco'), ('Azul'), ('Preto'), ('Vermelho'), ('Verde'), ('Incolor');''')

        # Da o commit nos comandos que estão dento das aspas e fecha tudo
        conn.commit()
        conn.close()

    def adicionar_carta(self, nome, tipo, custo, quantidade):
        # Insere uma nova carta na tabela cartas
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Cartas (nome, tipo, custo, quantidade) VALUES (?, ?, ?, ?)''', (nome, tipo, custo, quantidade))
        id_carta = cursor.lastrowid #O lastrowid pega o id da nova carta que foi auto incrementado
        conn.commit()
        conn.close()

        return id_carta

    def buscar_cores(self):
        #Retorna uma lista de tuplas com os dados das cores (id_cor, nome)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id_cor, nome FROM Cores")
        cores = cursor.fetchall()
        conn.close()
        return cores
    
    def vincular_cores_a_carta(self, id_carta, lista_id_cores):
    
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        #Percorre a lista de IDs das cores e para cada cor marcada, insere uma linha na tabela cartas_cores
        for id_cor in lista_id_cores:
            cursor.execute(
                "INSERT INTO cartas_cores (id_carta, id_cor) VALUES (?, ?)",
                (id_carta, id_cor)
            )

        conn.commit()
        conn.close()

    #Busca as cartas para serem mostradas na minha lista
    def buscar_cartas_com_cores(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT
                Cartas.id_carta,
                Cartas.nome,
                Cartas.tipo,
                Cartas.custo,
                Cartas.quantidade,
                GROUP_CONCAT(Cores.nome, ', ') as cores
            FROM Cartas
            LEFT JOIN cartas_cores ON Cartas.id_carta = cartas_cores.id_carta
            LEFT JOIN Cores ON cartas_cores.id_cor = Cores.id_cor
            GROUP BY Cartas.id_carta
                       ''')
        
        resultados = cursor.fetchall()
        conn.close()
        return resultados
    
    #Exclui carta selecionada na minha lista
    def excluir_carta(self, id_carta):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON") #Ativa suporte a FK para excluir em cascata
        cursor = conn.cursor()

        # Primeiro remove da tabela relacional
        cursor.execute("DELETE FROM Cartas WHERE id_carta = ?", (id_carta,))

        conn.commit()
        conn.close()
