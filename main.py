def planets(p):
    placment = "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"
    for i in range (0, len (placment)):
        if p == placment [i]:
            return i

    
    
    
    
    return placment [p]

print (planets("earth"))