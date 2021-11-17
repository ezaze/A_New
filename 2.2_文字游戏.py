

def game(a):
    b = a + "-"
    c = b[1:] + b[:1] + "y"
    return c

print(game("Python"))