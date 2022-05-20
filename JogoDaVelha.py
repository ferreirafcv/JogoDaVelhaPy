###########################################
# Projeto Final - Jogo da Velha em Python #
###########################################

# Cria o tabuleiro
tabuleiro = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

# Teste p/ verificar se o jogo continua ou termina
jogo_continua = True

# Vencedor do jogo
vencedor = None

# Jogador ativo na rodada (jogo começa com jogador "O")
jogador_ativo = "O"

# Função mostra o tabuleiro do jogo e o tabuleiro guia de posições
def mostra_tabuleiro():
    print("\n")
    print(tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2] + "     1 | 2 | 3")
    print(tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5] + "     4 | 5 | 6")
    print(tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8] + "     7 | 8 | 9")
    print("\n")

# Função realiza a jogada
def faz_jogada(jogador):
    print("É a vez do Jogador " + jogador + ".")
    posicao = input("Escolha uma posição (1 - 9): ")
  
    jogada_valida = False

    while not jogada_valida:    
        while posicao not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:            
            posicao = input("Escolha uma posição (1 - 9): ")
     
        posicao = int(posicao) - 1
    
        if tabuleiro[posicao] == " ":
            jogada_valida = True
        else:
            print("Posição indisponível! Tente novamente!")

    tabuleiro[posicao] = jogador
  
    mostra_tabuleiro()

# Função verifica se há vencedor
def verifica_vencedor():
    global vencedor
  
    # Verifica se há vencedor em alguma sequência (linha, coluna ou diagonal)
    vencedor_linha = verifica_linhas()
    vencedor_coluna = verifica_colunas()
    vencedor_diagonal = verifica_diagonais()
    
    if vencedor_linha:            
        vencedor = vencedor_linha
    elif vencedor_coluna:
        vencedor = vencedor_coluna
    elif vencedor_diagonal:
        vencedor = vencedor_diagonal
    else:
        vencedor = None

# Função verifica se há vencedor nas linhas
def verifica_linhas():
    global jogo_continua

    linha_1 = tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != " "
    linha_2 = tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != " "
    linha_3 = tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != " "
    
    if linha_1 or linha_2 or linha_3:
        jogo_continua = False        
    if linha_1:
        return tabuleiro[0] 
    elif linha_2:
        return tabuleiro[3] 
    elif linha_3:
        return tabuleiro[6] 
    else:
        return None

# Função verifica se há vencedor nas colunas
def verifica_colunas():
    global jogo_continua

    coluna_1 = tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != " "
    coluna_2 = tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != " "
    coluna_3 = tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != " "
    
    if coluna_1 or coluna_2 or coluna_3:
        jogo_continua = False
    if coluna_1:
        return tabuleiro[0] 
    elif coluna_2:
        return tabuleiro[1] 
    elif coluna_3:
        return tabuleiro[2]   
    else:
        return None

# Função verifica se há vencedor nas diagonais
def verifica_diagonais():
    global jogo_continua

    diagonal_1 = tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != " "
    diagonal_2 = tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != " "
    
    if diagonal_1 or diagonal_2:
        jogo_continua = False
    if diagonal_1:
        return tabuleiro[0] 
    elif diagonal_2:
        return tabuleiro[2]
    else:
        return None

# Função verifica se há empate
def verifica_empate():
    global jogo_continua
  
    if " " not in tabuleiro:
        jogo_continua = False
        return True
    else:
        return False

# Função alterna jogadores "O" e "X"
def alterna_jogador():
    global jogador_ativo

    if jogador_ativo == "O":
        jogador_ativo = "X"
    elif jogador_ativo == "X":
        jogador_ativo = "O"

# Início do jogo
mostra_tabuleiro()

while jogo_continua:
    faz_jogada(jogador_ativo)    
    verifica_vencedor()
    verifica_empate()    
    alterna_jogador()
  
if vencedor == "X" or vencedor == "O":
   print("******************")
   print("Jogador " + vencedor + " venceu!")
   print("******************")
elif vencedor == None:
   print("---------------")
   print("Ih, deu velha!")
   print("---------------")