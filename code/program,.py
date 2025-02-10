import json
from packaging import parse_packaging, calc_total_units, get_unit

all_packages = []
with open('data/packaging.txt', 'r') as file:
    for line in file:
        if not line.strip():
            continue

        package = parse_packaging(line.strip())
        total = calc_total_units(package)
        unit = get_unit(package)
        print(f"{line.strip()} => total units: {total} {unit}")
        all_packages.append(package)
with open('data/packaging.json', 'w') as json_file:
    json.dump(all_packages, json_file, indent=4)