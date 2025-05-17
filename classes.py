# ---- Nutrition Classes ----

# This class represents a food item
# Each food item has a name and counts of proteins, fats, carbs, and calories
# It also has a description
class food_item:
    def __init__(self, name, protein, fats, carbs):
        self.name = name
        self.description = None
        self.protein = protein
        self.fats = fats
        self.carbs = carbs
        self.cals = (9*self.fats) + (4*self.carbs) + (4*self.protein)
                   

# This class represents a meal
# Each meal is a collection of food items
# It also contains other meal data and comments
class meal:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.food_items = []
        self.comments = None       

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
# Each daily nutrition log is a collection of meals
# It also contains other nutrition data and comments
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

# This class represents a cardio exercise
# Each cardio exercise has a name, duration, distance, and calories burned
# It also has a description
class cardio_exercise:
    def __init__(self, name, duration, distance, calories_burned):
        self.name = name
        self.duration = duration
        self.distance = distance
        self.calories_burned = calories_burned
        self.description = None

        
# This class represents a resistance exercise
# Each resistance exercise has a name, sets, reps, and weight
# It also has a volume (sets * reps * weight) and a description
class resistance_exercise:
    def __init__(self, name, sets, reps, weight):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.volume = self.sets * self.reps * self.weight
        self.description = None


# This class represents a workout
# Each workout is a collection of exercises
# It also contains other workout data and comments
class workout:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.exercises = []
        self.other_exercises = None
        self.comments = None

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def remove_exercise(self, exercise):
        self.exercises.remove(exercise)

    def get_duration(self):
        duration = self.end_time - self.start_time
        return duration

    
# This class represents a daily activity log
# Each daily activity log is a collection of workouts
# It also contains other activity data and comments
class activity_log:
    def __init__(self):
        self.workouts = []
        self.other_activities = None
        self.comments = None

    def add_workout(self, workout):
        self.workouts.append(workout)

    def remove_workout(self, workout):
        self.workouts.remove(workout)

    def get_total_duration(self):
        total_duration = 0
        for workout in self.workouts:
            total_duration += workout.get_duration()
        return total_duration


# ---- Daily Entry Class ----

# This class represents a daily exercise and nutrition entry
# Each daily entry has a date, day of the week, weight, and logs for nutrition and activity
# It also has comments
class daily_entry:
    def __init__(self, date, day_of_week, weight):
        self.date = date
        self.day_of_week = day_of_week
        self.weight = weight
        self.nutrition_log = nutrition_log()
        self.activity_log = activity_log()
        self.comments = None

