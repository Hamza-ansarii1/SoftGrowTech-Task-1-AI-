# Project : Recommendation System
# Tool : Python
# Benefit : Foundation for building AI-powered recommendation systems for movies, products, music, using machine learning later.

recommendation = {
    "python":["Macine learning","Data Science","Web Development"],
    "ai":["Deep learning","Computer Vision","NLP"],
    "movies":["inception","intersteller","The matrix"]
}

choice = input("Enter your interest: ").lower()

if choice in recommendation:
    print("Recommend itmes")

    for item in recommendation[choice]:
        print("-",item)
else:
    print("No recommendations available.")