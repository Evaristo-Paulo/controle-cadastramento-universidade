import os
from Funcionario import Funcionario
from Universidade import Universidade


universidade_agostinho_neto = Universidade('Agostinho Neto')

def msg_erro(mensagem):
    print(f' ERRO: {mensagem}')

def menu_opcao():
    print(' MENU')
    print(' 1 | Cadastrar Departamento')
    print(' 2 | Cadastrar Funcionário (Técnico)')
    print(' 3 | Cadastrar Funcionário (Docente)')
    print(' 4 | Buscar Departamento')
    print(' 5 | Buscar Funcionário (Nome)')
    print(' 6 | Listar Todos Departamentos')
    print(' 7 | Listar Todos Funcionários')
    print(' 8 | Listar Todos Departamentos e seus Respectivos Funcionarios')
    print(' 9 | Listar Todos Funcionários (Técnico)')
    print('10 | Listar Todos Funcionários (Docente)')
    print(' 0 | Sair')
    print()

def limpa_tela():
    print('')
    input(' Digite ENTER para voltar ao MENU...')
    os.system('cls')

def menu(op):
    if op == 1:
        print(' Cadastrar Departamento')
        codigo = input('     Código: ')
        if universidade_agostinho_neto.buscar_departamento(codigo) is None:
            universidade_agostinho_neto.adicionar_departamento(codigo)
    elif op == 2:
        print(' Cadastrar Funcionário (Técnico)')
        codigo = input('     Código Departamento: ')
        departamento = universidade_agostinho_neto.buscar_departamento(codigo)
        if departamento is not None:
            nome = input('     Nome Funcionário: ')
            novo_funcionario = Funcionario(nome, 'Técnico')
            departamento.adicionar_funcionario(novo_funcionario)
        else:
            msg_erro(f'Não conseguimos localizar o departamento {codigo}.')
    elif op == 3:
        print(' Cadastrar Funcionário (Docente)')
        codigo = input('     Código Departamento: ')
        departamento = universidade_agostinho_neto.buscar_departamento(codigo)
        
        if departamento is not None:
            nome = input('     Nome Funcionário: ')
            novo_funcionario = Funcionario(nome, 'Docente')
            departamento.adicionar_funcionario(novo_funcionario)
        else:
            msg_erro(f'Não conseguimos localizar o departamento {codigo}.')
    elif op == 4:
        print(' Buscar Departamento')
        codigo = input('     Código Departamento: ')
        departamento = universidade_agostinho_neto.buscar_departamento(codigo)

        if departamento is not None:
            departamento.exibir()
        else:
            msg_erro(f'Não conseguimos localizar o departamento {codigo}.')
    elif op == 5:
        print(' Buscar Funcionário (Nome)')
        nome = input('     Nome: ')
        funcionario = universidade_agostinho_neto.buscar_funcionario(nome)
        
        if funcionario is not None:
            funcionario.exibir()
        else:
            msg_erro(f'Não conseguimos localizar o funcionário {nome}.')
    elif op == 6:
        print(' Listar Todos Departamentos')
        universidade_agostinho_neto.listar_departamentos()
    elif op == 7:
        print(' Listar Todos Funcionários')
        universidade_agostinho_neto.listar_funcionarios()
    elif op == 8:
        print(' Listar Todos Departamentos e seus Respectivos Funcionarios')
        universidade_agostinho_neto.listar_departamentos_respectivos_funcionarios()
    elif op == 9:
        print(' Listar Todos Funcionários (Técnico)')
        universidade_agostinho_neto.listar_funcionarios(filtro='Técnico')
    elif op == 10:
        print(' Listar Todos Funcionários (Docente)')
        universidade_agostinho_neto.listar_funcionarios(filtro='Docente')
    elif op == 0:
        return
    else:
        print(' ERRO: Não conseguimos reconhecer esta opção.')

    limpa_tela()

    
