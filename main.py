from menu import menu, menu_opcao

while True:
    menu_opcao()
    str_op = input('Informa a opção desejada: ')
    int_op = int(str_op)
    print()
    menu(int_op)