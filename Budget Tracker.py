def add_expense(expenses):
    name = input("Harcama adı: ")
    try:
        amount = float(input("Tutar (₺): "))
        expenses.append({"name": name, "amount": amount})
        print("Harcama eklendi.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def list_expenses(expenses):
    if not expenses:
        print("Henüz harcama yok.")
        return
    print("\n--- Harcamalar ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['name']} - {exp['amount']}₺")
    print("------------------")

def main():
    expenses = []
    while True:
        print("\n1. Harcama Ekle")
        print("2. Harcamaları Listele")
        print("3. Çıkış")
        choice = input("Seçim: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
