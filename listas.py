print("hola mundo")
lista=[1, "hola", 3,67, [1,2,3]]
print(lista[1])
a=[00, "python", 3.87]
print(a[-1])
#append
lista=[1,2]
lista.append(3)
print(lista) #[1, 2, 3, 4]

#extend
lista=[1, 2]
lista.extend([3, 4])
print(lista) #[1, 2, 3, 4]

#insert
lista=[1, 3]
lista.insert(2, "casa")
print(lista)

#remove
lista=[1,2,3,4, "ultimo", "jose"]
lista.remove("ultimo")
print(lista)