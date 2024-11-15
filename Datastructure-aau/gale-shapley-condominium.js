#!/usr/bin/node

/**
 * Dataset: Condominium Assignment Problem (Using Gale-Shapley Algorithm)
 *
 * **Description**: 
 * This dataset represents a list of condominium apartments and their preferences for residents, as well as the preferences of each resident for apartments.
 * The problem can be solved using the Gale-Shapley algorithm, which finds a stable assignment between residents and apartments based on mutual preferences.
 * 
 * **Key Entities**:
 * - **Residents**: Individuals who are looking to be assigned to apartments. Their preferences for apartments are listed in `resident_preferences`.
 * - **Condominiums (Apartments)**: Apartments in different condominiums, each with a block and room number (e.g., `Gerji-B1-101`), are listed in `condominium_preferences`.
 * 
 * **Data Structure**:
 * 1. **resident_preferences**: An object where keys are resident names, and the values are arrays of apartment names sorted by preference (highest to lowest).
 * 2. **condominium_preferences**: An object where keys are apartment names (formatted as `Condominium-B{block}-room`), and the values are arrays of resident names sorted by preference (highest to lowest).
 * 
 * **Problem Statement**:
 * - Each resident wants to be assigned to an apartment they prefer, and each apartment has a ranking of preferred residents.
 * - Use the Gale-Shapley algorithm to find a stable matching where no resident and apartment prefer each other over their current assignments.
 * 
 * **Example Use**:
 * - The Gale-Shapley algorithm is commonly used in matching problems like the stable marriage problem, where both parties have preferences for each other.
 * - In this scenario, the algorithm ensures that each resident gets an apartment and no resident and apartment prefer each other more than their assigned pair.
 * 
 * **Dataset**:
 * - 6 condominiums with 3 apartments each.
 * - 6 residents with ranked preferences for apartments.
 */

// Residents' preferences for specific apartments in condominiums



const condominium_preferences = {
    'Gerji-B1-101': ['Biruk', 'Abebe', 'Chaltu', 'Desta', 'Kebede', 'Girma'],  
    'Gerji-B1-102': ['Abebe', 'Biruk', 'Chaltu', 'Desta', 'Kebede', 'Girma'],
    'Jemo-B10-101': ['Abebe', 'Biruk', 'Chaltu', 'Desta', 'Kebede', 'Girma'],
    'Jemo-B10-102': ['Abebe', 'Biruk', 'Desta', 'Chaltu', 'Kebede', 'Girma'],  
    'Lafto-B3-301': ['Chaltu', 'Desta', 'Biruk', 'Abebe', 'Kebede', 'Girma'],  
    'Lafto-B3-302': ['Desta', 'Chaltu', 'Biruk', 'Abebe', 'Kebede', 'Girma']
    }

const resident_preferences = {
    'Abebe': ['Lafto-B3-302', 'Jemo-B10-101', 'Gerji-B1-102', 'Gerji-B1-101', 'Jemo-B10-102', 'Lafto-B3-301'],
    'Biruk': ['Jemo-B10-101', 'Gerji-B1-102', 'Jemo-B10-102', 'Lafto-B3-302', 'Gerji-B1-101', 'Lafto-B3-301'],
    'Chaltu': ['Gerji-B1-101', 'Lafto-B3-301', 'Jemo-B10-101', 'Gerji-B1-102','Lafto-B3-302', 'Jemo-B10-102'],
    'Desta': ['Lafto-B3-301', 'Jemo-B10-102', 'Lafto-B3-301', 'Gerji-B1-102', 'Jemo-B10-101','Gerji-B1-101'],
    'Girma': ['Lafto-B3-301', 'Jemo-B10-101', 'Gerji-B1-102', 'Lafto-B3-302', 'Gerji-B1-101', 'Jemo-B10-102'],
    'Kebede': ['Lafto-B3-301', 'Gerji-B1-102', 'Jemo-B10-101', 'Lafto-B3-302', 'Gerji-B1-101', 'Jemo-B10-102'],
    }
// Object.fromEntries([[]])

let free_condominum = Object.entries(condominium_preferences).map(condo => condo[0])
let condo_assigned_resident = Object.fromEntries(Object.entries(condominium_preferences).map(condo => [condo[0], 0]))
let resident_condo_choice = Object.fromEntries(Object.entries(resident_preferences).map(resident => [resident[0], null]))

console.log(condo_assigned_resident)
console.log(resident_condo_choice)
// console.log(condo_resident)

