count = 5
test_array = [1, 4, 5, 4, 5]
# test_array = [1, 2, 3, 4, 5]
unique_array = list(set(test_array))
# unique_array = list(unique_array)
total_length = len(test_array)
unique_length = len(unique_array)
length = total_length - unique_length
max_number = max(unique_array)
for i in range(length):
    i = i + 1
    number = max_number + i
    unique_array.append(number)

total_marks = sum(unique_array)
print("Total Marks are "+str(total_marks))


'''
def mutate(arr): arr[0] = 0


x = [1, 2, 3]
mutate(x)
print(x)
'''


'''
def func(a, b):
    if b == 0:
        return a
    else:
        return func(a ^ b, (a & b) << 1)


print(func(5, 6))
'''


'''
x, y = 1, 1


def f():
    global x
    y = 0
    for i in (10, 20, 30):
        x += 1
        y += i
        f()
        print(x, y)
'''



