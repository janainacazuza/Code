from evaluation import Evaluation
class Restaurant:
    """Class to represent a restaurant."""
    restaurants = []

    def __init__(self, name, category):
        """Constructor method.
        Inputs:
            name: str
            category: str
        """
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._evaluation = []
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        """Method to represent the class object."""
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        """Class method to list all restaurants."""
        print(f"{'Name'} | {'Category'} | {'Status'} | {'Rating'}")
        for restaurant in cls.restaurants:
            print(f'{restaurant._name} | {restaurant._category} | {restaurant.active} | {restaurant.average_score}')

       
    @property
    def active(self):
        """Property to return the status of the restaurant."""
        return 'Active' if self._active else 'Inactive'    
    
    def restaurant_status(self):
        """Method to change the status of the restaurant."""
        self._active = not self._active

    def add_evaluation(self, client, score):
        """Method to add an evaluation to the restaurant.
        Inputs:
            client: str
            score: int
        """
        if 0 < score < 5:
            evaluation = Evaluation(client, score)
            self._evaluation.append(evaluation)
        else:
            print('Score must be between 1 and 5')

    @property
    def average_score(self):
        """Property to return the average score of the restaurant."""
        if not self._evaluation:
            return ""
        sum_scores = sum([evaluation._score for evaluation in self._evaluation])
        score_number = len(self._evaluation)
        average = round(sum_scores / score_number, 1)
        return average 