from datetime import datetime
import json

lost_items = []
found_items = []

print("Lost & Found Matcher")


# ---------------- VALIDATION ----------------

def validate_required(value, field_name):
    if value.strip() == "":
        print(field_name, "cannot be empty.")
        return False

    return True

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD.")
        return False


# ---------------- JSON FUNCTIONS ----------------

def save_data(lost_items, found_items):
    data = {
        "lost_items": lost_items,
        "found_items": found_items
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully!")


def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        return data.get("lost_items", []), data.get("found_items", [])

    except FileNotFoundError:
        return [], []

    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with empty data.")
        return [], []


# ---------------- SEARCH ----------------

def search_items(items, category=None, location=None):
    results = []

    for item in items:

        if category is not None:
            if item["category"].lower() != category.lower():
                continue

        if location is not None:
            if item["location"].lower() != location.lower():
                continue

        results.append(item)

    return results


# ---------------- KEYWORDS ----------------

def get_keywords(description):
    words = description.lower().split()
    return set(words)


# ---------------- MATCHING ----------------

def calculate_match(lost_item, found_item):
    score = 0

    # Check category
    if lost_item["category"].lower() == found_item["category"].lower():
        score += 40

    # Check location
    if lost_item["location"].lower() == found_item["location"].lower():
        score += 30

    # Check description keywords
    lost_keywords = get_keywords(lost_item["description"])
    found_keywords = get_keywords(found_item["description"])

    common_keywords = lost_keywords & found_keywords

    if len(lost_keywords) > 0:
        keyword_score = (len(common_keywords) / len(lost_keywords)) * 30
        score += keyword_score

    return score


def get_keyword_match(lost_item, found_item):
    lost_keywords = get_keywords(lost_item["description"])
    found_keywords = get_keywords(found_item["description"])

    common_keywords = lost_keywords & found_keywords

    if len(common_keywords) == 0:
        return "No"

    if lost_keywords.issubset(found_keywords):
        return "Full"

    return "Partial"


def find_matches(lost_items, found_items):
    matches = []

    for lost_item in lost_items:
        for found_item in found_items:

            score = calculate_match(lost_item, found_item)

            if score >= 50:
                matches.append({
                    "lost_id": lost_item["id"],
                    "found_id": found_item["id"],
                    "score": score
                })

    return matches


# ---------------- UPDATE STATUS ----------------

def update_status(items):
    item_id = input("Enter report ID: ").strip()

    for item in items:

        if item["id"] == item_id:

            print("Current Status:", item["status"])

            new_status = input(
                "Enter new status (Open/Matched/Returned): "
            ).strip()

            if new_status.lower() == "open":
                item["status"] = "Open"

            elif new_status.lower() == "matched":
                item["status"] = "Matched"

            elif new_status.lower() == "returned":
                item["status"] = "Returned"

            else:
                print("Invalid status.")
                return

            print("Status updated successfully!")
            print("New Status:", item["status"])

            return

    print("Report ID not found.")


# ---------------- OPEN REPORTS ----------------

def show_open_reports(lost_items, found_items):

    print("\nOpen Lost Reports:")

    found_open_lost = False

    for item in lost_items:

        if item["status"] == "Open":
            print(item)
            found_open_lost = True

    if not found_open_lost:
        print("No open lost reports found.")


    print("\nOpen Found Reports:")

    found_open_found = False

    for item in found_items:

        if item["status"] == "Open":
            print(item)
            found_open_found = True

    if not found_open_found:
        print("No open found reports found.")


# ==================================================
# MAIN APPLICATION
# ==================================================

def main():

    # ---------------- LOAD EXISTING DATA ----------------

    lost_items, found_items = load_data()

    print("\nExisting data loaded.")

    print("Lost items:", len(lost_items))
    print("Found items:", len(found_items))


    # ---------------- REGISTER LOST ITEM ----------------

    while True:

        print("\nRegister Lost Item")

        item_id = input("Enter lost item ID: ")

        if not validate_required(item_id, "Lost item ID"):
            continue

        category = input("Enter category: ")

        if not validate_required(category, "Category"):
            continue

        description = input("Enter description: ")

        if not validate_required(description, "Description"):
            continue

        location = input("Enter location: ")

        if not validate_required(location, "Location"):
            continue

        date = input("Enter date (YYYY-MM-DD): ")

        if not validate_date(date):
            continue

        lost_item = {
            "id": item_id,
            "category": category,
            "description": description,
            "location": location,
            "date": date,
            "status": "Open"
        }

        lost_items.append(lost_item)

        print("\nLost item registered successfully!")

        answer = input(
            "Do you want to register another lost item? (yes/no): "
        )

        if answer.lower() == "no":
            break


    # ---------------- REGISTER FOUND ITEM ----------------

    while True:

        print("\nRegister Found Item")

        found_id = input("Enter found item ID: ")

        if not validate_required(found_id, "Found item ID"):
            continue

        found_category = input("Enter category: ")

        if not validate_required(found_category, "Category"):
            continue

        found_description = input("Enter description: ")

        if not validate_required(found_description, "Description"):
            continue

        found_location = input("Enter location: ")

        if not validate_required(found_location, "Location"):
            continue

        found_date = input("Enter date (YYYY-MM-DD): ")

        if not validate_date(found_date):
            continue

        found_item = {
            "id": found_id,
            "category": found_category,
            "description": found_description,
            "location": found_location,
            "date": found_date,
            "status": "Open"
        }

        found_items.append(found_item)

        print("\nFound item registered successfully!")

        answer = input(
            "Do you want to register another found item? (yes/no): "
        )

        if answer.lower() == "no":
            break


    # ---------------- SEARCH ----------------

    print("\nSearch Items")

    search_category = input(
        "Enter category to search (or press Enter to skip): "
    )

    search_location = input(
        "Enter location to search (or press Enter to skip): "
    )


    if search_category.strip() == "":
        search_category = None

    if search_location.strip() == "":
        search_location = None


    lost_results = search_items(
        lost_items,
        category=search_category,
        location=search_location
    )

    found_results = search_items(
        found_items,
        category=search_category,
        location=search_location
    )


    print("\nMatching Lost Items:")
    print(lost_results)

    print("\nMatching Found Items:")
    print(found_results)


    # ---------------- POSSIBLE MATCHES ----------------

    print("\nPossible Matches:")

    matches = find_matches(lost_items, found_items)


    if len(matches) == 0:

        print("No possible matches found.")

    else:

        for match in matches:

            lost_item = next(
                item for item in lost_items
                if item["id"] == match["lost_id"]
            )

            found_item = next(
                item for item in found_items
                if item["id"] == match["found_id"]
            )

            category_match = (
                lost_item["category"].lower()
                == found_item["category"].lower()
            )

            location_match = (
                lost_item["location"].lower()
                == found_item["location"].lower()
            )

            keyword_match = get_keyword_match(
                lost_item,
                found_item
            )

            print("\nPOSSIBLE MATCH FOUND")
            print("Lost Report:", match["lost_id"])
            print("Found Report:", match["found_id"])
            print("Category:", lost_item["category"])

            print(
                "Category Match:",
                "Yes" if category_match else "No"
            )

            print(
                "Location Match:",
                "Yes" if location_match else "No"
            )

            print("Keyword Match:", keyword_match)
            print("Match Score:", round(match["score"], 2))
            print("Status: Review Required")


    # ---------------- UPDATE STATUS ----------------

    print("\nUpdate Report Status")

    print("1. Update Lost Report")
    print("2. Update Found Report")

    choice = input("Enter your choice: ")


    if choice == "1":

        update_status(lost_items)

    elif choice == "2":

        update_status(found_items)

    else:

        print("Invalid choice.")


    # ---------------- OPEN REPORTS ----------------

    show_open_reports(lost_items, found_items)


    # ---------------- SAVE DATA ----------------

    save_data(lost_items, found_items)


# ==================================================
# RUN PROGRAM
# ==================================================

if __name__ == "__main__":
    main()