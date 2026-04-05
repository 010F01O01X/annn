def simulate(price, lots):
    scenarios = {
        "YÜKSELİR": price * 1.07,
        "DÜŞER": price * 0.95,
        "YATAY": price * 1.01
    }

    results = {}

    for name, future_price in scenarios.items():
        profit = (future_price - price) * lots
        results[name] = round(profit, 2)

    return results