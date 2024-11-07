
def main():
    user_id = 1

    while True:
        name = input("Ismingizni kiriting: ")
        lastname = input("Familyangizni kiriting: ")

        while True:
            try:
                age = int(input("Yoshingizni kiriting: "))
                break
            except ValueError:
                print("Iltimos, yoshi raqam shaklida bo'lishi kerak.")

        while True:
            phone = input("Telefon raqamingizni kiriting (+998 formatida): ")
            if phone.startswith("+998") and phone[4:].isdigit() and len(phone) == 13:
                break
            else:
                print("Noto'g'ri telefon raqami. Iltimos, +998 formatida kiriting.")

        email = input("Email manzilingizni kiriting: ")
        address = input("Manzilingizni kiriting: ")

        user_info = {
            'id': user_id,
            'name': name,
            'lastname': lastname,
            'age': age,
            'phone': phone,
            'email': email,
            'address': address
        }

        with open("users_info.txt", "a") as file:
            file.write(str(user_info) + "\n")

        user_id += 1

        another = input("Yana ma'lumot kiritasizmi? (ha/yo'q): ")
        if another.lower() != 'ha':
            break


if __name__ == "__main__":
    main()