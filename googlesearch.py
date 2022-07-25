from googlesearch import search 

busca = str(input('[Digite algo para buscar no Google]\n'))

result = list(
    search(
        busca,
        lang = 'pt-br',
        num_results=5
    )
)
#print(result)
print('[Resultados da busca]')
for c in range (0, len(result)):
  print('\n[ {} ] {}'.format(c+1, result[c]))
