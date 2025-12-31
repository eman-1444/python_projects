# Decision Tree (main thing)

def calculate_risk(data):
    if data["age"] < 18:
        return data["weight"] > 60
    elif data["age"] > 30:
        return data["smoker"]
    else:
        # Age 18-30: Low risk factors defined
        return False
def calculate_user_risk():
    age = int(input("Enter your age: "))
    if age < 18:
      weight = float(input("Enter your weight: "))
      if weight > 60:
        print("You have a high risk due to your high weight and young age.")
      else:
        print("You have a low risk due to your healthy weight and young age.")
    elif age > 30:
      smoker = input("Are you a smoker? (y/n): ")
      if smoker == "y":
        print("You have a high risk since you are older and smoke.")
      else:
        print("You have a low risk since you do not smoke.")
    else:
      print("You have a low risk since you are in the age range 18-30.")

def print_risk(risk):
    if risk:
        print("High Risk")
    else:
        print("Low risk")

def print_tree():
    print("DECISION TREE LOGIC:")
    print()
    print()
    print("                 ┌─────────────┐")
    print("                 │  Age < 18   │")
    print("                 └──────┬──────┘")
    print("                        │")
    print("          ┌─────────────┼─────────────┐")
    print("          │                           │")
    print("          |                           |")
    print("          │                           │")
    print("          │                           │")
    print("          │                           │")
    print("          │                           │")
    print("    ┌─────▼─────┐               ┌─────▼─────┐")
    print("    │Weight > 60│               | Age > 30? │")
    print("    └──────┬────┘               └─────┬─────┘ ")
    print("           │                          │")
    print("       ┌───┴───┐                  ┌───┴───┐")
    print("       │       │                  │       │")
    print("       |       |                  |       |")
    print("       │       │                  │       │")
    print("       │       │                  │       │")
    print("     True    False             Smoker?  False")
    print("                                  |        ")
    print("                                  |        ")
    print("                                  |        ")
    print("                              ┌───┴───┐    ")
    print("                            True    False   ")

    print()

# calculate risk given a list of 3 features
def calculate_row_risk(features):
    age_y, age_o, weight, smoker = features

    if age_y:
      if age_o:
        if smoker:
          return True
        else:
          return False
      else:
        if weight:
            return True
        else:
            return False
    elif age_o:
        if smoker:
          return True
        else:
          return False
    else:
        return False

print_tree()
# calculate_user_risk()

# Truth table
# create truth table for a given data set
# all possible combinations
def create_truth_table_all():
  truth_table = [[], []]
  truth_table[0] = ["Age < 18(Ay)", "Age > 30(Ao)", "Weight(W)", "Smoker(S)", "High Risk"]

  for i in range(1, 2**4 + 1):
    truth_table.append([])

    if i == 1:
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 2:
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(False) #
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 3:
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(False)
      truth_table[i].append(True) #
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 4:
      truth_table[i].append(True) #
      truth_table[i].append(True)
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 5:
      truth_table[i].append(True) #
      truth_table[i].append(False)
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 6:
      truth_table[i].append(True)#
      truth_table[i].append(False)
      truth_table[i].append(True)
      truth_table[i].append(False)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 7:
      truth_table[i].append(True)#
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(True)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 8:
      truth_table[i].append(True)#
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 9:
      truth_table[i].append(False)#
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 10:
      truth_table[i].append(False)#
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(False)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 11:
      truth_table[i].append(False)#
      truth_table[i].append(True)
      truth_table[i].append(False)
      truth_table[i].append(True)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 12:
      truth_table[i].append(False)#
      truth_table[i].append(True)
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 13:
      truth_table[i].append(False) #
      truth_table[i].append(False)
      truth_table[i].append(True)
      truth_table[i].append(True)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 14:
      truth_table[i].append(False) #
      truth_table[i].append(False)
      truth_table[i].append(True)
      truth_table[i].append(False)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 15:
      truth_table[i].append(False) #
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(True)
      truth_table[i].append(calculate_row_risk(truth_table[i]))
    elif i == 16:
      truth_table[i].append(False) #
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(False)
      truth_table[i].append(calculate_row_risk(truth_table[i]))

  return truth_table

