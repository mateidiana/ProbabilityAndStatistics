import random
from itertools import product
from itertools import permutations, combinations
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon, uniform
from scipy.stats import binom

def ex1():
    # Man simuliere mit Hilfe von scipy.stats.uniform.rvs 1000 zuf¨allige Punkte aus dem Quader
    # [−1, 1] × [−1, 1] × [−1, 1] ⊂ R^3
    # Sei D die ZG welche Distanz dieser Punkte zum Ursprung (0,0,0) darstellt.
    # Man schatze den Erwartungswert (numpy.mean) und die Varianz von D (numpy.var).
    num_points = 1000
    # Generate random points in the cube [-1, 1] × [-1, 1] × [-1, 1]
    points = uniform.rvs(loc=-1, scale=2, size=(num_points, 3))
    # Calculate the distance to the origin for each point
    distances = np.linalg.norm(points, axis=1)
    # Calculate the mean and variance of distances
    mean_distance = np.mean(distances)
    variance_distance = np.var(distances)
    print(f"Estimated Mean Distance: {mean_distance:.4f}")
    print(f"Estimated Variance of Distance: {variance_distance:.4f}")


def ex2():
    # a) Man generiere alle Permutationen von mutig. Wie viele solche Permutationen gibt es?
    # b) Man generiere zwei zuf¨allige Permutationen von mutig.
    # c) Man generiere alle Variationen mit vier Buchstaben aus dem String mutig. Wie viele solche Variationen
    # gibt es?
    # d) Man generiere alle Kombinationen mit zwei Buchstaben aus dem String mutig. Wie viele solche Kombinationen
    # gibt es?
    # a
    string = "mutig"
    all_perm = list(permutations(string))
    num_perm = len(all_perm)

    print("Alle Perm", all_perm)
    print("Anzahl", num_perm)

    # b
    print(random.sample(string, len(string)))
    print(random.sample(string, len(string)))

    # c
    var = list(permutations(string, 4))
    num_var = len(var)

    print("Alle Var", var)
    print("Anzahl Var", num_var)

    # d
    comb = list(combinations(string, 2))
    num_comb = len(comb)

    print("Alle Komb", comb)
    print("Anzahl Komb", num_comb)


def ex3():
    # In einer Urne sind 3 blaue, 3 rote und 4 weiße Kugeln. Ein Spieler zieht nacheinander ohne
    # Zur¨ucklegen 3 Kugeln. Der Spieler erh¨alt 5 e, wenn alle drei gezogenen Kugeln dieselbe Farbe haben. Er
    # erh¨alt 2 e, wenn die drei Kugeln unterschiedliche Farben aufweisen. Bei allen anderen F¨allen muss der
    # Spieler 1 e bezahlen. Wie viel gewinnt oder verliert im Mittel der Spieler pro Spiel? Man vergleiche das
    # theoretische Resultat mit den Ergebnissen von zuf¨alligen Simulationen.
    n = 1000
    d = []
    k = []
    for i in range(n):
        kugeln = random.sample(["b", "r", "w"], counts=[3, 3, 4], k=3)
        if len(set(kugeln)) == 1:
            d.append(5)
        elif len(set(kugeln)) == 3:
            d.append(2)
        else:
            d.append(-1)

    print("mean sim", np.mean(d))

    p = [
        3 / 10 * 2 / 9 * 1 / 8 + 3 / 10 * 2 / 9 * 1 / 8 + 4 / 10 * 3 / 9 * 2 / 8,
        3 / 10 * 3 / 9 * 4 / 8 + 3 / 10 * 4 / 9 * 3 / 8 + 4 / 10 * 3 / 9 * 3 / 8 + 3 / 10 * 3 / 9 * 4 / 8 + 3 / 10 * 4 / 9 * 3 / 8 + 4 / 10 * 3 / 9 * 3 / 8,
        1 - (3 / 10 * 2 / 9 * 1 / 8 + 3 / 10 * 2 / 9 * 1 / 8 + 4 / 10 * 3 / 9 * 2 / 8 +
             3 / 10 * 3 / 9 * 4 / 8 + 3 / 10 * 4 / 9 * 3 / 8 + 4 / 10 * 3 / 9 * 3 / 8 + 3 / 10 * 3 / 9 * 4 / 8 + 3 / 10 * 4 / 9 * 3 / 8 + 4 / 10 * 3 / 9 * 3 / 8)
    ]
    x = [5, 2, -1]
    e = 0
    print(p)

    for i in range(len(p)):
        e += p[i] * x[i]
    print("mean th", e)


