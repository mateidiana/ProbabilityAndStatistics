import numpy
from matplotlib.pyplot import grid, xticks, show, ylabel, xlabel, title, hist, bar, legend
from numpy import random, argmax, array, mean, arange
from scipy.stats import binom
from random import randrange
#Labor 4: A1 Simulation  zufallige  Werte  fur X
# import numpy
# N=3
# x=[0,1,3,5]
# P=[0.4,0.1,0.3,0.2]
# rng = numpy.random.default_rng()
# r=rng.choice(x, size=N , replace=True, p=P)
# print(r)


# import numpy
# from matplotlib.pyplot import bar, show, grid, legend, xticks
# N=1000
# x=[0,1,3,5]
# P=[0.4,0.1,0.3,0.2]
# rng=numpy.random.default_rng()
# r=rng.choice(x, size=N, replace=True, p=P)
# X, count= numpy.unique(r,return_counts=True)
# bar(X, count/N, width=0.8,color="red",edgecolor="green", label="relative Haufigkeiten")
# bar(x,P,width=0.5,color="blue",edgecolor="black", label="theoretische Wkt")
# legend(loc="lower center")
# xticks(range(1,6))
# grid()
# show()

#A2

# N=1000
# x=[0,1,2,3,4]
# P=[0.25,0.35,0.25,0.1,0.05]
# rng=numpy.random.default_rng()
# r=rng.choice(x, size=N, replace=True, p=P)
# X, count= numpy.unique(r,return_counts=True)
# bar(X, count/N, width=0.8,color="red",edgecolor="green", label="relative Haufigkeiten")
# bar(x,P,width=0.5,color="blue",edgecolor="black", label="theoretische Wkt")
# legend(loc="lower center")
# xticks(range(1,6))
# grid()
# show()
# print("Anhand der Simulationen Wkt hochstens 1 Tippfehler", (count[0]+count[1])/N)
# print("Theoretische Wkt hochstens 1 Tippfehler", P[0]+P[1])
# E=numpy.mean(r)
# Et=sum([x[i]*P[i] for i in range(len(x))])
# print("Aus Simulationen sind durchschnittlich ", E, "Tippfehler")
# print("Theoretisch sind durchschnittlich ", Et, "Tippfehler")


# #Labor 4: A3 Beispiel
# from scipy.stats import binom
# N=10;n=8; p=0.5
# X = binom.rvs(n, p,size= N)
# print(N,"zufallige Werte fur X:")
# print(X)
# k=5
# w=binom.pmf(k,n,p)
# print("binom.pmf(",k,",",n,",",p,") berechnet die Wkt. P( X =",k,f")={w:.5f}")
#
# N=1000
# r=binom.rvs(n, p,size= N)
# P=[binom.pmf(i,n,p) for i in range (n+1)]
# rng=numpy.random.default_rng()
# X, count= numpy.unique(r,return_counts=True)
# bar(X, count/N, width=0.8,color="red",edgecolor="green", label="relative Haufigkeiten")
# bar(X,P,width=0.5,color="blue",edgecolor="black", label="theoretische Wkt")
# k=1
# w=binom.pmf(k,n,p)
# print("binom.pmf(", k, "," , n, ",", p, ") berechnet die Wkt. P( X =",k,f")={w:.5f}")
# xticks(range(0,n+1))
# show()

#A4

# from scipy.stats import binom
# N=1000
# n=8
# p=0.5
# R=binom.rvs(n,p,size=N)
#
# X, count = numpy.unique(R, return_counts=True)
# P=[binom.pmf(i,n,p) for i in range(n+1)]
#
# print("Aus Simulationen: Wkt hochstens 3 Rechner angegriffen", sum([count[i]/N for i in range(4)]))
# print("Theoretisch: Wkt hochstens 3 Rechner angegriffen", binom.pmf(3,n,p))
#
# print("Aus Simulationen: Wkt miindestens 4 Rechner angegriffen", sum([count[i]/N for i in range(4,8)]))
# print("Theoretisch: Wkt mindestens 4 Rechner angegriffen", 1-binom.cdf(4,n,p)+binom.pmf(4,n,p))
#
# print("Aus Simulationen: Wkt genau 4 Rechner angegriffen", count[4]/N)
# print("Theoretisch: Wkt genau 4 Rechner angegriffen", binom.pmf(4,n,p))

def ex1():
    # Generieren von zufalligen Werten der ZG: X ∼ /0   1   3   5  \
    #                                              \0.4 0.1 0.3 0.2/
    # Simulation von zufalligen Werten fur X in Python:
    n = 1000
    x = [0, 1, 3, 5]
    p = [0.4, 0.1, 0.3, 0.2]
    rng = numpy.random.default_rng()
    data = rng.choice(x, size=n, replace=True, p=p)
    results, count = numpy.unique(data, return_counts=True)

    # Man erstelle das Histogramm der relativen Haufigkeiten fur 1000 zufallige Werte von X. Auf demselben Bild
    # zeichne man auch die Balken fur die theoretischen Wahrscheinlichkeiten.
    bar(results, count / n, width=0.9, color="red", edgecolor="black", alpha=0.4, label="Relative probability")
    bar(x, p, width=0.7, color="blue", edgecolor="black", alpha=0.5, label="Theoretical probability")
    legend(loc="lower left")
    xticks(range(min(x), max(x) + 1))
    grid()
    show()


