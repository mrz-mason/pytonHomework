my_list = [8, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 5]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Повторяющиеся элементы в списке:", duplicates)