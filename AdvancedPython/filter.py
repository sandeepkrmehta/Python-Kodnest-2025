li = list(eval(input('Enter comma seperated element: ')))
print(f'Original List: {li}')

def even(ele):
    if ele % 2 == 0:
        return ele

even_li = list(filter(even, li))
print(f"Even List: {even_li}")
