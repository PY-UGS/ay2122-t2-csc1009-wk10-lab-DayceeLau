def moduleswitching(mod):
    match mod:
        case "CSC1009":
            return "Object-Oriented Programming"
        case "CSC1006":
            return "Mathematics 2"
        case "CSC1007":
            return "Operating Systems"
        case "CSC1008":
            return "Data Structures and Algorithms"
        case "CSC1010":
            return "Computer Networks"
        case _:
            return "Invalid"

x = input("Module code:")
print(moduleswitching(x))