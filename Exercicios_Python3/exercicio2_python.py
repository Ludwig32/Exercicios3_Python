produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
estoque = [100, 150, 80, 120, 60]

produto = input('Digite o nome do produto: ')

if produto in produtos:
    posicao = produtos.index(produto)

    print(f'Produto encontrado na posição {posicao}')
    print(f'Quantidade em estoque: {estoque[posicao]}')

else:
    print('Produto não encontrado')


