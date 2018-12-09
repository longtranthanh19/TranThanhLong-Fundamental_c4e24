import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot
# Prepare Data

machine_counts = [18, 4, 2]
# Prepare Labels

machine_name = ["PC", "Mac", "Linux"]

# Draw Pie

pyplot.pie(machine_counts, labels = machine_name, autopct="%.1f%%", shadow=True, explode=[0, 0.1, 0])
pyplot.title("PC vs Mac vs Linux Usage")
pyplot.axis("equal")
# Show Pie

pyplot.show()