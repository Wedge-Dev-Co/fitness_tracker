def fats_to_cals(fats):
    return fats * 9
def carbs_to_cals(carbs):
    return carbs * 4
def protein_to_cals(protein):
    return protein * 4
def total_cals(fats, carbs, protein):
    return fats_to_cals(fats) + carbs_to_cals(carbs) + protein_to_cals(protein)

class food_item:
    def __init__(self, name, fats, carbs, protein):
        self.name = name
        self.fats = fats
        self.carbs = carbs
        self.protein = protein

    def __str__(self):
        return f"{self.name}: {self.fats}g fats, {self.carbs}g carbs, {self.protein}g protein"

    def __repr__(self):
        return f"food_item({self.name}, {self.fats}, {self.carbs}, {self.protein})"
    
    def __cals__(self):
        return total_cals(self.fats, self.carbs, self.protein)