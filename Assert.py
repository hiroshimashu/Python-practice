def eat_junk(food):
    assert food in [
        'pizza', 
        'ice cream', 
        'candy'
    ], "food must be junk"
    return f"nom nom nom {food}"

print(eat_junk('pizza'))

