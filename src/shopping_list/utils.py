def calc_line_total(item):
    """Aprēķina vienas rindas summu (qty × price)."""
    return round(item["qty"] * item["price"], 2)


def calc_grand_total(items):
    """Aprēķina visu produktu kopējo summu."""
    total = 0
    for item in items:
        total += calc_line_total(item)
    return round(total, 2)


def count_units(items):
    """Aprēķina kopējo vienību skaitu."""
    total_units = 0
    for item in items:
        total_units += item["qty"]
    return total_units
