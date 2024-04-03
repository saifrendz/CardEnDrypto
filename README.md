# Credit Card Encryption and Decryption System

A secure web application for encrypting and decrypting credit card numbers using Python and Flask.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to provide a secure solution for encrypting and decrypting credit card numbers to ensure data privacy and security during transmission and storage. The system utilizes the Flask web framework in Python to create a user-friendly interface for encrypting and decrypting credit card data securely.

## Features

- Encrypt credit card numbers using the Advanced Encryption Standard (AES) encryption algorithm.
- Decrypt encrypted credit card numbers to retrieve the original card number.
- Basic input validation to ensure the credit card number format is valid.
- Store encrypted credit card numbers in a text file for persistence.

## Technologies Used

- Python: Programming language used for backend development.
- Flask: Micro web framework for building the web application.
- cryptography: Python library for secure encryption and decryption.
- HTML/CSS: Frontend markup and styling for the web interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip package manager

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/credit-card-encryption.git
    ```

2. Navigate to the project directory:

    ```bash
    cd credit-card-encryption
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask development server:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Enter a valid credit card number in the input field on the homepage.
2. Click the "Encrypt" button to encrypt the credit card number.
3. To decrypt an encrypted credit card number, input the index of the card in the text file and click the "Decrypt" button.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.