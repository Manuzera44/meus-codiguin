#Um sistema simples de cadastro feito por Adrian Holz, Emanuel Cardoso da Silva, e Gustavo Joaquim Fabiam da N2.
import re
pessoas = []
print("\nSeja Bem-vindo ao cadastro simples da Britânia! ")
def cadastrar_pessoa():
    print("\n===== Cadastro de Colaborador =====")
    while True:
        nome = input("\nDigite o nome do Colaborador: ")

        if nome.strip() == "":
            print("\nErro: Insira um nome válido. Tente novamente.\n")
        elif nome != nome.strip():
            print("\nErro: Não pode haver espaços no início ou no fim. Tente novamente.\n")
        else:
            break
    
    while True:
        sexo = input("\nQual é o sexo do Colaborador?\n1- Masculino\n2- Feminino\nEscolha uma opção: ")
        if sexo.strip() == "":
            print("\nErro: Insira algo. Tente novamente.\n")
        elif sexo != sexo.strip():
            print("\nErro: Não pode haver espaços no início ou no fim. Tente novamente.\n")
        elif int(sexo) == 1:
            sexo = "Masculino"
            break
        elif int(sexo) == 2:
            sexo = "Feminino"
            break
        else:
            print("\nErro: Insira um número entre 1 e 2. Tente novamente.\n")

    while True:
        cpf = input("\nDigite o CPF do Colaborador (apenas números ou com pontos e hífen): ")

        if validar_cpf(cpf):
            break
        else:
            print("\nErro: Isira um CPF válido. Tente novamente.\n")

    while True:
        idade = int(input("\nDigite a idade do Colaborador: "))
        if idade < 0:
            print("\nErro: Insira uma idade válida. Tente novamente.\n")
        elif idade < 18:
            print("\nErro: Para realizar o cadastro, é necessário possuir idade mínima de 18 anos.. Tente novamente.\n")
        else:
            break
 
    while True:
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        email = input("\nDigite o E-mail do Colaborador: ")

        if email.strip() == "":
            print("\nErro: Insira um E-mail válido. Tente novamente.\n")
        elif not re.match(email_regex, email):
            print("\nErro: Insira um email válido. Tente novamente.\n")
        else:
            break


    while True:
        cep = input("\nDigite o CEP do Colaborador: ").strip().replace("-", "")
        if not cep.isdigit():
            print("\nErro: Insira apenas números. Tente novamente.\n")
        elif len(cep) != 8:
            print("\nErro: Insira 8 dígitos. Tente novamente.\n")
        else:
            break

        
    pessoa = {
        "nome": nome,
        "sexo": sexo,
        "cpf": cpf,
        "idade": idade,
        "email": email,
        "cep": cep
    }
    pessoas.append(pessoa)
    if sexo == "Masculino":
        print(f"\nO {nome} foi cadastrado com sucesso!\n")
    else:
        print(f"\nA {nome} foi cadastrada com sucesso!\n")

def listar_pessoas():
    if not pessoas:
        print("\nErro: A lista está vazia.\n")
    else:
        print("\n===== Lista de Colaboradores =====")
        for i, p in enumerate(pessoas):
            print(f"Matrícula: {i+1}\nNome: {p['nome']}\nSexo: {p['sexo']}\nCPF: {p['cpf']}\nIdade: {p['idade']}\nE-mail: {p['email']}\nCEP: {p['cep']}\n============================")

