def parse_packaging(packaging_data: str) -> list[dict]:
    result = []
    parts = packaging_data.split("/")
    
    for part in parts:
        quantity_unit, _ = part.strip().split(" in ")
        parts = quantity_unit.strip().split(" ")
        quantity = int(parts[0])
        unit = " ".join(parts[1:]) 
        result.append({unit: quantity})
    
    return result
   
def calc_total_units(package: list[dict]) -> int:
    total = 1
    for item in package:
        total *= list(item.values())[0]
    return total

def get_unit(package: list[dict]) -> str:
    return list(package[0].keys())[0]

if __name__ == '__main__':
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)
    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")