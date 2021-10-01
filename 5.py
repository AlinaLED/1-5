try:
  a=float(input('Введите длину стороны куба:'))
  r=float(input('Введите радиус цилиндра:'))
  h=float(input('Введите высоту цилиндра:'))
  v=float(input('Введите объем жидкости:'))
  if (a**3>v) or (3,14*r**2*h>v) or (a**3+3,14*r**2*h>v):
      print('Нет')
  else:
      print('Да')  
except ValueError: 
    print('Это не число. Введите число.')   
