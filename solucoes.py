import string
def sao_anagramas(string1, string2):

  pass


def cifra_de_cesar(texto,deslocamento):
    # Caso o deslocamento seja maior que a quantidade de letras no alfabeto, tira o "excedente"
    if(deslocamento > 25):
        deslocamento = deslocamento % 25
    # Transformamos o texto em um array com as letras
    lettersList = list(texto)
    # Aqui é o nosso array de saída
    lettersOut = []
    for letter in lettersList:
        # Como vamos usar o código asc da letra várias vezes, adicionamos ele em uma variável
        letterAscCode = int(ord(letter))
        # Verificamos se a letra em questão esta dentro do universo de letras maíusculas da tabela asc
        if(letterAscCode >= 65 and letterAscCode <= 90):
            # Caso o deslocamento vá para fora da lista de letras maíusculas, esse if se encarrega de corrigir o deslocamento final
            if((letterAscCode + deslocamento) > 90):
                lettersOut.append(chr(letterAscCode + deslocamento - 26))
                continue
            # Caso tudo esteja correto, apenas retornamos a letra deslocada
            lettersOut.append(chr(letterAscCode + deslocamento))
            continue
        # Fazemos exatamente a mesma coisa, mas agora para letras minúsculas
        if(letterAscCode >= 97 and letterAscCode <= 122):
            if((letterAscCode + deslocamento) > 122):
                lettersOut.append(chr(letterAscCode + deslocamento - 26))
                continue
            lettersOut.append(chr(letterAscCode + deslocamento))
            continue
        # Aqui vai capturar, por exemplo, um espaço, um parenteses, algo que não seja uma letra
        lettersOut.append(letter)
    # Aqui juntamos tudo em uma string e retornamos ela
    return ''.join(lettersOut)


def encontrar_maior_palavra(frase):
    caracteres_indesejados = string.punctuation + string.digits

    tabela_traducao = str.maketrans(caracteres_indesejados, ' ' * len(caracteres_indesejados))
    frase_sem_pontuacao = frase.translate(tabela_traducao)

    palavras = frase_sem_pontuacao.split()
    
    if not palavras:
        return "String vazias não são aceitas, por favor insira uma palavra!"
    
    maior_palavra = ""
    
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
            
    return maior_palavra

frase_digitada = input("Digite uma frase: ")

resultado = encontrar_maior_palavra(frase_digitada)

print(f"A maior palavra é: {resultado}")




pass


