
bill_counter = 1000

def new_bill_number():
    global bill_counter

    bill_counter += 1

    return "HB" + str(bill_counter)
