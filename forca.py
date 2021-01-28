def jogar():
  imprime_mensagem_abertura()
  palavras_e_dicas = le_arquivo()
  numero_sorteado = sortear_numero(palavras_e_dicas)
  palavra_secreta = carrega_palavra_secreta(palavras_e_dicas, numero_sorteado)
  dica = carrega_dica(palavras_e_dicas, numero_sorteado)


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
  
if __name__ == "__main__":
  jogar()