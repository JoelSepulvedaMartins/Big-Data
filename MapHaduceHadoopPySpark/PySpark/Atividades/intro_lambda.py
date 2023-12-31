# -*- coding: utf-8 -*-
"""intro_lambda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B5ypxQw3MQePVBUWU0WuPvGgl0lDYG8N
"""

def fahr2cel(temp):
  temp =  (temp-32)*(5/9)
  return temp

t = fahr2cel(100)
t

t = lambda temp: (temp-32) * (5/9)
t(100)

(lambda temp: (temp-32)*(5/9))(100)

# função que faz a soma de dois números
ans = lambda x,y: x+y
ans(10,5)

# função que filtra uma lista retornado somente os valores pares
lista = [1,4,6,3,1,7,9,3,4,6]
def filtra_pares(lista):
  l = []
  for x in lista:
    if x%2 == 0:
      l.append(x)
  return l

pares = filtra_pares(lista)
pares

pares = list(filter(lambda x: x%2 == 0, lista))
pares

from functools import reduce
numbers = [1, 5, 2, 12, 10]

p = reduce(lambda x,y: x*y if x>y else x+y, numbers)
p

class Product:
  # construtor da classe
  def __init__(self, description, price):
    self.description = description
    self.price = price

  # método para escrever os atributos de um objeto
  def __str__(self):
    return f"Produto: {self.description}\nPreço: {self.price:.2f}\n"

# cria uma lista com 3 objetos do tipo Product
obj1 = Product("Cadeira gamer", 999)
obj2 = Product("Mouse Logitech", 515)
obj3 = Product("Monitor 23 pol", 1400)

lista_produtos = [obj1, obj2, obj3]

for i in lista_produtos:
  print(i)

# aumenta o preço em 10% de cada produto
nova_lista = list(map(lambda p: Product(p.description, p.price*1.1), lista_produtos))

for i in nova_lista:
  print(i)

# retorna os produtos que possuem um preço acima de 1000
maiores_precos = list(filter(lambda p: p.price > 1000, nova_lista))
for i in maiores_precos:
  print(i)

from functools import reduce
# soma o preço de todos os produtos
soma_preco = reduce(lambda x,y: x+y, map(lambda x: x.price, nova_lista))
print(f"{soma_preco:.2f}")

# retornar o objeto com o maior preço
maior_preco = reduce(lambda x,y: x if x.price > y.price else y, nova_lista)
print(maior_preco)

