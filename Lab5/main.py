import scipy
from numpy import random
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, uniform
import random

# Teepackungen, die von einer bestimmten Firma abgef¨ullt werden, sollten mit jeweils 200 g Inhalt
# abgef¨ullt werden. Die abgef¨ullte Menge Tee X in einer Packung ist normal verteilt X ∼ N(μ, σ2); die daf¨ur
# zust¨andige Abf¨ullmaschine hat eine Standardabweichung von σ = 3 g und ist auf einen Erwartungswert
# μ = 199 g eingestellt.
# a) Anhand 1000 simulierten Daten, welche ist im Mittel die abgef¨ullte Menge Tee in einer Packung?
# b) Mit welcher Wahrscheinlichkeit werden in einer Packung weniger als 195 g Tee abgef¨ullt? Mit welcher
# Wahrscheinlichkeit werden in einer Packung zwischen 195 g und 198 g Tee abgef¨ullt? Mit welcher
# Wahrscheinlichkeit werden in einer Packung mehr als 195 g Tee abgef¨ullt? Man vergleiche das Ergebnis
# mit den theoretischen Wahrscheinlichkeiten.
# c) Die generierten Daten der Stichprobe sollen in 16 Klassen (Intervallen) eingeteilt und man zeichne das
# entsprechende Histogramm der relativen H¨aufigkeiten mit hist..
# d) Mit Hfg, Klasse=numpy.histogram(Daten, bins=16) z¨ahle man wie viele Daten in jeder Klasse sind
# (ausdrucken mit print).
def ex1():
    mu = 199
    sigma = 3
    N = 1000
    Daten = norm.rvs(mu, sigma, N)
    print("Im Mittel sind in einem Beutel ", np.mean(Daten), "g Tee")
    print("Die Wkt dass im Beutel weniger als 195g Tee sind, ist schatzungsweise", np.mean(Daten < 195))
    print("Die theoretische Wkt dass die Beutel weniger als 195g Tee sind, ist", norm.cdf(195, mu, sigma))
    print("Die Wkt, dass im Beutel zw 195 und 198 g Tee sind, ist", np.mean((Daten >= 195) & (Daten <= 198)))
    print("Die theoretische Wkt, dass im Beutel zw 195 und 198 g Tee sind",
          norm.cdf(198, mu, sigma) - norm.cdf(195, mu, sigma))
    print("Die Wkt, dass im Beutel mehr als 195g sind, ist", np.mean(Daten > 195))
    print("Die theoretische Wkt, dass im Beutel mehr als 195g sind, ist", 1 - norm.cdf(195, mu, sigma))

    Anzahl_bins = 16
    plt.hist(Daten, bins=Anzahl_bins, density=True, edgecolor="black", label="rel. Hfg")
    x = np.linspace(min(Daten), max(Daten), 100)
    plt.plot(x, norm.pdf(x, mu, sigma), label="Dichtefunktion")
    plt.legend(loc="upper left")
    plt.show()

    Hfg, Klasse = np.histogram(Daten, bins=Anzahl_bins)
    for i in range(Anzahl_bins - 1):
        print(f"({i + 1:2d}) absolute Hfg {Hfg[i]:3d} der Klasse [{Klasse[i]:8.4f}, {Klasse[i + 1]:8.4f}]")

