def add_elements(a, b):
    result = []
    for item_a, item_b in zip(a, b):
        result.append(item_a + item_b)
    return result

with open('input.txt', 'r') as f:
    lines = f.readlines()
last_line1, last_line2 = lines[-2], lines[-1]

list1 = list(map(int, last_line1[: -1].split(',')))
list2 = list(map(int, last_line2[: -1].split(',')))

new_list = add_elements(list1, list2)
with open('input.txt', 'a') as f:
    for i, item in enumerate(new_list):
        f.write(str(item))     
        if i < len(new_list) - 1:
            f.write(',')
        else:
            f.write('\n')