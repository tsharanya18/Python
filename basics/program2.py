n = input1
k = input2
test_array = input3
window_id = ''
for i in range(n):
    if i == k:
        window_id = test_array[i]
        print(window_id)
        test_array.remove(test_array[i])
        print(test_array)
test_array.insert(0, window_id)
print(test_array)