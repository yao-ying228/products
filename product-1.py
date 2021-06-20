products = []
while True:
    name = input('商品名稱 : ')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    p = [name,price]       
    products.append(p)
print(products)



