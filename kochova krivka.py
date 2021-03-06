import turtle

f = 'F'
y = list('F+F--F+F')
rada = [f]

pravidla = {f: y}

opakovani = int (input('počet generací: '))

def lsystem (rada, pravidla, opakovani):
  for _ in range (opakovani):
    x = []
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
w.bgcolor('black')
w.title('Kochova vločka')
w.screensize()
w.setup(width = 1.0, height = 1.0)
turtle.Turtle()
turtle.color('white')
r = lsystem(rada, pravidla, opakovani)
  
turtle.penup()
turtle.goto(-400,-200)
turtle.pendown()


for pismenko in r:
  if pismenko == 'F':
     turtle.forward(5)
  elif pismenko == '-':
     turtle.right(60)
  elif pismenko == '+':
      turtle.left(60)
