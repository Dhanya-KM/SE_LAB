def notes_needed(amount):
    if not isinstance(amount, str):
        return None
    try:
        return int(amount.replace(',', '')) // 100
    except ValueError:
        return None

def mask_card(card_number):
    if not isinstance(card_number, str):
        return None
    groups = card_number.split()
    if len(groups) != 4:
        return None
    return "XXXX XXXX XXXX " + groups[3]

def average_withdrawal(amounts_csv):
    if not isinstance(amounts_csv, str):
        return None
    try:
        amounts = [int(a) for a in amounts_csv.split(',')]
    except ValueError:
        return None
    return sum(amounts) // len(amounts)

def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    result = notes_needed(user_input)
    print("Number of 100 Notes:", result)

    print("\n==== Running mask_card ====")
    user_input = input("Enter a card number (e.g. 1234 5678 9012 3456): ")
    result = mask_card(user_input)
    print("Masked Card:", result)

    print("\n==== Running average_withdrawal ====")
    user_input = input("Enter withdrawals as CSV (e.g. 500,1000,2000): ")
    result = average_withdrawal(user_input)
    print("Average Withdrawal:", result)

if __name__ == "__main__":
    main()
