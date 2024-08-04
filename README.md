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
│
├── database/               # Database scripts and files
│   ├── __init__.py
│   ├── db_operations.py    # Database operations
│   └── product_features.db # SQLite database file
├── archive/                   # Contains archived Excel files
│
├── product_category/       # Product categorization logic
│   ├── __init__.py         # Package initialization
│   ├── analog_camera.py    # Analog camera subclass
│   ├── base_product.py     # Base class for products
│   ├── generic_product.py  # Generic product subclass
│   ├── product_factory.py  # Factory function to create product instances
│   └── new_category.py     # Placeholder for new category subclass
│
├── scripts/                # Main scripts for running the application
│   ├── main.py             # Main script to run the application
│   └── product_ui.py       # Script for running the GUI
│
├── tests/                  # Unit tests for the application
│   ├── test_main.py        # Tests for main script
│   └── test_product_category.py # Tests for product categories
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
└── prompt_template.txt     # Structured prompt template for generating project guidance
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

### ChatGPT Prompt Template

`prompt_template.txt` contains a structured prompt template used to generate guidance and detailed instructions for interacting with the product_categorization repository. It can be used by users to get comprehensive insights and help for understanding and modifying the repository's code and structure.

### Step-by-Step Guide to Adding a New Product Class

1. **Create a New File for the Category**

   Navigate to the `product_category` directory and create a new Python file for your category. For a "Digital Camera" category, create a file named `digital_camera.py`:

   ```bash
   product_categorization/product_category/digital_camera.py
   ```

2. **Define the New Subclass**

   In `digital_camera.py`, define a class that inherits from `Product`. Implement initialization and feature extraction specific to this category.

   ```python
   # digital_camera.py

   from .base_product import Product

   class DigitalCamera(Product):
       """
       Class for products in the Digital Camera line.
       """

       def __init__(self, sap_code, model_name):
           super().__init__(sap_code, model_name)

           self.class_name = 'Digital Camera'
           self.class_num = '04'  # Assign a unique class number

           # Example: Extract model details and features specific to digital cameras
           if self.model_name.startswith('DC-'):
               self.brandline = 'Canon'
               self._process_model(5)
               self.extract_features_canon()

       def extract_features_canon(self):
           """
           Extract features specific to Canon Digital Cameras.
           """
           # Implement feature extraction logic for Canon digital cameras
           self.feature1 = self.body[2] + ' MP'
           self.feature2 = 'Optical Zoom' if 'OZ' in self.model_name else 'Digital Zoom'
           self.feature3 = self.extract_feature_focal_length()

       def extract_feature_focal_length(self):
           """
           Example method to extract focal length feature.
           """
           # Dummy implementation
           return '35-105mm' if '35' in self.model_name else '28-80mm'
   ```

   - **Initialization**: Initialize the subclass with a constructor that calls the parent class (`Product`) constructor.
   - **Feature Extraction**: Implement methods to extract and process features unique to the category.

3. **Update the Factory Function**

   Integrate the new subclass into the factory function to create instances of the new product type when appropriate conditions are met.

   Edit `product_factory.py` to include the new class:

   ```python
   # product_factory.py

   from .base_product import Product
   from .analog_camera import Analog_Camera
   from .generic_product import Generic_Product
   from .digital_camera import DigitalCamera  # Import the new category

   def create_product(sap_code, model_name):
       """
       Factory function to create a product instance based on criteria.
       """

       product = Product(sap_code, model_name)

       # Check criteria for Analog_Camera
       if product.model_name.startswith('DS-2C') or product.model_name.startswith('HWT-') or product.model_name.startswith('THC-'):
           return Analog_Camera(sap_code, model_name)

       # Check criteria for DigitalCamera
       if product.model_name.startswith('DC-'):
           return DigitalCamera(sap_code, model_name)

       # Default to Generic_Product if no specific subclass criteria are met
       return Generic_Product(sap_code, model_name)
   ```

   - **Factory Logic**: Add a condition that checks the model name or other criteria to determine when to instantiate the `DigitalCamera` class.

4. **Update `__init__.py`**

   Add the new subclass to the `__init__.py` file so it can be easily imported from the `product_category` module:

   ```python
   # product_category/__init__.py

   from .base_product import Product
   from .analog_camera import Analog_Camera
   from .generic_product import Generic_Product
   from .digital_camera import DigitalCamera  # Import the new category
   from .product_factory import create_product

   __all__ = ['Product', 'Analog_Camera', 'Generic_Product', 'DigitalCamera', 'create_product']
   ```

5. **Test the New Class**

   Create tests to ensure your new category class functions as expected. Add tests in `tests/test_product_category.py`:

   ```python
   # tests/test_product_category.py

   import pytest
   from product_category.digital_camera import DigitalCamera

   def test_digital_camera_initialization():
       dc = DigitalCamera('12345', 'DC-CanonX-35')
       assert dc.class_name == 'Digital Camera'
       assert dc.class_num == '04'
       assert dc.feature1 == 'X MP'  # Replace X with expected value
       assert dc.feature2 == 'Optical Zoom'
       assert dc.feature3 == '35-105mm'
   ```

   - **Test Initialization**: Verify that the class initializes correctly with the proper attributes.
   - **Test Feature Extraction**: Ensure that features are correctly extracted based on the model details.

6. **Run Tests**

   Run the tests to ensure that everything is working as expected:

   ```bash
   pytest tests
   ```

   Ensure all tests pass and that your new category class integrates smoothly with the existing system.

### Guidelines

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.
- Ensure all tests pass before submitting a pull request.
- Provide a detailed description of the changes in your pull request, including any new features or fixes.

Thank you for contributing to the project!
