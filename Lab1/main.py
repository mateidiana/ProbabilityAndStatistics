import random
from math import factorial, perm
import itertools
from itertools import permutations, combinations
from more_itertools import distinct_permutations
from itertools import combinations_with_replacement

# help("random.sample")
# help("math.factorial")
# help("itertools.permutations")


print(perm(4,4))
print(perm(4,2))

print("Alle Permutationen von ABC",list(permutations("ABC")))
print("Alle Kombinationen von ABC je 2", list(combinations("ABC", 2)))

# #1 a Man generiere alle Permutationen von sicher. Wie viele solche Permutationen gibt es?
print("Alle Permutationen von sicher", list(permutations("sicher")))
print(len(list(permutations("sicher"))))

# #b Man generiere zwei zuf¨allige Permutationen von sicher.
print("Zwei zufallige Permutationen von sicher", random.sample(list(permutations("sicher")),2))

# #c Man generiere alle Variationen je zwei Buchstaben aus dem String sicher. Wie viele solche Variationen gibt
# es?
print("Alle Variationen je 2 Buchstaben von sicher", list(permutations(list("sicher"),2)))

# #d Welche ist die gesamte Anzahl der Variationen je 3 Buchstaben von MATHE?
print(len(list(permutations(list("MATHE"),3))))

# #e Man generiere alle Kombinationen (d.h. alle Anordnungen ohne Wiederholung, ohne Ber¨ucksichtigung der
# Reihenfolge) je 3 Buchstaben aus dem String MATHE.
print(list(combinations(list("MATHE"),3)))

# #f Welche ist die gesamte Anzahl der Kombinationen je 3 Buchstaben von MATHE?
print(len(list(combinations(list("MATHE"),3))))

# #2
M=list(distinct_permutations("AABB"))
print(M)
m = len(M)
print("Anzahl Permutationen von AABB mit Wiederholung:",m)

for p in distinct_permutations("1112"):
    print("".join(p))

n= list(distinct_permutations("1112"))
n = len(n)
print("Anzahl Permutationen von 1112 mit Wiederholung:",n)

# #3
M = list(combinations_with_replacement("ABC",2))
print("Alle Kombinationen von ABC je 2, mit Wiederholung",M)

k = len(M)
print("Anzahl Kombinationen von ABC je 2 mit Wiederholung:",k)

# Wie viele Mo¨glichkeiten gibt es 6 rote Kugeln in 4 Kartons aufzuteilen? Manche Kartons ko¨nnen leer
# bleiben. Man z¨ahle alle m¨oglichen Anordnungen auf. Hinweis: Wir bezeichnen die vier Kartons mit 1,2,3,4.
# Eine m¨ogliche Anordnung ist: [1,1,2,3,3,3], d.h. 2 Kugeln im Karton ”1”, eine Kugel im Karton ”2”, 3 Kugeln
# im Karton ”3” und keine Kugel im Karton ”4”.
print(list(itertools.combinations_with_replacement("1234",6)))
print(len(list(itertools.combinations_with_replacement("1234",6))))
