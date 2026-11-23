import time
import os
while True:
        print("----- Calculadora -----")
        num1 = float(input(("Escreva o primeiro número: ")))
        num2 = float(input(("Escreva o segundo número: ")))
        operacao = input("Escreva a operação (+, -, *, /): ")
        if operacao == "+":
                print(f"O resultado é {num1 + num2:.2f}") 
                time.sleep(3)
                os.system('cls')
        elif operacao == "-":
                print(f"O resultado é {num1 - num2:.2f}")
                time.sleep(3)
                os.system('cls')
        elif operacao == "*":
                print(f"O resultado é {num1 * num2:.2f}")
                time.sleep(3)
                os.system('cls')
        elif operacao == "/":
                print(f"O resultado é {num1 / num2:.2f}")
                time.sleep(3)
                os.system('cls')
        else:
                print("Insira uma operação válida! ")
                time.sleep(3)
                os.system('cls')