fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
animals = ['dog', 'cat', 'lion']

for f in fruits:
    print(f)

for a in animals:
    print(a)

# O (F + A)

print('------------------')
for a in animals:
    for f in fruits:
        print(f'{a} eats {f}')

num = len(animals)
while num > 0:  # 3
    print(num)
    num -= 1
    for f in fruits:
        print(f'{num} ----> {f}')  # 2
    for a in animals:
        print(f'{num} ----> {a}')  # 1

# O (A * (F + A)) => O(AF + A**2)

print('------------------')
for a in animals:
    print(a)
u = 0
while u < len(animals):
    print(u)
    u += 1
# O(A+A) => O(A)

def counter(num):
    print(num)
    if num > 0:
        counter(num - 1)

counter(3)