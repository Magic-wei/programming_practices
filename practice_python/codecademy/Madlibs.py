"""
In this project, we'll use Python to write a Mad Libs word game! Mad Libs have short stories with blank spaces that a player can fill in. The result is usually funny (or strange).
"""

# The template for the story

print("Let's begin with Mad Libs!")
name = input("Enter a name: ")
print("Next, you are supposed to input three adjectives: ")
adj1 = input("The first adjective: ")
adj2 = input("The second adjective: ")
adj3 = input("The third adjective: ")

verb = input("Next, you should input one verb: ")

print("And two nouns, ")

noun1 = input("The first noun: ")
noun2 = input("The second noun: ")

print("Next, we'll arrive at the most interesting part...")
animal = input("Input a animal: ")
food = input("Input a food: ")
fruit = input("Input a fruit: ")
superhero = input("Input a superhero: ")
country = input("Input a country: ")
dessert = input("Input a dessert: ")
year = input("Input a year: ")

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." %(name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)

print(STORY)
