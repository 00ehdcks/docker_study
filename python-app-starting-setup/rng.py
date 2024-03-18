from random import randint

min_number = int(input('Please enter the min number: '))
max_number = int(input('Please enter the max number: '))

if (max_number < min_number): 
  print('Invalid input - shutting down...')
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)

#도커에서 일반적인 run으로는 사용자의 입력을 받을 수 없다.
#-i(interactive모드), -t(입력허용)를 결합하여 작성해야한다.
#start는 -i만 사용하여도 가능하다
