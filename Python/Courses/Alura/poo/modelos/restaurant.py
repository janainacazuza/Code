class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f"{'Name'} | {'Category'} | {'Status'}")
        for restaurant in cls.restaurants:
            print(f'{restaurant._name} | {restaurant._category} | {restaurant.active}')

       
    @property
    def active(self):
        return 'Active' if self._active else 'Inactive'    
    
    def restaurant_status(self):
        self._active = not self._active
