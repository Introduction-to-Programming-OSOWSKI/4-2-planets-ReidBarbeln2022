def planets(p):
    placment = "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"
    for i in range (0, len (placment)):
        if p == placment [i]:
            return i + 1

    return "russia is not a planet"
    
    
    
    return placment [p]

print (planets("mercury"))