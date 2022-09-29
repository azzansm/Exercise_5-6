# def fixed_profit():
#     burger = int(input('Enter burger selling price: '))
#     soda = int(input('Enter soda selling price: '))
#     combo = int(input('Enter combo meal selling price: '))
#     return (burger+soda-combo)
# print(f'The fixed price is ${fixed_profit():.2f}')

def point():
    px = int(input('Enter the point px: '))
    py = int(input('Enter the point py: '))
    qx = int(input('Enter the point qx: '))
    qy = int(input('Enter the point qy: '))
    x = qx-px
    y = qy-py
    r = (qx+x,qy+y)
    return (r)
print(f'The point r = {point()}')