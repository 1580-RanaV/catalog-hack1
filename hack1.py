class virtual_shopping_mall:
    def __init__(self):
        # initialize the products available in the mall
        # each product has a name, a set of available sizes with description, and a price
        self.products = {
            "1": {"name": "tshirt", "sizes": {"s": "small", "m": "medium", "l": "large"}, "price": 20},
            "2": {"name": "jeans", "sizes": {"30": "30 inches", "32": "32 inches", "34": "34 inches"}, "price": 40},
            "3": {"name": "jacket", "sizes": {"m": "medium", "l": "large", "xl": "extra large"}, "price": 60}
        }


    def display_products(self):
        # display a welcome message and products list
        print("welcome to the virtual shopping mall!\n")
        print("available products:")
        for key, product in self.products.items():
            # format the sizes and display the product details
            sizes = ', '.join([f"{size} ({desc})" for size, desc in product["sizes"].items()])
            print(f"{key}. {product['name']} - sizes: {sizes} - price: ${product['price']}")


    def try_on(self, product_id, size):
        #checking if the product and size are available
        product = self.products.get(product_id)
        if product:
            size_desc = product["sizes"].get(size)
            if size_desc:
                # output the result of trying on the product
                print(f"\ntrying on {product['name']} in size {size} ({size_desc})...")
                print(f"perfect fit! the {product['name']} looks great on you!\n")
            else:
                print(f"\nsorry, size {size} is not available for {product['name']}.\n")
        else:
            print("\ninvalid product selection.\n")

    def run(self):
        # main loop to keep the program running until the user decides to quit
        while True:
            self.display_products()
            choice = input("enter the product number to try on or 'q' to quit: ")
            if choice.lower() == 'q':
                print("\nthank you for visiting the virtual shopping mall! see you!")
                break
            size = input("enter your size: ")
            self.try_on(choice, size)

if __name__ == "__main__":
    mall = virtual_shopping_mall()
    mall.run()
