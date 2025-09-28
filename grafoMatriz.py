import math
import heapq
from collections import deque

# Grafo Não Direcionado
class TGrafoND:
    
    TAM_MAX_DEFAULT = 100

    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n  # Número de vértices
        self.m = 0  # Número de arestas
        self.adj = [[0.0 for i in range(n)] for j in range(n)]
        
        self.itens = {}  # {indice: "nome do item"}
        self.itens_reverso = {}  # {"nome do item": indice}
        self.tipo_grafo = 0  # Tipo padrão do grafo

    def insereA(self, v, w, peso=1.0):
        """Insere uma aresta no Grafo não-dirigido com peso"""
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            raise IndexError("Vértice inválido.")
        if self.adj[v][w] == 0:  # Se a aresta não existe
            self.adj[v][w] = float(peso)
            self.adj[w][v] = float(peso)  # Insere aresta nas duas direções
            self.m += 1  # Atualiza qtd arestas

    def insereV(self, nome_vertice):
        """Insere um vértice no grafo"""
        novo_vertice = self.n

        # Cria nova matriz expandida
        nova_adj = [[0.0 for _ in range(self.n + 1)] for _ in range(self.n + 1)]

        # Copia dados da matriz antiga
        for i in range(self.n):
            for j in range(self.n):
                nova_adj[i][j] = self.adj[i][j]
        
        # Atualiza estruturas
        self.adj = nova_adj     
        self.n += 1

        # Inicializa dicionários se não existirem
        if not hasattr(self, 'itens'):
            self.itens = {}  # DICIONÁRIO
            self.itens_reverso = {}

        # Adiciona o novo vértice
        self.itens[novo_vertice] = nome_vertice
        self.itens_reverso[nome_vertice] = novo_vertice

        print(f" Vértice {novo_vertice} '{nome_vertice}' inserido com sucesso!")
        return novo_vertice
        
    def gravar_grafo_arquivo(self, caminho_arquivo="Grafo.txt"):
        """Grava o grafo completo no arquivo SEM PESO"""
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                # Escreve tipo do grafo
                tipo = getattr(self, 'tipo_grafo', 0)
                f.write(f"{tipo}\n")
                
                # Escreve número de vértices
                f.write(f"{self.n}\n")
                
                # Escreve vértices nomeados
                for vertice in sorted(self.itens.keys()):
                    nome = self.itens[vertice]
                    f.write(f'{vertice} "{nome}"\n')
                
                # Conta e escreve arestas
                arestas = []
                for i in range(self.n):
                    for j in range(i + 1, self.n):
                        if self.adj[i][j] > 0:
                            arestas.append((i, j))
                
                # Escreve número total de entradas de arestas (bidirecionais)
                f.write(f"{len(arestas) * 2}\n")
                
                # Escreve arestas (ambas direções)
                for i, j in arestas:
                    f.write(f"{i} {j}\n")
                    f.write(f"{j} {i}\n")
            
            print(f" Grafo gravado no arquivo {caminho_arquivo}")
            return True
            
        except Exception as e:
            print(f" Erro ao gravar arquivo: {e}")
            return False

    def removeA(self, v, w):
        """Remove uma aresta v-w do Grafo não-dirigido"""
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            raise IndexError("Aresta inválida.")
        if self.adj[v][w] > 0:  # testa se temos a aresta
            self.adj[v][w] = 0.0
            self.adj[w][v] = 0.0  # Remove também a aresta inversa
            print(f"Aresta entre os vértices {v} e {w} removida com sucesso.")
            self.m -= 1  # atualiza qtd arestas
        else:
            print(f"Aresta entre os vértices {v} e {w} não pôde ser removida.")

    def removeV(self, v):

        """Remove um vértice do grafo"""
        if v < 0 or v >= self.n:
            raise IndexError("Vértice inválido.")

        vertice_removido = self.get_nome_item(v)

        arestas_removidas = sum(1 for i in range(self.n) if self.adj[v][i] > 0)
        self.m -= arestas_removidas

        nova_matriz = [[0.0 for _ in range(self.n - 1)] for _ in range(self.n - 1)]

        for i in range(self.n):
            if i == v:
                continue
            new_i = i if i < v else i - 1

            for j in range(self.n):
                if j == v:
                    continue
                new_j = j if j < v else j - 1
                nova_matriz[new_i][new_j] = self.adj[i][j]

        del self.itens[v]
        del self.itens_reverso[vertice_removido]

        novo_itens = {}
        novo_itens_reverso = {}

        for old_id, nome in self.itens.items():
            new_id = old_id if old_id < v else old_id -1
            novo_itens[new_id] = nome
            novo_itens_reverso[nome] = new_id

        self.adj = nova_matriz
        self.itens = novo_itens
        self.itens_reverso = novo_itens_reverso
        self.n -= 1

        print(f"Vértice {v} ({vertice_removido}) removido com sucesso.")

    def e_completo(self):
        """Verifica se o Grafo não-dirigido é completo"""
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.adj[i][j] == 0:  # Se falta uma aresta entre vértices diferentes
                    return False
        return True
    
    def arquivo_para_matriz_adjacencia(self, caminho):
        # Dicionário para mapear nomes dos itens para índices
        self.itens = {}  # {indice: "nome do item"}
        self.itens_reverso = {}  # {"nome do item": indice}
        
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = [l.strip() for l in f if l.strip()]

        if len(linhas) < 3:
            raise ValueError("Arquivo inválido: muito poucas linhas")

        # Lê o tipo do grafo (primeira linha)
        tipo_grafo = int(linhas[0])
        
        # Lê o número de vértices (segunda linha)
        num_vertices = int(linhas[1])
        
        # Ajusta o tamanho do grafo
        self.n = num_vertices
        self.adj = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
        self.m = 0
        
        linha_atual = 2
        
        # Lê as definições dos vértices (linhas com aspas)
        while linha_atual < len(linhas) and '"' in linhas[linha_atual]:
            linha = linhas[linha_atual]
            partes = linha.split('"')
            
            if len(partes) >= 2:
                numero_parte = partes[0].strip()
                if numero_parte.isdigit():
                    vertice = int(numero_parte)
                    nome_item = partes[1].strip()
                    self.itens[vertice] = nome_item
                    self.itens_reverso[nome_item] = vertice
            
            linha_atual += 1
        
        # Verifica se existe uma linha com o número de arestas
        num_arestas = None
        if linha_atual < len(linhas):
            try:
                # Tenta interpretar como número de arestas
                possivel_num_arestas = int(linhas[linha_atual])
                # Se for um número isolado, provavelmente é o número de arestas
                if linha_atual + 1 < len(linhas):
                    proxima_linha = linhas[linha_atual + 1].split()
                    if len(proxima_linha) >= 2 and proxima_linha[0].isdigit() and proxima_linha[1].isdigit():
                        num_arestas = possivel_num_arestas
                        linha_atual += 1
            except ValueError:
                pass
        
        # Lê as arestas
        arestas_lidas = 0
        while linha_atual < len(linhas):
            linha = linhas[linha_atual]
            partes = linha.split()
            
            if len(partes) >= 2 and partes[0].isdigit() and partes[1].isdigit():
                v = int(partes[0])
                w = int(partes[1])
                peso = float(partes[2]) if len(partes) >= 3 else 1.0
                
                # Verifica se os vértices são válidos
                if 0 <= v < self.n and 0 <= w < self.n:
                    # Só insere se a aresta ainda não existe (evita duplicatas)
                    if self.adj[v][w] == 0:
                        self.insereA(v, w, peso)
                        arestas_lidas += 1
            
            linha_atual += 1
        
        # Relatório
        print(f"Grafo carregado:")
        print(f"  - Tipo do grafo: {tipo_grafo} ({'não orientado' if tipo_grafo < 4 else 'orientado'})")
        if tipo_grafo in [1, 3, 5, 7]:
            print(f"    (com peso nos vértices)")
        if tipo_grafo in [2, 3, 6, 7]:
            print(f"    (com peso nas arestas)")
        print(f"  - Total de vértices: {self.n}")
        print(f"  - Arestas únicas inseridas: {self.m}")
        if num_arestas:
            print(f"  - Número de arestas declarado no arquivo: {num_arestas}")
            print(f"  - Arestas processadas do arquivo: {arestas_lidas}")
        
        # Armazena o tipo do grafo para uso posterior
        self.tipo_grafo = tipo_grafo

    def get_nome_item(self, vertice):
        #Retorna o nome do item associado ao vértice
        return self.itens.get(vertice, f"V{vertice}")

    def show_matriz_paginada(self, cols_por_pagina=20):
        # Exibe a matriz de adjacência em formato de paginas

        if self.n == 0:
            print("\nO grafo está vazio.")
            return

        LARGURA_CELULA = 5
        LARGURA_ROTULO_LINHA = 25

        num_paginas = math.ceil(self.n / cols_por_pagina)

        for pagina_atual in range(num_paginas):
            inicio_col = pagina_atual * cols_por_pagina
            fim_col = min(inicio_col + cols_por_pagina, self.n)

            print("\n" + "=" * 80)
            print(f" Matriz de adjacência - página  {pagina_atual + 1} de {num_paginas}")
            print(f" (Exibindo colunas de {inicio_col} a {fim_col - 1})")
            print("=" * 80)

            # Imprime os números das colunas no topo
            print(f"{'':<{LARGURA_ROTULO_LINHA}}", end="")
            for j in range(inicio_col, fim_col):
                # Centraliza o número da coluna no espaço da célula
                print(f"{str(j):^{LARGURA_CELULA}}", end="")
            print() 
            
            linha_separadora = "-" * (LARGURA_ROTULO_LINHA + (fim_col - inicio_col) * LARGURA_CELULA)
            print(linha_separadora)

            # Imprime as Linhas da Matriz
            for i in range(self.n):
                rotulo_completo = f"{i}: {self.get_nome_item(i)}"
                if len(rotulo_completo) > LARGURA_ROTULO_LINHA - 1:
                    rotulo = rotulo_completo[:LARGURA_ROTULO_LINHA - 4] + "..."
                else:
                    rotulo = rotulo_completo
                
                # Imprime o rótulo da linha, alinhado à esquerda
                print(f"{rotulo:<{LARGURA_ROTULO_LINHA}}", end="")

                # Imprime os valores das células daquela linha para a página atual
                for j in range(inicio_col, fim_col):
                    valor = int(self.adj[i][j])
                    # Centraliza o valor da célula no espaço definido
                    print(f"{str(valor):^{LARGURA_CELULA}}", end="")
                print()

            print(linha_separadora)

            # --- Controle de Navegação ---
            if pagina_atual < num_paginas - 1:
                try:
                    # Condicional para continuar impressao ou parar
                    escolha = input("--> Pressione Enter para a próxima página ou digite 's' para sair: ").lower()
                    if escolha == 's':
                        print("Retornando ao menu...")
                        break
                except KeyboardInterrupt:
                    print("\nOperação cancelada. Retornando ao menu...")
                    break
            else:
                print("Fim da visualização da matriz.")
                input("--> Pressione Enter para voltar ao menu principal.")
    
    def mostrar_conteudo_arquivo(self, caminho_arquivo="Grafo.txt"):
        """Mostra o conteúdo do arquivo Grafo.txt de forma visualmente atraente"""
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                linhas = [linha.strip() for linha in f if linha.strip()]
            
            if len(linhas) < 3:
                print(" Arquivo inválido ou vazio.")
                return
            
            print("\n" + "="*70)
            print("         CONTEÚDO DO ARQUIVO GRAFO.TXT")
            print("="*70)
            
            # 1. TIPO DO GRAFO
            tipo_grafo = int(linhas[0])
            tipos_desc = {
                0: "Não orientado sem peso",
                1: "Não orientado com peso no vértice", 
                2: "Não orientado com peso na aresta",
                3: "Não orientado com peso nos vértices e arestas",
                4: "Orientado sem peso",
                5: "Orientado com peso no vértice",
                6: "Orientado com peso na aresta", 
                7: "Orientado com peso nos vértices e arestas"
            }
            
            print(f"\n  TIPO DO GRAFO:")
            print(f"   Código: {tipo_grafo}")
            print(f"   Descrição: {tipos_desc.get(tipo_grafo, 'Tipo desconhecido')}")
            
            # 2. NÚMERO DE VÉRTICES
            num_vertices = int(linhas[1])
            print(f"\n ESTATÍSTICAS:")
            print(f"   Total de vértices: {num_vertices}")
            
            # 3. VÉRTICES NOMEADOS
            linha_atual = 2
            vertices_nomeados = {}
            
            while linha_atual < len(linhas) and '"' in linhas[linha_atual]:
                linha = linhas[linha_atual]
                partes = linha.split('"')
                
                if len(partes) >= 2:
                    numero_parte = partes[0].strip()
                    if numero_parte.isdigit():
                        vertice = int(numero_parte)
                        nome = partes[1].strip()
                        vertices_nomeados[vertice] = nome
                
                linha_atual += 1
            
            print(f"   Vértices nomeados: {len(vertices_nomeados)}")
            
            # 4. NÚMERO DE ARESTAS  
            num_arestas_arquivo = None
            if linha_atual < len(linhas):
                try:
                    possivel_num_arestas = int(linhas[linha_atual])
                    # Verifica se a próxima linha contém uma aresta
                    if linha_atual + 1 < len(linhas):
                        proxima_linha = linhas[linha_atual + 1].split()
                        if len(proxima_linha) >= 2 and proxima_linha[0].isdigit() and proxima_linha[1].isdigit():
                            num_arestas_arquivo = possivel_num_arestas
                            linha_atual += 1
                except ValueError:
                    pass
            
            if num_arestas_arquivo:
                print(f"   Entradas de arestas no arquivo: {num_arestas_arquivo}")
                print(f"   Arestas únicas estimadas: {num_arestas_arquivo // 2}")
            
            
            # 6. ARESTAS (CONEXÕES)
            arestas_brutas = []
            while linha_atual < len(linhas):
                linha = linhas[linha_atual]
                partes = linha.split()
                
                if len(partes) >= 2 and partes[0].isdigit() and partes[1].isdigit():
                    v1 = int(partes[0])
                    v2 = int(partes[1])
                    peso = partes[2] if len(partes) >= 3 else "1.0"
                    arestas_brutas.append((v1, v2, peso))
                
                linha_atual += 1
            
            # Remove duplicatas
            arestas_unicas = []
            arestas_vistas = set()
            
            for v1, v2, peso in arestas_brutas:
                # (a,b) é igual a (b,a)
                aresta = tuple(sorted([v1, v2]))
                if aresta not in arestas_vistas:
                    arestas_vistas.add(aresta)
                    arestas_unicas.append((v1, v2, peso))
            
            print(f"\n CONEXÕES:")
            if arestas_unicas:
                print("   Formato: Vértice1 ↔ Vértice2")
                print("   " + "-" * 50)
                
                for idx, (v1, v2, peso) in enumerate(arestas_unicas[:100]):
                    nome1 = vertices_nomeados.get(v1, f"V{v1}")
                    nome2 = vertices_nomeados.get(v2, f"V{v2}")
                    
                    # Trunca nomes longos
                    nome1 = nome1[:20] + "..." if len(nome1) > 20 else nome1
                    nome2 = nome2[:20] + "..." if len(nome2) > 20 else nome2
                    
                    print(f"   {v1:3d} ({nome1}) ↔ {v2:3d} ({nome2})")
                
            else:
                print("   Nenhuma conexão encontrada no arquivo.")
            
            # 7. RESUMO FINAL
            print(f"\n RESUMO:")
            print(f"   • Tipo: {tipos_desc.get(tipo_grafo, 'Desconhecido')}")
            print(f"   • Vértices totais: {num_vertices}")
            print(f"   • Vértices nomeados: {len(vertices_nomeados)}")
            print(f"   • Conexões únicas: {len(arestas_unicas)}")
            print(f"   • Tamanho do arquivo: {len(linhas)} linhas")
            
            print("="*70)
            
        except FileNotFoundError:
            print(f" Arquivo '{caminho_arquivo}' não encontrado.")
        except Exception as e:
            print(f" Erro ao ler arquivo: {e}")

    def mostrar_conexoes_detalhadas(self, caminho_arquivo="Grafo.txt", limite=20):
        """Mostra conexões do arquivo de forma mais detalhada"""
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                linhas = [linha.strip() for linha in f if linha.strip()]
            
            print("\n" + "="*80)
            print("            CONEXÕES DETALHADAS DO ARQUIVO")
            print("="*80)
            
            # Carrega vértices nomeados
            vertices_nomeados = {}
            linha_atual = 2
            
            while linha_atual < len(linhas) and '"' in linhas[linha_atual]:
                linha = linhas[linha_atual]
                partes = linha.split('"')
                
                if len(partes) >= 2:
                    numero_parte = partes[0].strip()
                    if numero_parte.isdigit():
                        vertice = int(numero_parte)
                        nome = partes[1].strip()
                        vertices_nomeados[vertice] = nome
                
                linha_atual += 1
            
            # Pula linha do número de arestas se existir
            if linha_atual < len(linhas):
                try:
                    int(linhas[linha_atual])
                    linha_atual += 1
                except ValueError:
                    pass
            
            # Carrega e organiza conexões
            conexoes_por_vertice = {}
            
            while linha_atual < len(linhas):
                linha = linhas[linha_atual]
                partes = linha.split()
                
                if len(partes) >= 2 and partes[0].isdigit() and partes[1].isdigit():
                    v1 = int(partes[0])
                    v2 = int(partes[1])
                    
                    if v1 not in conexoes_por_vertice:
                        conexoes_por_vertice[v1] = []
                    conexoes_por_vertice[v1].append(v2)
                
                linha_atual += 1
            
            # Mostra conexões organizadas
            vertices_mostrados = 0
            for vertice in sorted(conexoes_por_vertice.keys()):
                if vertices_mostrados >= limite:
                    print(f"\n... (mais {len(conexoes_por_vertice) - limite} vértices com conexões)")
                    break
                
                nome_origem = vertices_nomeados.get(vertice, f"Vértice {vertice}")
                conexoes = sorted(set(conexoes_por_vertice[vertice]))  # Remove duplicatas
                
                print(f"\n {vertice:3d}: {nome_origem}")
                print(f"    Conectado a {len(conexoes)} vértice(s):")
                
                for idx, destino in enumerate(conexoes[:10]):  # Máximo 10 conexões por vértice
                    nome_destino = vertices_nomeados.get(destino, f"V{destino}")
                    print(f"      → {destino:3d}: {nome_destino}")
                
                if len(conexoes) > 10:
                    print(f"      → ... (mais {len(conexoes) - 10} conexões)")
                
                vertices_mostrados += 1
            
            total_conexoes = sum(len(set(conexoes)) for conexoes in conexoes_por_vertice.values())
            print(f"\n Total de conexões no arquivo: {total_conexoes}")
            print(f" Estimativa de arestas únicas: {total_conexoes // 2}")
            
        except FileNotFoundError:
            print(f" Arquivo '{caminho_arquivo}' não encontrado.")
        except Exception as e:
            print(f" Erro ao processar arquivo: {e}")


    def conexidade(self):
        """
        Verifica se o grafo é conexo usando Busca em Profundidade (DFS).
        Esta versão é mais robusta e corrige o bug do vértice isolado.
        Retorna 0 se for conexo, 1 se for desconexo.
        """
        # Um grafo com 0 ou 1 vértice é, por definição, conexo.
        if self.n == 0: # Grafo com 0 vértices é desconexo
            return 1
        if self.n == 1: # Grafo com 1 vértice é conexo
            return 0

        visitado = [False] * self.n

        def dfs(v):
            visitado[v] = True
            for w in range(self.n):
                if self.adj[v][w] > 0 and not visitado[w]:
                    dfs(w)

        # Inicia a busca a partir do primeiro vértice.
        dfs(0)

        # se todos os vértices foram visitados após uma única busca a partir de um ponto.
        if all(visitado):
            return 0  # Conexo
        else:

            return 1  # Desconexo
