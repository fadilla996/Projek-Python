is_tall=False
is_heavy=False

if is_tall and is_heavy :
    print("Big")
elif is_tall and not (is_heavy) :
    print("Tall")
elif not (is_tall) or (is_heavy) :
    print("Human")
elif not (is_tall and is_heavy) :
    print("small")

else:
    print("random")

a = "aiueo"
b = "a"
if b in a:
    print("yes")