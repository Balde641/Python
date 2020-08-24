import random 
import string
# Satunnaisuus
print(random.randint(1, 10))

# Nopan heittäminen
print("Silmäluku: ", random.randint(1,6))
# Toinen vaihtoehto, kuten edellinen
print("Silmäluku: " +  str(random.randint(1,6)))

# Kolikon heittäminen
a = ["kruuna", "klaava"]
print("Tulos: " + random.choice(a))

# Salasanan arpoja
merkkienmaara = 0
salasana = ""
while(merkkienmaara < 8):
    salasana += random.choice(string.ascii_lowercase)
    merkkienmaara += 1
print(salasana)

# Toinene esimerkki
salasana = ""
for x in range(8):
    salasana += random.choice(string.ascii_lowercase)
print(salasana)    


# Sekoittaja
def sekoitaLista(luvut):
    random.shuffle(luvut)

def tulostaLista(luvut):
    print(luvut)

luvut = [1, 2, 3, 4, 5, 6, 7, 8]
sekoitaLista(luvut)
tulostaLista(luvut)

# Vihollisen sijainnit
sijaintilista=[]
for i in range(0,200):
    n = str(random.randint(0,100)) + "," + str(random.randint(0,100))
    sijaintilista.append(n)
print(sijaintilista)    

# Listan järjestäminen
lista = [1, 3, 5, 4]
lista.sort()
print(lista)

# Pistelista

# Kierrokset = True
# x = []
# y = []
# lisaaInput = ""
# while Kierrokset:
#     lisaaInput = input("Anna pelaaja: ")
#     if lisaaInput == "lopeta":
#         Kierrokset = False

#     else:
#         x.append(lisaaInput)
#         varY = input("Anna pisteet")
#         print(len(varY))
#         if len(varY)>2:
#             y.append(str(0)) + "" + str(varY)
#         else:
#             y.append(varY)

# esiintymat =                   


