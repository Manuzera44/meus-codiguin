import random
pokemons = []

def cadpokemon():
   
    Nome = input("Qual o Nome do seu pokemon?: ")
    if not Nome:
        print("Não pode ser vazio.Escreva algo válido.")
        Nome = input("Qual o Nome do seu pokemon?: ")
    Tipo = input("Qual o tipo do seu pókemon?: ")
    if not Tipo:
         print("Não pode ser vazio.Escreva algo válido.")
         Tipo = input("Qual o tipo do seu pókemon?: ")
    Ataque = input("Qual o ataque do seu pokemon?:")
    if not Ataque:
        print("Não pode ser vazio.Escreva algo válido.")
        Ataque = input("Qual o ataque do seu pokemon?:")
    Pv = int(input("Qual a vida do seu pokemon?:"))
    if not Pv:
         print("Não pode ser vazio.Escreva algo válido.")
         Pv = int(input("Qual a vida do seu pokemon?: "))

    pokemons.append({"Nome" : Nome, "tipo": Tipo, "Ataque": Ataque, "pontos_de_vida": Pv })
    print("Seu pokemon foi capturado!")

def listarpokemon():
    if not pokemons:
        print("Não há pokemons na pokedex")
    print("-----Lista da Pokedex-----")
    for i, Nome  in enumerate(pokemons):
        print(f"{i +1}.{Nome['Nome']}-Tipo:{Nome['tipo']}")

def batalhar():
    if len(pokemons) < 2:
        print("Não há pokemons para batalha!!")
    print("BATALHA POKEMON!")
    listarpokemon()
    indice1 = int(input("Qual o número do Pokemon você quer ver batalhar?: ")) - 1
    indice2 = int(input("Qual o número do segundo pokemon que voce quer ver batalhar?: ")) -1 
    if indice1 == indice2:
        print("os pokemons tem que serem diferentes.")
        return
    p1 = pokemons[indice1]
    p2 = pokemons[indice2]

    
    while p1['pontos_de_vida'] > 0 and p2['pontos_de_vida'] >0:
        input(f"O {p1['Nome']} irá atacar(de ENTER para passar)")
        dano = random.randint(50, 75)
        pokemons[indice2]['pontos_de_vida'] -= dano
        print(f"o dano de {dano} foi tirado da vida do pokemon do oponente a vida atual dele é {pokemons[indice2]['pontos_de_vida']}")
        if p2['pontos_de_vida'] <= 0:
            print(f"O Campeão foi o {p1['Nome']}")
            break
        input(f"O {p2['Nome']} irá atacar(de ENTER para passar)")
        dano = random.randint(50, 75)
        pokemons[indice1]['pontos_de_vida'] -= dano
        print(f"o dano de {dano} foi tirado da vida do pokemon do oponente a vida atual dele é {pokemons[indice1]['pontos_de_vida']}")
        if p1['pontos_de_vida'] <= 0:
            print(f"O Campeão foi o {p2['Nome']}")
        
    
def pokedex():
    print("-----Pokedéx do zarpinha-----")
    print("1- Cadastrar Um Pokemon👹")
    print("2- Listar Pokemons👾")
    print("3- Batalhar⚔️")
    print("4- Sair")

opcao = 0
while opcao != 4:
    pokedex()
    opcao = int(input("Qual a opção que você deseja?: "))
    if opcao == 1:
        cadpokemon()
    elif opcao == 2:
        listarpokemon()
    elif opcao == 3:
        batalhar()
    elif opcao == 4:
         print("Saindo da pokedéx. Boas capturas!")
    elif opcao == ' ':
        print("opção inválida.")
