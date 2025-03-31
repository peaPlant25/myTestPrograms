print("COLLATZ CONJECTURE PATH CALCULATOR")
a = int(input('''Enter the number for the collatz conjecture test.
>'''))

print(a)
while a != 1:
    if a % 2 == 0:
        a /= 2
    else:
        a = 3*a + 1
    print(a)
else:
    print("That's it! You are doomed to end at 1!")