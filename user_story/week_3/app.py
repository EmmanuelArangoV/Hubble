from pathlib import Path
from user_story.week_3.service.inventory import Inventory
from user_story.week_3.persistence.archives import fileCSV
from user_story.week_3.service.validations import valid_string, parse_positive_float, parse_positive_int, \
    parse_answer, ctext

CSV_PATH = Path(__file__).parent / 'inventory.csv'


def load_inventory(inv) -> Inventory:
    storage = fileCSV(CSV_PATH)
    try:
        choice = input(ctext("Do you want to overwrite current in memory inventory? (y/n): ", 'prompt')).strip().lower()
        if parse_answer(choice):
            storage.load_csv(inv, overwrite=True)
        else:
            storage.load_csv(inv, overwrite=None)
    except Exception:
        # If file missing or error, start empty inventory silently
        pass
    return inv


def ask_name(inv: Inventory) -> str:
    while True:
        raw = input(ctext("Product name: ", 'prompt')).capitalize()
        try:
            name = valid_string(raw)
            if not inv.name_available(name):
                print(ctext("Name already exists. Try another.", 'warning'))
                continue
            return name
        except ValueError as e:
            print(ctext(str(e), 'error'))


def ask_price() -> float:
    while True:
        raw = input(ctext("Price: ", 'prompt'))
        try:
            return parse_positive_float(raw)
        except ValueError as e:
            print(ctext(str(e), 'error'))


def ask_quantity() -> int:
    while True:
        raw = input(ctext("Quantity: ", 'prompt'))
        try:
            return parse_positive_int(raw)
        except ValueError as e:
            print(ctext(str(e), 'error'))


def add_product(inv: Inventory):
    print(ctext("\n=== Add Product ===", 'info'))
    name = ask_name(inv)
    price = ask_price()
    quantity = ask_quantity()
    inv.add_product(name, price, quantity)


def update_product(inv: Inventory):
    print(ctext("\n=== Update Product ===", 'info'))
    name = input(ctext("Exact product name: ", 'prompt')).capitalize()
    new_price_raw = input(ctext("New price (enter to keep): ", 'prompt'))
    new_qty_raw = input(ctext("New quantity (enter to keep): ", 'prompt'))

    new_price = None
    new_qty = None

    if new_price_raw.strip():
        try:
            new_price = parse_positive_float(new_price_raw)
        except ValueError as e:
            print(ctext(f"Invalid price: {e}", 'error'))
            return

    if new_qty_raw.strip():
        try:
            new_qty = parse_positive_int(new_qty_raw)
        except ValueError as e:
            print(ctext(f"Invalid quantity: {e}", 'error'))
            return

    inv.update_product(name, price=new_price, quantity=new_qty)


def delete_product(inv: Inventory):
    print(ctext("\n=== Delete Product ===", 'info'))
    name = input(ctext("Exact product name: ", 'prompt')).capitalize()
    inv.delete_product(name)


def search_products(inv: Inventory):
    print(ctext("\n=== Search Product ===", 'info'))
    term = input(ctext("Search term (exact or partial): ", 'prompt')).strip().capitalize()
    if not term:
        print(ctext("Empty search.", 'warning'))
        return
    mode = input(ctext("Partial match? (y/n): ", 'prompt')).strip().lower()
    partial = parse_answer(mode)
    results = inv.search_product(term, filter=True if partial else None)
    if not results:
        print(ctext("No products found.", 'warning'))
    else:
        print(ctext(f"Found {len(results)} product(s):", 'info'))
        for p in results:
            print(ctext(f"- {p.name} | Price: ${p.price} | Quantity: {p.quantity}", 'info'))


def show_stats(inv: Inventory):
    print(ctext("\n=== Statistics ===", 'info'))
    stats = inv.statistics()
    print(ctext(f"Total units: {stats['total_units']}", 'info'))
    print(ctext(f"Total value: {stats['total_value']}", 'info'))
    me = stats['most_expensive_product']
    ms = stats['most_stocked_product']
    print(ctext("Most expensive: " + (me.name if me else "N/A"), 'info'))
    print(ctext("Highest stock: " + (ms.name if ms else "N/A"), 'info'))


def save_inventory(inv: Inventory):
    storage = fileCSV(CSV_PATH)
    try:
        storage.save_csv(inv)
    except Exception as e:
        print(ctext(f"Error saving inventory: {e}", 'error'))


def menu():
    inv = Inventory()
    while True:
        print(ctext("\n===== INVENTORY MENU =====", 'info'))
        print(ctext("1. Add product", 'prompt'))
        print(ctext("2. Show inventory", 'prompt'))
        print(ctext("3. Search product", 'prompt'))
        print(ctext("4. Update product", 'prompt'))
        print(ctext("5. Delete product", 'prompt'))
        print(ctext("6. Show statistics", 'prompt'))
        print(ctext("7. Save inventory to CSV", 'prompt'))
        print(ctext("8. Load from CSV", 'prompt'))
        print(ctext("9. Exit", 'prompt'))
        choice = input(ctext("Option: ", 'prompt'))
        match choice:
            case '1':
                add_product(inv)
            case '2':
                print(ctext("\n=== Inventory ===", 'info'))
                inv.show_inventory()
            case '3':
                search_products(inv)
            case '4':
                update_product(inv)
            case '5':
                delete_product(inv)
            case '6':
                show_stats(inv)
            case '7':
                save_inventory(inv)
            case '8':
                inv = load_inventory(inv)
            case '9':
                if not inv.persistence:
                    ans = input(ctext("Unsaved changes. Save before exit? (y/n): ", 'prompt')).strip().lower()
                    if parse_answer(ans):
                        save_inventory(inv)
                print(ctext("Exiting...", 'info'))
                break
            case _:
                print(ctext("Invalid option.", 'error'))

if __name__ == '__main__':
    menu()