def ex2():
    # Die Zeit T (in Sekunden), die ein Drucker benotigt, um ein Werbeplakat zu drucken, folgt einer
    # Exponentialverteilung Exp(α) mit dem Parameter α = 1/12

    # a) Man simuliere N = 1000 Daten fur eine Stichprobe.
    # Welche ist die durchschnittliche Druckzeit fur das Drucken eines Plakats?
    n = 1000
    alpha = 1 / 12
    data = expon.rvs(loc=0, scale=1 / alpha, size=n)
    mean = np.mean(data)
    print("Mean is: ", mean)

    # b) Man zeichne ein Histogramm mit 12 Klassen fur die simulierten Daten und auf demselben Bild zeichne
    # man die Dichtefunktion scipy.stats.expon.pdf(x,loc=0,scale=1/alpha).
    hist, bins, _ = plt.hist(data, bins=12, density=True, edgecolor='black', label='Histogram')
    x = np.linspace(min(bins), max(bins), 1000)
    pdf_values = expon.pdf(x, loc=0, scale=1 / alpha)
    plt.plot(x, pdf_values, label='Exponential PDF')
    plt.title('Histogram and Exponential PDF of Print Time')
    plt.xlabel('Print Time (seconds)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.show()
    # Additional part for printing class information
    hfg, klassen = np.histogram(data, bins=12)
    for i in range(len(hfg)):
        print(f"Klasse {i + 1:2d}: {hfg[i]:3d} Daten, [{bins[i]:8.4f}, {bins[i + 1]:8.4f}]")

    # c) Man schatze danach die Wahrscheinlichkeiten P(T < 20), P(T > 10), P(10 < T < 30).
    probability_less_than_20 = np.mean(data < 20)
    probability_greater_than_10 = np.mean(data > 10)
    probability_between_10_and_30 = np.mean((data > 10) & (data < 30))

    # Man vergleiche das Ergebnis mit den theoretischen Wahrscheinlichkeiten, welche man mit
    # scipy.stats.expon.cdf(x,loc=0,scale=1/alpha) berechnet.
    theoretical_probability_less_than_20 = expon.cdf(20, loc=0, scale=1 / alpha)
    theoretical_probability_greater_than_10 = 1 - expon.cdf(10, loc=0, scale=1 / alpha)
    theoretical_probability_between_10_and_30 = expon.cdf(30, loc=0, scale=1 / alpha) - expon.cdf(10, loc=0,
                                                                                                  scale=1 / alpha)

    print(f"Estimated Probability T < 20: {probability_less_than_20}")
    print(f"Theoretical Probability T < 20: {theoretical_probability_less_than_20}\n")

    print(f"Estimated Probability T > 10: {probability_greater_than_10}")
    print(f"Theoretical Probability T > 10: {theoretical_probability_greater_than_10}\n")

    print(f"Estimated Probability 10 < T < 30: {probability_between_10_and_30}")
    print(f"Theoretical Probability 10 < T < 30: {theoretical_probability_between_10_and_30}")

    # d) Die generierten Daten der Stichprobe wurden in 12 Klassen (Intervallen) eingeteilt. Man zahle und
    # gebe an wie viele Daten in jeder Klasse sind, und man zeichne auf einem neuen Bild das entsprechende
    # Histogramm der absoluten Haufigkeiten.
    # matplotlib.pyplot.hist(Daten,bins=12,density=False,edgecolor="black",label="absolute Hfg.")
    absolute_hfg, bins = np.histogram(data, bins=12)

    # Print the counts in each class
    for i in range(len(absolute_hfg)):
        print(f"Klasse {i + 1:2d}: {absolute_hfg[i]:3d} Daten, [{bins[i]:8.4f}, {bins[i + 1]:8.4f}]")

    # Draw the histogram of absolute frequencies
    plt.hist(data, bins=12, density=False, edgecolor="black", label="absolute Hfg.")
    plt.xlabel('T')
    plt.ylabel('Absolute Frequency')
    plt.title('Histogram of Absolute Frequencies')
    plt.legend()
    plt.show()

    # e) Auf einem anderen Bild zeichne man auf dem Intervall [0, 10] die Dichtefunktion der Exp(1) Verteilung.
    # Generate x values for the plot
    x_values = np.linspace(0, 10, 100)

    # Calculate the corresponding y values using the density function of Exp(1)
    y_values = expon.pdf(x_values, loc=0, scale=1)

    # Plot the density function
    plt.plot(x_values, y_values, 'r-', label='Density Function (Exp(1))')

    # Set plot labels and title
    plt.xlabel('T')
    plt.ylabel('Density')
    plt.title('Density Function of Exp(1) Distribution')
    plt.legend()
    plt.show()

def ex3():
    # Jedesmal, wenn Professor X eine Gruppe von 6 Personen trifft, wettet er 6 e, dass mindestens
    # zwei von diesen 6 Personen im gleichen Monat Geburtstag haben. Anhand Simulationen sch¨atze man:
    # den durchschnittlichen Gewinn oder Verlust bei dieser Wette, bzw. die Wahrscheinlichkeit p, mit welcher
    # Professor X eine Wette gewinnt.

    N = 1000
    x = [-6, 6]
    p = 1 - (12 * 11 * 10 * 9 * 8 * 7) / (12 ** 6)
    P = [1 - p, p]
    Zfg_Zahlen = random.choices(x, weights=P, k=N)
    print("Die Wkt, mit welcher Prof x eine Wette gewinnt, ist", p)
    print("Anhand Simulationen gewinnt der Professor im Durchschnitt", np.mean(Zfg_Zahlen), "Euro")
    print(f"Theoretischer Erwartungswert ist {(sum(x[i] * P[i] for i in range(len(x)))):6f}")


# 1) Man stelle die Dichtefunktion bzw. die Verteilungsfunktion f¨ur
# a) X ∼ Unif[−2, 2];
# b) X ∼ Exp(2);
# grafisch dar auf den Intervallen: [-3,3] f¨ur a); [0,4] f¨ur b).
# 2) Man sch¨atze in jedem Fall anhand Simulationen P(1 < X < 1.5). Man vergleiche den gesch¨atzen Wert
# mit dem theoretischen Wert indem man spezifische Python Befehle benutzt!
# 3) Man sch¨atze in jedem Fall anhand Simulationen den Erwartungswert E(X) und die Varianz V (X).
def ex4():
    # 1
    N = 1000
    alpha = 2
    DatenUnif = scipy.stats.uniform.rvs(loc=-2, scale=4, size=N)
    DatenExpon = scipy.stats.expon.rvs(loc=0, scale=1 / alpha, size=N)

    xunif = np.linspace(min(DatenUnif), max(DatenUnif), 100)
    xexpon = np.linspace(min(DatenExpon), max(DatenExpon), 100)

    yunif = scipy.stats.uniform.pdf(xunif, loc=-2, scale=4)
    yexpon = scipy.stats.expon.pdf(xexpon, loc=0, scale=1 / alpha)

    # -3,3
    xunif = np.linspace(-3, 3, 100)
    yunif = scipy.stats.uniform.pdf(xunif, loc=-2, scale=4)

    plt.plot(xunif, yunif, "r-", label="Unif Dichte")
    plt.plot(xunif, scipy.stats.uniform.cdf(xunif), "r-", label="Unif Verteilungs")

    plt.legend()
    plt.show()

    # 0,4
    xexpon = np.linspace(0, 4, 100)

    yexpon = scipy.stats.expon.pdf(xexpon, loc=0, scale=1 / alpha)
    plt.plot(xexpon, yexpon, "r-", label="Expon Dichte")
    plt.plot(xexpon, scipy.stats.expon.cdf(xexpon), "r-", label="Expon Verteilungs")
    plt.legend()
    plt.show()

    # 2
    punif = len([x for x in DatenUnif if 1 <= x <= 1.5]) / N
    pexpon = len([x for x in DatenExpon if 1 <= x <= 1.5]) / N

    print("Simulation")
    print(punif)
    print(pexpon)

    th_unif = scipy.stats.uniform.cdf(1.5, loc=-2, scale=4) - scipy.stats.uniform.cdf(1, loc=-2, scale=4)
    th_expon = scipy.stats.expon.cdf(1.5, scale=1 / 2) - scipy.stats.expon.cdf(1, loc=0, scale=1 / alpha)

    print("Theoretisch")
    print(th_unif)
    print(th_expon)

    # 3
    eunif = np.mean(DatenUnif)
    eexpon = np.mean(DatenExpon)
    print("Erwartungs")
    print(eunif)
    print(eexpon)

    vunif = np.var(DatenUnif)
    vexpon = np.var(DatenExpon)
    print("Varianz")
    print(vunif)
    print(vexpon)



def Simulation_Ziehung():
    urne = [0]*4+[1]*6
    Ziehung_schwarz=0
    for _ in range(3):
        kugel=random.choice(urne)
        urne.remove(kugel)
        if kugel==1:
            Ziehung_schwarz+=1
        else:
            break
    return Ziehung_schwarz


def ex5():
    # N = 1000
    # x = [Simulation_Ziehung() for _ in range(N)]
    #
    # sum = 0
    # for i in range(len(x)):
    #     if x[i] == 3:
    #         sum += 30
    #
    #     elif x[i] == 2:
    #         sum += 25
    #
    #     else:
    #         sum += -5
    #
    # print(sum / N)


    # In einer Urne sind 4 weiße und 6 schwarze Kugeln. Ein Spieler zieht nacheinander eine Kugel
    # ohne Zurucklegen. Das Spiel ist aus, wenn er eine weisse Kugel zieht oder wenn er dreimal gezogen hat.
    # Die Zufallsvariable X zeigt die Anzahl der gezogenen schwarzen Kugeln.
    # a) Welches ist die (theoretische) Wahrscheinlichkeitsverteilung von X und simuliere zufallige Werte fur X.
    # b) Der Spieler erhalt 30 Punkte, wenn er drei schwarze Kugeln gezogen hat. Er erhalt 25 Punkte, wenn er
    # zwei schwarze Kugeln zieht. In allen anderen Fallen verliert er 5 Punkte. Anhand Simulationen schatze
    # man die mittlere Punktezahl des Spielers. Man vergleiche das Ergebnis mit dem theoretischen Ergebnis.
    print("Theoretische:")
    print(f"P(X = 0) = P(erste Kugel ist weiß) = {4 / 10}")
    print(f"P(X = 1) = P(erste Kugel schwarz, zweite Kugel weiß) = {6 / 10 * 4 / 9}")
    print(f"P(X = 2) = P(erste und zweite Kugel schwarz, dritte Kugel weiß) = {6 / 10 * 5 / 9 * 4 / 8}")
    print(f"P(X = 3) = P(erste und zweite und dritte Kugel schwarz) = {6 / 10 * 5 / 9 * 4 / 8}")

    num_simulations = 1000
    count_black_0 = 0
    count_black_1 = 0
    count_black_2 = 0
    count_black_3 = 0
    score = 0
    for _ in range(num_simulations):
        balls = random.sample(["w", "s"], counts=[4, 6], k=3)
        if balls[0] == 'w':
            count_black_0 += 1
            score -= 5
        elif balls[1] == 'w':
            count_black_1 += 1
            score -= 5
        elif balls[2] == 'w':
            count_black_2 += 1
            score += 25
        else:
            count_black_3 += 1
            score += 30
    print("Relative:")
    print(f"P(X = 0) = P(erste Kugel ist weiß) = {count_black_0 / num_simulations:.2f}")
    print(f"P(X = 1) = P(erste Kugel schwarz, zweite Kugel weiß) = {count_black_1 / num_simulations:.2f}")
    print(f"P(X = 2) = P(erste und zweite Kugel schwarz, dritte Kugel weiß) = {count_black_2 / num_simulations:.2f}")
    print(f"P(X = 3) = P(erste und zweite und dritte Kugel schwarz) = {count_black_3 / num_simulations:.2f}")

    print(f"P(Y = 30) = {count_black_3 / num_simulations:.2f}")
    print(f"P(Y = 25) = {count_black_2 / num_simulations:.2f}")
    print(f"P(Y = -5) = {(count_black_0 + count_black_1) / num_simulations:.2f}")
    print(f"E(Y) = Average score: {score / num_simulations}")


def main():
    # ex1()
    # ex2()
    # ex3()
    ex4()
    #ex5()


if __name__ == "__main__":
    main()



