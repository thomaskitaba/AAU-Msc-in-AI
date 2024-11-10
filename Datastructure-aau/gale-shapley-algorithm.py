#!/usr/bin/python3
""" Gale-Shapley Algorithm Implementation
Parameters:
- men_preferences (dict): A dictionary where each key is a man and the value is a list of women in preference order.
- women_preferences (dict): A dictionary where each key is a woman and the value is a list of men in preference order.
"""




def galeShapleyMenPropose(m, w):
    free_men = [key for key in m.keys()]
    
    print(free_men)
    
    # while(free_men):
        

if __name__ == "__main__":

    men_preferences = {
        'Abebe': ['Tigist', 'Meklit', 'Lensa'],
        'Bekele': ['Meklit', 'Tigist', 'Lensa'],
        'Chala': ['Tigist', 'Meklit', 'Lensa']
    }

    women_preferences = {
        'Tigist': ['Bekele', 'Abebe', 'Chala'],
        'Meklit': ['Abebe', 'Bekele', 'Chala'],
        'Lensa': ['Abebe', 'Bekele', 'Chala']
    }
    galeShapleyMenPropose(men_preferences, women_preferences)