while(free_condominum != 0) {
    const condo = free_condominum.shift();
    const resident = condominium_preferences[condo][condo_assigned_resident[condo]];
    condo_assigned_resident[condo] += 1;
    current_condo = resident_condo_choice[resident];

    if (resident_condo_choice[resident] == null) {
        resident_condo_choice[resident] = condo
    } else {
        if (resident_preferences[resident].indexOf(condo) < resident_preferences[resident].indexOf(current_condo)) {
            resident_condo_choice[resident] = condo;
            free_condominum.push(current_condo);
        }
        if (resident_preferences[resident].indexOf(condo)   >  resident_preferences[resident].indexOf(current_condo)) {
            free_condominum.push(condo)
        }
    }
    // condo_assigned_resident[]


    // console.log(`removed ${condo} at index ${free_condominum.indexOf(condo)}`);

}
console.log(resident_condo_choice)

// const resident_preferences = {
//     'Abebe': ['Jemo-B10-102', 'Gerji-B1-101', 'Summit-B2-503', 'Megenagna-B5-202', 'Bole Bulbula-B7-401', 'Lafto-B3-301'],
//     'Biruk': ['Gerji-B1-103', 'Summit-B2-502', 'Bole Bulbula-B7-403', 'Jemo-B10-101', 'Megenagna-B5-203', 'Lafto-B3-303'],
//     'Chaltu': ['Summit-B2-501', 'Gerji-B1-102', 'Megenagna-B5-202', 'Jemo-B10-103', 'Lafto-B3-302', 'Bole Bulbula-B7-402'],
//     'Desta': ['Lafto-B3-303', 'Summit-B2-501', 'Gerji-B1-101', 'Bole Bulbula-B7-402', 'Jemo-B10-101', 'Megenagna-B5-201'],
//     'Elias': ['Megenagna-B5-201', 'Gerji-B1-102', 'Jemo-B10-102', 'Bole Bulbula-B7-401', 'Summit-B2-503', 'Lafto-B3-301'],
//     'Fikre': ['Bole Bulbula-B7-403', 'Jemo-B10-103', 'Lafto-B3-302', 'Gerji-B1-103', 'Megenagna-B5-203', 'Summit-B2-502']
// };

// // Condominiums' preferences for residents
// const condominium_preferences = {
//     'Gerji-B1-101': ['Biruk', 'Abebe', 'Chaltu', 'Elias', 'Desta', 'Fikre'],
//     'Gerji-B1-102': ['Abebe', 'Chaltu', 'Desta', 'Fikre', 'Elias', 'Biruk'],
//     'Gerji-B1-103': ['Chaltu', 'Elias', 'Fikre', 'Abebe', 'Biruk', 'Desta'],
//     'Jemo-B10-101': ['Desta', 'Biruk', 'Chaltu', 'Abebe', 'Fikre', 'Elias'],
//     'Jemo-B10-102': ['Abebe', 'Elias', 'Biruk', 'Chaltu', 'Desta', 'Fikre'],
//     'Jemo-B10-103': ['Fikre', 'Desta', 'Chaltu', 'Elias', 'Biruk', 'Abebe'],
//     'Megenagna-B5-201': ['Elias', 'Biruk', 'Abebe', 'Fikre', 'Desta', 'Chaltu'],
//     'Megenagna-B5-202': ['Chaltu', 'Desta', 'Fikre', 'Abebe', 'Elias', 'Biruk'],
//     'Megenagna-B5-203': ['Fikre', 'Chaltu', 'Abebe', 'Desta', 'Elias', 'Biruk'],
//     'Lafto-B3-301': ['Abebe', 'Elias', 'Biruk', 'Chaltu', 'Fikre', 'Desta'],
//     'Lafto-B3-302': ['Fikre', 'Chaltu', 'Desta', 'Biruk', 'Abebe', 'Elias'],
//     'Lafto-B3-303': ['Desta', 'Abebe', 'Elias', 'Fikre', 'Chaltu', 'Biruk'],
//     'Bole Bulbula-B7-401': ['Chaltu', 'Fikre', 'Desta', 'Abebe', 'Biruk', 'Elias'],
//     'Bole Bulbula-B7-402': ['Desta', 'Chaltu', 'Biruk', 'Abebe', 'Elias', 'Fikre'],
//     'Bole Bulbula-B7-403': ['Fikre', 'Biruk', 'Desta', 'Abebe', 'Chaltu', 'Elias'],
//     'Summit-B2-501': ['Biruk', 'Chaltu', 'Elias', 'Desta', 'Abebe', 'Fikre'],
//     'Summit-B2-502': ['Chaltu', 'Fikre', 'Desta', 'Biruk', 'Abebe', 'Elias'],
//     'Summit-B2-503': ['Elias', 'Abebe', 'Biruk', 'Chaltu', 'Desta', 'Fikre']
// };


