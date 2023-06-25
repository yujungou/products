products = []
while True:
	name = input('Please enter the product name: ')
	if name == 'q':
		break
	price = input('Please enter the product price: ')
	p = [name, price]
	products.append(p)
print(products)