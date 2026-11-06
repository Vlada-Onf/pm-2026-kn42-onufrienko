import csv, math, random


def simulate(velocity, remaining, runs=10000):
    """Повертає (P50, P85): за скільки спринтів закривається залишок."""
    random.seed(1)                       # щоб прогін можна було повторити
    results = []
    for _ in range(runs):                # одна симуляція
        left = remaining
        sprints = 0
        while left > 0:                  # поки робота не скінчилась
            left -= random.choice(velocity)   # випадкова швидкість з історії
            sprints += 1                 # рахуємо спринт
        results.append(sprints)
    results.sort()
    p50 = results[math.ceil(runs * 0.50) - 1]
    p85 = results[math.ceil(runs * 0.85) - 1]
    return p50, p85


# 1. Мої дані з velocity.csv
rows = list(csv.DictReader(open("velocity.csv", encoding="utf-8")))
mine = [int(r["points_done"]) for r in rows]
print("Мої спринти (points_done):", mine)
print("Весь перший реліз, 45 points: P50, P85 =", simulate(mine, 45))
print("Залишок після двох спринтів, 10 points: P50, P85 =", simulate(mine, 10))

# 2. Навчальні дані курсу, окремо від моїх
ref = [int(r["points_done"]) for r in csv.DictReader(
    open("lr09_reference_velocity.csv", encoding="utf-8"))]
print()
print("Навчальні дані, 220 points:")
for name, v in [("усі 12 спринтів", ref),
                ("спринти 1 і 2", ref[0:2]),
                ("спринти 5 і 6", ref[4:6])]:
    print(" ", name, v, "P50, P85 =", simulate(v, 220))