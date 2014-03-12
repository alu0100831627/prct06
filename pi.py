#! usr/bin/python
#! encoding UTF-8
def aproxpi (n):
  s = 0.0
  for i in range(1,n+1):
    xi= float((i-0.5)/n)
    f_xi= float(4/(1+xi**2))
    s = s + f_xi
    r = s / n    
  return r
n=int(raw_input('Introduzca el numero de intervalos que desea: '))
v=int(raw_input('Introduce el numero de veces que deseas que se repita: '))
l=[ ]
for i in range(1,v+1):
  x=aproxpi(n*i)
  l=l+[x] 
  print x
print l
