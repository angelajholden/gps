# A fruit store manages its inventory by using Python dictionaries. Each dictionary has a string name of any fruit as key and  its integer quantity in inventory as the corresponding value.
#
# An example:
#
# d = {"apples":47, "lemons":144, "mangos":23, 'durian': 1, 'tangerines', 20}
#
# Define a function total_items(fruit_dict) which returns the int total number of items within the fruit inventory dictionary fruit_dict.
#
# For the example, total_items(d) should return 235, since 47+144+23+1+20 == 235.
#
# Your function should work for *any* fruit inventory dictionary.

# total = 0
# mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
# for akey in mydict:
#    if len(akey) > 3:
#       total = total + mydict[akey]
# print(total)

def total_items(fruit_dict):
    total = 0
    for akey in fruit_dict:
        total += fruit_dict[akey]
    print(total)

# fruit_dict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
fruit_dict = {"apples":47, "lemons":144, "mangos":23, 'durian': 1, 'tangerines': 20}

total_items(fruit_dict)
