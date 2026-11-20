num1 = float(input(("Escreva o primeiro número: ")))
num2 = float(input(("Escreva o segundo número: ")))
operacao = input("Escreva a operação (+, -, *, /): ")
if operacao == "+":
        print(f"O resultado é {num1 + num2:.2f}") 

elif operacao == "-":
        print(f"O resultado é {num1 - num2:.2f}")
       
elif operacao == "*":
        print(f"O resultado é {num1 * num2:.2f}")
      
elif operacao == "/":
        print(f"O resultado é {num1 / num2:.2f}")