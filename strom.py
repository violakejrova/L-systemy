import turtle


pravidla= {'M': ('S[+M][-M]SM'),
           'S': ('SS')}
rada = 'M'


opakovani = int (input('počet generací: '))

def lsystem (rada, pravidla, opakovani):
  for _ in range (opakovani):
    x = ''
    for pismenko in rada:
          if pismenko in pravidla:
            x += pravidla[pismenko]
          else:
            x += pismenko
    rada = x
  return rada


for q in range (opakovani+1):
  print('generace {}: {}'.format(q, lsystem(rada,pravidla, q)))


  
w = turtle.Screen()
w.setup(width = 1.0, height = 1.0)
turtle.Turtle() 
r = lsystem(rada, pravidla, opakovani)


turtle.penup()
turtle.goto(0,-250)
turtle.pendown()

turtle.left(90)
pozice = []
uhel = []

for pismenko in r:
    if pismenko == 'M':
        turtle.color('green')
        turtle.forward(5)
            
    elif pismenko == 'S':
        turtle.color('brown')
        turtle.forward(5)
        
    elif pismenko == '+':
        turtle.left(45)
            
    elif pismenko == '-':
        turtle.right(45)
                    
    elif pismenko == '[':
        a = turtle.pos()
        pozice.append(a)
        b = turtle.heading()
        uhel.append(b)
        
    elif pismenko == ']':
        turtle.penup()
        turtle.goto(pozice[-1])
        del pozice[-1]        
        turtle.setheading(uhel[-1])
        del (uhel[-1])
        turtle.pendown()
  

    
    

