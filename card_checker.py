def card_checker(card_no):
    card_no = card_no.replace(" ", "")
    
    if card_no.isdigit() == False:
        print('Invalid Card')
        return
    card_no = list(card_no)

    total_sum = 0

    if len(card_no) != 16:
        print('Invalid Card')
        return

    for i in range(len(card_no)):  # Iterate over indices
        num = int(card_no[i])  # Convert character to integer

        if i % 2 == 0:  # Double every second digit (assuming Luhn's Algorithm-like approach)
            temp = num * 2
            if temp >= 10:  # Sum the digits of a double-digit number
                total_sum += temp // 10 + temp % 10
            else:
                total_sum += temp
        else:
            total_sum += num  # Directly add odd-positioned digits

    if total_sum % 10 == 0:
        print('Valid Credit / Debit Card')
    else:
        print('Invalid Card')

def main():
    card_no = input("Enter card number: ")
    card_checker(card_no)

if __name__ == "__main__":
    main()
