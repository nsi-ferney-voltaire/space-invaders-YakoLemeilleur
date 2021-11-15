import turtle
fred = turtle.Turtle()

def carre (fred, L):
        fred.goto(0, 0)
        for i in range (4):
            
            fred.forward(L)
            fred.right(90)
          
        
carre (fred, 100)

def choix_couleur (nombre):
    if nombre %2==0:
        return black
else:
    return white