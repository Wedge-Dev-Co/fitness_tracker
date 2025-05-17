# This is a simple nutrition tracking program
# It allows the user to log exercise and nutrition data on a daily basis
# It also allows the user to view their progress over time


# ---- Nutrition Classes ----
# This class represents a food item
class food_item:
    def __init__(self, name, fats, carbs, protein):
        self.name = name
        self.fats = fats
        self.carbs = carbs
        self.protein = protein
        self.cals = (9*fats) + (4*carbs) + (4*protein)
        self.description = None
           

# This class represents a meal
class meal:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.food_items = []
        self.notes = None       

    def add_food_item(self, food_item):
        self.food_items.append(food_item)

    def remove_food_item(self, food_item):
        self.food_items.remove(food_item)
    
    def get_total_cals(self):
        total_cals = 0
        for item in self.food_items:
            total_cals += item.cals
        return total_cals
    
    def get_total_protein(self):
        total_protein = 0
        for item in self.food_items:
            total_protein += item.protein
        return total_protein

    def get_total_fats(self):
        total_fats = 0
        for item in self.food_items:
            total_fats += item.fats
        return total_fats
    
    def get_total_carbs(self):
        total_carbs = 0
        for item in self.food_items:
            total_carbs += item.carbs
        return total_carbs
    

# This class represents a daily nutrition log
class nutrition_log:
    def __init__(self):
        self.meals = []
        self.other_nutrition = None
        self.comments = None

    def add_meal(self, meal):
        self.meals.append(meal)

    def remove_meal(self, meal):
        self.meals.remove(meal)
    
    def get_total_cals(self):
        total_cals = 0
        for meal in self.meals:
            total_cals += meal.get_total_cals()
        return total_cals
    
    def get_total_protein(self):
        total_protein = 0
        for meal in self.meals:
            total_protein += meal.get_total_protein()
        return total_protein
    
    def get_total_fats(self):
        total_fats = 0
        for meal in self.meals:
            total_fats += meal.get_total_fats()
        return total_fats
    
    def get_total_carbs(self):
        total_carbs = 0
        for meal in self.meals:
            total_carbs += meal.get_total_carbs()
        return total_carbs


# ---- Exercise Classes ----
# This class represents an exercise
class exercise:
    def __init__(self):
        pass


# This class represents a workout
class workout:
    def __init__(self):
        pass


# This class represents a daily workout log
class activity_log:
    def __init__(self):
        pass


# ---- Daily Entry Class ----
# This class represents a daily exercise and nutrition entry
class daily_entry:
    def __init__(self):
        pass
