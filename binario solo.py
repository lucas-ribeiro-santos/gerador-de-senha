n1 = int(input("digite um numero--->"))
listagem = []
while n1 >= 1 :
    listagem.insert(0, n1%2)
    n1 = n1 // 2
resultado = "".join(str(i) for i in listagem)
print('_________________')
print(     resultado       )
print('_________________')
