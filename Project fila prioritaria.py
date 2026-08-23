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
                
        while True:
            print(f"{magenta}----PACIENTE ESTÁ CONSCIENTE?----{fim}")
            print("1 - Sim")
            print("2 - Não")
            escolha0 = input("Digite um número: ").strip()
            if escolha0 == "1" or escolha0 == "2":
                break
            print(f"{vermelho}Opção inválida! Digite 1 para Sim ou 2 para Não.{fim}\n")
            
        sleep(1)
        
        if escolha0 == "2":
            print(f"{vermelho}Paciente: {Nome} | Idade: {Idade}\nPrioridade CRÍTICA \nAtendimento Imediato.{fim}")
            sleep(3)
            continue
            
        elif escolha0 == "1":
            sleep(2)
            
        while True:
            print(f"{magenta}--------------------Subtriagem--------------------{fim}")
            print("1 - Respiratória")
            print("2 - Dor")
            print("3 - Neurológica")
            print("4 - Preferencial")
            sintoma_principal = input("Selecione a categoria principal: ").strip()
            if sintoma_principal in ["1", "2", "3", "4"]:
                break
            print(f"{vermelho}Opção inválida! Escolha de 1 a 4.{fim}\n")
                        
        # ---------------- SUBTRIAGEM RESPIRATÓRIA ----------------
        if sintoma_principal == "1":
            sleep(2)
            while True:
                print(f"{magenta}----SELECIONE O ESTADO DO PACIENTE----{fim}")
                print('1 - Não consegue falar')
                print('2 - Respiração muito difícil')
                print('3 - Falta de ar moderada')
                print('4 - Desconforto leve')
                escolha = input('Digite o número do sintoma: ').strip()
                if escolha in ["1", "2", "3", "4"]:
                    break
                print(f"{vermelho}Opção inválida! Escolha de 1 a 4.{fim}\n")
                    
            sleep(3)
            if escolha == "1":
                print(f"{vermelho}Paciente: {Nome} | Idade: {Idade}\nPrioridade CRÍTICA \nAtendimento Imediato.{fim}")
            elif escolha == "2":
                print(f"{vermelho_suave}Paciente: {Nome} | Idade: {Idade}\nPrioridade MUITO ALTA \nAtendimento em até 10 minutos.{fim}")
            elif escolha == "3":
                print(f"{amarelo}Paciente: {Nome} | Idade: {Idade}\nPrioridade ALTA \nAtendimento em até 30 minutos.{fim}")
            elif escolha == "4":
                print(f"{verde}Paciente: {Nome} | Idade: {Idade}\nPrioridade BAIXA \nAtendimento em até 120 minutos.{fim}")

        # ---------------- SUBTRIAGEM DOR ----------------
        elif sintoma_principal == "2":
            sleep(3)
            while True:
                print(f"{magenta}----SELECIONE O NÍVEL DE DOR----{fim}")
                print("1 - Dor Intensa")
                print("2 - Dor forte persistente")
                print("3 - Dor moderada")
                print("4 - Dor leve")
                escolha = input("Digite o número do sintoma: ").strip()
                if escolha in ["1", "2", "3", "4"]:
                    break
                print(f"{vermelho}Opção inválida! Escolha de 1 a 4.{fim}\n")
                    
            sleep(1)
            if escolha == "1":
                print(f"{vermelho}Paciente: {Nome} | Idade: {Idade}\nPrioridade CRÍTICA \nAtendimento Imediato.{fim}")
            elif escolha == "2":
                print(f"{vermelho_suave}Paciente: {Nome} | Idade: {Idade}\nPrioridade MUITO ALTA \nAtendimento em até 10 minutos.{fim}")
            elif escolha == "3":
                print(f"{amarelo}Paciente: {Nome} | Idade: {Idade}\nPrioridade ALTA \nAtendimento em até 30 minutos.{fim}")
            elif escolha == "4":
                print(f"{verde}Paciente: {Nome} | Idade: {Idade}\nPrioridade BAIXA \nAtendimento em até 120 minutos.{fim}")
