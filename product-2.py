import os #operating systeam

#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
    print('太棒了,找到檔案了')
    with open('products.csv' , 'r' , encoding = 'utf-8') as f :
        for line in f :
            if '商品 , 價格 ' in line :
                continue        
            name , price =line.strip().split(',')
            products.append([name , price])
    print(products)      
else:
    print('糟糕!檔案遺失了...')

#讓使用者輸入
while True:
    name = input('商品名稱 : ')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    price = int(price)
    products.append([name , price])
print(products)

#印出所有購買紀錄
for p in products :
	print(p[0] , '的價錢是' , p[1])

#將資料寫入
with open('products.csv' , 'w' , encoding ='utf-8') as f : 
    f.write('商品 , 價格 \n')
    for p in products :
        f.write(p[0] + ',' + str(p[1]) + '\n')


