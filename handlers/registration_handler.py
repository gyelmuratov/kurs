
def regis_handlers():
    javob  = input("Ro'yxatdan o'tmoqchimisiz? (ha/yo'q)").strip().lower()

    if javob in ['ha']:
        print('Registartsiya boshlandi')
        first_name = input("First name: ")
        last_name = input("Last name: ")
        phone_number = input("Phone number: ")
        return first_name, last_name, phone_number

    else:
        print('Registratsiya bekor qilindi')
        return None