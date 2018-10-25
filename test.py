import calculator as calc

print('\nTitle: TC1 - Test my_sum')

###########################################################

print('\nStep: 1')

step_result = 'ERROR'

v1 = 4
v2 = 6
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = 10
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 2')

step_result = 'ERROR'

v1 = 0
v2 = 0
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = 0
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 3')
step_result = 'ERROR'

v1 = 3.5
v2 = 0
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = 3.5
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 4')
step_result = 'ERROR'

v1 = 0.0
v2 = 20000000
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = 20000000.0
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 5')
step_result = 'ERROR'

v1 = 'a'
v2 = 1
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = 'a1'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 6')
step_result = 'ERROR'

v1 = 'a'
v2 = 'b'
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = 'ab'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 7')
step_result = 'ERROR'

v1 = -5.5
v2 = -5
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = -10.5
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 8')
step_result = 'ERROR'

v1 = '-a'
v2 = 'a'
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = '-aa'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 9')
step_result = 'ERROR'

v1 = 'char'
v2 = 5
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = 'char5'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 10')
step_result = 'ERROR'

v1 = '.'
v2 = 5
print('ACTION: Addition {} and {}'.format(v1, v2))

exp = '.5'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################


print('\nTitle: TC2 - Test my_sub')

###########################################################

print('\nStep: 11')

step_result = 'ERROR'

v1 = 4
v2 = 6
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = -2
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 12')

step_result = 'ERROR'

v1 = 0
v2 = 0
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = 0
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 13')
step_result = 'ERROR'

v1 = 3.5
v2 = 0
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = 3.5
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 14')
step_result = 'ERROR'

v1 = 0.0
v2 = 2
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = -2.0
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 15')
step_result = 'ERROR'

v1 = 'a'
v2 = 1
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 16')
step_result = 'ERROR'

v1 = 'a'
v2 = 'b'
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 17')
step_result = 'ERROR'

v1 = -5.5
v2 = -5
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = -10.5
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 18')
step_result = 'ERROR'

v1 = '-a'
v2 = 'a'
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = '-aa'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sum(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 19')
step_result = 'ERROR'

v1 = 'char'
v2 = 5
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 20')
step_result = 'ERROR'

v1 = None
v2 = 5
print('ACTION: Subtraction {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_sub(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################


print('\nTitle: TC3 - Test my_mul')

###########################################################

print('\nStep: 21')

step_result = 'ERROR'

v1 = 4
v2 = 6
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 24
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 22')

step_result = 'ERROR'

v1 = 0
v2 = 0
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 0
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 23')
step_result = 'ERROR'

v1 = 3.5
v2 = 0
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 0.0
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 24')
step_result = 'ERROR'

v1 = 0.0
v2 = 2
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 0.0
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 25')
step_result = 'ERROR'

v1 = 'a'
v2 = 1
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 'a'
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 26')
step_result = 'ERROR'

v1 = 'a'
v2 = 'b'
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 27')
step_result = 'ERROR'

v1 = -5.5
v2 = -5
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 27.5
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 28')
step_result = 'ERROR'

v1 = '-a'
v2 = 'a'
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 29')
step_result = 'ERROR'

v1 = 'ch'
v2 = 3
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 'chchch'
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 30')
step_result = 'ERROR'

v1 = 1234567890
v2 = 1234567890
print('ACTION: Multiplication {} and {}'.format(v1, v2))

exp = 1524157875019052100
print('EXPECTED: {}'.format(exp))

obs = calc.my_mul(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################


print('\nTitle: TC4 - Test my_div')

###########################################################

print('\nStep: 31')

step_result = 'ERROR'

v1 = 4
v2 = 6
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 2/3
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 32')

step_result = 'ERROR'

v1 = 0
v2 = 0
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 33')
step_result = 'ERROR'

v1 = 3.5
v2 = 0
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 34')
step_result = 'ERROR'

v1 = 0.0
v2 = 2
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 0.0
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 35')
step_result = 'ERROR'

v1 = 'a'
v2 = 1
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 36')
step_result = 'ERROR'

v1 = 'a'
v2 = 'b'
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 37')
step_result = 'ERROR'

v1 = -5.5
v2 = -5
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 1.1
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp == obs:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 38')
step_result = 'ERROR'

v1 = '-a'
v2 = 'a'
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 39')
step_result = 'ERROR'

v1 = 'ch'
v2 = 3
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################

print('\nStep: 40')
step_result = 'ERROR'

v1 = 9
v2 = None
print('ACTION: Division {} and {}'.format(v1, v2))

exp = 'ERROR'
print('EXPECTED: {}'.format(exp))

obs = calc.my_div(var1=v1, var2=v2)
print('OBSERVED: {}'.format(obs))

if exp[:5] == obs[:5]:
    step_result = 'PASSED'
else:
    step_result = 'FAILED'
    print('INFO: This function should work for v. 1.1')

print('Step result {}'.format(step_result))

###########################################################
