products = []
while True:
    name = input('商品名稱 : ')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    
    p = []
    p.append(name)
    p.append(price)         #line 8-10 可簡化寫成: p[name,price] 
    products.append(p)
print(products)
print(products[2][1])


