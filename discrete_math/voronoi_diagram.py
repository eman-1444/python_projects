import matplotlib.pyplot as plt
import numpy as np

def get_user_coordinates(iterations):
  for i in range(0, iterations):
    print("Enter coordinate #" + str(i + 1) + " (Seperate x and y with a space)")
    coordinate = input().split()
    coordinate = list(map(float, coordinate))
    coordinates.append(coordinate)
  return coordinates

def find_midpoint(coordinate1, coordinate2):
  mid_y = (coordinate2[1] + coordinate1[1]) / 2
  mid_x = (coordinate2[0] + coordinate1[0]) / 2
  return [mid_x, mid_y]


def find_slope(coordinate1, coordinate2):
  return (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])

def find_reciprocal(num):
  return (-1 / num)

# turn this into an equation with matplotlib
def find_equation(slope, midpoint, x):
  # y = y1 + m(x - x1)
  return midpoint[1] + slope * (x - midpoint[0])

def find_base(slope, midpoint):
  # y = y1 + m(x - x1)
  return midpoint[1] + slope * (-midpoint[0])

def set_coordinate_text(coordinates):
  for i in range(len(coordinates)):
    plt.text(coordinates[i][0], coordinates[i][1], "(" + str(coordinates[i][0]) + ", " + str(coordinates[i][1]) + ")")

def create_points(coordinates):
  for i in range(len(coordinates)):
    x = np.array([coordinates[i][0]])
    y = np.array([coordinates[i][1]])
    plt.plot(x, y, "o")

def create_perpendicular_bisector(coordinate1, coordinate2, line_name):
  midpoint = find_midpoint(coordinate1, coordinate2)
  midpoints.append(midpoint)

  slope = find_slope(coordinate1, coordinate2)
  slope = find_reciprocal(slope)

  x = np.linspace(-20, 20, 100)
  y = find_equation(slope, midpoint, x)
  line = y
  plt.plot(x, y, label = line_name)

  # coordinate text
  set_coordinate_text(coordinates)

  # coordinate point
  create_points(coordinates)
  return line

def find_distance(coordinate1, coordinate2):
  return np.sqrt(abs((coordinate2[0] - coordinate1[0])**2) + abs((coordinate2[1] - coordinate1[1])**2))

def find_closest_point(coordinates, new_coordinate):
  distances = []
  min = 9999999999
  closest_point = []
  for i in range(len(coordinates)):
    distances.append(find_distance(coordinates[i], new_coordinate))
    if min > distances[i]:
      min = distances[i]
      closest_point = coordinates[i]
  return closest_point

def find_intersection(slope1, base1, slope2, base2):
  return (base1 - base2) / (slope2 - slope1)


coordinates = []
midpoints = []
plt.figure(figsize = (8, 6))

user_coordinates = get_user_coordinates(3)

# sort list in ascending order of y
coordinates.sort(key = lambda coordinate: coordinate[1])

# test coordinates
# coordinates.append([0,1])
# coordinates.append([5,5])
# coordinates.append([2,8])

slope1 = find_slope(coordinates[0], coordinates[1])
slope1 = find_reciprocal(slope1)

slope2 = find_slope(coordinates[0], coordinates[2])
slope2 = find_reciprocal(slope2)

line1 = create_perpendicular_bisector(coordinates[0], coordinates[1], "1")
line2 = create_perpendicular_bisector(coordinates[0], coordinates[2], "2")
line3 = create_perpendicular_bisector(coordinates[1], coordinates[2], "3")

x_intersect = find_intersection(slope1, find_base(slope1, midpoints[0]), slope2, find_base(slope2, midpoints[1]))
y_intersect = find_equation(slope1, midpoints[0], x_intersect)

# linespace is the domain of the graph what will be shown
x = np.linspace(-20, 20, 100)

# sector 1
plt.fill_between(x, line1, -20, color="blue")

# sector 3
plt.fill_between(x, line1, max(line1), color="purple")
plt.fill_between(x, line2, max(line1), color="purple")

# sector 2
plt.fill_between(x, line1, line3, where = (line1 < y_intersect), color="yellow", interpolate=True)

print("Enter your new coordinate: ")
new_coordinate = input().split()
new_coordinate = list(map(float, new_coordinate))

closest_point = find_closest_point(coordinates, new_coordinate)

print("The closest point to " + str(new_coordinate) + " is " + str(closest_point))

plt.plot(new_coordinate[0], new_coordinate[1], "o")
plt.text(new_coordinate[0], new_coordinate[1], "(" + str(new_coordinate[0]) + ", " + str(new_coordinate[1]) + ")")

plt.xlim(-20, 20)
plt.ylim(-20, 20)

plt.legend()
plt.show()