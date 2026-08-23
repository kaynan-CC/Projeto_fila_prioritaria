from time import sleep

# Cores
verde = '\033[1;32m'
vermelho = '\033[1;31m'
vermelho_suave = '\033[38;5;203m'
amarelo = '\033[1;33m'
ciano = '\033[1;36m'
magenta = '\033[1;35m'
fim = '\033[0m'

while True:
    print(f"{magenta}--------------------BEM-VINDO AO FILA ZERO--------------------{fim}")
    sleep(1)
    print(f"{magenta}Processando...{fim}")
    sleep(3)
    
    while True:
        print(f"{magenta}----Deseja cadastrar um paciente?----{fim}")
        print("1 - Sim")
        print("2 - Não")
        continuar = input("Digite o número para ação: ").strip()
        if continuar == "1" or continuar == "2":
            break
        print(f"{vermelho}Opção inválida! Digite apenas 1 ou 2.{fim}\n")
        
    sleep(1)
    
    if continuar == "2":
        print(f"{magenta}Saindo...{fim}")
        break
        
    elif continuar == "1":
        print(f"{magenta}----CADASTRO DO PACIENTE----{fim}")
        sleep(1)
        Nome = input("Nome: ").upper().strip()
        sleep(1)
        
        while True:
            idade_input = input("Idade: ").strip()
            if idade_input.isdigit():
                Idade = int(idade_input)
                if 0 <= Idade <= 120:
                    break
            print(f"{vermelho}Idade inválida! Digite apenas números inteiros (Ex: 25).{fim}")
            
        sleep(2)