def ex4():
    # Eine Urne enthalt 10 Kugeln mit der Ziffer 0, 20 Kugeln mit der Ziffer 1, 20 Kugeln mit der Ziffer 2.
    # Aus der Urne werden 3 Kugeln ohne Zurucklegen gezogen. X sei das Produkt der 3 erhaltenen Zahlen.
    # Man schatze anhand Simulationen den Erwartungswert und die Varianz von X!
    # Man erstelle anhand Simulationen das Histogramm der absoluten Haufigkeiten fur die Werte von X!
    # In ein zweites Bild zeichne man ein zweites Histogramm mit den (theoretischen) Wahrscheinlichkeiten der ZG X.
    n = 10000
    urne = [0, 1, 2]
    counts = [10, 20, 20]
    simulated_values = []
    for _ in range(n):
        draws = random.sample(urne, counts=counts, k=3)
        product_value = np.prod(draws)
        simulated_values.append(product_value)

    # Berechne Erwartungswert und Varianz
    mean_value = np.mean(simulated_values)
    variance_value = np.var(simulated_values)
    print(f"Erwartungswert von X: {mean_value}")
    print(f"Varianz von X: {variance_value}")

    # Histogramm der absoluten Häufigkeiten
    plt.hist(simulated_values, bins=np.arange(min(simulated_values), max(simulated_values) + 2) - 0.5, density=False,
             edgecolor="black", label="absolute Hfg.")
    plt.title('Histogramm der absoluten Haufigkeiten')
    plt.xlabel('X')
    plt.ylabel('Absolute Haufigkeit')
    plt.show()

    # Histogramm mit theoretischen Wahrscheinlichkeiten
    all_possible_outcomes = list(product(urne, repeat=3))
    theoretical_probabilities = [counts[0] / sum(counts) * counts[1] / sum(counts) * counts[2] / sum(counts) for _ in
                                 all_possible_outcomes]

    plt.hist(simulated_values, bins=np.arange(min(simulated_values), max(simulated_values) + 2) - 0.5, density=True,
             edgecolor="black", label="relative Hfg.")
    # plt.plot(theoretical_probabilities, bins=np.arange(min(simulated_values), max(simulated_values) + 2) - 0.5,
    #          density=True, label="theoretische Wahrscheinlichkeiten")
    plt.title('Histogramm mit theoretischen Wahrscheinlichkeiten')
    plt.xlabel('X')
    plt.ylabel('Relative Haufigkeit')
    plt.legend()
    plt.show()


def ex5():
    # Sei die Gleichung zweiten Grades x^2 + Bx + C = 0, wobei B, C ∼ Unif[−1, 1] unabhangige ZG sind.
    # Anzahl der Simulationen
    num_simulations = 10000

    # Zufallsvariablen B und C
    B_values = uniform.rvs(loc=-1, scale=2, size=num_simulations)
    C_values = uniform.rvs(loc=-1, scale=2, size=num_simulations)

    # a) die Wahrscheinlichkeit, dass beide Wurzeln der Gleichung reell sind;
    real_roots = []
    for i in range(num_simulations):
        if B_values[i] ** 2 - 4 * C_values[i] >= 0:
            real_roots.append(
                (((-B_values[i] + np.sqrt(B_values[i] ** 2 - 4 * C_values[i])) / 2),
                 ((-B_values[i] - np.sqrt(B_values[i] ** 2 - 4 * C_values[i])) / 2))
            )
    prob_real_roots = len(real_roots) / num_simulations
    print(f"a) Wahrscheinlichkeit, dass beide Wurzeln reell sind: {prob_real_roots:.4f}")

    # b) die Wahrscheinlichkeit, dass beide Wurzeln der Gleichung positiv sind;
    num_pos_roots = 0
    for i in range(len(real_roots)):
        if real_roots[i][0] >= 0 and real_roots[i][1] >= 0:
            num_pos_roots += 1
    prob_positive_roots = num_pos_roots / num_simulations
    print(f"b) Wahrscheinlichkeit, dass beide Wurzeln positiv sind: {prob_positive_roots:.4f}")

    # c) den Erwartungswert und die Varianz der Summe der beiden Wurzeln.
    sum_roots = []
    for i in range(len(real_roots)):
        sum_roots.append(real_roots[i][0] + real_roots[i][1])
    expected_value = np.mean(sum_roots)
    variance = np.var(sum_roots)
    print(f"c) Erwartungswert der Summe der Wurzeln: {expected_value:.4f}")
    print(f"   Varianz der Summe der Wurzeln: {variance:.4f}")


