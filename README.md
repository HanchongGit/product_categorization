# Product Categorization System

The Product Categorization System is a Python-based application designed to categorize and manage product data efficiently.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)

## Project Structure

```
product_categorization/
│
├── product_category/
│   ├── __init__.py
│   ├── base_product.py
│   ├── analog_camera.py
│   ├── generic_product.py
│   ├── product_factory.py
│   └── utils.py
│
├── database/
│   ├── __init__.py
│   ├── loader.py
│   └── data_files/
│       ├── products.csv
│       └── products.xlsx
│
├── scripts/
│   ├── __init__.py
│   └── main.py
│
└── tests/
    ├── __init__.py
    ├── test_product_category.py
    ├── test_analog_camera.py
    ├── test_generic_product.py
    └── test_factory.py
```

### Key Components

- **`product_category/`**: Contains the core classes for managing products, including the base `Product` class, specific product types (e.g.`Analog_Camera`, `Generic_Product`), and the factory for creating product instances.

- **`database/`**: Manages loading product data from CSV and Excel files. The `data_files/` directory holds database file for (SAP Code)-(Model Name) mapping.

- **`scripts/`**: Contains executable scripts, such as `main.py`, which demonstrates how to use the product categorization system.

- **`tests/`**: Includes unit tests for each component of the system, ensuring reliability and correctness.

## Setup and Installation

### Prerequisites

- Python 3.6 or later
- `pip` (Python package manager)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/product_categorization.git
   cd product_categorization
   ```

2. **Create a Virtual Environment** 

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts ctivate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. **Run the Main Script**

   Navigate to the project root and execute the main script using Python:

   ```bash
   python -m scripts.main
   ```

2. **Add New Products**

   Modify the CSV or Excel files in the `database/data_files/` directory to include new products. The system automatically loads these files upon execution.

3. **Extend Functionality**

   To add new product types, create a new subclass in the `product_category` directory and update the factory function in `product_factory.py`.

## Testing

1. **Run Tests**

   Use `pytest` to run all unit tests in the `tests` directory:

   ```bash
   pytest tests
   ```

2. **Add New Tests**

   Create new test files or extend existing ones to cover additional functionality or edge cases.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

