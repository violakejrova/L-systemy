import turtle

pravidla = {'L' : 'L+R++R-L--LL-R+',
            'R': '-L+RR++R+L--L-R'}
rada = ['L']
uhel = 60

opakovani = int(input('Počet generací: '))


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
  

    
barva = ['red','orange','yellow','green','blue','purple']
b = 0

  
w = turtle.Screen()
w.setup(width = 1.0, height = 1.0)
turtle.Turtle() 
r = lsystem(rada, pravidla, opakovani)
turtle.speed(500000)
turtle.color(barva[b])
a = []

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()

for pismenko in r:
    if pismenko == 'L':
        turtle.forward(5)
        a+='.'
        
    elif pismenko == 'R':
        turtle.forward(5)
        a+='.'
        
    elif pismenko == '+':
        turtle.left(uhel)
        
    elif pismenko == '-':
        turtle.right(uhel)
        
    if len(a) == 500:
        b+=1        
        if b == (len(barva)):
            b = 0
        turtle.color(barva[b])
        a = []