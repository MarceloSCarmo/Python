from sentences import get_determiner, get_noun, get_verb, \
    get_preposition, get_prepositional_phrase, get_adjective
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():

    single_nouns = ["bird", "boy", "car", "cat", "child",\
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(4):
        noun = get_noun(1)
        assert noun in single_nouns
    
    plural_noun = ["birds", "boys", "cars", "cats", "children",\
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):
        nouns = get_noun(2)
        assert nouns in plural_noun


def test_get_verb():

    past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(4):

        verb_past = get_verb(0,"past")
        assert verb_past in past

    
    present = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    present_plural = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    for _ in range(4):
        
        verb_single = get_verb(1,"present")
        assert verb_single in present

    for _ in range(4):

        verb_plural = get_verb(2,"present")
        assert verb_plural in present_plural
    
    future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    for _ in range(4):
        verb_future = get_verb(0,"future")
        assert verb_future in future


def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along",
            "around", "at", "before", "behind", "below",
            "beyond", "by", "despite", "except", "for",
            "from", "in", "into", "near", "of",
            "off", "on", "onto", "out", "over",
            "past", "to", "under", "with", "without"]

    for _ in range(4):
        preposition = get_preposition('')
        assert preposition in prepositions


def test_get_prepositional_phrase():

    """
    So you could write code in the test_get_prepositional_phrase function that 
    
    1.calls the get_prepositional_phrase function 
    2.calls the Python string split method to separate the returned phrase into a list of words 
    3.verifies that the length of the list is three
    
    In addition for each word in the list,
    you could write an assert statement that verifies that each word is the correct English part of speech."""

    #   quantity == 1

    for _ in range(4):
                
        prepositional_phrase = get_prepositional_phrase(1)

        prepositional_phrase.split(sep=' ', maxsplit=-1)

        assert prepositional_phrase
        
    #   quantity == 2
    
    for _ in range(4):
                
        prepositional_phrase = get_prepositional_phrase(2)

        prepositional_phrase.split(sep=' ', maxsplit=-1)

        assert prepositional_phrase



def test_get_adjective():

    adjectives = ["beautiful", "honest", "positive", "shy", "bald", "tall", "cool", "handsome", "poor", "rich"]

    for _ in range(4):
        adjective = get_adjective('')
        assert adjective in adjectives


pytest.main(["-v", "--tb=line", "-rN", __file__])