def ex6():
    # In einer Urne sind 20 rote Kugeln, 15 blaue Kugeln, 5 grune Kugeln und 10 schwarze Kugeln. Man
    # simuliere N(= 200, 1000, . . .) Ziehungen mit Zurucklegen und zeige (print) die relative Haufigkeit an mit
    # welcher jede Farbe auftaucht. Man vergleiche die theoretischen Resultate mit den Ergebnissen aus den
    # Simulationen. Man gebe die Ergebnisse der ersten 10 Ziehungen an!
    n = 1000
    count_red = 0
    count_green = 0
    count_blue = 0
    count_black = 0
    for _ in range(n):
        urn = np.array(['red'] * 20 + ['blue'] * 15 + ['green'] * 5 + ['black'] * 10)
        draws = np.random.choice(urn, size=10, replace=True)
        for draw in draws:
            if draw == 'red':
                count_red += 1
            elif draw == 'blue':
                count_blue += 1
            elif draw == 'green':
                count_green += 1
            else:
                count_black += 1

    print(f"P(rot) = {count_red / (n * 10)}")
    print(f"P(blau) = {count_blue / (n * 10)}")
    print(f"P(grun) = {count_green / (n * 10)}")
    print(f"P(schwarz) = {count_black / (n * 10)}")

    total_balls = 20 + 15 + 5 + 10
    prob_red = 20 / total_balls
    prob_blue = 15 / total_balls
    prob_green = 5 / total_balls
    prob_black = 10 / total_balls
    print(f"Theoretische Wahrscheinlichkeiten:")
    print(f"P(rot) = {prob_red}")
    print(f"P(blau) = {prob_blue}")
    print(f"P(grun) = {prob_green}")
    print(f"P(schwarz) = {prob_black}")


def ex7():
    # Beim Herstellungsprozess einer Ware ist bekannt, dass 80% fehlerfrei, 15% mit leichten (vernachl
    # ¨assigbaren) Fehlern und 5% mit großen Fehlern hergestellt werden. Sei die Zufallsgr¨oße X die Anzahl
    # der Waren mit großen Fehlern von insgesamt 80 Waren aus dem Herstellungsprozess.
    # a) Man simuliere 500 m¨ogliche Werte der ZG X.
    # b) Wie groß ist die theoretische Wahrscheinlichkeit, dass von den n¨achsten hergestellten 80 Exemplaren
    # dieser Ware a) h¨ochstens 6; b) genau 10; c) mindestens 5
    # große Fehler besitzen?

    prob_no_defect = 0.80
    prob_light_defect = 0.15
    prob_big_defect = 0.05

    # a) Man simuliere N=100 mögliche Werte der ZG X.
    num_simulations = 100
    num_products = 100
    big_defects = []
    for _ in range(num_simulations):
        simulated_data = np.random.choice(["no_defect", "light_defect", "big_defect"], size=num_products, replace=True,
                                          p=[prob_no_defect, prob_light_defect, prob_big_defect])
        big_defects.append(np.sum(simulated_data == "big_defect"))
    print(f"{num_simulations} simulations and their number of big_defects priducts:\n", big_defects)

    # b) Welches ist die mittlere Anzahl M der Waren mit großen Fehlern (anhand der simulierten Daten)?
    num_big_defect = 0
    for _ in range(num_simulations):
        simulated_data = np.random.choice(["no_defect", "light_defect", "big_defect"], size=num_products, replace=True,
                                          p=[prob_no_defect, prob_light_defect, prob_big_defect])
        num_big_defect += np.sum(simulated_data == "big_defect")
    print("Average number of big defects: ", num_big_defect / num_simulations)

    # c) Wie groß ist die theoretische Wahrscheinlichkeit, dass von den nächsten hergestellten 100 Exemplaren dieser Ware
    # 1) höchstens 3; 2) genau 10; 3) mindestens 4 große Fehler besitzen?
    print(f"Theoretical probability max 3: {binom.cdf(3, num_products, prob_big_defect):.2f}")
    print(f"Theoretical probability exactly 10: {binom.pmf(10, num_products, prob_big_defect):.2f}")
    print(f"Theoretical probability min 4: {1 - binom.cdf(3, num_products, prob_big_defect):.2f}")


def ex8():
    # Eine Maschine produziert im Mittel 10mm lange Schrauben mit einer Standardabweichung von 1mm.
    # Die L¨ange der Schrauben kann als normalverteilt angesehen werden. Anhand von (a) Simulationen (b)
    # spezifischen Anweisungen berechne man die gesch¨atzte bzw. theoretische Wahrscheinlichkeit daf¨ur, dass
    # (c) eine Schraube k¨urzer ist als 9 mm;
    # (d) eine Schraube h¨ochstens 10.1 mm und mindestens 8.9 mm lang ist.
    mu = 10
    sigma = 1
    simulations = 1000
    data = norm.rvs(mu, sigma, simulations)

    print(f"Probability shorter than 9mm (Simulations): {np.mean(np.array(data < 9)):.2f}")
    print(f"Probability between 10.1mm and 8.9 (Simulations): "
          f"{np.mean(np.array(data < 10.1) & np.array(data > 8.9)):.2f}")
    print(f"Probability shorter than 9mm (Theoretical): {norm.cdf(9, loc=mu, scale=sigma):.2f}")
    print(f"Probability between 10.1mm and 8.9 (Theoretical): "
          f"{norm.cdf(10.1, loc=mu, scale=sigma) - norm.cdf(8.9, loc=mu, scale=sigma):.2f}")


