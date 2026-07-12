def verify_card_number(card_number):
    if '-' in card_number:
        card_number = card_number.replace('-', '')
    if ' ' in card_number:
        card_number = card_number.replace(' ', '')

    sum_ = int(card_number[-1])

    print(card_number)
    
    current = 1
    for i in range(len(card_number)-2, -1,-1):
        if current%2 != 0:
            if int(card_number[i])*2 > 9:
                sum_ += int(card_number[i])*2 - 9
            else:
                sum_ += int(card_number[i])*2
        else:
            sum_ += int(card_number[i])
        current += 1

    if sum_%10 == 0:
        return "VALID!"
    return "INVALID!"


