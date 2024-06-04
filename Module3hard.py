data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(summa):
    total = 0
    for number in summa:
        if isinstance(number, list | tuple | set):
            total += calculate_structure_sum(number)
        elif isinstance(number, dict):
            for i in number:
                total += len(i)
            total += sum(number.values())
        elif isinstance(number, int):
            total += number
        elif isinstance(number, str):
            total += len(number)

    return total

result = calculate_structure_sum(data_structure)
print(result)
