import random

def jogar():
  imprime_mensagem_abertura()
  palavras_e_dicas = le_arquivo()
  numero_sorteado = sortear_numero(palavras_e_dicas)
  palavra_secreta = carrega_palavra_secreta(palavras_e_dicas, numero_sorteado)
  dica = carrega_dica(palavras_e_dicas, numero_sorteado)
  letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
  enforcado = False
  vencedor = False
  tentativas = 8
  desenha_forca(tentativas)
  while enforcado == False and vencedor == False:
      print("A dica é:", dica)
      print(letras_acertadas)
      letra_selecionada = escolher_letra()
      if letra_selecionada in palavra_secreta:
        print("Você acertou")
        letras_acertadas = colocar_letras_acertadas(letra_selecionada, letras_acertadas, palavra_secreta)
      else:
        tentativas -= 1
    enforcado = perdeu(tentativas, palavra_secreta)
    vencedor = ganhou(letras_acertadas)
  print("Fim do jogo")

def imprime_mensagem_abertura():
  print("*********************************")
  print("***Bem vindo ao jogo da Forca!***")
  print("*********************************")

def le_arquivo():
  arquivo = open("palavras.txt", "r")
  palavras_e_dicas = []
  for linha in arquivo:
    palavras_e_dicas.append(linha)
  arquivo.close()
  return palavras_e_dicas

def sortear_numero(palavras_e_dicas):
  numero_sorteado = random.randrange(0,len(palavras_e_dicas))
  return numero_sorteado

def carrega_palavra_secreta(palavras_e_dicas, numero_sorteado):
  palavra_e_dica = palavras_e_dicas[numero_sorteado]
  palavra_e_dica = palavra_e_dica.split(",")
  indice = 0
  for elemento in palavra_e_dica:
    if indice == 0:
      elemento = elemento.strip()
      palavra = elemento
    indice += 1
  return palavra.upper()

def carrega_dica(palavras_e_dicas, numero_sorteado):
  palavra_e_dica = palavras_e_dicas[numero_sorteado]
  palavra_e_dica = palavra_e_dica.split(",") 
  indice = 0
  for elemento in palavra_e_dica:
    if indice == 1:
      elemento = elemento.strip()
      dica = elemento
    indice += 1
  return dica.upper()

def inicializa_letras_acertadas(palavra):
  return ["_" for letra in palavra]

def escolher_letra():
  letra = input("Digite uma letra: ")
  letra_sem_espaco = letra.strip()
  return letra_sem_espaco.upper()

def colocar_letras_acertadas(letra_selecionada, letras_acertadas, palavra_secreta):
  letras_acertadas[palavra_secreta.find(letra_selecionada)] = letra_selecionada
  return letras_acertadas

def ganhou(letras_acertadas):
  if "_" not in letras_acertadas:
    limpar_tela()
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.   /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    return True
  else:
    return False

def perdeu(tentativas, palavra_secreta):
  limpar_tela()
  desenha_forca(tentativas)
  if tentativas == 0:
    limpar_tela()
    print("Você perdeu")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    return True
  else:
    return False

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 8):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif(tentativas == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    elif(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    elif(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    elif(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    elif(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    elif (tentativas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def limpar_tela():
  print("\n"*30)

if __name__ == "__main__":
  jogar()