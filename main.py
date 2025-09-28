'''' 
Projeto Teoria dos Grafos - Amplify

Nomes e RA:
Bernardo de Souza Pereira - 10312871
Matheus Queiroz Gregorin - 10418143
Pedro Henrique Cagnoni Guimaraes - 10417477

O projeto utiliza matriz de adjacência para representar grafos.
'''

from grafoMatriz import TGrafoND


def mostrar_menu():
    """Exibe o menu de opções"""
    print("\n" + "=" * 50)
    print("       SISTEMA DE GRAFOS - MENU")
    print("=" * 50)
    print("a) Ler dados do arquivo grafo.txt")
    print("b) Gravar dados no arquivo grafo.txt")
    print("c) Inserir vértice")
    print("d) Inserir aresta")
    print("e) Remover vértice")
    print("f) Remover aresta")
    print("g) Mostrar conteúdo do arquivo")
    print("h) Mostrar grafo")
    print("i) Apresentar conexidade do grafo")
    print("j) Encerrar a aplicação")
    print("=" * 50)

def main():
    """Função principal com menu interativo"""
    grafo = TGrafoND()
    
    print(" SISTEMA DE GRAFOS MUSICAIS")
    print("Projeto Teoria dos Grafos - Amplify")
    
    while True:
        mostrar_menu()
        
        try:
            opcao = input("\nEscolha uma opção (a-j): ").strip().lower()
            
            if opcao == 'a':
                # Ler dados do arquivo grafo.txt
                try:
                    grafo.arquivo_para_matriz_adjacencia("Grafo.txt")
                    print(" Arquivo lido com sucesso!")
                except FileNotFoundError:
                    print(" Erro: Arquivo 'Grafo.txt' não encontrado.")
                except Exception as e:
                    print(f" Erro ao ler arquivo: {e}")
                    
            elif opcao == 'b':
                # Gravar dados no arquivo grafo.txt
                try:
                    grafo.gravar_grafo_arquivo("Grafo.txt")
                except Exception as e:
                    print(f" Erro ao gravar arquivo: {e}")
                
            elif opcao == 'c':
                # Inserir vértice
                try:
                    nome_vertice = input("Digite uma música/artista/gênero para adicionar um novo vértice: ").strip()
                    if nome_vertice:
                        novo_vertice = grafo.insereV(nome_vertice)
                        print(f" Vértice {novo_vertice} '{nome_vertice}' inserido com sucesso!")
                    else:
                        print(" Nome do vértice não pode estar vazio.")
                except Exception as e:
                    print(f" Erro ao inserir vértice: {e}")
        

            elif opcao == 'd':
                # Inserir aresta
                try:
                    v1 = int(input("Digite o primeiro vértice: "))
                    v2 = int(input("Digite o segundo vértice: "))
                    
                    grafo.insereA(v1, v2)
                    nome1 = grafo.get_nome_item(v1)
                    nome2 = grafo.get_nome_item(v2)
                    print(f" Aresta inserida: {v1}({nome1}) <-> {v2}({nome2})")
                    
                except ValueError:
                    print(" Erro: Digite números válidos.")
                except IndexError:
                    print(" Erro: Vértice inválido.")
                except Exception as e:
                    print(f" Erro ao inserir aresta: {e}")
                    
            elif opcao == 'e':
                # Remover vértice
                try:
                    vertice = int(input("Digite o vértice a ser removido: "))
                    nome = grafo.get_nome_item(vertice)
                    grafo.removeV(vertice)
                    print(f" Vértice {vertice} '{nome}' removido com sucesso!")
                    
                except ValueError:
                    print(" Erro: Digite um número válido.")
                except IndexError:
                    print(" Erro: Vértice inválido.")
                except Exception as e:
                    print(f" Erro ao remover vértice: {e}")
                    
            elif opcao == 'f':
                # Remover aresta
                try:
                    v1 = int(input("Digite o primeiro vértice: "))
                    v2 = int(input("Digite o segundo vértice: "))
                    
                    nome1 = grafo.get_nome_item(v1)
                    nome2 = grafo.get_nome_item(v2)
                    
                    grafo.removeA(v1, v2)
                    print(f" Aresta removida: {v1}({nome1}) <-> {v2}({nome2})")
                    
                except ValueError:
                    print(" Erro: Digite números válidos.")
                except IndexError:
                    print(" Erro: Vértice inválido.")
                except Exception as e:
                    print(f" Erro ao remover aresta: {e}")
                    
            elif opcao == 'g':
                try:
                    print("\n OPÇÕES DE VISUALIZAÇÃO DO ARQUIVO:")
                    print("1. Visão geral do arquivo")
                    print("2. Conexões detalhadas")
                    
                    sub_opcao = input("Escolha (1-2): ").strip()
                    
                    if sub_opcao == '1':
                        grafo.mostrar_conteudo_arquivo("Grafo.txt")
                    elif sub_opcao == '2':
                        limite = input("Quantos vértices mostrar? (padrão 66): ").strip()
                        limite = int(limite) if limite.isdigit() else 20
                        grafo.mostrar_conexoes_detalhadas("Grafo.txt", limite)
                    else:
                        print(" Opção inválida.")
                        
                except Exception as e:
                    print(f" Erro ao mostrar conteúdo do arquivo: {e}")
                    
            elif opcao == 'h':
                # Printa a matriz no formato de paginas, para possibilitar uma melhor visualizacao
                grafo.show_matriz_paginada()
                    
            elif opcao == 'i':
                # Apresentar conexidade do grafo
                print(f"\n ANÁLISE DE CONEXIDADE:")
               
                conexidade = grafo.conexidade()
                
                if conexidade == 0:
                    print("O grafo é conexo")
                else:
                    print("O grafo é desconexo")
                    
            elif opcao == 'j':
                print("\n Encerrando aplicação...")
                print("Obrigado por usar o AmpliFy!")
                break
                
            else:
                print(" Opção inválida! Escolha uma letra de 'a' a 'j'.")
                
        except KeyboardInterrupt:
            print("\n\n Aplicação encerrada pelo usuário.")
            break
        except Exception as e:
            print(f" Erro inesperado: {e}")
        
        # Pausa para o usuário ver o resultado
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()



