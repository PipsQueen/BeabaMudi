import random

def titulo():
    arquivo = open("TextoGerado.txt", "r", encoding = "utf-8")

    palavras = []

    for word in arquivo:
        words = word.split()
        for x in range(len(words)):
            if len(words[x]) > 4:
                palavras.append(words[x])
            
    qualPalavra  = random.randint(0, len(palavras) - 1)
    
    arquivo.close
    palavra = palavras[qualPalavra].title()
    arquivo.open("TituloGerado.txt","w", encoding = "utf-8")
    arquivo.write(palavra)
    arquivo.close

