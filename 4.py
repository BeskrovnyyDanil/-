a=int(input('Введите целое число А '))
b=int(input('Введите целое число В<A '))
for i in range(a-(a+1)%2, b-b%2, -2):
    print(i,end='')