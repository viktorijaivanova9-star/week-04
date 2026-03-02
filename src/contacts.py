import json
import sys
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"✓ Pievienots: {name} ({phone})")

def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Nav neviena kontakta.")
        return
    print("Kontakti:")
    for i, c in enumerate(contacts, start=1):
        print(f"  {i}. {c['name']} — {c['phone']}")

def search_contacts(term):
    contacts = load_contacts()
    results = [c for c in contacts if term.lower() in c['name'].lower()]
    print(f"Atrasti {len(results)} kontakti:")
    for i, c in enumerate(results, start=1):
        print(f"  {i}. {c['name']} — {c['phone']}")

def main():
    if len(sys.argv) < 2:
        print("Lūdzu, ievadi komandu: add/list/search")
        return
    cmd = sys.argv[1].lower()
    if cmd == "add" and len(sys.argv) == 4:
        add_contact(sys.argv[2], sys.argv[3])
    elif cmd == "list":
        list_contacts()
    elif cmd == "search" and len(sys.argv) == 3:
        search_contacts(sys.argv[2])
    else:
        print("Nepareiza komanda vai argumenti.")

if __name__ == "__main__":
    main()
