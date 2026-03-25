import matplotlib.pyplot as plt

x = [0, 0.5, 1, 0, 0]
y = [2/9, 1/6, 1/5, 0, 1/5]
plt.xlabel('I')
plt.ylabel('A')
plt.axis([0, 1, 0, 1])
plt.title('Graphe IA')
plt.axline((0, 1), (1, 0), color='red', linestyle='--', zorder=1)
plt.scatter(x, y, zorder=3, clip_on=False)
plt.savefig("correction_devoir_1/Design/img_design/graph.svg", format="svg")
plt.show()