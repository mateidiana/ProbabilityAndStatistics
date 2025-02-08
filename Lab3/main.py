import random
import numpy
from random import randrange
from matplotlib.pyplot import bar, show, grid, legend, xticks
from math import comb

# # 1 In einer Urne sind 6 rote Kugeln, 4 blaue Kugeln und 6 gr¨une Kugeln. Man zieht 3 Kugeln
# hintereinander ohne Zur¨ucklegen. Man betrachtet die Ereignisse:
# A:“mindestens eine rote Kugel wurde entnommen”
# B:“alle entnommenen Kugeln haben dieselbe Farbe”.
# 1) Anhand Simulationen sch¨atze man die Wahrscheinlichkeiten P(A), P(B), P(A ∩ B), P(B|A).
# 2) Man gebe auch die theoretischen Wahrscheinlichkeiten an f¨ur P(A), P(B), P(A ∩ B), P(B|A).

def ex1():
    countA = 0
    countB = 0
    countAB = 0
    n = 1000
    for i in range(n):
        kugeln = random.sample(['r', 'b', 'g'], counts=[6, 4, 6], k=3)
        if 'r' in kugeln:
            countA += 1
        if len(set(kugeln)) == 1:
            countB += 1
        if 'r' in kugeln and len(set(kugeln)) == 1:
            countAB += 1

    print('Simulationen')
    print('P(A) ' + str(countA / n))
    print('P(B) ' + str(countB / n))
    print('P(A and B) ' + str(countAB / n))
    print('P(B mit A) ' + str(countAB / countA))

    probA = 1 - (10 / 16 * 9 / 15 * 8 / 14)
    probB = (6 / 16 * 5 / 15 * 4 / 14) + (6 / 16 * 5 / 15 * 4 / 14) + (4 / 16 * 3 / 15 * 2 / 14)
    print('Theoretisch')
    print('P(A) ' + str(probA))
    print('P(B) ' + str(probB))
    print('P(A and B) ' + str(probA * probB))
    probAB = (probA * probB)
    print('P(B mit A) ' + str((probAB / probA)))


# # 2
def ex2():
    N = 2000
    daten = [randrange(1, 7) for _ in range(N)]
    print(daten)
    z, count = numpy.unique(daten, return_counts=True)
    d = dict([(z[i], count[i] / N) for i in range(0, 6)])
    print(d)
    bar(z, count / N, width=0.9, color="red", edgecolor="black", label="relative Haufigkeiten")
    D = dict([(k, 1 / 6) for k in range(1, 7)])
    bar(D.keys(), D.values(), width=0.7, color="blue", edgecolor="black", label="theoretische Wahrscheinlichkeiten")
    legend(loc="lower left")
    xticks(range(0, 7))
    grid()
    show()


# # 3 Drei W¨urfel werden geworfen. Das Spiel gewinnt derjenige, der die Summe der drei aufgetauchten
# Zahlen vorhersagt.
# (1)Man simuliere dieses Spiel N-mal (z.B. 1000), man erstelle das Histogramm der relativen H¨aufigkeiten.
# Auf demselben Bild zeichne man auch die Balken f¨ur die theoretischen Wahrscheinlichkeiten. Man
# vergleiche die theoretischen Ergebnisse mit den erhaltenen Werten aus den Simulationen.
# (2) Auf welche Zahl (oder Zahlen) muss man wetten, um die gr¨oßten Gewinnchancen zu haben?
# (3) Welche ist die theoretische Wahrscheinlichkeit, dass diese Zahl (oder Zahlen) auftaucht? Man
# vergleiche das theoretische Resultat mit den erhaltenen Ergebnissen der Simulationen.
def ex3():
    N = 500
    daten1 = [randrange(1, 7) for _ in range(N)]
    daten2 = [randrange(1, 7) for _ in range(N)]
    daten3 = [randrange(1, 7) for _ in range(N)]
    sum_of_arrays = numpy.array(daten1) + numpy.array(daten2) + numpy.array(daten3)

    z, count = numpy.unique(sum_of_arrays, return_counts=True)
    print(z, count / N)

    bar(z, count / N, width=0.9, color="red", edgecolor="black", label="relative Haufigkeiten")

    s = []
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                s.append(i + j + k)
    zs, counts = numpy.unique(s, return_counts=True)

    bar(zs, counts / len(s), width=0.6, color="yellow", edgecolor="black", label="Theoretische Wahrscheinlichkeiten")

    ms = max(count)
    for i in range(len(z)):
        if count[i] == ms:
            print("(Aus Simulationen) Man wette auf die Summe:", z[i], "diese hat die relative Haufigkeit:",
                  count[i] / N)

    M = max(counts)
    for i in range(len(zs)):
        if counts[i] == M:
            print("(Theoretisch) Man wette auf die Summe:", zs[i], "diese hat die theor Wahrsch:", counts[i] / len(s))

    legend(loc="lower center")
    xticks(range(3, 19))
    grid()
    show()


