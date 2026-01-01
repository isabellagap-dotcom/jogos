import os
import random

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=================================================================\n")
    print('======================== Jogo da Forca ==========================\n')
    print("=================================================================\n")
    jogo()


def boneco(tentativas):
    estagios = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           |
           |
           |
           |
           -
        """
    ]
    print(estagios[tentativas])

def jogo():
    lista = ['banana', 'abacaxi', 'laranja', 'morango', 'uva', 'melancia', 'kiwi', 'manga', 'pessego', 'caju']
    palavra_oculta = list(random.choice(lista))
    palavra = ['_'] * len(palavra_oculta)
    tentativas = 6
    tentativas_iniciais = tentativas  # Salva o número inicial de tentativas
    letras_tentadas = []
    
    while tentativas > 0 and palavra != palavra_oculta:
        boneco(tentativas)
        print('Palavra: ', ' '.join(palavra))
        print(f'Tentativas restantes: {tentativas}')
        print('Letras já tentadas: ', ' '.join(letras_tentadas))
        letra = input('Digite uma letra: ').lower()
        
        if letra in letras_tentadas:
            print('Você já tentou essa letra. Tente outra.')
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra_oculta:
            for i, char in enumerate(palavra_oculta):
                if char == letra:
                    palavra[i] = letra
            print('Boa! Você acertou uma letra.\n')
        else:
            tentativas -= 1
            print('Letra incorreta. Tente novamente.\n')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if palavra == palavra_oculta:
        print("\n=================================================================\n")
        print(f'Parabéns! Você venceu! A palavra era: {"".join(palavra_oculta)}')
        # Calcula a pontuação baseada nas tentativas RESTANTES
        score(tentativas)
    else:
        print("\n=================================================================\n")
        print(f'Você perdeu! A palavra era: {"".join(palavra_oculta)}')
    
    jogar_novamente()

def score(tentativas_restantes):
    # Calcula a pontuação: quanto mais tentativas restantes, maior a pontuação
    score = int((tentativas_restantes / 6) * 1000)  # Ajuste o multiplicador conforme desejado
    
    print(f'Sua pontuação: {score} pontos')
    
    try:
        with open('score.txt', 'r') as file:
            melhor_score = int(file.read())
        
        if score > melhor_score:
            with open('score.txt', 'w') as file:
                file.write(str(score))
                print(f'⭐ Novo recorde! Pontuação: {score} ⭐')
        else:
            print(f'Melhor pontuação: {melhor_score} pontos')
            
    except (FileNotFoundError, ValueError):
        # Se o arquivo não existir ou estiver vazio, cria com a pontuação atual
        with open('score.txt', 'w') as file:
            file.write(str(score))
            print(f'Primeira pontuação registrada: {score} pontos')

def jogar_novamente():
    print("\n=================================================================\n")
    escolha = input('Deseja jogar novamente? (s/n): ').lower()
    if escolha == 's':
        main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Obrigado por jogar! Até a próxima.')

if __name__ == '__main__':
    main()
