# Predefined favorite foods for the hypothetical classmate
classmate_favorite_foods = {"pizza", "sushi", "tacos", "burger", "pasta"}

# Getting user's favorite foods
user_favorite_foods = set()  # Using a set to store user input and avoid duplicates

# Asking user for their favorite foods
user_favorite_foods.add(input("Enter your first favorite food: ").strip().lower())
user_favorite_foods.add(input("Enter your second favorite food: ").strip().lower())
user_favorite_foods.add(input("Enter your third favorite food: ").strip().lower())

# Comparing favorite foods
common_foods = user_favorite_foods.intersection(classmate_favorite_foods)

# Output results
if common_foods:
    print(f"Our common favorite food(s): {', '.join(common_foods)}")
else:
    print("We have no common favorite foods.")
