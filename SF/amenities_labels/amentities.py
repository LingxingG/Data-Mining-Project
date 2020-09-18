import numpy as np
import pandas as pd

# input in ur own listings.csv path
file_path = ""
df = pd.read_csv(file_path)
amentities_col = df.amenities

amentities_dict = {}
id = 0
for amentities in amentities_col:
    x_striped = amentities[1:-1]
    x_arr = x_striped.split(',')
    
    for amentity in x_arr:
        name = (amentity.strip())[1:-1]
        if name not in amentities_dict:
            amentities_dict[name] = 1
        else:
            amentities_dict[name] += 1

# amentities_dict
sorted_amentities = sorted(amentities_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_amentities)