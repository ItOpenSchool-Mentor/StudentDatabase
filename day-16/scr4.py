
lst1 = [1, 2, 3]

match lst1:
    case [x, y]:
        print(f"x = {x}, y = {y}")
    case [x, y, z]:
        print(f"x = {x}, y = {y}, z = {z}")
    case [x]:
        print(f"x = {x}")
        
