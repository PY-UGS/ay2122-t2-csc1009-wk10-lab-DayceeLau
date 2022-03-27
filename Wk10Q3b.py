def moduleswitching(mod):
    match mod:                      #Switch case
        case "CSC1009":             #mod = CSC1009
            return "Object-Oriented Programming"
        case "CSC1006":             #mod = CSC1006
            return "Mathematics 2"
        case "CSC1007":             #mod = CSC1007
            return "Operating Systems"
        case "CSC1008":             #mod = CSC1008
            return "Data Structures and Algorithms"
        case "CSC1010":             #mod = CSC1010
            return "Computer Networks"
        case _:                     #mod is not one of the above cases
            return "Invalid"

x = input("Module code:")
print(moduleswitching(x))
