# CHECKOUT_KATA_ASSIGNMENT_NARESH

## Description

This is a simple supermarket checkout system that calculates the total price of items added to the cart by a customer. Each item is represented by a letter (e.g., A, B, C, D) and may have special discount offers when purchased in bulk.

For example, item 'A' costs Rs 50 individually, but a special offer gives 3 A's for Rs 130. The system handles items in any order and applies discounts where applicable.



## Tech Stack

- **Python**: Core programming language
- **Pytest**: For unit testing
- **OOP & MVT Structure**: Used for clean and scalable design



## To run the app locally, follow the steps below:

### 1. Clone the Repo

git clone https://github.com/ankit-jds/checkout_kata.git
cd checkout_kata


### 2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run the App

python main.py


You will be prompted to enter items like `AAABBD`, and the app will calculate the total price based on the pricing rules.



## Running Tests

To run the unit tests, use the following command:

pytest


All test cases are written using `pytest` and are located inside the `tests/` directory.



## Design Decisions

* **OOP Design**: Used classes for both `Product` and `Checkout` to make the system extensible.
* **Modular Structure**: Business logic is separated from the input/output layer for better testability and readability.
* **Discount Logic**: Clearly defined in a dictionary and handled using clean calculations.

---

## Future Improvements

* Add support for new promotions via configuration or database
* Convert this into a REST API using FastAPI or Flask
* Add a CLI or web-based frontend for easier interaction
