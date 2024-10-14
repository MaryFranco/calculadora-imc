#Rascunho calculadora IMC
#funcao para calculo do imc
#Saudacao, pedir peso, pedir altura

#Função realizar calculo imc
def calculo_imc (x, y):
    result = x / (y ** 2)
    return result

#Função de converter cm em metros
def converter_altura(y):
    if altura == int:
        result_altura = y/100
        return(result_altura)

#Entrada de valores
print("Bem vindo a calculadora de IMC") 
peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))
while altura != float:
    try:
       altura = float(input("Digite sua altura"))
       break
    finally:
        
imc = calculo_imc (peso, altura)

#Ponto condicional
if imc < 18:
    print("Seu imc é de ", imc, " e seu peso está abaixo do normal")

elif imc >= 18 or imc < 24.9:
    print("Seu imc é de ", imc, "e seu peso está dentro do normal")

elif imc >= 25 or imc <29.9:
    print("Seu imc é de ", imc, "e seu seu peso está acima do normal")

elif imc > 30:
    print("Seu imc é de ", imc, "e você está sofrendo de obesidade")

else:
    print("Dados invalidos")