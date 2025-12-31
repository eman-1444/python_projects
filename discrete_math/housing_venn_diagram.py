from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
from matplotlib_venn.layout.venn3 import DefaultLayoutAlgorithm

data = [[2000, 5, 1, 2804500],
 [2000, 4, 1, 2803600],
 [2000, 3, 1, 2802700],
 [2000, 2, 1, 2801800],
 [2000, 1, 1, 2800900],
 [3000, 5, 1, 3704500],
 [3000, 4, 1, 3703600],
 [3000, 3, 1, 3702700],
 [3000, 2, 1, 3701800],
 [3000, 1, 1, 3700900],
 [4000, 5, 1, 4604500],
 [4000, 4, 1, 4603600],
 [4000, 3, 1, 4602700],
 [4000, 2, 1, 4601800],
 [4000, 1, 1, 4600900],
 [2000, 5, 0, 1804500],
 [2000, 4, 0, 1803600],
 [2000, 3, 0, 1802700],
 [2000, 2, 0, 1801800],
 [2000, 1, 0, 1800900],
 [3000, 5, 0, 2704500],
 [3000, 4, 0, 2703600],
 [3000, 3, 0, 2702700],
 [3000, 2, 0, 2701800],
 [3000, 1, 0, 2700900],
 [4000, 5, 0, 3604500],
 [4000, 4, 0, 3603600],
 [4000, 3, 0, 3602700],
 [4000, 2, 0, 3601800],
 [4000, 1, 0, 3600900],
 [1000, 5, 1, 1904500],
 [1000, 4, 1, 1903600],
 [1000, 3, 1, 1902700],
 [1000, 2, 1, 1901800],
 [1000, 1, 1, 1900900],
 [1000, 5, 0, 904500],
 [1000, 4, 0, 903600],
 [1000, 3, 0, 902700],
 [1000, 2, 0, 901800],
 [1000, 1, 0, 900900]]

def get_avg(set):
  return sum(set) // len(set)

def createSets(set_A, set_B, set_C, set_D, data):

  for i in range(0, len(data)):
    for j in range(0, len(data[i])):
      current_price = data[i][3]
      current_item = data[i][j]
      if j == 0:
        # square ft
        if current_item > 2000:
          set_A.add(current_price)
      elif j == 1:
        # rooms
        if current_item > 2:
          set_B.add(current_price)
      elif j == 2:
      # parking
        if current_item == 1:
          set_C.add(current_price)

  # create set for prices that match none of the criteria
  for i in range(0, len(data)):
    price = (data[i][3])
    if price not in set_A and price not in set_B and price not in set_C:
      set_D.add(price)

# set of housing prices with >2000 sq ft
set_A = set()
# set of housing prices with >2 rooms
set_B = set()
# set of hosuing prices with parking
set_C = set()
# set of hosuing that matches none
set_D = set()


createSets(set_A, set_B, set_C, set_D, data)

A_only = set_A - set_B - set_C
B_only = set_B - set_A - set_C
C_only = set_C - set_A - set_B

AnB = (set_A & set_B) - set_C
AnC = (set_A & set_C) - set_B
BnC = (set_B & set_C) - set_A

AnBnC = set_A & set_B & set_C

A_avg = get_avg(A_only)
B_avg = get_avg(B_only)
C_avg = get_avg(C_only)

AnB_avg = get_avg(AnB)
AnC_avg = get_avg(AnC)
BnC_avg = get_avg(BnC)

AnBnC_avg = get_avg(AnBnC)

_An_Bn_C_avg = get_avg(set_D)

plt.figure(figsize=(9,9))
even_circles = DefaultLayoutAlgorithm(fixed_subset_sizes = (1,1,1,1,1,1,1))

diagram = venn3([set_A, set_B, set_C], ("SetA: > 2000 sqft", "SetB: > 2 Rooms", "Set C: Parking"), layout_algorithm = even_circles)
circle_border = venn3_circles(subsets = (1,1,1,1,1,1,1), linestyle = "solid")

plt.axis("on")

diagram.get_label_by_id("100").set_text(A_avg)
diagram.get_label_by_id("010").set_text(B_avg)
diagram.get_label_by_id("001").set_text(C_avg)

diagram.get_label_by_id("110").set_text(AnB_avg)
diagram.get_label_by_id("101").set_text(AnC_avg)
diagram.get_label_by_id("011").set_text(BnC_avg)

diagram.get_label_by_id("111").set_text(AnBnC_avg)


plt.gca().set_facecolor("lightgrey")

diagram.get_patch_by_id("111").set_color("white")

plt.title("Venn Diagram")

plt.annotate(_An_Bn_C_avg, xy = (0, 0), xytext = (0.4, -0.5))
plt.annotate("U=40", xy = (0, 0), xytext = (-0.68, 0.65))

plt.show()

new_house_sector = ""
new_house_prediction = ""

print("Enter the house's sqft: ")
sqft = int(input())
if sqft > 2000:
  new_house_sector += "1"
else:
  new_house_sector += "0"

print("Enter house's number of rooms: ")
rooms = int(input())
if rooms > 2:
  new_house_sector += "1"
else:
  new_house_sector += "0"

print("Does the house include parking? ")
parking = int(input())
if parking == 1:
  new_house_sector += "1"
else:
  new_house_sector += "0"

print("Enter the house's price: ")
price = int(input())

if new_house_sector == "000":
  new_house_prediction = _An_Bn_C_avg
else:
  new_house_prediction = diagram.get_label_by_id(new_house_sector).get_text()

print(new_house_sector)
print(new_house_prediction)
if int(new_house_prediction) < price:
  print("The house is overvalued, a bad deal")
elif int(new_house_prediction) == price:
  print("The house has the expected value, a fine deal")
else:
  print("The house is undervalued, a good deal")