##MadLibs game
##A word game where you fill in the blanks to create a funny story.
## --- Space Odyssey Mad Libs ---

# Collecting the ingredients for our story
hero_name = input("Enter a name: ")
planet = input("Enter a fictional planet name: ")
adjective1 = input("Enter a 'gross' adjective: ")
food = input("Enter a type of food: ")
verb_ing = input("Enter a verb ending in 'ing': ")
superpower = input("Enter a superpower: ")
sound_effect = input("Enter a funny sound effect: ")
adjective2 = input("Enter a 'happy' adjective: ")

# The Grand Reveal
print("\n--- THE MISSION LOG ---")
print(f"Captain {hero_name} touched down on the planet {planet}.")
print(f"The ground felt {adjective1}, and the air smelled like {food}.")
print(f"Suddenly, a group of aliens started {verb_ing} toward the ship!")
print(f"Thinking fast, {hero_name} used {superpower} to save the day.")
print(f"The aliens let out a loud '{sound_effect}!' and ran away.")
print(f"It was a {adjective2} day for the Galactic Federation.")