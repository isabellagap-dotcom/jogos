import random
import time
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=================================================================\n")
    print('======================== Jogo da Velha ==========================\n')
    print("=================================================================\n")
    
    tabuleiro = criar_tabuleiro()
    jogador_humano = escolher_simbolo()
    jogar(tabuleiro, jogador_humano)

def escolher_simbolo():
    """Permite ao jogador escolher X ou O"""
    while True:
        simbolo = input("Escolha seu símbolo (X ou O): ").upper()
        if simbolo in ['X', 'O']:
            return simbolo
        print("Símbolo inválido! Escolha X ou O.")

def criar_tabuleiro():
    """Cria um tabuleiro vazio 3x3"""
    return [["__", "__", "__"],
            ["__", "__", "__"],
            ["__", "__", "__"]]

def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro atual"""
    print("\nTabuleiro atual:")
    for i, linha in enumerate(tabuleiro):
        linha_formatada = [f"{celula:<2}" for celula in linha]
        print(f"{i}    {' | '.join(linha_formatada)}")
    print(     "\n      0   1   2  (colunas)\n")

def jogar(tabuleiro, jogador_humano):
    """Loop principal do jogo"""
    jogadas = 0
    jogador_atual = 'X'  # X sempre começa
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=================================================================\n")
        print('======================== Jogo da Velha ==========================\n')
        print("=================================================================\n")
        
        mostrar_tabuleiro(tabuleiro)
        
        if jogador_atual == jogador_humano:
            # Vez do jogador humano
            print(f"Sua vez (Você é {jogador_humano})")
            linha, coluna = obter_jogada_humana(tabuleiro)
        else:
            # Vez do computador
            print(f"Vez do computador ({'O' if jogador_humano == 'X' else 'X'})")
            linha, coluna = obter_jogada_computador(tabuleiro)
            print(f"Computador escolheu: Linha {linha}, Coluna {coluna}")
            time.sleep(2)
        
        # Faz a jogada
        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1
        
        # Verifica fim de jogo
        resultado = verificar_vitoria(tabuleiro, jogador_atual, jogadas)
        if resultado != "continuar":
            mostrar_tabuleiro(tabuleiro)
            print(resultado)
            break
        
        # Alterna jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

def obter_jogada_humana(tabuleiro):
    """Obtém uma jogada válida do jogador humano"""
    while True:
        try:
            linha = int(input("Escolha a linha (0, 1, 2): "))
            coluna = int(input("Escolha a coluna (0, 1, 2): "))
            
            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida! Escolha linhas e colunas entre 0 e 2.")
                continue
                
            if tabuleiro[linha][coluna] != "__":
                print("Posição já ocupada! Escolha outra.")
                continue
                
            return linha, coluna
            
        except ValueError:
            print("Entrada inválida! Por favor, insira números inteiros.")

def obter_jogada_computador(tabuleiro):
    """Gera uma jogada aleatória para o computador"""
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == "__":
            return linha, coluna

def verificar_vitoria(tabuleiro, jogador_atual, jogadas):
    """Verifica se há um vencedor ou empate"""
    simbolo = jogador_atual
    vencedor = False
    
    # Verifica linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo:
            vencedor = True
    
    # Verifica colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo:
            vencedor = True
    
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo:
        vencedor = True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo:
        vencedor = True
    
    # Verifica empate
    if jogadas == 9:
        return "🤝 Empate! O tabuleiro está cheio."
    if vencedor:
        return f"🎉 Jogador {simbolo} venceu!"
    
    return "continuar"

if __name__ == "__main__":
    main()
