import random

"""
    import random library
    create a list of words []
    
    """


def main():

    # Determine each parameter
    # parameter 1 for single and parameter 2 for plural
    single_quantity = 1
    plural_quantity = 2
    past_tense = "past"
    present_tense = "present"
    future_tense = "future"
    adjective = ""

    # creating 6 differents setences

    first_setence = f"{get_determiner(single_quantity).capitalize()}\
    {get_noun(single_quantity)} {get_verb(single_quantity, past_tense)}\
    {get_adjective(adjective)} {get_prepositional_phrase(single_quantity)}"
    
    second_setence = f"{get_determiner(single_quantity).capitalize()}\
    {get_noun(single_quantity)} {get_verb(single_quantity, present_tense)}\
    {get_adjective(adjective)} {get_prepositional_phrase(single_quantity)}"
    
    third_setence = f"{get_determiner(single_quantity).capitalize()}\
    {get_noun(single_quantity)} {get_verb(single_quantity, future_tense)}\
    {get_adjective(adjective)} {get_prepositional_phrase(single_quantity)}"
    
    fourth_setence = f"{get_determiner(plural_quantity).capitalize()}\
    {get_noun(plural_quantity)} {get_verb(plural_quantity, past_tense)}\
    {get_adjective(adjective)}  {get_prepositional_phrase(plural_quantity)}"
    
    fiveth_setence = f"{get_determiner(plural_quantity).capitalize()}\
    {get_noun(plural_quantity)} {get_verb(plural_quantity, present_tense)}\
    {get_adjective(adjective)}  {get_prepositional_phrase(plural_quantity)}"
    
    sixth_setence = f"{get_determiner(plural_quantity).capitalize()} \
    {get_noun(plural_quantity)} {get_verb(plural_quantity, future_tense)}\
    {get_adjective(adjective)}  {get_prepositional_phrase(plural_quantity)}"

    # printing the setences

    print(f"{first_setence}")
    print(f"{second_setence}")
    print(f"{third_setence}")
    print(f"{fourth_setence}")
    print(f"{fiveth_setence}")
    print(f"{sixth_setence}")




def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase."""
    
    """ 1.Preposition
        2.Determiner
        3.Noun
    """

    prepositional_phrase = f"{get_preposition(0)} {get_determiner(quantity)} {get_noun(quantity)}"
    

    return prepositional_phrase

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    
    if quantity == 1:
        noun_list = ["bird", "boy", "car", "cat", "child",\
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        noun_list = ["birds", "boys", "cars", "cats", "children",\
        "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(noun_list)
    return noun
    
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past":
        verb_list = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verb_list = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verb_list = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    else:
        verb_list = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    verb = random.choice(verb_list)
    return verb

def get_preposition(preposition):
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]
    
    preposition = random.choice(prepositions) 

    return preposition

def get_adjective(adjective):

    adjectives = ["beautiful", "honest", "positive", "shy", "bald", "tall", "cool", "handsome", "poor", "rich"]

    adjective = random.choice(adjectives)

    return adjective


if __name__ == "__main__":
    main()
    