def print_truth_table(truth_table):
  print("\nTRUTH TABLE FOR HEART ATTACK RISK")

  row_size = 71

  for iteration in range(row_size):
      print("-", end = "")
  print()

  # print header rows
  for i in range(len(truth_table[0])):
    if i == 0:
      print("|", end = " ")
    print(f"{truth_table[0][i]:<12}", end = "| ")

  for i in range(1, len(truth_table)):
    print()

    for iteration in range(row_size):
      print("-", end = "")

    print()

    # print rows
    for j in range(len(truth_table[i])):
      if j == 0:
        print("|", end = " ")
      print(f"{str(truth_table[i][j]):<12}", end = "| ")

  print()

user_table = create_truth_table_all()
print_truth_table(user_table)

# Karnough map

def print_karnough_map():
  print("\nKARNOUGH MAP")
  empty = ""

  print("""
         W     |    _W
   -------------------------                      Legend
   |  T  |  T  |  F  |  F  | _Ao                  Ay = Age < 18
 Ay-----------------------------                  Ao = Age > 30
   |  T  |  T  |  T  |  F  |                      W = Weight > 60
----------------------------  Ao                  S = Smoker?
   |  F  |  T  |  T  |  F  |
_Ay-----------------------------
   |  F  |  F  |  F  |  F  | _Ao
   -------------------------
     _S  |     S     |  _S
  """)

print_karnough_map()

# Logic Statement
def create_logic_statements(truth_table):
  logic_statement = ""
  logic_statement_list = []
  # index 0 = Agey (Ay)
  # index 1 = Ageo (Ao)
  # index 2 = weight (W)
  # index 3 = Smoker (S)
  for i in range(1, len(truth_table)):
    if logic_statement != "":
      logic_statement_list.append(logic_statement)
    logic_statement = ""
    for j in range(0, len(truth_table[i])):
      if j == 0:
        if truth_table[i][j] == True:
          logic_statement += "Ay^"
        else:
          logic_statement += "_Ay^"

      if j == 1:
        if truth_table[i][j] == True:
          logic_statement += "Ao^"
        else:
          logic_statement += "_Ao^"

      if j == 2:
        if truth_table[i][j] == True:
          logic_statement += "W^"
        else:
          logic_statement += "_W^"

      if j == 3:
        if truth_table[i][j] == True:
          logic_statement += "S"
        else:
          logic_statement += "_S"
        logic_statement += " = " + str(truth_table[i][len(truth_table[i]) - 1])

  # logic_statement_list.append("SvWvH = True")
  return logic_statement_list

def get_true_statements(logic_statements):
  true_statements = []
  for statement in logic_statements:
    if "True" in statement:
      true_statements.append(statement)
  return true_statements

def print_logic_statments(logic_statments):
  print("\nLOGIC STATEMENTS")

  for i in range(len(logic_statments)):
    print("-" * 26)
    print(f"| {logic_statments[i]:<22} |")
  print("-" * 26)
  print()

def print_simplified_logic_statements():
  print("\nLOGIC STATEMENT")
  print("-" * 26)
  print("(Ay^W)v(Ao^S)")
  print("-" * 26)
  print()

#statments = create_logic_statements(user_table)
#true_statements = get_true_statements(statments)
#print_logic_statments(true_statements)
print_simplified_logic_statements()

# Venn diagram
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as mpatches

