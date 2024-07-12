# Task 1 
class Product:
    def __init__(self, name, price, quantity):
        """
        Initializes a Product with name, price, and quantity
        """
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def read(self):
         print(f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}')
        
class Book(Product):
    def __init__(self, name, price, quantity, author):
        """
        Initializes a Book, inheriting from Product, with additional author information
        """
        super().__init__(name, price, quantity)
        self.author = author
        
    def read(self):
        """
        Prints information about the book, including its name, price, quantity, and author
        """
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
   
   
ptoduct_1 = Product('Notebook', 10000, 10)
ptoduct_1.read()
    
book_1 = Book('English', 23.45, 50, 'Mitchel')
book_1.read()
        
        
# Task 2
class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu
        
    def __str__(self):
        return f"Restaurant: {self.name}, Cuisine: {self.cuisine}, Menu: {self.menu}"
    
    def is_dish_available(self, dish_name, quantity):
        """
        Checks if a dish is available in the menu and if the requested quantity is available
        Returns:
            bool: True if the dish is available in sufficient quantity, False otherwise
        """
        dish_info = self.menu.get(dish_name)
        return dish_info and dish_info['quantity'] >= quantity
    
class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
        
    def order(self, dish_name, quantity):
        """
        Orders a dish in the specified quantity and updates the menu accordingly
        Returns:
            float or str: The total cost of the order if successful, or an error message if the order cannot be fulfilled
        """
        if not self.is_dish_available(dish_name, quantity):
            return f"Requested quantity not available or dish '{dish_name}' not found"
        
        dish_info = self.menu[dish_name]
        current_quantity = dish_info['quantity']
        
        if quantity > current_quantity:
            return f"Requested quantity not available for '{dish_name}'"
        
        total_cost = dish_info['price'] * quantity
        dish_info['quantity'] -= quantity
        
        return total_cost
        
    
menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))
print(mc.order('burger', 15))
print(mc.order('soup', 5))

        
 