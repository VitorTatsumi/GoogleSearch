#Código para fazer uma busca no Google e retornar a quantidade de resultados desejados através de uma lista ordenada.

from googlesearch import search 

busca = str(input('[Digite algo para buscar no Google]\n'))
num = int(input('[Deseja obter quantos resultados de busca? (máx. 10)]\n'))

result = list(
    search(
        busca,
        lang = 'pt-br',
        num_results=num-1
    )
)
#print(result)
print('[Resultados da busca]')
for c in range (0, len(result)):
  print('\n[ {} ] {}'.format(c+1, result[c]))
