n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
pnome = nome[0].title()
unome = nome[-1].title()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {pnome}')
print(f'Seu último nome é {unome}')