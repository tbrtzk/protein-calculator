from food import Food


class ProteinCalculator:

    def __init__(self, food_list):
        self.food_bank = []
        for food in food_list:
            name = food["name"]
            protein = food["protein"]
            new_food = Food(name, protein)
            self.food_bank.append(new_food)

    def get_food(self):
        choice = input("Which food do you want to check?").lower()
        for food in self.food_bank:
            if food.name == choice:
                return food

    def get_quantity(self, food):
        return int(input(f"How much of {food.name} did you eat?"))

    def calculate(self):
        food = self.get_food()
        food.quantity = self.get_quantity(food)
        protein_per_portion = food.get_protein_per_portion()
        print(f"With this portion of {food.name} you ate {protein_per_portion}g of Protein")