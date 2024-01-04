# Importando a biblioteca para limpar a tela do console
import os

# Definindo o tabuleiro
tabuleiro = [' ' for _ in range(9)]


# Função para exibir o tabuleiro
def exibir_tabuleiro():
    for i in range(0, 9, 3):
        print(f'{tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]}')
        if i < 6:
            print('--+---+--')


# Função para a jogada do jogador
def jogada_jogador(posicao):
    if tabuleiro[posicao] == ' ':
        tabuleiro[posicao] = 'X'
    else:
        print('Posição inválida. Tente novamente.')


# Função para a jogada do computador (implementação simples)
def jogada_computador():
    # Lógica simples: o computador escolhe a primeira posição vazia
    for i in range(9):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            break


# Função para verificar vitória
def verificar_vitoria(simbolo):
    # Lógica para verificar vitória em linhas, colunas e diagonais
    # Retornar True se houver vitória, False caso contrário
    pass  # Você precisará implementar a lógica de verificação de vitória aqui


# Loop principal do jogo
while True:
    exibir_tabuleiro()
    posicao = int(input('Escolha uma posição (0-8): '))
    jogada_jogador(posicao)
    # Verificar vitória do jogador
    # Verificar empate
    jogada_computador()
    # Verificar vitória do computador
    # Verificar empate
