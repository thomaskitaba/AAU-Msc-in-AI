#!/usr/bin/python3
# """ Gale-Shapley Algorithm Implementation
# Parameters:
# - m (dict): A dictionary where each key is a man and the value is a list of women in preference order.
# - w (dict): A dictionary where each key is a woman and the value is a list of men in preference order.
# """


def galeShapleyMenPropose(m, w):
    "gale shapley algorithm"
    free_men = [key for key in m.keys()]
    women_partner = {woman: None for woman in w}
    man_next_proposal = {man: 0 for man in m}
    # print(free_men)
    # print(women_partner)
    # print(man_next_proposal)
    
    while(free_men):
        man = free_men.pop(0)
        woman = m[man][man_next_proposal[man]]
        man_next_proposal[man] += 1
        current_partner = women_partner[woman]
        if (current_partner == None):
            women_partner == man
            
        else:
            
            if (w[woman].index(man) < w[woman].index(current_partner)):
                women_partner[woman] = man
                free_men.append(current_partner)
            if (w[woman].index(man) > w[woman].index(current_partner)):
                free_men.append(man)
        
    print(f"Men Propose: {[(women, man) for women, men in women_partner.items()]}")
    
def galeShapleyWomenPropose(m, w):
    free_women = list(woman for woman in w)
    men_partner = {man: None for man in m}
    woman_next_proposal = {woman: 0 for woman in w}
    
    # print(free_women)
    # print(men_partner)
    # print(woman_next_proposal)
    
    while(free_women):
        woman = free_women.pop(0)
        woman_next_proposal[woman] += 1
        man = w[woman][woman_next_proposal[woman]]
        current_partner = men_partner[man]
        
        if (current_partner == None):
            men_partner[man] = woman
        else:
            if (m[man].index(woman) < m[man].index(current_partner)):
                men_partner[man] = woman
                free_women.append(current_partner)
            if (m[man].index(woman) > m[man].index(current_partner)):
                free_women.append(woman)
    
    print(f"Women Propose: {[(man, woman) for man, woman in men_partner.items()]}")
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
    galeShapleyWomenPropose(men_preferences, women_preferences)