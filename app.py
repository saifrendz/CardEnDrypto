from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Simulated database to store encrypted credit card data
credit_cards = []


def validate_credit_card(card_number):
    # Perform validation logic here, e.g., using regex or a library
    if len(card_number.strip()) != 16:
        return False
    return True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    credit_card_number = request.form['credit_card_number']

    if not credit_card_number.strip():
        return "Credit card number cannot be blank!"

    if not validate_credit_card(credit_card_number):
        return "Invalid credit card number format!"

    encrypted_card = cipher_suite.encrypt(credit_card_number.encode())
    credit_cards.append(encrypted_card)
    return "Credit card encrypted successfully!"


@app.route('/decrypt', methods=['POST'])
def decrypt():
    index = int(request.form['index'])
    try:
        encrypted_card = credit_cards[index]
        decrypted_card = cipher_suite.decrypt(encrypted_card).decode()
        return f"Decrypted Credit Card Number: {decrypted_card}"
    except IndexError:
        return "Invalid index!"


if __name__ == '__main__':
    app.run(debug=True)