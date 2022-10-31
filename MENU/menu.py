def menu():
    print("[1] hambúrguer simples")
    print("[2] hambúrguer com bacon")
    print("[3] hambúrguer com coca")
    print("[4] hambúrguer com salada")
    print("[5] hambúrguer vegetariano")
    print("[0] Finalizar")

menu()
option = int(input("Bem-vindx, escolha o seu burguer favorite: "))

while option != 0:
    if option == 1:
        print("ótima escolha!")
        pass
    elif option == 2:
        print("Bacon pode te matar, mesmo assim, ótima escolha!")
        pass
    elif option == 3:
        print("a escolha do capitalista! =)")
        pass
    elif option == 4:
        print("O melhor x-salada de São Paulo")
        pass
    elif option == 5:
        print("Se é para comer hambúrguer, que seja de carne")
        pass
    else: 1print("essa não é uma opção válida")

    print()
    menu()
    option = int(input("Bem-vindx, escolha o seu burguer favorite: "))

print("obrigado por pedir nossos lanches")