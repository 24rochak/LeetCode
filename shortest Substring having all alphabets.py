def calc(str):
    last = 96
    for i in str:
        if (ord(i.lower()) - last) == 1:
            print(i, ord(i.lower()), last)
            last = ord(i.lower())

    print(last)
    if last == ord('z'):
        return True
    else:
        return False


str = "a lot of people, be something, C algha, dghala, edhga, ftuggahaghaiafjgahalhk qafsl agagam afagnasfkhgs Ogahapqrhglaghashlh thgl uqlgha vagagh wagklha xaghhknmbv yaxbvmZ"
print(calc(str))
