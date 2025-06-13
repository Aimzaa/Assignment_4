def mad_libs():
    print("Let\'s play Mad Libs! fill in the blanks with your own words.")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adj = input("Gice me a funny adjective: ")
    random_obj = input("Give me a random object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")
    story = f'''
Once upon a time, there was a {funny_adj} {name} who lived in
{place}. One day, {name} was walking down the street when {name} saw a
{random_obj} lying on the ground. {name} picked it up and started to
{action_verb} it. Suddenly, a {animal} appeared out of nowhere and
started to {action_verb} {name}. {name} was so surprised that {name}
started to {action_verb} and shout "{funny_exclamation}"!'''
    
    print("\n Here is your Mad Lib story: ")
    print(story)

if __name__ == "__main__":
    mad_libs()