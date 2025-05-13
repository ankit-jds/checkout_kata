from services.checkout import Checkout

if __name__ == "__main__":
    input_string = input("Enter items (e.g., AAABBD): ").strip().upper()
    checkout = Checkout()
    for char in input_string:
        checkout.scan(char)
    print(f"Total price: Rs {checkout.total()}")
