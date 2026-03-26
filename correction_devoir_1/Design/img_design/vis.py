import matplotlib.pyplot as plt

# GestionTransport, plan_voyage, gestion_reservation, gestionPaiement, config_space
I = [0, 0.5, 1, 0, 0]
A = [2/9, 1/6, 1/5, 0, 1/5]
labels = [
    "GestionTransport",
    "plan_voyage",
    "gestion_reservation",
    "gestionPaiement",
    "config_space"
]
offsets = [
    (45, 5),    # GestionTransport
    (-20, 10),  # plan_voyage
    (-45, -15),  # gestion_reservation
    (45, 5),     # gestionPaiement
    (35, -15)   # config_space
]

plt.xlabel('I')
plt.ylabel('A')
plt.axis([0, 1, 0, 1])
plt.title('Graphe IA')
plt.axline((0, 1), (1, 0), color='red', linestyle='--', zorder=1)
plt.scatter(I, A, zorder=3, clip_on=False)

for x, y, label, (dx, dy) in zip(I, A, labels, offsets):
    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(dx, dy),
        ha='center'
    )

plt.savefig("correction_devoir_1/Design/img_design/graph.svg", format="svg")
plt.show()