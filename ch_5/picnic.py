allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought
print("apples: " + str(total_brought(allGuests, 'apples')))
print("pretzels: " + str(total_brought(allGuests, 'pretzels')))
print("ham sandwiches: " + str(total_brought(allGuests, 'ham sandwiches')))
print("apple pies: " + str(total_brought(allGuests, 'apple pies')))
print("cups: " + str(total_brought(allGuests, 'cups')))
