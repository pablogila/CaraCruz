import random as r
from tqdm import tqdm # Para añadir una barra de carga en el bucle

# En este bucle elegimos cara o cruz.
# No nos deja avanzar hasta que no escribamos cara o cruz como personas normales que somos.
t = False
while t == False:
    print("Elige: ¿cara o cruz?")
    q = (input())
    if q == "cara" or q == "cruz":
        t = True
    else:
        print ("Perdona?? que si quieres cara o cruz, no es tan complicado  -_-")

print("¿Cuántas tiradas quieres hacer?")
N=int(input())

o = 0
x = 0

print("Lanzando muchas monedas...\n")
# Tiramos la moneda N veces.
# Si es < 0.5, será cara; si es mayor, cruz.
for i in tqdm(range(0, N)):
    if r.random() < 0.5:
        o+=1
    else:
        x+=1

# Veamos los resultados
print("\ncaras:  ",o)
print("cruces: ",x,"\n")
# ¿Quién ha ganado?
if o > x:
    print("Ganan CARAS por ",abs(o-x),"tiradas\n")
    if q == "cara":
        print("Enhorabuena! ganaste!")
    else: print("Lo siento... has perdido  :(")
elif o < x:
    print("Ganan CRUCES por ",abs(o-x),"tiradas\n")
    if q == "cruz":
        print("Enhorabuena! ganaste!")
    else: print("Lo siento... has perdido  :(")
elif o == x:
    print("Empate! todo el mundo gana!!\n")

input("\n Pulsa ENTER para salir")