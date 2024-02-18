class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, open):
        """
        Constructor method to initialize the Restaurant object with given attributes.
        
        Parameters:
            restaurant_name (str): The name of the restaurant.
            cuisine_type (str): The type of cuisine served.
            open (bool): Whether the restaurant is currently open or closed.
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open

    def describe_restaurant(self):
        """
        Method to describe the restaurant by printing its attributes.
        """
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Currently {'open' if self.open else 'closed'}")

    def is_open(self):
        """
        Method to check if the restaurant is currently open or closed and print the status.
        """
        print("Currently open" if self.open else "Currently closed")

# Creating an instance of the Restaurant class
restaurant1 = Restaurant("McDonalds", "Burgers", True)

# Calling methods to describe the restaurant and check if it's open
restaurant1.describe_restaurant()
restaurant1.is_open()
