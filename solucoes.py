def sao_anagramas(string1, string2):
    
    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()
    
    
    return sorted(s1) == sorted(s2)



while True:
    try:
        palavra1 = input("Digite a primeira palavra/frase (ou 'sair' para encerrar): ").strip()
        if palavra1.lower() == "sair":
            print("Programa encerrado.")
            break
        if not palavra1:  
            print("⚠️ Você não digitou nada, tente novamente.\n")
            continue

        palavra2 = input("Digite a segunda palavra/frase (ou 'sair' para encerrar): ").strip()
        if palavra2.lower() == "sair":
            print("Programa encerrado.")
            break
        if not palavra2:
            print("⚠️ Você não digitou nada, tente novamente.\n")
            continue

        if sao_anagramas(palavra1, palavra2):
            print(f"✅ SIM! '{palavra1}' é um anagrama de '{palavra2}'\n")
        else:
            print(f"❌ NÃO! '{palavra1}' não é um anagrama de '{palavra2}'\n")

    except KeyboardInterrupt:
        print("\n⛔ Programa interrompido pelo usuário.")
        break

    except Exception as e:
        print(f"⚠️ Ocorreu um erro inesperado: {e}\n")



def cifra_de_cesar(texto,deslocamento):


  pass



def valida_cpf(cpf_string):

  pass