def create_venn_diagram():
    print("\nVENN DIAGRAM - HEART ATTACK RISK")

    fig, ax = plt.subplots(figsize=(14, 6))

    # Create 4 circles side by side with overlaps
    # W, Ay, Ao, S (left to right)

    # Define circle positions - arranged horizontally with overlaps
    circles = [
        Circle((2.8, 0.5), 0.45, facecolor='green', alpha=0.3, linewidth=2.5, edgecolor='black'),
        Circle((3.5, 0.5), 0.45, facecolor='red', alpha=0.3, linewidth=2.5, edgecolor='black'),
        Circle((4.2, 0.5), 0.45, facecolor='blue', alpha=0.3, linewidth=2.5, edgecolor='black'),
        Circle((4.9, 0.5), 0.45, facecolor='orange', alpha=0.3, linewidth=2.5, edgecolor='black')
    ]

    # Add circles to plot
    for circle in circles:
        ax.add_patch(circle)

    # Labels above each circle (moved higher to be outside)
    ax.text(2.8, 1.15, 'W', fontsize=18, fontweight='bold', ha='center')
    ax.text(3.5, 1.15, 'Ay', fontsize=18, fontweight='bold', ha='center')
    ax.text(4.2, 1.15, 'Ao', fontsize=18, fontweight='bold', ha='center')
    ax.text(4.9, 1.15, 'S', fontsize=18, fontweight='bold', ha='center')

    # Add descriptions below labels (also moved higher)
    ax.text(2.8, 1.0, '(Weight > 60)', fontsize=9, ha='center', style='italic')
    ax.text(3.5, 1.0, '(Age < 18)', fontsize=9, ha='center', style='italic')
    ax.text(4.2, 1.0, '(Age > 30)', fontsize=9, ha='center', style='italic')
    ax.text(4.9, 1.0, '(Smoker)', fontsize=9, ha='center', style='italic')

    # Mark the HIGH RISK intersection regions
    # W ∩ Ay (left intersection)
    ax.text(3.15, 0.5, 'HIGH\nRISK\n(true)', fontsize=9, ha='center', va='center',
            fontweight='bold', color='darkred',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.9, edgecolor='red', linewidth=2))

    # Ao ∩ S (right intersection)
    ax.text(4.55, 0.5, 'HIGH\nRISK\n(true)', fontsize=9, ha='center', va='center',
            fontweight='bold', color='darkred',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.9, edgecolor='red', linewidth=2))

    # Mark the LOW RISK intersection region
    # Ay ∩ Ao (middle intersection)
    ax.text(3.85, 0.5, 'LOW\nRISK\n(false)', fontsize=9, ha='center', va='center',
            fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9, edgecolor='blue', linewidth=2))

    # Mark the LOW RISK for variable only regions
    # Only W
    ax.text(2.8, 0.5, 'LOW\nRISK\n(false)', fontsize=9, ha='center', va='center',
            fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9, edgecolor='blue', linewidth=2))

    # Only Ay
    ax.text(3.5, 0.5, 'LOW\nRISK\n(false)', fontsize=9, ha='center', va='center',
            fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9, edgecolor='blue', linewidth=2))

    # Only Ao
    ax.text(4.2, 0.5, 'LOW\nRISK\n(false)', fontsize=9, ha='center', va='center',
            fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9, edgecolor='blue', linewidth=2))

    # Only S
    ax.text(4.9, 0.5, 'LOW\nRISK\n(false)', fontsize=9, ha='center', va='center',
            fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9, edgecolor='blue', linewidth=2))


    # Add note for Age 18-30 (outside all circles)
    ax.text(5.30, 0.05, 'Age 18-30:\nLOW RISK\n(false)',
            fontsize=9, ha='left', fontweight='bold', color='darkblue',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.9, edgecolor='blue', linewidth=2))

    # Set axis properties
    ax.set_xlim(1.6, 6.0)
    ax.set_ylim(-0.1, 1.4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    plt.title('Heart Attack Risk Assessment - Venn Diagram\nHigh Risk: (Ay ∧ W) ∨ (Ao ∧ S)',
              fontsize=18, fontweight='bold', pad=20)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='green', alpha=0.3, edgecolor='black', linewidth=2, label='W: Weight > 60'),
        mpatches.Patch(facecolor='red', alpha=0.3, edgecolor='black', linewidth=2, label='Ay: Age < 18'),
        mpatches.Patch(facecolor='blue', alpha=0.3, edgecolor='black', linewidth=2, label='Ao: Age > 30'),
        mpatches.Patch(facecolor='orange', alpha=0.3, edgecolor='black', linewidth=2, label='S: Smoker'),
        mpatches.Patch(facecolor='yellow', edgecolor='red', linewidth=2, label='HIGH RISK (true) zones'),
        mpatches.Patch(facecolor='lightgreen', edgecolor='blue', linewidth=2, label='LOW RISK (false) zones')
    ]
    ax.legend(handles=legend_elements, loc='lower center', fontsize=11, ncol=6,
              bbox_to_anchor=(0.512, -0.15))

    plt.tight_layout()
    plt.show()

create_venn_diagram()



# Logic circuit
def create_logic_circuit():
    print("\nLOGIC CIRCUIT DIAGRAM")
    print("-" * 21)
    print("""

    Ay (Age < 18)─────────────────\\
                                   AND────────────────\\
    W (Weight > 60)───────────────/                    \\
                                                        OR───────────────── HIGH RISK (True)
    Ao (Age > 30)─────────────────\\                    /
                                   AND────────────────/
    S (Smoker)────────────────────/


    """)
create_logic_circuit()