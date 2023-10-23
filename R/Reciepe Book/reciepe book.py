class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {
            "ingredients": ingredients,
            "instructions": instructions
        }

    def get_recipe(self, name):
        return self.recipes.get(name)

    def list_recipes(self):
        return list(self.recipes.keys())

    def delete_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]

# Example usage:
if __name__ == "__main__":
    recipe_book = RecipeBook()

    while True:
        print("1. Add Recipe")
        print("2. View Recipe")
        print("3. List Recipes")
        print("4. Delete Recipe")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions: ")
            recipe_book.add_recipe(name, ingredients, instructions)
            print("Recipe added.")
        elif choice == "2":
            name = input("Enter recipe name: ")
            recipe = recipe_book.get_recipe(name)
            if recipe:
                print(f"Recipe: {name}")
                print(f"Ingredients: {', '.join(recipe['ingredients'])}")
                print(f"Instructions: {recipe['instructions']}")
            else:
                print(f"Recipe '{name}' not found.")
        elif choice == "3":
            recipes = recipe_book.list_recipes()
            if recipes:
                print("Recipes:")
                for recipe_name in recipes:
                    print(recipe_name)
            else:
                print("No recipes found.")
        elif choice == "4":
            name = input("Enter recipe name to delete: ")
            recipe_book.delete_recipe(name)
            print(f"Recipe '{name}' deleted.")
        elif choice == "5":
            break
