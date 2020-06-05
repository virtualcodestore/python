class Restaurant(object):
    """A simple attempt to model a Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        """Initialize name and age attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe details of the restaurant"""
        print("The restaurant name is :" + self.restaurant_name.title())
        print("The Cuisine type is: " + self.cuisine_type.title())
    def open_restaurant(self):
        """Personlised greeting to the user"""
        print(self.restaurant_name.title() + " is open.")


