import sys
from storage import load_list, save_list

def add_item(name, price):
    try:
        price = float(price)
    except ValueError:
        print("Cena jāievada kā skaitlis!")
        return
    items = load_list()
    items.append({"name": name, "price": price})
    save_list(items)
    print(f"✓ Pievienots: {name} ({price:.2f} EUR)")

def list_items():
    items = load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    print("Iepirkumu saraksts:")
    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item['name']} — {item['price']:.2f} EUR")

def total():
    items = load_list()
    total_sum = sum(item['price'] for item in items)
    print(f"Kopā: {total_sum:.2f} EUR ({len(items)} produkti)")

def clear():
    save_list([])
    print("Iepirkumu saraksts iztīrīts.")

def main():
    if len(sys.argv) < 2:
        print("Komandas: add/list/total/clear")
        return
    cmd = sys.argv[1].lower()
    if cmd == "add" and len(sys.argv) == 4:
        add_item(sys.argv[2], sys.argv[3])
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