def editar_pessoa():
    if not pessoas:
        print("\nErro: A lista está vazia.\n")
    else:
        listar_pessoas()
        indice = int(input("\nDigite a matrícula do Colaborador para editar: ")) - 1
        for p in (pessoas):
            print(f"Nome: {p['nome']}\nSexo: {p['sexo']}\nCPF: {p['cpf']}\nIdade: {p['idade']}\nE-mail: {p['email']}\nCEP: {p['cep']}\n============================")

        while True:
            print("\nOque você deseja alterar?")
            print("1. Nome")
            print("2. Sexo")
            print("3. CPF")
            print("4. Idade")
            print("5. E-mail")
            print("6. CEP")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                print(pessoas[indice]['nome'])
                while True:
                    nome = input("\nDigite o novo nome: ")

                    if nome.strip() == "":
                        print("\nErro: Insira um nome válido. Tente novamente.\n")
                    elif nome != nome.strip():
                        print("\nErro: Não pode haver espaços no início ou no fim. Tente novamente.\n")
                    else:
                        pessoas[indice]['nome'] = nome
                        print("\nO Nome foi atualizado com sucesso!\n")
                        break
                
            elif opcao == '2':
                print(pessoas[indice]['sexo'])
                while True:
                    sexo = int(input("\nQual é o novo sexo do Colaborador?\n1- Masculino\n2- Feminino\nEscolha uma opção: "))
                    if sexo.strip() == "":
                        print("\nErro: Insira algo. Tente novamente.\n")
                    elif sexo != sexo.strip():
                        print("\nErro: Não pode haver espaços no início ou no fim. Tente novamente.\n")
                    elif sexo == 1:
                        sexo = "Masculino"
                        break
                    elif sexo == 2:
                        sexo = "Feminino"
                    elif sexo > 2 or sexo <1:
                        print("\nErro: Insira um número entre 1 e 2. Tente novamente.\n")
                    else:
                        pessoas[indice]['sexo'] = sexo
                        print("\nO Sexo foi atualizado com sucesso!\n")
                        break
            
            elif opcao == '3':
                print(pessoas[indice]['cpf'])
                while True:
                    cpf = input("\nDigite o novo CPF do Colaborador: ")
                    if validar_cpf(cpf):
                        pessoas[indice]['cpf'] = cpf
                        print("\nO CPF foi atualizado com sucesso!\n")
                        break
                    else:
                        print("\nErro: Insira um CPF válido. Tente novamente.\n")

            elif opcao == '4':
                while True:
                    idade = int(input("Digite a nova idade do Colaborador: "))
                    if idade < 0:
                        print("\nErro: Insira uma idade válida. Tente novamente.\n")
                    else:
                        pessoas[indice]['idade'] = idade
                        break
            
            elif opcao == '5':
                while True:
                    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                    email = input("\nDigite o novo E-mail do Colaborador: ")

                    if email.strip() == "":
                        print("\nErro: Insira um E-mail válido. Tente novamente.\n")
                    elif not re.match(email_regex, email):
                        print("\nErro: Insira um email válido. Tente novamente.\n")
                    else:
                        pessoas[indice]['email'] = email
                        break
                
            elif opcao == '6':
                cep = input("\nDigite o novo CEP do Colaborador: ").strip().replace("-", "")

                if len(cep) != 8:
                    print("\nErro: Insira 8 dígitos. Tente novamente.\n")
                if not cep.isdigit():
                    print("\nErro: Insira apenas números. Tente novamente.\n")
                else:
                    pessoas[indice]['cep'] = cep
                    break
            elif opcao == '7':
                return
            else:
                print("\nErro: Opção inválida. Tente novamente.\n")
    
def excluir_pessoa():
    if not pessoas:
        print("\nErro: A lista está vazia.")
    else:
        listar_pessoas()
        indice = int(input("\nDigite a matrícula do colaborador que deseja desativar: ")) - 1
        for p in (pessoas):
            print(f"Nome: {p['nome']}\nSexo: {p['sexo']}\nCPF: {p['cpf']}\nIdade: {p['idade']}\nE-mail: {p['email']}\nCEP: {p['cep']}\n============================")
        while True:
            excluir = input("\nVocê realmente deseja excluir?\n1- Sim\n2- Não\nEscolha uma opção: ").strip()
            if excluir == "":
                print("\nErro: Insira algo. Tente novamente.\n")
            elif excluir not in ["1", "2"]:
                print("\nErro: Insira 1 ou 2. Tente novamente.\n")
            elif excluir == "1":
                if pessoas[indice]['sexo'] == "Masculino":
                    print(f"O {pessoas[indice]['nome']} foi desativado com sucesso!")
                else:
                    print(f"A {pessoas[indice]['nome']} foi desativada com sucesso!")
                pessoas.pop(indice)
                break
            else:
                return

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma1 * 10) % 11
    dig1 = 0 if dig1 == 10 else dig1
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma2 * 10) % 11
    dig2 = 0 if dig2 == 10 else dig2
    return cpf[-2:] == f"{dig1}{dig2}"

def menu():
    while True:
        print("\n===== MENU DO RECURSOS HUMANOS =====")
        print("1. Cadastrar Colaborador")
        print("2. Listar Colaboradores")
        print("3. Editar Colaborador")
        print("4. Desativar Colaborador")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            editar_pessoa()
        elif opcao == '4':
            excluir_pessoa()
        elif opcao == '5':
            print("\nEncerrando o sistema....")
            break
        else:
            print("\nErro: Opção inválida. Tente novamente.\n")

menu()

#teste dos guri
