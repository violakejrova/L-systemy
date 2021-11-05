import turtle

pravidla = {'x' : ('+yF-xFx-Fy+'),
            'y' : ('-xF+yFy+Fx-')}

rada = ['x']

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
turtle.goto(-620,-280)
turtle.pendown()
turtle.speed(10000)

for pismenko in r:
    if pismenko == 'x':
        pass
        
    elif pismenko == 'y':
        pass
        
    elif pismenko == 'F':
        turtle.forward(10)
        
    elif pismenko == '+':
        turtle.left(90)
        
    elif pismenko == '-':
        turtle.right(90)