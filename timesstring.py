def countn(lall):
    d = dict()
    for value in lall:
        if value not in d:
            d[value] = 1
        else:
            d[value] += 1
    return d


# string="""There once was a king named Midas who did a good deed for a Satyr. And he was then granted a wish by Dionysus, the god of wine.
# For his wish, Midas asked that whatever he touched would turn to gold. Despite Dionysus’ efforts to prevent it, Midas pleaded that this was a fantastic wish, and so, it was bestowed. """
string = input("Enter a string:")
lall = string.split()
print("List of elements in the string:", lall)
di = dict()
di = countn(lall)
print("Displys all the elemsnt swith number of times they have occured:")
print(di)
for k in list(di.keys()):
    if di[k] <= 3:
        del di[k]

print("Elements having values less than 3 : ")
for items in di:
    print("'{}' have occured {} number of times ".format(items, di[items]))
