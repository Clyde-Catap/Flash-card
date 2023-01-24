from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

french_data = pandas.read_csv("data/french_words.csv")
french_dict = french_data.to_dict()
# print(french_dict["French"])
# print(french_dict)
# print(french_dict["French"][0])
# print(french_dict["English"][0])


lister = []

for x in french_dict["French"]:
    lister.append(x)

value = []
value_e = []

for g in lister:
    gg = french_dict["French"][g]
    value.append(gg)

for g in lister:
    gg = french_dict["English"][g]
    value_e.append(gg)

new_dict= {}

res = {}
for key in value:
    for x in value_e:
        res[key] = x
        value_e.remove(x)
        break

#
print(res)

res.pop("partie")
print(res)


x = random.choice(french_dict["French"])
print(french_dict["French"])

del french_dict[x]

print(french_dict)

# french_dict.remove()
#
# trial = pandas.DataFrame(french_dict)
# trial.to_csv("trail.csv", header=False)
# lister = []
#
# for x in gg:
#     lister.append(x)
#
# print(lister)





