# Python code for Q-system and NATM Class
# The Q-value may be used for classification of the rock mass around an underground opening,
# as well as for field mapping.
# This python code based on the Using the Q-system Handbook, NGI, June 2022

def get_rqd ():
    
    return float(input("Rock Quality Designation value: "))

def get_joint_set_number ():
    
    print("""

    Joint set number:
    
    1. Massive, no or few joints
    2. One joint set
    3. One joint set plus random joints
    4. Two joint sets
    5. Two joint sets plus random joints
    6. Three joint sets
    7. Three joint sets plus random joints
    8. Four or more joint sets, random heavily jointed 'sugar cube', etc
    9. Crushed rock, earth-like
    
    """)
    
    jn = input("Choose joint set number: ")
    
    joint_set_values = {'1': 0.5, '2': 2, '3': 3, '4': 4, '5': 6, '6': 9, '7': 12, '8': 15, '9': 20}

    return joint_set_values.get(jn, "Error!") 


def get_joint_roughness_number ():
    
    print("""

    Joint roughness number:
    
    1. Discontinuous joints
    2. Rough or irregular, undulating
    3. Smooth, undulating
    4. Slickensided, undulating
    5. Rough, irregular, planar
    6. Smooth, planar
    7. Slickensided, planar
    8. Zone containing clay minerals thick enough to prevent rock-wall contact when sheared
    
    """)

    jr = input("Choose joint roughness number: ")
    
    joint_roughness_values = {'1': 4, '2': 3, '3': 2, '4': 1.5, '5': 1.5, '6': 1, '7': 0.5, '8': 1}

    return joint_roughness_values.get(jr, "Error!")

def get_joint_alteration_number ():
    
    print ("""

    Joint alteration number:
    
    Rock-wall contact (no mineral fillings, only coatings)
    
    1. Tightly healed, hard, non-softening, impermeable filling, i.e., quartz or epidote.
    2. Unaltered joint walls, surface staining only. Φr = 25-35° 
    3. Slightly altered joint walls. Non-softening mineral coatings; sandy particles, clay-free disintegrated rock, etc. Φr = 25-30°
    4. Silty or sandy clay coatings, small clay fraction (non-softening). Φr = 20-25°
    5. Softening or low friction clay mineral coatings, i.e., kaolinite or mica. Also chlorite, talc gypsum, graphite, etc., and small quantities of swelling clays. Φr = 8-16°
    
    Rock-wall contact before 10 cm shear (thin mineral fillings)
    
    6. Sandy particles, clay-free disintegrated rock, etc. Φr = 25-30°
    7. Strongly over-consolidated, non-softening, clay mineral fillings (continuous, but <5 mm thickness). Φr = 16-24°
    8. Medium or low over-consolidation, softening, clay mineral fillings (continuous, but <5 mm thickness). Φr = 12-16°
    9. Swelling-clay fillings, i.e., montmorillonite (continuous, but <5 mm thickness). Value of Ja depends on percent of swelling clay-size particles. Φr = 6-12°
    
    No rock-wall contact when sheared (thick mineral fillings)
    
    10. Zones or bands of disintegrated or crushed rock. Strongly over-consolidated. Φr = 16-24°
    11. Zones or bands of clay, disintegrated or crushed rock. Medium or low over-consolidation or softening fillings. Φr = 12-16°
    12. Zones or bands of clay, disintegrated or crushed rock. Swelling clay. Ja depends on percent of swelling clay-size particles. Φr = 6-12°
    13. Thick continuous zones or bands of clay. Strongly over-consolidated. Φr = 12-16°
    14. Thick, continuous zones or bands of clay. Medium to low over-consolidation. Φr = 12-16°
    15. Thick, continuous zones or bands with clay. Swelling clay. Ja depends on percent of swelling clay-size particles. Φr = 6-12°
   
    """)
    
    ja = input("Choose joint alteration number:   ")
    
    joint_alteration_values = {'1': 0.75, '2': 1, '3': 2, '4': 3, '5': 4, '6': 4, '7': 6, '8': 8, '9': 10, '10': 6, '11':8, '12': 10, '13': 10, '14': 13, '15': 16}

    return joint_alteration_values.get(ja, "Error!")
      

def get_water_reduction_factor ():
    
    print("""

    Joint Water Reduction Factor:
    
    1. Dry excavations or minor inflow ( humid or a few drips)
    2. Medium inflow, occasional outwash of joint fillings (many drips/rain)
    3. Jet inflow or high pressure in competent rock with unfilled joints
    4. Large inflow or high pressure, considerable outwash of joint fillings
    5. Exceptionally high inflow or water pressure decaying with time. Causes outwash of material and perhaps cave in
    6. Exceptionally high inflow or water pressure continuing without noticeable decay. Causes outwash of material and perhaps cave in
    
    """)
    
    jw = input(" Choose joint water reduction factor:   ")
      
    water_reduction_factor_values = {'1': 1, '2': 0.66, '3': 0.5, '4': 0.33, '5': 0.15, '6': 0.05}

    return  water_reduction_factor_values.get(jw, "Error!")
    
