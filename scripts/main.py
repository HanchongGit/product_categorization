from product_category import create_product

def main():
    # Example product creation
    products_to_create = [
        ("300508317", "DS-2CE16D8T-IT3(3.6mm)(O-STD)"),
        ("202002308", "K3G501-C"),
        ("123456789", "XYZ-Model")
    ]

    for sap_code, model_name in products_to_create:
        product = create_product(sap_code, model_name)
        print(product)

if __name__ == "__main__":
    main()
