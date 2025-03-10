import re

def identify_card_type(card_no):
    """Identifies the type of credit/debit card based on the number."""
    card_types = {
        "Visa": r"^4\d{12,18}$",
        "Mastercard": r"^5[1-5]\d{14}$",
        "American Express": r"^3[47]\d{13}$",
        "Discover": r"^6(?:011|5\d{2})\d{12}$",
        "Diners Club": r"^3(?:0[0-5]|[68]\d)\d{11}$",
        "JCB": r"^(?:2131|1800|35\d{2})\d{12}$",
        "UnionPay": r"^62\d{14,17}$"
    }
    
    for card_type, pattern in card_types.items():
        if re.match(pattern, card_no):
            return card_type
    return "Unknown"

def is_valid_luhn(card_no):
    """Validates card number using Luhn's algorithm."""
    card_no = [int(digit) for digit in card_no[::-1]]  # Reverse the number
    total_sum = sum(card_no[0::2])  # Add digits in odd positions

    for digit in card_no[1::2]:  # Double even-positioned digits
        doubled = digit * 2
        total_sum += doubled if doubled < 10 else doubled - 9  # Sum digits if >= 10

    return total_sum % 10 == 0

def card_checker(card_no):
    """Checks card validity and displays information."""
    card_no = card_no.replace(" ", "").replace("-", "")

    if not card_no.isdigit():
        print("Invalid Card: Contains non-numeric characters.")
        return

    card_type = identify_card_type(card_no)
    if card_type == "Unknown":
        print("Invalid Card: Unrecognized card type.")
        return

    if is_valid_luhn(card_no):
        masked_card = "*" * (len(card_no) - 4) + card_no[-4:]  # Mask all but last 4 digits
        print(f"Valid {card_type} Card: {masked_card}")
    else:
        print("Invalid Card: Failed Luhn check.")

def main():
    while True:
        card_no = input("Enter card number (or type 'exit' to quit): ").strip()
        if card_no.lower() == "exit":
            break
        card_checker(card_no)

if __name__ == "__main__":
    main()
