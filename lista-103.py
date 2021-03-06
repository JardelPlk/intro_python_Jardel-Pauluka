###
# Exercicios
###
print()
book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
print(book1.split('by')[0])
print(book2.split('by')[0])
print(book3.split('by N')[0])

# 2) Salve o titulo de cada livro em uma variável
titulo1 = book1.split('by')[0].strip()# remover espaçõs em bransco strip
titulo2 = book2.split('by')[0].strip()
titulo3 = book3.split('by N')[0].strip()

# 3) Quantos caracteres cada título tem?
print('\nQuantidade de caracteres do título 1:',len(titulo1))
print('Quantidade de caracteres do título 2:',len(titulo2))
print('Quantidade de caracteres do título 3:',len(titulo3))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
autor1 = book1.split('by')[1]
autor1 = autor1.split(',')[0].strip()
ano1 = book1.split(',')[1].strip()
print('\n{'+titulo1+'} - {'+autor1+'}, {'+ano1+'}')

autor2 = book2.split('by')[1]
autor2 = autor2.split(',')[0].strip()
ano2 = book2.split(',')[1].strip()
print('{'+titulo2+'} - {'+autor2+'}, {'+ano2+'}')

autor3 = book3.split('by')[1]
autor3 = autor3.split(',')[0].strip()
ano3 = book3.split(',')[1].strip()
print('{'+titulo3+'} - {'+autor3+'}, {'+ano3+'}')

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta
print()
palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

palindrome_comparacao = palindrome_one.replace(' ', '')
palindrome_comparacao = palindrome_comparacao.lower()
palindrome_comparacao_invertida = palindrome_comparacao[::-1]
resposta = palindrome_comparacao == palindrome_comparacao_invertida
print(palindrome_one,'é palindrome?',resposta)

palindrome_comparacao = palindrome_two.replace(' ', '')
palindrome_comparacao = palindrome_comparacao.lower()
palindrome_comparacao_invertida = palindrome_comparacao[::-1]
resposta = palindrome_comparacao == palindrome_comparacao_invertida
print(palindrome_two,'é palindrome?',resposta)

palindrome_comparacao = palindrome_three.replace(' ', '')
palindrome_comparacao = palindrome_comparacao.lower()
palindrome_comparacao_invertida = palindrome_comparacao[::-1]
resposta = palindrome_comparacao == palindrome_comparacao_invertida
print(palindrome_three,'é palindrome?',resposta)

palindrome_comparacao = palindrome_four.replace(' ', '')
palindrome_comparacao = palindrome_comparacao.lower()
palindrome_comparacao_invertida = palindrome_comparacao[::-1]
resposta = palindrome_comparacao == palindrome_comparacao_invertida
print(palindrome_four,'é palindrome?',resposta)