# 4 Welche Wahrscheinlichkeiten p1, p2, p3 sch¨atzt folgendes Programm? Welche sind die theoretischen
# Werte f¨ur p1, p2, p3?
def ex4():
    c1, c2, a1, a2 = 0, 0, 0, 0
    N = 10000
    A = list(range(1, 21))
    for _ in range(N):
        i = numpy.random.randint(len(A))
        v = A[i]
        c1 = c1 + (v % 2)  # wie viele ungerade
        c2 = c2 + ((v % 2) == 0)  # wie viele zahlen gerade
        a1 = a1 + (v % 2) * ((v % 3) == 0)  # zahlt ob v ungerade ist und teilbar durch 3
        a2 = a2 + ((v % 2) == 0) * (6 <= v and v <= 10)  # zahlt ob v gerade und zw 6 und 10
    p1 = a1 / c1
    p2 = a2 / c2
    p3 = c1 / N
    print("Aus den Simulationen :")
    print(f"p1=",
          p1)  # Bedingte Wahrsch, eine zufallige Zahl aus A ist teilbar durch 3 wenn man weiss, die Zahl ist ungerade
    print(f"p2=",
          p2)  # Bedingte Wahrsch, eine zufallige Zahl aus A ist 6 7 8 9 od 10 wenn man weiss die Zahl ist gerade
    print(f"p3=", p3)  # Bedingte Wahrsch, eine zufallige Zahl aus A ist ungerade

    w1 = 3 / 10
    w2 = 3 / 10
    w3 = 10 / 20

    print("Theoretusche Wkt :")
    print(f"w1=",
          w1)  # Bedingte Wahrsch, eine zufallige Zahl aus A ist teilbar durch 3 wenn man weiss, die Zahl ist ungerade
    print(f"w2=",
          w2)  # Bedingte Wahrsch, eine zufallige Zahl aus A ist 6 7 8 9 od 10 wenn man weiss die Zahl ist gerade
    print(f"w3=", w3)  # Bedingte Wahrsch, eine zufallige Zahl aus A ist ungerade


def ex5():
    # Welche ist die Wahrscheinlichkeit, dass in einer Gruppe von 5 Personen genau zwei Personen
    # Geburtstag im selben Monat haben und die anderen drei Personen verschiedene Geburtstage haben?
    # a) Man lose die Aufgabe anhand Simulationen.
    num_simulations = 100000
    count_successful = 0  # Zählt die erfolgreichen Simulationen
    for _ in range(num_simulations):
        birthdays = [random.randint(1, 12) for _ in range(5)]  # Zufällige Auswahl von Geburtsmonaten
        # Überprüfen, ob genau zwei Personen im selben Monat Geburtstag haben und die anderen drei verschieden sind
        if len(birthdays) == len(set(birthdays)) + 1:
            count_successful += 1
    probability = count_successful / num_simulations
    print(f"Simulierte Wahrscheinlichkeit: {probability}")

    # b) Man gebe die theoretische Wahrscheinlichkeit an. Annahme:
    # die Wahrscheinlichkeit, dass eine zufallig gewahlte Person Geburtstag in einem bestimmten Monat hat ist 1/12
    total_outcomes = 12 ** 5
    ways_two_shared = comb(5, 2)
    ways_remaining = 11 * 10 * 9
    print(ways_two_shared)
    probability = ways_two_shared * ways_remaining / total_outcomes
    print(f"Thoretical probability: {probability}")


def ex6():
    # Man schatze anhand Simulationen die Wahrscheinlichkeit, dass beim zweimaligen Werfen eines
    # Wurfels die Summe der Zahlen mindestens 7 ist (Summe ≥ 7),
    # a) unter der Bedingung, dass beim ersten Wurf eine 4 erhalten wurde;\
    num_simulations = 100000
    count_successful = 0
    for _ in range(num_simulations):
        first_throw = 4
        second_throw = random.randint(1, 6)
        if first_throw + second_throw >= 7:
            count_successful += 1
    probability = count_successful / num_simulations
    print(f"Simulierte Wahrscheinlichkeit unter Bedingung a): {probability}")

    # b) unter der Bedingung, dass beim zweiten Wurf eine gerade Zahl erhalten wurde.
    num_simulations = 100000
    count_successful = 0
    for _ in range(num_simulations):
        first_throw = random.randint(1, 6)
        second_throw = random.choice([2, 4, 6])
        if first_throw + second_throw >= 7:
            count_successful += 1
    probability = count_successful / num_simulations
    print(f"Simulierte Wahrscheinlichkeit unter Bedingung b): {probability}")

    # c) Welche sind die theoretischen Wahrscheinlichkeiten bei a), bzw. b) ?
    # a) begins with 4 => 3, 4, 5 or 6 are needed => probability = 4/6
    # b) case 1: 2 => 5, 6              => 2/6
    #    case 2: 4 => 3, 4, 5, 6        => 4/6      => probability = (2/6 + 4/6 + 6/6)/3
    #    case 3: 6 => 1, 2, 3, 4, 5, 6  => 6/6


def main():
    # ex1()
    #ex2()
    # ex3()
    # ex4()
    #ex5()
    ex6()


if __name__ == "__main__":
    main()


