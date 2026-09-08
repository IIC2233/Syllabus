def mystery(deck):
    size = len(deck)
    
    for step in range(1, size):
        chosen = deck[step]
        shadow = step - 1
        
        while shadow >= 0 and deck[shadow] > chosen:
            deck[shadow + 1] = deck[shadow]
            shadow -= 1
            
        deck[shadow + 1] = chosen
        
    return deck

print(mystery([4, 1, 3]))