def listar(nomes):
    print'Listar os nomes: '
    for nome in nomes:
        print nome

# -*- coding: utf-8 -*-


def cadastrar(nomes):
    print'Digite o seu nome: '
    nomes = raw_input()
    nomes.append(nomes)



def menu ():
    nomes = []
    escolha = ''
    while(escolha != '0' ):
        print('Digite : 1 - cadastrar 2 - Listar 0 - Sair')
        escolha = raw_input()
        if (escolha == '1'):
            cadastrar()
        if (escolha == '2'):
            listar()
        menu()