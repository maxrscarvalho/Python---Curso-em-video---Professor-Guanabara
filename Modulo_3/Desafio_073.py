'''Crie uma tupla preenchida com os 20 primeiros colocados 
da tabela do campeonato brasileiro de futebol, na ordem de 
colocacao. Depois mostre: 

A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem Alfabetica.
D) Em que posicao na tabela esta o time da Chapecoense.'''

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atletico PR', 'Atletico MG', 'Fortaleza', 'Sao Paulo', 'America MG', 'Botafogo', 'santos', 'Goias', 'Bragantino', 'Coritiba', 'Cuiaba', 'Ceara', 'Atletico GO', 'Avai', 'Juventude')

print(f'Os 5 primeiros colocados sao: ',times[0:5])
print('-=-'*20)
print(f'Os ultimos 4 times sao:', times[16:20])
print('-=-'*20)
print(sorted(times))
print('-=-'*20)
print('O time do Goias esta na posicao',times.index('Goias'))
