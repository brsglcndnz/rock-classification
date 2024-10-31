'''
Python code for Rock Mass Rating and NATM Class
The Rock Mass Rating (RMR) classification system was proposed by Bieniawski
and takes into account the following six parameters:
uniaxial compressive strength; rock quality designation (RQD); discontinuity spacing;
discontinuity conditions; discontinuity orientation; and groundwater conditions.
'''

def rock_strength():
    ucs = float(input("Uniaxial compressive strength (Mpa): "))
    
    if ucs < 1:
        return 0
    elif ucs < 5:
        return 1
    elif ucs < 25:
        return 2
    elif ucs < 50:
        return 4
    elif ucs < 100:
        return 7
    elif ucs < 250:
        return 12
    else:
        return 15

def get_rqd():
    rqd = float(input("Rock Quality Designation value: "))
    
    if rqd < 25:
        return 5
    elif rqd < 50:
        return 8
    elif rqd < 75:
        return 13
    elif rqd < 90:
        return 17
    else:
        return 20

def get_discontinities_spacing():
    print("""
    Spacing of discontinuities:
    1. < 60 mm
    2. 60 - 200 mm
    3. 200 - 600 mm
    4. 0.6 - 2 m
    5. > 2 m
    """)
    spacing = input("Choose spacing of discontinuities: ")
    discontinities_spacing_values = {'1': 5, '2': 8, '3': 10, '4': 15, '5': 20}
    return discontinities_spacing_values.get(spacing, "Error!")

def get_discontinities_length():
    print("""
    Discontinuities length:
    1. > 20 m
    2. 10 - 20 m
    3. 3 - 10 m
    4. 1 - 3 m
    5. < 1 m
    """)
    length = input("Choose discontinuities length: ")
    discontinities_length_values = {'1': 5, '2': 8, '3': 10, '4': 15, '5': 20}
    return discontinities_length_values.get(length, "Error!")

def get_discontinities_separation():
    print("""
    Discontinuities separation:
    1. > 5 mm
    2. 1 - 5 mm
    3. 0.1 - 1 mm
    4. < 0.1 mm
    5. None
    """)
    separation = input("Choose discontinuities separation: ")
    discontinities_separation_values = {'1': 0, '2': 1, '3': 4, '4': 5, '5': 6}
    return discontinities_separation_values.get(separation, "Error!")

def get_discontinities_roughness():
    print("""
    Discontinuities roughness:
    1. Slickensided
    2. Smooth
    3. Slightly rough
    4. Rough
    5. Very rough
    """)
    roughness = input("Choose discontinuities roughness: ")
    discontinities_roughness_values = {'1': 0, '2': 1, '3': 3, '4': 5, '5': 6}
    return discontinities_roughness_values.get(roughness, "Error!")

def get_discontinities_infilling():
    print("""
    Discontinuities infilling:
    1. Soft filling > 5 mm
    2. Soft filling < 5 mm
    3. Hard filling > 5 mm
    4. Hard filling < 5 mm
    5. None
    """)
    infilling = input("Choose discontinuities infilling: ")
    discontinities_infilling_values = {'1': 0, '2': 2, '3': 2, '4': 4, '5': 6}
    return discontinities_infilling_values.get(infilling, "Error!")

def get_discontinities_weathering():
    print("""
    Discontinuities weathering:
    1. Decomposed
    2. Highly weathered
    3. Moderately weathered
    4. Slightly weathered
    5. Unweathered
    """)
    weathering = input("Choose discontinuities weathering: ")
    discontinities_weathering_values = {'1': 0, '2': 1, '3': 3, '4': 5, '5': 6}
    return discontinities_weathering_values.get(weathering, "Error!")

def get_groundwater():
    print("""
    Groundwater:
    1. Flowing (> 125 lt/min)
    2. Dripping (25 - 125 lt/min)
    3. Wet (10 - 25 lt/min)
    4. Damp (< 10 lt/min)
    5. Completely dry
    """)
    groundwater = input("Choose groundwater: ")
    discontinities_groundwater_values = {'1': 0, '2': 1, '3': 3, '4': 5, '5': 6}
    return discontinities_groundwater_values.get(groundwater, "Error!")

def get_orientation():
    print("""
    Discontinuity orientation:
    1. Very unfavourable
    2. Unfavourable
    3. Fair
    4. Favourable
    5. Very favourable
    """)
    orientation = input("Choose discontinuity orientation for tunnels: ")
    discontinity_orientation_values = {'1': -12, '2': -10, '3': -5, '4': -2, '5': 0}
    return discontinity_orientation_values.get(orientation, "Error!")

def calculate_rmr_value(strength, rqd, spacing, length, separation, roughness, infilling, weathering, groundwater, orientation):
    return strength + rqd + spacing + length + separation + roughness + infilling + weathering + groundwater + orientation

def main():
    try:
        strength = rock_strength()
        rqd = get_rqd()
        spacing = get_discontinities_spacing()
        length = get_discontinities_length()
        separation = get_discontinities_separation()
        roughness = get_discontinities_roughness()
        infilling = get_discontinities_infilling()
        weathering = get_discontinities_weathering()
        groundwater = get_groundwater()
        orientation = get_orientation()
        
        rmr = calculate_rmr_value(strength, rqd, spacing, length, separation, roughness, infilling, weathering, groundwater, orientation)
        
        if rmr >= 81:
            print(f"RMR value = {round(rmr, 0)} Very good rock")
        elif rmr >= 61:
            print(f"RMR value = {round(rmr, 0)} Good rock")
        elif rmr >= 41:
            print(f"RMR value = {round(rmr, 0)} Fair rock")
        elif rmr >= 21:
            print(f"RMR value = {round(rmr, 0)} Poor rock")
        else:
            print(f"RMR value = {round(rmr, 0)} Very poor rock")
            
        if rmr < 5:
                print("NATM class = C5")
                
        elif rmr < 10:
            print("NATM class = C4")
                
        elif rmr < 15:
            print("NATM class = C3")
                
        elif rmr < 20:
            print("NATM class = C2")
                
        elif rmr < 29:
            print("NATM class = C1")
                
        elif rmr < 47:
            print("NATM class = B3")
                
        elif rmr < 58:
            print("NATM class = B2")
                
        elif rmr < 65:
            print("NATM class = B1")
                
        elif rmr < 80:
            print("NATM class = A2")
                
        else:
            print("NATM class = A1")
        
    except ValueError:
        print("Please enter valid numerical values where required.")

if __name__ == "__main__":
    main()
