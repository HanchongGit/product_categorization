# Product Categorization

This project is designed to categorize products based on their features and specifications. It utilizes a database to store product data and a factory pattern for creating product objects. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Features](#features)
- [Testing](#testing)
- [Contributing](#contributing)

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/product-categorization.git
    cd product-categorization
    ```

2. **Create a Virtual Environment** (Optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    Make sure you have all necessary packages installed. You can do this by using:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

You can run the main application script to experiment with the product categorization application:

```bash
python -m scripts.main
```
To run the GUI interface, use:

```bash
python -m scripts.product_ui
```


## Directory Structure

```
product_categorization/
├── archive/                   # Contains archived Excel files
├── database/                  # Database scripts and files
│   ├── __init__.py
│   ├── db_operations.py
│   └── product_features.db
├── product_category/          # Product categorization logic
│   ├── analog_camera.py
│   ├── base_product.py
│   ├── generic_product.py
│   └── product_factory.py
├── scripts/                   # Main scripts for running the application
│   ├── main.py
│   └── product_ui.py
├── tests/                     # Unit tests for the application
└── requirements.txt           # Project dependencies
```

## Features

- **Product Categorization**: Categorizes products based on features using a factory pattern.
- **Database Integration**: Uses SQLite for data storage and retrieval.
- **Excel File Handling**: Imports product data from Excel files.

## Testing

Unit tests are provided for the main components of the application. To run the tests, use:

```bash
pytest tests
```

Ensure that you have installed `pytest` by checking the `requirements.txt`.

## Contributing

Contributions are welcome! If you have ideas or enhancements, feel free to fork the repository and submit a pull request.

1. **Fork the Project**: Click the "Fork" button at the top right of the repository page on GitHub.
2. **Create Your Feature Branch**: 
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Commit Your Changes**: Ensure your commit messages are clear and descriptive.
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/new-feature
   ```
5. **Open a Pull Request**: Navigate to the original repository and click the "Compare & pull request" button.

### Adding New Categorization Rules

If you want to add new categorization rules, please work under the `product_category` module. Specifically:

- **Add New Classes or Methods**: Implement new categorization logic by creating new classes or extending existing ones like `analog_camera.py` or `generic_product.py`.
- **Document Your Changes**: Clearly comment your code and update any relevant documentation to explain your categorization logic.

### Designing Tests

Design tests under the `tests` directory to ensure your new categorization rules function as expected:

- **Create New Test Files**: Add test files corresponding to your new categories, such as `test_new_category.py`.
- **Use Pytest**: Structure your tests using the `pytest` framework to maintain consistency with existing tests.
- **Test Cases**: Cover edge cases, typical use cases, and any potential failure modes. Ensure tests are comprehensive.

### Guidelines

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
- Ensure all tests pass before submitting a pull request.
- Provide a detailed description of the changes in your pull request, including any new features or fixes.

Thank you for contributing to the project!
