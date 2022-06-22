
i = 0
fibonacci = [1,1]
num = int(input('Digite um número: '))

while num > len(fibonacci):
	fibo.append(fibonacci[i] + fibonacci[i+1])
	i+=1

print ('Fibonacci(%d): %d' %(num,fibonacci[num-1]))
