from functions import (
add_clients,
add_order,
add_product,
delete_client,
get_clients,
get_order,
get_product,
)

from functions import (
    add_clients,
    add_order,
    add_product,
    delete_client,
    get_clients,
    get_order,
    get_product,
)

while True:
    print("\nIzvēlne")
    print("1 - Pievienot klientu")
    print("2 - Pievienot preci")
    print("3 - Pievienot pasūtījumu")
    print("4 - Pasūtījumu saraksts")
    print("5 - Klientu saraksts")
    print("6 - Parādīt pasūtījumu")

    choise = input("Izvēle: ")

    if choise == "1":
        name = input("Klienta vārds: ")
        surname = input("Klienta uzvārds: ")
        client_id = add_clients(name, surname)
        print("Klients pievienots, ID: ", client_id)

    elif choise == "2":
        name = input("Preces nosaukums: ")
        price = input("Preces cena: ")
        product_id = add_product(name, price)
        print("Prece pievienota, ID: ", product_id)

    elif choise == "3":
        print("\nKlientu saraksts:")
        for client in get_clients():
            print(client)

        print("\nPreces saraksts:")
        for product in get_product():
            print(product)

        client_id = input("Klienta ID: ")
        product_id = input("Preces ID: ")
        order_id = add_order(client_id, product_id)
        print("Pasūtījums pievienots, ID: ", order_id)

    elif choise == "4":
        print("\nPasūtījumu saraksts:")
        for order in get_order():
            print(order)

    elif choise == "5":
        print("\nKlientu saraksts:")
        for client in get_clients():
            print(client)
        client_id = int(input("Ievadi klienta ID, ko izdzēst: "))
        if delete_client(client_id) > 0:
            print("Klients izdzēsts.")
        else:
            print("Klients ar šādu ID nav atrasts.")

    elif choise == "7":
        break