def ex2():
    # Uber die Zufallsgroße X ist Anzahl von Fehlern in den online Artikeln einer bestimmten Zeitung ist bekannt:
    # in 25% der Artikeln sind keine Tippfehler, in 35% der Artikel ist ein Tippfehler, in 25% der Artikel sind zwei, in
    # 10% drei und auf dem Rest vier Tippfehler.
    # a) Man generiere zufallige Werte fur X.
    simulations = 1000
    errors = [0, 1, 2, 3, 4]
    probability = [0.25, 0.35, 0.25, 0.10, 0.05]
    rng = numpy.random.default_rng()
    data = rng.choice(errors, size=simulations, replace=True, p=probability)
    values, count = numpy.unique(data, return_counts=True)

    # b) Man schatze anhand der Simulationen die Wahrscheinlichkeit, dass hochstens 1 Tippfehler in einem zufallig
    # gewahlten Artikel auftaucht.
    print(f"Probability of max 1 error: {(count[0] + count[1]) / simulations}")

    # c) Wie viele Tippfehler sind durchschnittlich (im Mittel) in einem online Artikel dieser Zeitung zu erwarten, d.h.
    # man verlangt die Schatzung von dem Erwartungswert E(X). Man berechne den theoretischen Erwartungswert.
    print(f"Average error count: {numpy.mean(data)}")
    print(f"Theoretical average error count: {sum(x * p for x, p in zip(errors, probability))}")


# Man generiere N (z.B. 1000) Werte der Zufallsgr¨oße X mit binomialer Verteilung X ∼ Bino(n, p) mit
# n = 8, p = 0.5. Man benutze hierf¨ur scipy.stats.binom.rvs.
# ▶ Man erstelle das Histogramm der relativen H¨aufigkeiten der zuf¨alligen Werten von X. Auf demselben Bild
# zeichne man auch die Balken f¨ur die theoretischen Wahrscheinlichkeiten, f¨ur diese benutze man
# scipy.stats.binom.pmf.
def ex3():
    n = 1000
    max_value = 8
    probability = 0.5
    all_values = []

    for i in range(max_value + 1):
        all_values.append(i)

    x = binom.rvs(max_value, probability, size=n)
    w = binom.pmf(all_values, max_value, probability)

    bar(all_values, w, width=0.9, color="red", edgecolor="black", label="Theor. Wkt ")
    xticks(range(0, max_value + 1))

    xx, count = numpy.unique(x, return_counts=True)
    bar(xx, count / n, width=0.6, color="blue", edgecolor="black", label="Rel. Haufigkeiten ")

    legend(loc="upper right")

    grid()
    show()


def ex4():
    # In einem Computerpool sind 7 Rechner. Die Wahrscheinlichkeit, dass ein neuer Virus
    # einen Rechner angreift ist 0.4, unabhangig von anderen Rechnern.
    #
    # Man gebe die Antworten anhand Simulationen (binom.rvs) und vergleiche diese mit den theoretischen
    # Wahrscheinlichkeiten (hierfur benutze man binom.cdf, binom.pmf).

    simulations = 1000
    nr_computers = 7
    probability = 0.4
    values_sim = binom.rvs(nr_computers, probability, size=simulations)

    # Welche ist die Wahrscheinlichkeit, dass der Virus:
    # a) hochstens 3 Rechner
    count = 0
    for value in values_sim:
        if value <= 3:
            count += 1
    print(f"Max 3 computers (simulation): {count / simulations}")
    theoretical = binom.cdf(3, nr_computers, probability)
    print(f"Theoretical: {theoretical:.3f}")

    # b) mindestens 4 Rechner
    count = 0
    for value in values_sim:
        if value >= 4:
            count += 1
    print(f"Min 4 computers (simulation): {count / simulations}")
    theoretical = 1 - binom.cdf(3, nr_computers, probability)
    print(f"Theoretical: {theoretical:.3f}")

    # c) genau 4 Rechner angreift?
    count = 0
    for value in values_sim:
        if value == 4:
            count += 1
    print(f"Genau 4 computers (simulation): {count / simulations}")
    theoretical = binom.pmf(4, nr_computers, probability)
    print(f"Theoretical: {theoretical:.3f}")


def ex5():
    # Anzahl der Simulationen
    num_simulations = 500

    results = []
    for _ in range(num_simulations):
        generated_numbers = random.choice(arange(1, 4), size=1000, p=[1 / 3] * 3)
        # Suche nach der Position der ersten 3 in den generierten Zahlen
        first_occurrence_index = argmax(generated_numbers == 3)
        # Anzahl der generierten Zahlen vor der ersten 3
        x = first_occurrence_index + 1
        results.append(x)

    hist(results, bins=arange(1, max(results) + 2) - 0.5, density=True, edgecolor='black')
    title('Histogram of X: Number of Generated Numbers before First 5')
    xlabel('X')
    ylabel('Probability')
    show()

    # P(X ≤ 3)
    probability_x_leq_3 = mean(array(results) <= 3)
    # P(X > 3)
    probability_x_gt_3 = mean(array(results) > 3)
    # Erwartungswert E(X)
    expectation_x = mean(results)
    # Schätzung durchführen
    # Ergebnisse ausgeben
    print(f"Estimated Probability P(X <= 3): {probability_x_leq_3}")
    print(f"Estimated Probability P(X > 3): {probability_x_gt_3}")
    print(f"Estimated Expectation E(X): {expectation_x}")

def ex6():
    #ahnlich mit A1
    N = 1000
    X = []

    for i in range(N):
        U = randrange(1, 4)
        print("U= ", U)
        c = 0
        while U != 3:
            U = randrange(1, 4)

            c += 1
        X.append(c)

    z, count = numpy.unique(X, return_counts=True)
    bar(z, count / N, width=0.9, color="red", edgecolor="black", label="relative Haufigkeiten")
    xticks(range(0, max(X)))
    show()


def main():
    #ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    ex6()


if __name__ == "__main__":
    main()








