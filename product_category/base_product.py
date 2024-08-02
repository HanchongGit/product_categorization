import re

class Product:
    """
    Base class for products.
    """

    # Class variable to store the product database
    product_data_by_sap = {}
    product_data_by_model = {}

    def __init__(self, sap_code, model_name):
        self.sap_code = str(sap_code).strip() if sap_code else None
        self.model_name = str(model_name).strip() if model_name else None

        # Validate that at least one identifier is available
        if not self.sap_code and not self.model_name:
            raise ValueError("Product must have either a SAP code or a model name.")

        # Only look up in database if needed
        self._lookup_identifiers()
        
        self.class_name = 'Product'  # Default class name
        self.class_num = 'HIK'  # Default class number

        self.brandline = None
        self.body = None
        self.anno = None
        self.extn = None

        self.feature1 = None
        self.feature2 = None
        self.feature3 = None
        self.feature4 = None
        self.feature5 = None
        self.feature6 = None

    def _lookup_identifiers(self):
        """
        Looks up the missing SAP code or model name from the database if needed.
        """
        if not self.sap_code and self.model_name:
            self.sap_code = self.product_data_by_model.get(self.model_name)
        elif not self.model_name and self.sap_code:
            self.model_name = self.product_data_by_sap.get(self.sap_code)

    def _process_model(self, start_index):
        """
        Process model details based on the given starting index.
        """
        hyphen_index = self.model_name.find('-', start_index)
        if hyphen_index != -1:
            self.body = self.model_name[start_index:hyphen_index]
            self.anno = self.model_name[hyphen_index+1:]
        else:
            self.body = self.model_name[start_index:]
            self.anno = ''

        match = re.search(r'[^A-Za-z0-9]', self.anno)
        if match:
            pos = match.start()
            self.anno, self.extn = self.anno[:pos], self.anno[pos:]
        else:
            self.extn = ''

    def __repr__(self):
        return (
            f"{self.class_num}-{self.class_name}(\n"
            f"  model_name='{self.model_name or 'Unknown Model'}',\n"
            f"  sap_code='{self.sap_code or 'Unknown SAP'}',\n"
            f"  brandline='{self.brandline}',\n"
            f"  body='{self.body}',\n"
            f"  anno='{self.anno}',\n"
            f"  extn='{self.extn}',\n"
            f"  feature1='{self.feature1}',\n"
            f"  feature2='{self.feature2}',\n"
            f"  feature3='{self.feature3}',\n"
            f"  feature4='{self.feature4}',\n"
            f"  feature5='{self.feature5}',\n"
            f"  feature6='{self.feature6}'\n"
            f")"
        )
    
    # Common template functions for feature extraction
    
    def extract_feature_focal(self):
        """
        Extracts the lens type feature.
        """
        if re.findall(r'\b\d{1,2}\.\d-\d{1,2}\.\d(?:mm|MM)\b', self.extn):
            return 'Vari-Focal'
        elif 'VF' in self.anno or 'Z' in self.anno:
            return 'Vari-Focal'
        else:
            return 'Fixed Lens'

    def extract_feature_SHL(self):
        """
        Extracts the SHL (Smart Hybrid Light) feature.
        """
        return 'SHL' if 'L' in self.anno else 'No SHL'