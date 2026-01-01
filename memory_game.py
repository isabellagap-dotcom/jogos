import os
import random
import time

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo()
    jogo()

def jogo():
    lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    cartas = lista * 2
    random.shuffle(cartas)
    
    # Estado das cartas: True = encontrada/revelada, False = escondida
    cartas_encontradas = [False] * 16
    
    # Mostra todas as cartas para memorização
    print("\nMemorize as cartas (5 segundos):")
    show_cards(cartas)
    time.sleep(5)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo()
    
    inicio = time.time()
    pares_encontrados = 0
    tentativas = 0
    
    # Tabuleiro atual (começa tudo escondido)
    tabuleiro = ['🟫'] * 16
    
    while pares_encontrados < 8:
        # Mostra o tabuleiro atual
        print(f"\nPares encontrados: {pares_encontrados}/8 | Tentativas: {tentativas}")
        print("=" * 40)
        show_cards(tabuleiro)
        print("=" * 40)
        
        try:
            # Primeira carta
            while True:
                primeira = int(input("\nEscolha a posição da primeira carta (1-16): ")) - 1
                if primeira < 0 or primeira >= 16:
                    print("Posição inválida. Escolha entre 1 e 16.")
                elif cartas_encontradas[primeira]:
                    print("Esta carta já foi encontrada! Escolha outra.")
                else:
                    break
            
            # Revela primeira carta temporariamente
            temp_tabuleiro = tabuleiro.copy()
            temp_tabuleiro[primeira] = cartas[primeira]
            
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo()
            print(f"\nPares encontrados: {pares_encontrados}/8 | Tentativas: {tentativas}")
            print("=" * 40)
            show_cards(temp_tabuleiro)
            print("=" * 40)
            
            # Segunda carta
            while True:
                segunda = int(input("Escolha a posição da segunda carta (1-16): ")) - 1
                if segunda < 0 or segunda >= 16:
                    print("Posição inválida. Escolha entre 1 e 16.")
                elif segunda == primeira:
                    print("Você já escolheu esta carta. Escolha outra.")
                elif cartas_encontradas[segunda]:
                    print("Esta carta já foi encontrada! Escolha outra.")
                else:
                    break
            
            tentativas += 1
            
            # Revela segunda carta também
            temp_tabuleiro[segunda] = cartas[segunda]
            
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo()
            print(f"\nPares encontrados: {pares_encontrados}/8 | Tentativas: {tentativas}")
            print("=" * 40)
            show_cards(temp_tabuleiro)
            print("=" * 40)
            
            # Verifica se é um par
            if cartas[primeira] == cartas[segunda]:
                print("\n✅ PAR ENCONTRADO!")
                # Marca cartas como encontradas permanentemente
                cartas_encontradas[primeira] = True
                cartas_encontradas[segunda] = True
                # Atualiza tabuleiro permanente
                tabuleiro[primeira] = cartas[primeira]
                tabuleiro[segunda] = cartas[segunda]
                pares_encontrados += 1
                input("Pressione Enter para continuar...")
            else:
                print(f"\n❌ Não é um par: {cartas[primeira]} ≠ {cartas[segunda]}")
                print("As cartas serão escondidas novamente...")
                time.sleep(2)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo()
            
        except ValueError:
            print("Entrada inválida. Por favor, insira números entre 1 e 16.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo()
    
    # Fim do jogo
    fim = time.time()
    duracao = fim - inicio
    
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo()
    
    # Mostra tabuleiro final com todas as cartas
    print("🎉 PARABÉNS! VOCÊ ENCONTROU TODOS OS PARES! 🎉")
    print(f"\nTempo total: {duracao:.2f} segundos")
    print(f"Tentativas: {tentativas}")
    print("\nTabuleiro final:")
    print("=" * 40)
    show_cards(cartas)  # Mostra todas as cartas
    print("=" * 40)
    
    # Pergunta se quer jogar novamente
    while True:
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
        if jogar_novamente in ['s', 'sim']:
            main()
            break
        elif jogar_novamente in ['n', 'nao', 'não']:
            print("\nObrigado por jogar! Até a próxima!")
            break
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")

def show_cards(cartas):
    """
    Exibe as cartas em formato de grade 4x4
    """
    for i in range(4):
        for j in range(4):
            print(f'{cartas[i*4 + j]:^2}', end=' ')
        print()

def titulo():
    print("=================================================================")
    print('======================= Jogo da Memória =========================')
    print("=================================================================\n")

if __name__ == "__main__":
    main()