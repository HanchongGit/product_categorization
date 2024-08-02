import re
from .base_product import Product

class Generic_Product(Product):
    """
    Template class for other product lines. Inherit from this class to create specific product classes.
    """

    def __init__(self, sap_code=None, model_name=None):
        super().__init__(sap_code, model_name)

        self.class_name = 'Generic Product'
        self.class_num = 'XX'

        # Process model details specific to this product line
        if self.model_name:
            self._process_model(4)

            # Extract features specific to this product line
            self.extract_features()

    def extract_features(self):
        """
        Extract features specific to this product line.
        Customize this method as needed.
        """
        # Example feature extraction logic
        self.feature1 = "Generic Feature 1"
        self.feature2 = "Generic Feature 2"
