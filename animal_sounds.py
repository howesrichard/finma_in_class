def make_dog_bark(preamble, bark_number, finish):
    dog_bark_string = preamble + str(bark_number) + finish
    return dog_bark_string

def make_animal_sound(animal, preamble, sound_number, finish):
    if animal == "dog":
        animal_sound_string = make_dog_bark(preamble, sound_number, finish)
    else:
        animal_sound_string = "the cat meowed " + str(sound_number) + finish
    return animal_sound_string