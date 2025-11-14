def menu():
    print("Bem vindo ao protein-calc-gen")
    print("Escolha uma opção")
    print("1 - Calcular Proteina")
    print("2 - Calcular IMC")
    print("3 - Calular qtd de Agua")
    print("Qualquer outro numero - sair")
    
    # -- função para saber o objetivo do usuario
def menu_objetivo():
    print("Qual sua meta?")
    print("1 - Perder peso")
    print("2 - Manter peso")
    print("3 - Ganhar peso")
    
def calc_proteinas(peso, objetivo):
    if objetivo == 1:
        return peso * 2
    elif objetivo == 2:
        return peso * 1.6
    elif objetivo == 3:
        return peso * 1.8
    else:
        return None
    #o comando None, é para nao fazer nada
    
def calc_imc(peso, altura):
    return peso / (altura ** 2)

def imc(valor_imc):
    if valor_imc < 18.5:
        return "abaixo do peso"
    elif valor_imc < 24.9:
        return "peso normal"
    elif valor_imc < 29.9:
        return "sobre peso"
    else:
        return "obsesidade"
    
def calc_agua(peso):
   return (peso * 35) / 1000
    