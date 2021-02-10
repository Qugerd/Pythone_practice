a = int(input())
b = int(input())
c = int(input())

if c < a:
    print("Deficiency")

if c >= a:
    if c <= b:
        print("Normal")
    else:
        print("Excess")