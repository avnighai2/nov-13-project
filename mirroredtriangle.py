
rows = int(input("enter the number of stars:"))

print("Right Angle Triangle:")
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end='')
    print()  

print("\nMirrored Right Angle Triangle:")
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(' ', end='')  
    for k in range(i):
        print('*', end='')
    print()  
