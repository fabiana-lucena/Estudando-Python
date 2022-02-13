import forca
import adivinhacao
import forca_versao2

def escolhe_jogo():
    print("**********************************")
    print("********ESCOLHA O SEU JOGO********")
    print("**********************************")

    print("(1) Forca (2) Adivinhação (3) Forca Versão 2")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        print ("Jogando Forca Versão 2")
        forca_versao2.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()





