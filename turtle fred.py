import turtle

def  carré(tortue, L):
    for k in range(4):
        tortue.forward(L)
        tortue.right(90)
    return None
   
def choix_couleur(nombre):
    if nombre % 2 == 1
        return "black"
    else:
        return "white"
   
fred = turtle.Turtle()
carré(fred, 100)
turtle.exitonlick()
