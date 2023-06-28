import os # operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
    print('yeah! I found the file.')
    with open('products.csv', 'r', encoding= 'utf-8') as f:
    	for line in f:
    		if 'name, price' in line:
    			continue #進入下一輪迴圈
    		product, cost = line.strip().split(',')
    		products.append([product, cost])
    print(products)
else:
	print('I cannot find the file.')

#讓使用者輸入
while True:
	name = input('Please enter the product name: ')
	if name == 'q':
		break
	price = input('Please enter the product price: ')
	products.append([name, price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], 'price is', p[1])

#寫入檔案
with open('products.csv', 'w', encoding= 'utf-8') as f:
	f.write('name, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')