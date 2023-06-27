#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if 'name, price' in line:
			continue #continue為暫停接下來步驟，進入下個迴圈
		product, cost = line.strip().split(',')
		products.append([product, cost])
print(products)

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

#
with open('products.csv', 'w', encoding= 'utf-8') as f:
	f.write('name, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')