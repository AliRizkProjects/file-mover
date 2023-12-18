# Namen: Ali Rizk & Zohreh Asadi
# Tutor: Oskar


# A68

# b)
"""
Beweis durch Widerspruch:

- Wir nehmen an, der Graph hat keine Zyklen.
- Nun betrachten wir eine Kante (u,v) mit T2Nummer[v] > T2Nummer[u] (Knoten v wird während der Tiefensuche später beendet als Knoten u)
- Unsere Annahme war: Graph hat keine Zyklen, d.h. v muss entweder ein Kind oder ein Enkelknoten von u sein
- da die Tiefensuche rekursiv ist und die T2Nummern in aufsteigender Reihenfolge vergeben werden 
    => v wird erst dann beendet, nachdem alle Nachfolger von v vollständig bearbeitet worden sind
- wenn v ein Kindknoten von u ist, dann gibt es eine Kante (u,v), die zur Erzeugung des Baumes beiträgt.
    - v ist aber kind von u, also wurde v vor u beendet => Widerspruch
[]
"""

# c)

"""
Psuedocode mit annahme, dass T2 nummerierung bereits durchgefphrt wurde

stack = []
topological_order = []

# sortieren
for u in sortiere_nach_absteigenden_T2Nummern():
    stack.append(u)

# Topologisch sortieren
while stack nicht leer ist:
    u = stack.pop()
    topological_order.append(u)
"""

# d)
"""
Pseudo-Code:
1. wähle einen nicht besuchten Knoten u
2. führe Tiefensuche (wie im Code) aus, und markiere alle besuchten Knoten
3. wenn die Tiefensuche beendet ist (alle Nachbarn von u wurden besucht), füge u oben auf den stack hinzu
4. wiederhole Schritt 1-3, bis alle Knoten besucht wurden
"""

# -----------------------------------

# A69

"""
PDF
"""

#------------------------------------

# A70

# a)

def experiment(z):
    
    # Die Zahlen 0, 1, . . . , 1023 werden auf 1024 Fächer verteilt
    faecher = [0] * 1024

    for i in range(1024):
        # die Zahl i kommt in das Fach mit der Nummer f_z(i) := (z*i) mod 1024
        fach_nummer = (z*i) % 1024
        faecher[fach_nummer] += 1
    
    # vollstes fach bestimmen
    vollstes_fach = max(faecher)
    
    return vollstes_fach

z_werte = [0, 1, 2, 3, 4, 5, 10, 17]

for z in z_werte:
    vollstes_fach = experiment(z)
    print(f'Für z = {z}: Das vollste Fach wird mit {vollstes_fach} belegt.')


# Antwort: das vollste Fach hat 1024 Zahlen mit z=0


# b)

"""
Vermutung: f_z ist eine Permutation der Menge, wenn ggT(z, 1024) = 1
"""