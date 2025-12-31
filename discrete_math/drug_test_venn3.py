"""
U = 50
41 positive
21 positive A
21 positive B
31 positive C
9 positive with A + B
14 positive A + C
15 positive B + C
"""

from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn.layout.venn3 import DefaultLayoutAlgorithm
from matplotlib import pyplot as plt
import time

def find_center(pos_total, a_total, b_total, c_total, anb, anc, bnc):
  all = a_total + b_total + c_total + anb + anc + bnc
  all_pos = all - anb - anb - anc - anc - bnc - bnc
  return pos_total - all_pos

def find_a_only(a_total, AnB, AnC, center):
  return a_total - (AnB - center + AnC - center + center)

def find_b_only(b_total, AnB, BnC, center):
  return b_total - (AnB - center + BnC - center + center)

def find_c_only(c_total, AnC, BnC, center):
  return c_total - (AnC - center + BnC - center + center)

def find_greatest_positive_result(sectors):
  greatest = 0
  greatest_name = ""
  for k, v in sectors.items():
    if v > greatest:
      greatest = v
      greatest_name = k
  return (greatest_name, greatest)

def find_smallest_positive_result(sectors):
  smallest = sectors["An_Bn_C"]
  smallest_name = ""
  for k, v in sectors.items():
    if v < smallest:
      smallest = v
      smallest_name = k
  return (smallest_name, smallest)

def get_sector(sector_name):
  for k, v in all_sectors.items():
    if k == sector_name:
      return (k, v)

def get_user_sectors():
  print("Enter total: ")
  total = int(input())
  print("Enter number of positive results: ")
  pos_total = int(input())


  print("Enter total results for A: ")
  a_total = int(input())
  print("Enter total results for B: ")
  b_total = int(input())
  print("Enter total results for C: ")
  c_total = int(input())

  print("Enter total results for A intersects B: ")
  anb = int(input())
  print("Enter total results for A intersects C: ")
  anc = int(input())
  print("Enter total results for B intersects C: ")
  bnc = int(input())

  return total, pos_total, a_total, b_total, c_total, anb, anc, bnc

def display_questions():
  print("\n *** Enter exit to exit ***")
  print("- Enter greatest to find the combination with the greatest positive results.")
  print("- Enter smallest to find the combination with the worst results.")
  print("- Enter total to find the total number results")
  print("- Enter outlier to find the number of negative results")
  print("- Enter a_only to find the number of results for A only")
  print("- Enter b_only to find the number of results for B only")
  print("- Enter c_only to find the number of results for C only")
  print("- Enter A n B to find the number of results for the A intersects B combination")
  print("- Enter A n C to find the number of results for the A intersects C combination")
  print("- Enter B n C to find the number of results for the B intersects C combination")
  print("- Enter A n B n C to find the number of results for the combination of all three drugs together")

def ask_question():
  user_string = ""
  while user_string != "exit":
    display_questions()
    user_string = input()
    if user_string == "greatest":
      name, num = find_greatest_positive_result(positive_sectors)
      print("\nThe combination with the greatest positive results is " + name + " with " + str(num) + " positive results")
    elif user_string == "smallest":
      name, num = find_smallest_positive_result(positive_sectors)
      print("\nThe combination with the worst positive results is " + name + " with " + str(num) + " positive results")
    elif user_string == "total":
      print("\nThe total number of tests is " + str(total))
    elif user_string == "outlier":
      print("\nThe number of negative results is " + str(all_sectors["_An_Bn_C"]))
    elif user_string == "a_only":
      print("\nThe number of positive results for only drug A is " + str(all_sectors["An_Bn_C"]))
    elif user_string == "b_only":
      print("\nThe number of positive results for only drug B is " + str(all_sectors["_AnBn_C"]))
    elif user_string == "c_only":
      print("\nThe number of positive results for only drug C is " + str(all_sectors["_An_BnC"]))
    elif user_string == "A n B":
      print("\nThe number of positive results for the drug A and B combination is " + str(all_sectors["AnBn_C"]))
    elif user_string == "A n C":
      print("\nThe number of positive results for the drug A and C combination is " + str(all_sectors["An_BnC"]))
    elif user_string == "B n C":
      print("\nThe number of positive results for the drug B and C combination is " + str(all_sectors["_AnBnC"]))
    elif user_string == "A n B n C":
      print("\nThe number of positive results for the combination of all three drugs together is " + str(all_sectors["AnBnC"]))
    elif user_string == "exit":
      print("\nExiting...\n")
    else:
      print("\n* Please enter valid string")

data = get_user_sectors()
total = data[0]
positive_total = data[1]
outlier = total - positive_total

a_total = data[2]
b_total = data[3]
c_total = data[4]

AnB = data[5]
AnC = data[6]
BnC = data[7]

AnBnC = find_center(positive_total, a_total, b_total, c_total, AnB, AnC, BnC)

a_only = find_a_only(a_total, AnB, AnC, AnBnC)
b_only = find_b_only(b_total, AnB, BnC, AnBnC)
c_only = find_c_only(c_total, AnC, BnC, AnBnC)

AnB -= AnBnC
AnC -= AnBnC
BnC -= AnBnC

positive_sectors = {
    "An_Bn_C": a_only,
    "_AnBn_C": b_only,
    "_An_BnC": c_only,
    "AnBn_C": AnB,
    "An_BnC": AnC,
    "_AnBnC": BnC,
    "AnBnC": AnBnC}

all_sectors = {
    "An_Bn_C": a_only,
    "_AnBn_C": b_only,
    "_An_BnC": c_only,
    "AnBn_C": AnB,
    "An_BnC": AnC,
    "_AnBnC": BnC,
    "AnBnC": AnBnC,
    "_An_Bn_C": outlier}

plt.figure(figsize=(5,5))

even_circles = DefaultLayoutAlgorithm(fixed_subset_sizes = (1,1,1,1,1,1,1))
diagram = venn3(subsets=(a_only, b_only, AnB, c_only, AnC, BnC, AnBnC),
                set_labels=('A', 'B', 'C'),
                layout_algorithm = even_circles)
circle_border = venn3_circles(subsets = (1,1,1,1,1,1,1), linestyle = "solid")
plt.axis("on")
plt.gca().set_facecolor("lightgrey")

plt.title("Positive Drug Test Results")

plt.annotate(outlier, xy = (0, 0), xytext = (0.4, -0.5))
plt.annotate("U=" + str(total), xy = (0, 0), xytext = (-0.68, 0.65))

plt.show()
time.sleep(0.5)

ask_question()