def order_total(orders):
    return sum(o["qty"] * o["price"] for o in orders)

def normalize_labels(labels):
    out = []
    for l in labels:
        s = l
        for _ in range(5):
            s = s.strip().lower().replace(" ", "-")
        out.append(s)
    return out

def top_products(sales, n=3):
    totals = {}
    for product, qty in sales:
        totals[product] = totals.get(product, 0) + qty
    return sorted(totals, key=lambda p: (-totals[p], p))[:n]