def ex9():
    # Ein sechsseitiger Würfel wird auf vier Seiten mit einer 1 und auf zwei Seiten mit einer 2 übermalt. Er wird
    # zweimal geworfen.
    # 1) Die Zufallsvariable X gibt die Summe der erhaltenen Zahlen an. Man gebe alle möglichen Werte von X an und
    # die entsprechenden theoretischen Wahrscheinlichkeiten.
    # 2) Anhand von Simulationen schätze man
    # 2a) die zu erwartende Summe (d.h. E(X)) ; 2b) die Wahrscheinlichkeit dafür, dass die Summe größer als 2 ist.

    num_sims = 1000
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    for _ in range(num_sims):
        data = random.choices([1, 2], weights=[4 / 6, 2 / 6], k=2)
        if sum(data) == 2:
            sum_2 += 1
        elif sum(data) == 3:
            sum_3 += 1
        elif sum(data) == 4:
            sum_4 += 1

    print(f"Summe 2: {sum_2 / num_sims}")
    print(f"Summe 3: {sum_3 / num_sims}")
    print(f"Summe 4: {sum_4 / num_sims}")
    print(f"Theoretische Wahrscheinlichkeit Summe 2:", 4 / 6 * 4 / 6)
    print(f"Theoretische Wahrscheinlichkeit Summe 3:", 4 / 6 * 2 / 6 + 2 / 6 * 4 / 6)
    print(f"Theoretische Wahrscheinlichkeit Summe 4:", 2 / 6 * 2 / 6)


def ex10():
    # Ein ”Gl¨ucksrad” hat vier gleichgrosse Felder. Eines davon ist das Gewinnfeld. Anhand Simulationen,
    # wie groß ist die Wahrscheinlichkeit, dass beim viermaligen Drehen mindestens einmal ein Gewinn
    # gedreht wird?
    # Welche ist die theoretische Wahrscheinlichkeitsverteilung der Zufallsgr¨osse X: Anzahl Gewinne in 4
    # Drehungen des Gl¨ucksrads.
    simulation = 1000
    spins = 4
    win = 1

    def spin():
        return random.randint(1, 4) == 1  # zicem ca daca pica 1 ai castigat

    sim_wins = [sum(spin() for _ in range(spins)) >= win for _ in range(simulation)]

    est_prob = np.mean(sim_wins)

    print(f"Simulated Wins: {est_prob}")

    from scipy.stats import binom

    winning_probability = 1 / 4  # The probability of winning in a single spin
    total_spins = 4

    # P(X = 0) = 3/4 * 3/4 * 3/4 * 3/4 (vier mal verlieren)
    # P(X = 1) = (1/4 * 3/4 * 3/4 * 3/4) * 4 (1 mal gewinnen, 3 mal verlieren)
    # P(X = 2) = (1/4 * 1/4 * 3/4 * 3/4) * C4 je 2 (2 mal gewinnen, 2 mal verlieren)
    # P(X = 3) = (1/4 * 1/4 * 1/4 * 3/4) * C4 je 3 (3 mal gewinnen, 1 mal verlieren)
    # P(X = 4) = (1/4 * 1/4 * 1/4 * 1/4) (vier mal gewinnen)
    theoretical_probabilities = []
    for k in range(total_spins + 1):
        probability = binom.pmf(k, total_spins, winning_probability)
        theoretical_probabilities.append((k, probability))

    for k, probability in theoretical_probabilities:
        print(f"P(X = {k}) = {probability:.4f}")

    # probability = 1 - binom.pmf(1, total_spins, winning_probability)
    # print(probability)


def ex11():
    #ahnlich mit Lab5 A4
    pass


def ex12():
    # Seien n=4, p=0.25, X~Bino(n,p), Y=X^2 + 1. Man simuliere 1000 Werte für Y. Man erstelle das Histogramm
    # der absoluten Häufigkeiten für Y. Man schätze P(Y>5). Man vergleiche die geschätzte Wahrscheinlichkeit mit der
    # theoretischen Wahrscheinlichkeit.

    n = 4
    p = 0.25
    sims = 1000
    y = np.random.binomial(n, p, sims) ** 2 + 1

    plt.hist(y, bins=range(min(y), max(y) + 1), edgecolor='black')
    plt.show()

    print(f"P(y > 5): {np.sum(y > 5) / sims}")
    print(f"Theoretical: {1 - binom.cdf(5, n ** 2, p):.2f}")


def main():
    ex10()


if __name__ == "__main__":
    main()


