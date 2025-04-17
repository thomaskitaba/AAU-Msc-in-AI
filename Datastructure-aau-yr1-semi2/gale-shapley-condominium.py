#!/usr/bin/python3
# /**
#  * Dataset: Condominium Assignment Problem (Using Gale-Shapley Algorithm)
#  *
#  * **Description**: 
#  * This dataset represents a list of condominium apartments and their preferences for residents, as well as the preferences of each resident for apartments.
#  * The problem can be solved using the Gale-Shapley algorithm, which finds a stable assignment between residents and apartments based on mutual preferences.
#  * 
#  * **Key Entities**:
#  * - **Residents**: Individuals who are looking to be assigned to apartments. Their preferences for apartments are listed in `resident_preferences`.
#  * - **Condominiums (Apartments)**: Apartments in different condominiums, each with a block and room number (e.g., `Gerji-B1-101`), are listed in `condominium_preferences`.
#  * 
#  * **Data Structure**:
#  * 1. **resident_preferences**: An object where keys are resident names, and the values are arrays of apartment names sorted by preference (highest to lowest).
#  * 2. **condominium_preferences**: An object where keys are apartment names (formatted as `Condominium-B{block}-room`), and the values are arrays of resident names sorted by preference (highest to lowest).
#  * 
#  * **Problem Statement**:
#  * - Each resident wants to be assigned to an apartment they prefer, and each apartment has a ranking of preferred residents.
#  * - Use the Gale-Shapley algorithm to find a stable matching where no resident and apartment prefer each other over their current assignments.
#  * 
#  * **Example Use**:
#  * - The Gale-Shapley algorithm is commonly used in matching problems like the stable marriage problem, where both parties have preferences for each other.
#  * - In this scenario, the algorithm ensures that each resident gets an apartment and no resident and apartment prefer each other more than their assigned pair.
#  * 
#  * **Dataset**:
#  * - 6 condominiums with 3 apartments each.
#  * - 6 residents with ranked preferences for apartments.
#  */
# RESIDENTS CHOSE

def galeShapleyCondominium(r, c):
    unassigned_residents = [resident for resident in r]
    print(unassigned_residents)
    residents_next_preference = {resident: 0 for resident in r}
    print(residents_next_preference)
    condominium_assigned = {condominium: None for condominium in c}
    print(condominium_assigned)
    print("=============================")
    while(unassigned_residents):
        resident = unassigned_residents.pop(0)
        # print(f"poped resident value: {resident}")
        # residents prefered condominium
        condominium = r[resident][residents_next_preference[resident]]
        # print(f"residnts preference: {condominium}")

        residents_next_preference[resident] += 1
        # name of resident within the condominium
        current_assignment = condominium_assigned[condominium]
        # print(f"[condominium, redient] {condominium, current_assignment}")
        
        if (condominium_assigned[condominium] == None):
            condominium_assigned[condominium] = resident
            # print(f" after assignment {condominium_assigned}")
        else:
            if (c[condominium].index(resident) < c[condominium].index(current_assignment)):
                condominium_assigned[condominium] = resident
                unassigned_residents.append(current_assignment)
            if (c[condominium].index(resident)) > c[condominium].index(current_assignment):
                unassigned_residents.append(resident)

    # print([(resident, condominium) for resident, condominium in condominium_assigned.items()])
    print("Stable case")
    for key, value in condominium_assigned.items():
        print([key, value])
    
    # Algorithm Analysis
    # Best Case     O(n)
    # Worest Case  o(n^2)

if __name__ == "__main__":
        
   
    condominium_preferences = {
    'Gerji-B1-101': ['Biruk', 'Abebe', 'Chaltu', 'Desta', 'Kebede', 'Girma'],  
    'Gerji-B1-102': ['Abebe', 'Biruk', 'Chaltu', 'Desta', 'Kebede', 'Girma'],
    'Jemo-B10-102': ['Abebe', 'Biruk', 'Desta', 'Chaltu', 'Kebede', 'Girma'],  
    'Lafto-B3-301': ['Chaltu', 'Desta', 'Biruk', 'Abebe', 'Kebede', 'Girma'],  
    'Jemo-B10-101': ['Abebe', 'Biruk', 'Chaltu', 'Desta', 'Kebede', 'Girma'],
    'Lafto-B3-302': ['Desta', 'Chaltu', 'Biruk', 'Abebe', 'Kebede', 'Girma']
    }

    
    resident_preferences = {
    'Abebe': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301'],
    'Biruk': ['Jemo-B10-101', 'Gerji-B1-102', 'Jemo-B10-102', 'Lafto-B3-302', 'Gerji-B1-101', 'Lafto-B3-301'],
    'Chaltu': ['Gerji-B1-101', 'Lafto-B3-301', 'Jemo-B10-101', 'Gerji-B1-102','Lafto-B3-302', 'Jemo-B10-102'],
    'Desta': ['Lafto-B3-301', 'Jemo-B10-102', 'Lafto-B3-301', 'Gerji-B1-102', 'Jemo-B10-101','Gerji-B1-101'],
    'Girma': ['Lafto-B3-301', 'Jemo-B10-101', 'Gerji-B1-102', 'Lafto-B3-302', 'Gerji-B1-101', 'Jemo-B10-102'],
    'Kebede': ['Lafto-B3-301', 'Gerji-B1-102', 'Jemo-B10-101', 'Lafto-B3-302', 'Gerji-B1-101', 'Jemo-B10-102'],
    }
    galeShapleyCondominium(resident_preferences, condominium_preferences)
    #  resident_preferences = {
    # 'Abebe': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301'],
    # 'Biruk': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301'],
    # 'Chaltu': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301'],
    # 'Desta': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301'],
    # 'Girma': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301'],
    # 'Kebede': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301']
    # }