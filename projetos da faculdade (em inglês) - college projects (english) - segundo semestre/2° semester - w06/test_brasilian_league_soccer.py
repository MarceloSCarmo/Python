from brasilian_league_soccer import teams_dictionary_file 
import pytest

TEAM_NAME_INDEX = 0
TEAM_MACTHES_INDEX = 1
TEAM_WINS_INDEX = 2
TEAM_DRAW_INDEX = 3
TEAM_DEFEAT_INDEX = 4

def test_teams_dictionary_file():
    """Verify that the read_dictionary function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the teams_dictionary_file and store the returned
    
    teams_dictionary = teams_dictionary_file()
    assert isinstance(teams_dictionary, list), \
        f" expected a list but found a {type(teams_dictionary)}"

    # Create a key function that will be used by the sorted method.
    by_name = lambda element: element[TEAM_NAME_INDEX]

    # Sort the teams_dictionary by the element names.
    teams_dictionary = sorted(teams_dictionary, key=by_name)

    # Check each item in the products dictionary.
    check_product(teams_dictionary, 'Fortaleza': ['Fortaleza', '20', '16', '1', '3'])
    check_product(teams_dictionary, 'Flamengo': ['Flamengo', '20', '10', '3', '7'])
    check_product(teams_dictionary, 'RB Bragantino': ['RB Bragantino', '20', '13', '3', '4'])
    check_product(teams_dictionary, 'Santos': ['Santos', '20', '11', '6', '3'])
    check_product(teams_dictionary, 'Corinthians': ['Corinthians', '20', '5', '10', '5'])
    check_product(teams_dictionary, 'Sao Paulo': ['Sao Paulo', '20', '5', '15', '0'])
    check_product(teams_dictionary, 'Fluminense': ['Fluminense', '20', '7', '3', '10'])
    check_product(teams_dictionary, 'Botafogo': ['Botafogo', '20', '8', '2', '10'])
    check_product(teams_dictionary, 'Atletico Mineiro': ['Atletico Mineiro', '20', '13', '5', '2'])
    check_product(teams_dictionary, 'Cruzeiro': ['Cruzeiro', '20', '11', '7', '2'])
    check_product(teams_dictionary, 'America Mineiro': ['America Mineiro', '20', '15', '3', '2'])
    check_product(teams_dictionary, 'Curitiba': ['Curitiba', '20', '2', '3', '15'])
    check_product(teams_dictionary, 'Athletico PR': ['Athletico PR', '20', '4', '4', '12'])
    check_product(teams_dictionary, 'Bahia': ['Bahia', '20', '5', '1', '14'])
    check_product(teams_dictionary, 'Palmeiras': ['Palmeiras', '20', '6', '3', '11'])
    check_product(teams_dictionary, 'Gremio': ['Gremio', '20', '1', '10', '9'])
    check_product(teams_dictionary, 'Internacional': ['Internacional', '20', '5', '3', '12'])
    check_product(teams_dictionary, 'Goias': ['Goias', '20', '12', '6', '2'])

