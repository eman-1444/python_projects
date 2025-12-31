from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt

# venn3 creates a new venn diagram, subsets are the data i guess? set_labels for labels of three main circles
# making all the subsets one gives the circles an equal value so they are the same size
# each subset corresponds to (Abc, aBc, ABc, abC, AbC, aBC, ABC)
# e.g if you changed the last 1 to 2, it would increase its size compared to the rest of the circles
# i think that means that each number is a weight for each circle/section?
# we stored the venn3 diagram in the diagram variable
diagram = venn3(subsets = (1, 1, 1, 1, 1, 1, 1), set_labels = ("A", "B", "C"))
# venn3_circles helps with customizing the venn3 diagram
circle_border = venn3_circles(subsets = (1, 1, 1, 1, 1, 1, 1), linestyle = "solid")

# axis turns on the "border" we see, its actually the x and y axis
# on just lets us see the hidden x and y axis
# plt is pyplot, the whole thing being used to make the diagram
# it also looks like the axis must be turned on after the venn diagram is made, otherwise it won't show up
plt.axis("on")

# plt.gca() gets the axis, set_facecolor sets the background color
plt.gca().set_facecolor("lightgrey")

# id = bit stream
# text = text in circle baseed on bit stream
# diagram is the venn diagram we created
diagram.get_label_by_id("100").set_text("a, b, c")
diagram.get_label_by_id("010").set_text("d, e, f")
diagram.get_label_by_id("110").set_text("k, m, n")

diagram.get_label_by_id("001").set_text("g, h, j")
diagram.get_label_by_id("011").set_text("s, t, u")
diagram.get_label_by_id("101").set_text("p, q, r")

diagram.get_label_by_id("111").set_text("v, w, x")

diagram.get_patch_by_id("111").set_color("white")

# creates title
plt.title("Venn Diagram")

# annotate to create label at x,y coordinate
plt.annotate("y, z", xy = (0, 0), xytext = (0.4, -0.5))
plt.annotate("U=23", xy = (0, 0), xytext = (-0.68, 0.65))

# outputs diagram
plt.show()