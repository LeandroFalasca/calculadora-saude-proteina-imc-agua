from funcoes import *

while True:
    menu()
    opcao = int(input("Escolha a Opção"))
    
    if opcao == 1:
        menu_objetivo()
        objetivo = int(input("Qual seu Objetivo ?"))
        peso = float(input("qual seu peso(kg)?"))
        
        resultado_proteinas = calc_proteinas(peso, objetivo)
        print("Você precisa de", round(resultado_proteinas, 2), "g de proteína por dia.")
        # o comando round arredonda um numero. ex: 3,1415 - round(numero,2) = 3,14
    elif opcao == 2:
        peso = float(input("qual seu peso(kg)?"))
        altura = float(input("qual sua altura em metros"))
        resultado_imc = calc_imc(peso, altura)
        print(f"Seu IMC é {round(resultado_imc, 2)} — você está com {imc(resultado_imc)}.")
    elif opcao == 3:
        peso = float(input("Qual seu peso (kg)? "))
        resultado_agua = calc_agua(peso)
        print(f"Você deve ingerir aproximadamente {round(resultado_agua, 2)} ml de água por dia.")

    else:
        print("tchau")
        break
        
        
        
        