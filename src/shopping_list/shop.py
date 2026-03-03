import sys
from storage import load_list, save_list
from utils import calc_line_total, calc_grand_total, count_units


def add_item():
    if len(sys.argv) != 5:
        print("Lietošana: python shop.py add NOSAUKUMS DAUDZUMS CENA")
        return

    name = sys.argv[2]

    try:
        qty = int(sys.argv[3])
        if qty <= 0:
            raise ValueError
    except ValueError:
        print("Daudzumam jābūt pozitīvam skaitlim.")
        return

    try:
        price = float(sys.argv[4])
        if price <= 0:
            raise ValueError
    except ValueError:
        print("Cenai jābūt pozitīvam skaitlim.")
        return

    items = load_list()

    item = {
        "name": name,
        "qty": qty,
        "price": price
    }

    items.append(item)
    save_list(items)

    line_total = calc_line_total(item)

    print(f"✓ Pievienots: {name} × {qty} = {line_total:.2f} EUR")


def list_items():
    items = load_list()

    if not items:
        print("Saraksts ir tukšs.")
    else:
        print("Iepirkumu saraksts:")
        for i, item in enumerate(items, start=1):
            line_total = calc_line_total(item)
            print(
                f"{i}. {item['name']} × {item['qty']} — "
                f"{item['price']:.2f} EUR/gab. — {line_total:.2f} EUR"
            )


def total():
    items = load_list()

    if not items:
        print("Saraksts ir tukšs.")
    else:
        grand_total = calc_grand_total(items)
        total_units = count_units(items)

        print(
            f"Kopā: {grand_total:.2f} EUR "
            f"({total_units} vienības, {len(items)} produkti)"
        )


def clear():
    save_list([])
    print("Iepirkumu saraksts iztīrīts.")


def main():
    if len(sys.argv) < 2:
        print("Komandas: add/list/total/clear")
        return

    cmd = sys.argv[1].lower()

    if cmd == "add":
        add_item()
    elif cmd == "list":
        list_items()
    elif cmd == "total":
        total()
    elif cmd == "clear":
        clear()
    else:
        print("Nepareiza komanda vai argumenti.")


if __name__ == "__main__":
    main()


# src/shopping_list/shop.py
from storage import ensure_prices_file

# pārbauda un izveido prices.json, ja tāds nav
ensure_prices_file()
