# Lists and Dictionaries
# Let's make a pet management system
import pickle

# Dictionary containing pet data. #
pets: dict = {
    "Bob": {
        "age": 3,
        "type": "Goldfish",
        "gender": "F"
    },
    "Snuggles": {
        "age": 12,
        "type": "Dog",
        "gender": "M"
    }
}

def main() -> None:
    # The menu choice of the user
    choice: str = ""
    with open("pets.dat", 'rb') as f:
        pets = pickle.load(f)
    f.close()
    while choice != "0":
        choice = input("""

MENU
----
         0 : Quit
         1 : List Pets
         2 : Add Pet
         3 : Remove Pet
<PET_NAME> : See Pet info
      SAVE : Save Pet data
      LOAD : Load Pet data from file
                       
Go to:                 
""")
        print()
        if choice == "0":
            break
        elif choice == "1":
            for value in pets.keys():
                print(value)
        elif choice in pets.keys():
            print(pets[choice])
        elif choice == "2":
            name: str = input("What is the Pet's name? ")
            age: int = int(input("How old is the Pet in years? "))
            p_type: str = input("What type of pet is the Pet? ")
            gender: str = input("What gender is the Pet? ")
            pets[name] = {
                "age": age,
                "type": p_type,
                "gender": gender
            }
        elif choice == "3":
            name: str = input("Which Pet should be removed: ")
            if name in pets.keys():
                del pets[name]
        elif choice == "SAVE":
            with open('pets.dat', 'wb') as f:
                pickle.dump(pets, f)
            f.close()
        elif choice == "LOAD":
            with open("pets.dat", 'rb') as f:
                pets = pickle.load(f)["pets"]
            f.close()
        else:
            print("That is not a valid option!")
        

if __name__ == "__main__":
    main()