import re
from .base_product import Product

class Analog_Camera(Product):
    """
    Class for products in the Analog Camera line.
    """

    def __init__(self, sap_code, model_name):
        super().__init__(sap_code, model_name)
        
        self.class_name = 'Analog Camera'
        self.class_num = '03'

        if self.model_name.startswith('DS-2C'):
            self.brandline = 'Hikvision'
            self._process_model(5)
            self.extract_features_hikvision()

        elif self.model_name.startswith('HWT-'):
            self.brandline = 'HiWatch'
            self._process_model(4)
            self.extract_features_hiwatch()

        elif self.model_name.startswith('THC-'):
            self.brandline = 'HiLook'
            self._process_model(4)
            self.extract_features_hilook()

    def extract_features_hikvision(self):
        """
        Extracts features specific to Hikvision Analog Cameras.
        """
        mapping_feature1 = {
            'C': 'Others',
            'D': '2 MP',
            'F': 'Others',
            'H': '5 MP',
            'K': '5 MP',
            'U': '8 MP'
        }

        # Determine feature1 based on the character
        self.feature1 = mapping_feature1.get(self.body[3], None)

        mapping_feature2 = {
            "C0T": "Value",
            "D0T": "Value",
            "D3T": "Value",
            "H0T": "Value",
            "K0T": "Value",
            "U0T": "Value",
            "U1T": "Value",
            "D8T": "Pro",
            "D9T": "Pro",
            "H8F": "Pro",
            "U7T": "Pro",
            "DF0T": "ColorVu",
            "DF3T": "ColorVu",
            "DF8T": "ColorVu",
            "DFT": "ColorVu",
            "HFT": "ColorVu",
            "KF0T": "ColorVu",
            "KF3T": "ColorVu",
            "UF3T": "ColorVu"
        }

        # Extract feature2 using the mapping dictionary
        self.feature2 = next((pattern for pattern in mapping_feature2 if pattern in self.body[3:]), None)
        self.feature3 = mapping_feature2.get(self.feature2, '')

        self.feature4 = self.extract_feature_SHL()

        self.feature5 = self.extract_feature_focal()

        self.feature6 = 'POC' if 'E' in self.anno else 'No POC'

    def extract_features_hiwatch(self):
        """
        Extracts features specific to HiWatch Analog Cameras.
        """
        self.feature1 = self.body[2] + ' MP'

        self.feature2 = 'ColorVu' if self.body[3] == '9' else 'Basic'

        self.feature3 = 'IR Light'

        self.feature4 = self.extract_feature_focal()

    def extract_features_hilook(self):
        """
        Extracts features specific to HiLook Analog Cameras.
        """
        self.feature1 = self.body[2] + ' MP'

        self.feature2 = 'ColorVu' if self.body[3] == '9' else 'Basic'

        self.feature3 = 'IR Light(SHL)' if 'L' in self.anno else 'IR Light'

        self.feature4 = self.extract_feature_focal()