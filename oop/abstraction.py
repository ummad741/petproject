from abc import ABC, abstractmethod

# abstraction nma
# foydalanuvchiga kerakli methdo yoki function
# korsatib ichki systemani jarayoni yashirib qoyish

# real analog
# moshinani haydashda biz faqat gaz, tormoz, va rulni bilamizi
# ammo dvigitel ichida qanaqa event bovotganini bilmimiz va bunga
# extiyoj ham yoq shu abstraction


# incapsulation vs abstraction farqi

# incopsulation: data malumtoni himoyalash yashirish
# abstraction: faqat kerakli malumotni  ko'rsatish

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentSystem):
    def pay(self, amount):
        print(f"PayPal orqali {amount}$ tolov amalga oshirildi.")


class CreaditCard(PaymentSystem):
    def pay(self, amount):
        print(f"CredigCard orqali {amount}$ tolov amalga oshirildi.")


class Click(PaymentSystem):
    def pay(self, amount):
        print(f"Click orqali {amount}$ tolov amalga oshirildi.")


paypal = PayPal()
creadit_card = CreaditCard()
click = Click()
paypal.pay(40)
creadit_card.pay(40)
click.pay(40)


# cli payment system
def process_payment(payment_method, amount):
    payment_method.pay(amount)


def main():
    print("Tolov tizimiga xush kelibsiz!")
    print("Quyidagi usullardan birini tanlang:")
    print("1. PayPal")
    print("2. Kredit karta")
    print("3. Click")

    try:
        choice = int(input("tolov usulini tanlang: "))

        try:
            amount = float(input("Tolov summasini kiriting ($): "))
        except ValueError:
            print(" Notogri summa. Raqam kiriting.")

        if choice == 1:
            method = PayPal()
        elif choice == 2:
            method = CreaditCard()
        elif choice == 3:
            method = Click()
        else:
            print("Notogri tanlov")

        # tolov
        process_payment(method, amount)
    except:
        print("Raqam kiriting.")

# if/else vs try except
# if filename.endswith('.txt'):
#     open(filename)
# else:
#     print("Faqat .txt fayllar qabul qilinadi")

# # try/except
# try:
#     with open(filename) as f:
#         data = f.read()
# except FileNotFoundError:
#     print("Fayl topilmadi")
    

if __name__ == "__main__":
    main()
