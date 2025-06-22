#type:ignore
"""
Desafio: Controle de Estoque de uma Loja
Uma pequena loja precisa de um sistema simples para gerenciar seu estoque de produtos. Seu objetivo é criar um programa em Python que permita ao dono da loja:

Adicionar novos produtos ao estoque informando nome, quantidade e preço.

Atualizar a quantidade de um produto quando novas unidades forem compradas ou vendidas.

Exibir o estoque completo, mostrando os produtos disponíveis, suas quantidades e preços.

Calcular o valor total do estoque, multiplicando a quantidade pelo preço de cada produto.

Requisitos:
Use um dicionário para armazenar os produtos (chave: nome do produto, valor: dicionário com quantidade e preço).

Crie um menu interativo no terminal para o usuário escolher entre as opções (Adicionar, Atualizar, Exibir, Calcular valor total ou Sair).

O programa deve rodar em loop até o usuário optar por sair.


Escolha uma opção:  
1 - Adicionar Produto  
2 - Atualizar Quantidade  
3 - Exibir Estoque  
4 - Calcular Valor Total  
5 - Sair  

> 1  
Digite o nome do produto: Camiseta  
Digite a quantidade: 10  
Digite o preço: 35.90  
Produto adicionado com sucesso!  

> 3  
Estoque Atual:  
Camiseta - Quantidade: 10 - Preço: R$ 35.90  

"""
estoque = {}

while  True:
    print('========Controle de estoque=======')
    print('1 - Adicionar Produto')
    print('2 - Atualizar Quantidade')
    print('3 - Exibir Estoque')
    print('4 - Calcular Valor Total')
    print('5 - Sair')

    opcao = input('Escolhar umas das opções: ')

    if opcao == '1':
        nome = input('Qual produto deseja adicionar: ')
        quantidade = int(input('Quantos produto deseja adicionar: '))
        preco = float(input('Qual é o preço do produto: '))

        estoque[nome] = {"quantidade": quantidade, "preco": preco}
        print(f'produto "{nome}" Adicionado com sucesso!')

    elif opcao == '2':
        nome = input('Digite o produto que queira atualiar: ')

        if nome in estoque:
            nova_qtd = int(input('Digite a nova quantidade: '))
            estoque[nome]["quantidade"] = nova_qtd
            print(f'Quantidade do produto "{nome}" alterada para "{nova_qtd}"!')
        else:
            print("produto não encontrado!")
        
    elif opcao == '3':
        if not estoque:
            print('Estoque está vazio')
        else:
            print('=======Estoque Atual======')
            for produto, info in estoque.items():
                print(f'{produto} - Quantidade: {info["quantidade"]} - Preço: R {info['preco']:.2f}')
        
    elif opcao == '4':
        total = sum(info['quantidade'] * info['preco'] for info in estoque.values())
        print(f'Valor total do estoque é "{total:.2f}"')
        

    elif opcao == '5':
        print('Saindo do programa!')
        break
    else:   
        print('Opção selecionada inválida')

    