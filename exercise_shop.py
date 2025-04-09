
products= [
{"name": "Blush", "price":10},
{"name": "Lipstick", "price":90},
{"name": "Foundation", "price":20},
]

deliveries= [
    {"name": "National post", "fees":5},

    {"name": "DHL Express", "fees":10},
] 
# we do a for loop to display the products 
for index, product in enumerate(products):
   print(f"for {product["name"]} press {index}")
   # use a input to get user choice
   while True:
      user_product_index = int (input ("please enter the product number : \n"))
      try:
      user_product_index = int (user_product_index)

   
   # we need to check if the number is greater or equal than 0 and less than number of products
   
   if user_product_index >=0 and user_product_index < len(products):
      break
   else:
      print("This product does not exist")
      
      expect ValueError:
          print("Please enter only number")
      user_products = product[user_product_index]