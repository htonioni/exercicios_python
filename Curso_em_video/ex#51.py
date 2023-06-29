p_term = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
u_term = p_term + (10 * rz)
for x in range(p_term, u_term, rz):
    print(x, end=' => ')
print('ACABOU')