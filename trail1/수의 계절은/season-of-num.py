month = int(input())

if month >= 3 and month <= 11:
    if month >= 9:
        print("Fall")
    elif month >= 6:
        print("Summer")
    else:
        print("Spring")
else:
    print("Winter")