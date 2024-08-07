from .base_product import Product

class NonVideo(Product):
    """Class for non-video products categorization."""

    def __init__(self, sap_code, model_name):
        super().__init__(sap_code, model_name)
        
        self.class_name = 'Analog Camera'
        self.class_num = Product.class_name_to_num.get(self.class_name, None)

        if self.brandline == 'Pyronix':
            self.extract_feature_pyronix()
        elif self._matches_any(["*DS-K*", "*IC S50*", "*ISD-S*", "*NP-S*", "*DS-PEA*"]):
            self.feature1 = self.categorize_catalog()
            self.feature2 = self.categorize_product_type()
            self.feature3 = self.categorize_product_series()
            self.feature4 = self.categorize_technology()
            self.feature5 = self.categorize_two_wire_hd()
            self.feature6 = self.categorize_materials()
        elif self._matches_any(["*DS-P*"]):
            self.extract_feature_alarm()

    def categorize_catalog(self):
        if self._matches_any(["*DS-KA01*", "*DS-KA86*", "*DS-KAB8*", "*DS-KABD*", "*DS-KABH*", "*DS-KABV*", "*DS-KAD*", "*DS-KAW*", "*DS-KD*", "*DS-KH*", "*DS-KM*", "*DS-KIS*", "*DS-KV*", "*DS-KP*", "*DS-KB*", "*DS-PEA*"]):
            return "Intercom"
        elif self._matches_any(["*DS-K2*", "*DS-K1*", "*DS-K4*", "*DS-K5*", "*DS-K6*", "*DS-K7*", "*DS-KAB5*", "*DS-KAB-*", "*DS-KAB6*", "*DS-KAB3*", "*DS-KAS*", "*DS-KZX*", "*IC S50*"]):
            return "ACS"
        elif self._matches_any(["*DS-K3*"]):
            return "Gate&Tripod"
        elif self._matches_any(["*ISD-SM*", "*ISD-ST*", "*ISD-SC*", "*NP-SG*", "*NP-SH*"]):
            return "Security Inspection"
        else:
            return "others"

    def categorize_product_type(self):
        if self._matches_any(["*DS-KD*", "*DS-KV*", "*DS-KB*"]):
            return "Door Station"
        elif self._matches_any(["*DS-KH*", "*DS-KP*", "*DS-KM*"]):
            return "Indoor Station"
        elif self._matches_any(["*DS-KIS*"]):
            return "Intercom Kit"
        elif self._matches_any(["*DS-KA01*", "*DS-KAB1*", "*DS-KABD*", "*DS-KAB81*", "*DS-KABH*", "*DS-KABV*", "*DS-KAD*", "*DS-KAW*"]):
            return "Intercom Accessory"
        elif self._matches_any(["*DS-K2*"]):
            return "Control Panel"
        elif self._matches_any(["*DS-K11*", "*DS-K18*", "*DS-K12*"]):
            return "Card Reader"
        elif self._matches_any(["*DS-K1T*", "*DS-K1A*", "*DS-K56*", "*DS-K50*", "*DS-K63*"]):
            return "Terminal"
        elif self._matches_any(["*DS-K4*", "*DS-K7*", "*DS-K1F*", "*DS-KAB5*", "*DS-KAB-*", "*DS-KAB6*", "*DS-KAB3*", "*DS-KAS*", "*DS-KZX*", "*IC S50*", "*FM11RF08-M1*", "*S50+TK4100*", "*DS-KAB805*", "*DS-KAB502*"]):
            return "ACS Accessory"
        elif self._matches_any(["*DS-K3G*"]):
            return "Tripod"
        elif self._matches_any(["*DS-K3B5*", "*DS-K3B6*", "*DS-K3B8*", "*DS-K3B4*", "*DS-K3B2*", "*DS-K3B9*"]):
            return "Swing Barrier"
        elif self._matches_any(["*DS-K3BC*"]):
            return "Swing Gate"
        else:
            return "others"

    def categorize_product_series(self):
        if self._matches_any(["*DS-KD8003*", "*DS-KD9005*", "*DS-KD9000*"]):
            return "Main Unit"
        elif self._matches_any(["*DS-KD-D*", "*DS-KD-I*", "*DS-KD-B*", "*DS-KD-K*", "*DS-KD-E*", "*DS-KD-M*", "*DS-KD-TD*", "*DS-KD-VG*", "*DS-KD-PMR*"]):
            return "Sub Module"
        elif self._matches_any(["*DS-KD-AC*"]):
            return "Modular Bracket"
        elif self._matches_any(["*DS-KDE-AC*"]):
            return "2wire HD Bracket"
        elif self._matches_any(["*DS-KV8*13*", "*DS-KV6*", "*DS-KB*", "*DS-KV9*", "*DS-KV8*02*", "*DS-KV8*03*", "*DS-KV1101*"]):
            return "Villa Door Station"
        elif self._matches_any(["*DS-KD9*", "*DS-KD8103*", "*DS-KD8023*", "*DS-KD3003*", "*DS-KD3002*", "*DS-KD8*02*", "*DS-KD8*13*"]):
            return "Apartment Door Station"
        elif self._matches_any(["*DS-KD7003*", "*DS-KD7000*"]):
            return "2wire HD Main Unit"
        elif self._matches_any(["*DS-KH6320*WTE*", "*DS-KH6320*TE1*", "*DS-KH6320*TE2*", "*DS-KH6320*TDE1*", "*DS-KH6300*", "*DS-KH6310*", "*DS-KH834*"]):
            return "Pro Indoor Station"
        elif self._matches_any(["*DS-KH6350*"]):
            return "KH6350"
        elif self._matches_any(["*DS-KH6351*"]):
            return "KH6351"
        elif self._matches_any(["*DS-KH6320*LE*"]):
            return "KH6320Lite"
        elif self._matches_any(["*DS-KH7300*", "*DS-KH7000*", "*DS-KH7100*"]):
            return "2wire HD Indoor Station"
        elif self._matches_any(["*DS-KH835*", "*DS-KH852*", "*DS-KH811*", "*DS-KH830*"]):
            return "Ultra Indoor Station"
        elif self._matches_any(["*DS-KH9*"]):
            return "Smart Indoor Station"
        elif self._matches_any(["*DS-KH61*", "*DS-KH60*"]):
            return "Small Inch Indoor Station"
        elif self._matches_any(["*DS-KIS202*", "*DS-KIS203*", "*DS-KIS204*", "*DS-KIS212*", "*DS-KIS213*", "*DS-KIS205*", "*DS-KIS206*"]):
            return "KIS212"
        elif self._matches_any(["*DS-KIS101*", "*DS-KIS102*"]):
            return "KIS102"
        elif self._matches_any(["*DS-KIS302*", "*DS-KIS303*", "*DS-KIS311*", "*DS-KIS312*"]):
            return "KIS311"
        elif self._matches_any(["*DS-KIS703*"]):
            return "KIS703"
        elif self._matches_any(["*DS-KIS701*", "*DS-KIS702*", "*DS-KIS704*"]):
            return "KIS704"
        elif self._matches_any(["*DS-KIS602*", "*DS-KIS601*"]):
            return "KIS602"
        elif self._matches_any(["*DS-KIS604*"]):
            return "KIS604"
        elif self._matches_any(["*DS-KIS603*"]):
            return "KIS603"
        elif self._matches_any(["*DS-KIS607*"]):
            return "KIS607"
        elif self._matches_any(["*DS-KIS902*", "*DS-KIS901*"]):
            return "KIS902"
        elif self._matches_any(["*DS-KIS606*"]):
            return "KIS606"
        elif self._matches_any(["*VI-V*", "*VI-H*", "*VI-B*", "*VI-K*"]):
            return "Intercom HiLook"
        elif self._matches_any(["*DS-K27*"]):
            return "K27"
        elif self._matches_any(["*DS-K26*"]):
            return "K26"
        elif self._matches_any(["*DS-K28*"]):
            return "K28"
        elif self._matches_any(["*DS-K1109*"]):
            return "K1109"
        elif self._matches_any(["*DS-K1108*"]):
            return "K1108"
        elif self._matches_any(["*DS-K1107*"]):
            return "K1107"
        elif self._matches_any(["*DS-K18*"]):
            return "K18 series"
        elif self._matches_any(["*DS-K1T805*"]):
            return "K1T805"
        elif self._matches_any(["*DS-K1T502*", "*DS-K1T501*", "*DS-K1T500*"]):
            return "K1T502"
        elif self._matches_any(["*DS-K1T3*", "*DS-K1A3*"]):
            return "MinMoe distribution"
        elif self._matches_any(["*DS-K1T804*", "*DS-K1A8*", "*DS-K1T1*", "*DS-K1T2*"]):
            return "Fingerprint terminal"
        elif self._matches_any(["*DS-K1T6*", "*DS-K1T9*", "*DS-K50*", "*DS-K56*", "*DS-K63*"]):
            return "MinMoe project"
        elif self._matches_any(["*DS-K3G501*"]):
            return "K3G501"
        elif self._matches_any(["*DS-K3G411*"]):
            return "K3G411"
        elif self._matches_any(["*DS-K3B501*", "*DS-K3B411*"]):
            return "K3B501"
        elif self._matches_any(["*DS-K3B530*", "*DS-K3B601*"]):
            return "K3B530"
        elif self._matches_any(["*DS-K3B801*", "*DS-K3B802*"]):
            return "K3B801"
        elif self._matches_any(["*DS-K3BC430*", "*DS-K3BC411*"]):
            return "K3BC430"
        else:
            return "others"

    def categorize_technology(self):
        if self._matches_any(["*DS-KD8*E2*", "*DS-KD7*E2*", "*DS-KH*E2*", "*DS-KIS101*", "*DS-KIS102*", "*DS-KIS701*", "*DS-KIS702*", "*DS-KIS703*", "*DS-KIS704*", "*DS-KAD706*", "*DS-KAD*L*", "*DS-KAD*EP*", "*DS-KAW60-2N*", "*DS-KAW150-4N*"]):
            return "2wire"
        else:
            return "others"

    def categorize_two_wire_hd(self):
        if self._matches_any(["*DS-K*EY*", "*DS-KAW150-4N*"]):
            return "2wireHD"
        else:
            return "others"

    def categorize_materials(self):
        if self._matches_any(["*DS-KD7*E2*", "*DS-KD8*/NS*", "*DS-KD8*/S*", "*DS-KD9005*/S*", "*DS-KD-K*/S*", "*DS-KD-MF*/S*", "*DS-KD-AC*/S*", "*DS-KIS602*/S*", "*DS-KIS702*/S*"]):
            return "Stainless Steel"
        elif self._matches_any(["*DS-KH*W*"]):
            return "Wireless"
        elif self._matches_any(["*DS-KV6113*", "*DS-KV8113*"]):
            return "One button"
        elif self._matches_any(["*DS-KV8213*"]):
            return "Two Buttons"
        elif self._matches_any(["*DS-KV8413*"]):
            return "Four Buttons"
        elif self._matches_any(["*海外中性*", "*NEU*"]):
            return "NEU"
        else:
            return "STD"
        
    def extract_feature_alarm(self):
        self.feature1 = "Alarm"

    def extract_feature_pyronix(self):
        self.feature1 = "PYRONIX"