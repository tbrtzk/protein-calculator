class Food:
    def __init__(self, name, protein):
        self.name = name
        self.protein = protein
        self.quantity = 0

    def get_protein_per_portion(self):
        protein_per_portion = self.quantity * self.protein / 100
        return protein_per_portion




