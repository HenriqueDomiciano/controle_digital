k = 0 
coeficientes = [1,-1+((k-1)*0.3679),k*0.2642+0.3679]
l1 = coeficientes
l2 = coeficientes[::-1]
j = l2[0]/l1[0]
if abs(j)>1:
	print('SISTEMA INSTAVEL')
	quit()
for k in range(len(coeficientes)-1):
	print(f'LINHA {(k+1)*2-1} :{l1}')
	print(f'LINHA {(k+1)*2} : {l2}')
	print(f'J{k} {j}')

	l1 = [l1[i] - l2[i] * j for i in range(len(l1))]
	l1.pop(-1)
	l2 = l1[::-1]
	j = l2[0]/l1[0]
	if abs(j)>1:
		print(f'SISTEMA INSTAVEL {abs(j)}')
		break

else:
	print("SISTEMA ESTAVEL")
