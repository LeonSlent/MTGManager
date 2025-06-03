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


    def buscar_cartas_por_cores(self, cores_desejadas):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if not cores_desejadas:
            # se nenhuma cor foi selecionada retorna todas as cores
            cursor.execute('''
            SELECT Cartas.id_carta, Cartas.nome, Cartas.tipo, Cartas.custo, Cartas.quantidade,
                GROUP_CONCAT(Cores.nome, ', ') as cores
            FROM Cartas
            LEFT JOIN cartas_cores ON Cartas.id_carta = cartas_cores.id_carta
            LEFT JOIN Cores ON cartas_cores.id_cor = Cores.id_cor
            GROUP BY Cartas.id_carta
            ''')
            resultados = cursor.fetchall()
        else:
            #monta o fultro para filtrar cartas que tenha todas as cores selecionadas
            num_cores = len(cores_desejadas)
            placeholders = ','.join('?' for _ in cores_desejadas)
            # Consulta que:
            # 1) Agrupa por carta
            # 2) Confirma que a carta possui o número exato de cores (COUNT DISTINCT)
            # 3) Garante que todas as cores desejadas estão presentes (SUM CASE)
            query = f'''
                SELECT Cartas.id_carta, Cartas.nome, Cartas.tipo, Cartas.custo, Cartas.quantidade,
                    GROUP_CONCAT(Cores.nome, ', ') as cores
                FROM Cartas
                JOIN cartas_cores ON Cartas.id_carta = cartas_cores.id_carta
                JOIN Cores ON cartas_cores.id_cor = Cores.id_cor
                GROUP BY Cartas.id_carta
                HAVING COUNT(DISTINCT Cores.nome) = ?
                AND SUM(CASE WHEN Cores.nome IN ({placeholders}) THEN 1 ELSE 0 END) = ?
            '''

            params = [num_cores] + cores_desejadas + [num_cores]
            cursor.execute(query, params)
            resultados = cursor.fetchall()

        conn.close()
        return resultados
    
    def buscar_cartas_por_nome(self, texto):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Executa uma função que busca cartas cujo nome contenha o texto fornecido (LIKE %texto%)
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
            WHERE Cartas.nome LIKE ?
            GROUP BY Cartas.id_carta
        ''', ('%' + texto + '%',))  # %texto% para busca parcial no SQLite

        resultados = cursor.fetchall() # pega todos os resultados da consulta
        conn.close() # fecha a conexão com o banco
        return resultados # retorna a lista de cartas encontradas
    
    # No Model:

    def obter_carta_por_id(self, id_carta):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT Cartas.id_carta, Cartas.nome, Cartas.tipo, Cartas.custo, Cartas.quantidade,
                GROUP_CONCAT(Cores.nome, ', ') as cores
            FROM Cartas
            LEFT JOIN cartas_cores ON Cartas.id_carta = cartas_cores.id_carta
            LEFT JOIN Cores ON cartas_cores.id_cor = Cores.id_cor
            WHERE Cartas.id_carta = ?
            GROUP BY Cartas.id_carta
        ''', (id_carta,))

        carta = cursor.fetchone()
        conn.close()
        return carta
    
    def atualizar_carta(self, id_carta, nome, tipo, custo, quantidade, cores_ids):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Atualiza os dados básicos da carta
        cursor.execute('''
            UPDATE Cartas 
            SET nome = ?, tipo = ?, custo = ?, quantidade = ? 
            WHERE id_carta = ?
        ''', (nome, tipo, custo, quantidade, id_carta))

        # Remove todas as cores vinculadas à carta
        cursor.execute('DELETE FROM cartas_cores WHERE id_carta = ?', (id_carta,))

        # Insere as cores novas
        for id_cor in cores_ids:
            cursor.execute('INSERT INTO cartas_cores (id_carta, id_cor) VALUES (?, ?)', (id_carta, id_cor))

        conn.commit()
        conn.close()


