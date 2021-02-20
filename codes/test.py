'''
For question, see marathon-question.jgg
'''


arr = []
d = 42.195
a = input("enter the float number")
while a != 'q':
    try:
        if eval(a) <= 0:
            print("Invalid input")
            break
    except:
        print("invalid input")
        break
    if float(a)==d:
        continue
    else:
        arr.append(float(a))
    a = input()


arr.sort(reverse=True)
for i in arr[:4]:
    print(i)
