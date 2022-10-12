# som = 0
# nbr = input("Entrez un nombre : ") 

# print("La somme de ")
# for x in range(1, int(nbr) + 1):
#     som = som + x
#     print(x , " + ")
# print(som)

Nb =int(input("Entrez un nombre entre 1 et 3 "))
while Nb < 1 or Nb > 3:
    Nb = int(input("Saisie erronée. Entrez un nombre entre 1 et 3 "))
print("bravo")