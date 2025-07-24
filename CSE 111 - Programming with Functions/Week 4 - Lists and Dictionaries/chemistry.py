"""
- The lead chemist Mariana Cardoso has asked you to create a program with the 
following requirements:
    1. Ask the user for a chemical formula.
    2. Ask the user for the amount of the compound in grams (this is the sample_mass).
    3. Compute and display the molar mass.
    4. Compute and display the number of moles.
- Mariana has provided the following information:

    - A compound or molecule is described by a list of elements it contains. 
    - The element is identified by the element's symbol. 
    - If there is more than one atom of that element a number representing the number of 
    atoms in the compound will follow the element's symbol. Here are some examples.
        - H2O (water) has 2 Hydrogen atoms and 1 Oxygen atom.
        - C6H12O6 (glucose) has 6 Carbon atoms, 12 Hydrogen atoms, and 6 Oxygen atoms.

- To calculate the molar mass of a compound all you need to do is sum all of the weights 
of each atom in the compound.

- To calculate the number of moles in a sample use the following formula:
    - number_of_moles = sample_mass / molar_mass
"""
from formula import parse_formula


def make_periodic_table():
    """
    - Returns a dictionary object which contains all of the elements of the periodic table.
    - For each element the dictionary key should be the element's symbol.
    - The value contains a list where the first item in the list is the element's name and 
    the second item is the atomic mass.
    """
    periodic_table = {
        #symbol: [name, atomic_mass]
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        "Ar": ["Argon", 39.948],
        "As": ["Arsenic", 74.9216],
        "At": ["Astatine",210],
        "Au": ["Gold", 196.966569],
        "B":  ["Boron", 10.811],
        "Ba": ["Barium", 137.327],
        "Be": ["Beryllium", 9.012182],
        "Bi": ["Bismuth", 208.9804],
        "Br": ["Bromine", 79.904],
        "C": ["Carbon", 12.0107],
        "Ca": ["Calcium", 40.078],
        "Cd": ["Cadmium", 112.411],
        "Ce": ["Cerium", 140.116],
        "Cl": ["Chlorine", 35.453],
        "Co": ["Cobalt", 58.933195],
        "Cr": ["Chromium", 51.9961],
        "Cs": ["Cesium", 132.9054519],
        "Cu": ["Copper", 63.546],
        "Dy": ["Dysprosium", 162.5],
        "Er": ["Erbium", 167.259],
        "Eu": ["Europium", 151.964],
        "F": ["Fluorine", 18.9984032],
        "Fe": ["Iron", 55.845],
        "Fr": ["Francium", 223],
        "Ga": ["Gallium", 69.723],
        "Gd": ["Gadolinium", 157.25],
        "Ge": ["Germanium", 72.64],
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Hf": ["Hafnium", 178.49],
        "Hg": ["Mercury", 200.59],
        "Ho": ["Holmium", 164.93032],
        "I": ["Iodine", 126.90447],
        "In": ["Indium", 114.818],
        "Ir": ["Iridium", 192.217],
        "K": ["Potassium", 39.0983],
        "Kr": ["Krypton", 83.798],
        "La": ["Lanthanum", 138.90547],
        "Li": ["Lithium", 6.941],
        "Lu": ["Lutetium", 174.9668],
        "Mg": ["Magnesium", 24.305],
        "Mn": ["Manganese", 54.938045],
        "Mo": ["Molybdenum", 95.96],
        "N": ["Nitrogen", 14.0067],
        "Na": ["Sodium", 22.98976928],
        "Nb": ["Niobium", 92.90638],
        "Nd": ["Neodymium", 144.242],
        "Ne": ["Neon", 20.1797],
        "Ni": ["Nickel", 58.6934],
        "Np": ["Neptunium", 237],
        "O": ["Oxygen", 15.9994],
        "Os": ["Osmium", 190.23],
        "P": ["Phosphorus", 30.973762],
        "Pa": ["Protactinium", 231.03588],
        "Pb": ["Lead", 207.2],
        "Pd": ["Palladium", 106.42],
        "Pm": ["Promethium", 145],
        "Po": ["Polonium", 209],
        "Pr": ["Praseodymium", 140.90765],
        "Pt": ["Platinum", 195.084],
        "Pu": ["Plutonium", 244],
        "Ra": ["Radium", 226],
        "Rb": ["Rubidium", 85.4678],
        "Re": ["Rhenium", 186.207],
        "Rh": ["Rhodium", 102.9055],
        "Rn": ["Radon", 222],
        "Ru": ["Ruthenium", 101.07],
        "S": ["Sulfur", 32.065],
        "Sb": ["Antimony", 121.76],
        "Sc": ["Scandium", 44.955912],
        "Se": ["Selenium", 78.96],
        "Si": ["Silicon", 28.0855],
        "Sm": ["Samarium", 150.36],
        "Sn": ["Tin", 118.71],
        "Sr": ["Strontium", 87.62],
        "Ta": ["Tantalum", 180.94788],
        "Tb": ["Terbium", 158.92535],
        "Tc": ["Technetium", 98],
        "Te": ["Tellurium", 127.6],
        "Th": ["Thorium", 232.03806],
        "Ti": ["Titanium", 47.867],
        "Tl": ["Thallium", 204.3833],
        "Tm": ["Thulium", 168.93421],
        "U": ["Uranium", 238.02891],
        "V": ["Vanadium", 50.9415],
        "W": ["Tungsten", 183.84],
        "Xe": ["Xenon", 131.293],
        "Y": ["Yttrium", 88.90585],
        "Yb": ["Ytterbium", 173.054],
        "Zn": ["Zinc", 65.38],
        "Zr": ["Zirconium", 91.224]
    }
    return periodic_table

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """
    - Compute and return the total molar mass of all the elements listed in symbol_quantity_list.
    loop through the item's in the symbol_quantity_list
    - For each item in the list use the element's symbol to lookup the atomic mass of the 
    element in the periodic_table_dict dictionary.
    - Multiply the elements atomic weight by the quantity of atoms for the element 
    (from the symbol_quantity_list) and add that to the total mass.
    - Return the total mass.
    """
    ATOMIC_MASS = 1
    SYMBOL = 0
    QTY = 1
    molar_mass = 0
    for element in symbol_quantity_list:
        if element[SYMBOL] in periodic_table_dict:
            value = periodic_table_dict[element[SYMBOL]]
            atomic_mass = value[ATOMIC_MASS]
            quantity = element[QTY]
            total_mass = atomic_mass * quantity
            molar_mass += total_mass

    return molar_mass


def main():
    """
    - Asks the user for a chemical formula.
    - Asks the user for the sample size in grams.
    - Call parse_formula (from provided library) to get a list of elements in formula. 
    (store in a vaiable).
    - Call make_periodic_table function and store returned dictionary in variable.
    - Call compute_molar_mass to calculate the molar mass. Pass in the periodic table 
    dictionary and element list returned from the previous functions.
    - Display the molar mass.
    - Calculate Number of moles in the sample.
    - Display the Number of moles.
    """
    formula = input("Enter the molecular formula of the sample: ")
    sample_size = float(input("Enter the mass in grams of the sample: "))
    preiodic_table = make_periodic_table()
    molecule_list = parse_formula(formula, preiodic_table)
    molar_mass = compute_molar_mass(molecule_list, preiodic_table)
    moles = sample_size / molar_mass
    print(f"The molar mass of glucose: {molar_mass:.5f} grams/mole")
    print(f"The number of moles in the sample: {moles:.5f} moles")
   
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()        

