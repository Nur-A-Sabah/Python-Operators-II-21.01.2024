c = input("Enter a letter: ")

if c >= "a" and c <= "z":
    print(f"The character {c} is a lowercase alphabate")

elif c >= "A" and c <= "Z":
    print(f"The character {c} is a uppercase alphabate")
    
else:
    print(f"The character {c} is not an alphabate")