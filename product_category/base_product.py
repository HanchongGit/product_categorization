import re
import pandas as pd
from database import load_data_from_sql_table

class Product:
    """
    Base class for products.
    """

    # Class variable to store the product database as a DataFrame
    product_df = None
    database_loaded = False

    def __init__(self, sap_code, model_name):
        self.sap_code = str(sap_code).strip() if sap_code else None
        self.model_name = str(model_name).strip() if model_name else None

        # Validate that at least one identifier is available
        if not self.sap_code and not self.model_name:
            raise ValueError("Product must have either a SAP code or a model name.")
        
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
        self.feature7 = None
        self.feature8 = None
        self.feature9 = None
        self.feature10 = None
        
        # Load the product database if not already loaded
        if not Product.database_loaded:
            Product.load_product_database()

        # Look up identifiers and features in the DataFrame
        self._lookup_identifiers_and_features()
        
    
    @staticmethod
    def load_product_database():
        """Load the product database into a DataFrame if not already loaded."""
        # Load data from the 'feature_db' table
        feature_data = load_data_from_sql_table('database/product_features.db')

        # Create a DataFrame from the feature data
        Product.product_df = pd.DataFrame(feature_data)
        Product.product_df['sap_code'] = Product.product_df['sap_code'].astype(str)

        # Set 'sap_code' as the index for quick lookups
        Product.product_df.set_index('sap_code', inplace=True)

        Product.database_loaded = True

    def _lookup_identifiers_and_features(self):
        """
        Looks up the missing SAP code, model name, and features from the database if needed.
        """
        if self.sap_code:
            if self.sap_code in Product.product_df.index:
                product_info = Product.product_df.loc[self.sap_code]
                self.model_name = self.model_name or product_info['model_name']
                self._populate_features(product_info)
        elif self.model_name:
            result = Product.product_df[Product.product_df['model_name'] == self.model_name]
            if not result.empty:
                self.sap_code = self.sap_code or result.index[0]
                self._populate_features(result.iloc[0])

    def _populate_features(self, product_info):
        """Populate product features from the product information."""
        self.brandline = product_info.get('brandline')
        self.feature1 = product_info.get('feature1')
        self.feature2 = product_info.get('feature2')
        self.feature3 = product_info.get('feature3')
        self.feature4 = product_info.get('feature4')
        self.feature5 = product_info.get('feature5')
        self.feature6 = product_info.get('feature6')
        self.feature7 = product_info.get('feature7')
        self.feature8 = product_info.get('feature8')
        self.feature9 = product_info.get('feature9')
        self.feature10 = product_info.get('feature10')

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
            f"  feature6='{self.feature6}',\n"
            f"  feature7='{self.feature7}',\n"
            f"  feature8='{self.feature8}',\n"
            f"  feature9='{self.feature9}',\n"
            f"  feature10='{self.feature10}'\n"
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