def get_stress_reduction_factor ():
    
    print("""
    
    Stress Reduction Factor:
    
    Weak zones intersecting the underground opening, which may cause loosening of rock mass
    
    1. Multiple occurrences of weak zones within a short section containing clay or chemically disintegrated, very loose surrounding rock (any depth), or long sections with incompetent (weak) rock (any depth)
    2. Multiple shear zones within a short section in competent clay-free rock with loose surrounding rock (any depth)
    3. Single weak zones with or without clay or chemical disintegrated rock (depth ≤ 50m)
    4. Loose, open joints, heavily jointed or “sugar cube”, etc. (any depth)
    5. Single weak zones with or without clay or chemical disintegrated rock (depth > 50m)
    
    Competent, mainly massive rock, stress problems
    
    6. Low stress, near surface, open joints
    7. Medium stress, favourable stress condition
    8. High stress, very tight structure. Usually favourable to stability.
    9. Moderate spalling and/or slabbing after > 1 hour in massive rock
    10. Spalling or rock burst after a few minutes in massive rock
    11. Heavy rock burst and immediate dynamic deformation in massive rock
    
    Squeezing rock: plastic deformation in incompetent rock under the influence of high pressure
    
    12. Mild squeezing rock pressure
    13. Heavy squeezing rock pressure
    
    Swelling rock: chemical swelling activity depending on the presence of water
    
    14. Mild swelling rock pressure
    15. Heavy swelling rock pressure
    
    """)

    srf = input("Choose stress reduction factor:   ")
    
    stress_reduction_factor_values = {'1': 10, '2': 7.5, '3': 5, '4': 5, '5': 2.5, '6': 2.5, '7': 1, '8': 2, '9': 27.5, '10': 125, '11': 300, '12': 8, '13': 15, '14': 7.5, '15': 12.5}

    return stress_reduction_factor_values.get(srf, "Error!")       


def calculate_q_value (rqd, jr, jw, jn, ja, srf, purpose):
    
    if purpose == '1':
        return (rqd * jr * jw) / (jn * ja * srf)
    
    elif purpose == '2':
        return (rqd * jr * jw) / (3 * jn * ja * srf)
    
    elif purpose == '3':
        return (rqd * jr * jw) / (2 * jn * ja * srf)
    
    else:
        return None

def main():
    try:
        rqd = get_rqd()
        
        jn = get_joint_set_number()
        
        jr = get_joint_roughness_number()
        
        ja = get_joint_alteration_number()
        
        jw = get_water_reduction_factor()
        
        srf = get_stress_reduction_factor()
        
        purpose = input("Choose purpose of analysis (1: General, 2: Tunnel intersections, 3: Portals): ")

        q = calculate_q_value(rqd, jr, jw, jn, ja, srf, purpose)
        
        if q is not None:
            
            if q >= 400:
                print(f"Q value = {round(q, 3)} Exceptionally good rock")
                
            elif q >= 100:
                print(f"Q value = {round(q, 3)} Extremely good rock")
                
            elif q >= 40:
                print(f"Q value = {round(q, 3)} Very good rock")
                
            elif q >= 10:
                print(f"Q value = {round(q, 3)} Good rock")
                
            elif q >= 4:
                print(f"Q value = {round(q, 3)} Fair rock")
                
            elif q >= 1:
                print(f"Q value = {round(q, 3)} Poor rock")
                
            elif q >= 0.1:
                print(f"Q value = {round(q, 3)} Very poor rock")
                
            elif q >= 0.01:
                print(f"Q value = {round(q, 3)} Extremely poor rock")
                
            else:
                print(f"Q value = {round(q, 3)} Exceptionally poor rock")
            
            
            if q < 0.002:
                print("NATM class = C5")
                
            elif q < 0.01:
                print("NATM class = C4")
                
            elif q < 0.015:
                print("NATM class = C3")
                
            elif q < 0.03:
                print("NATM class = C2")
                
            elif q < 0.1:
                print("NATM class = C1")
                
            elif q < 1:
                print("NATM class = B3")
                
            elif q < 4:
                print("NATM class = B2")
                
            elif q < 10:
                print("NATM class = B1")
                
            elif q < 80:
                print("NATM class = A2")
                
            else:
                print("NATM class = A1")
                
        else:
            print("The Q value could not be calculated due to invalid input.")
    
    except ValueError:
        print("Please enter valid numerical values where required.")

if __name__ == "__main__":
    main()




