import string
def sao_anagramas(string1, string2):

  pass


def cifra_de_cesar(texto,deslocamento):


  pass



def encontrar_maior_palavra(frase):

    tabela_traducao = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    frase_sem_pontuacao = frase.translate(tabela_traducao)

    palavras = frase_sem_pontuacao.split()
    
    if not palavras:
        return ""
    
    maior_palavra = ""
    
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
            
    return maior_palavra

frase_digitada = input("Digite uma frase: ")

resultado = encontrar_maior_palavra(frase_digitada)

print(f"A maior palavra é: {resultado}")




pass


