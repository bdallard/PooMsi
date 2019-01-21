import os
import numpy as np
import re
import pandas as pd
import json

if False:
	raw_listings = open("data/listings.csv").readlines()

	# This will clean shifted ; that are in title and cause column mismatch
	for i, line in enumerate(raw_listings):
		matches = [(m.start(0), m.end(0)) for m in re.finditer(r"(?![\d+;]).*;(?=entire_home|private_room|shared_room)", line)]
		if len(matches) == 0 or len(matches) > 1:
			continue
		m = matches[0]
		new_line = line[:m[0]] + line[m[0]:m[1]-1].replace(";", ",") + line[m[1]-1:]
		raw_listings[i] = new_line

	open("clean/listings.csv", "w").write("".join(raw_listings))

dataset = pd.read_csv("clean/listings.csv", sep=";")

# Now we consider features as variables :
new_columns = []

def get_value_of(data, key):
	return 0 if key not in data else data[key]

keywords = [ "beds", "bedrooms", "bathrooms", "is_rebookable", "is_new_listing", "is_fully_refundable", "is_host_highly_rated", "is_business_travel_ready" ]

for key in keywords:
	values = []

	for i, row in dataset.iterrows():
		row_data = json.loads(row["features"])
		values.append(get_value_of(row_data, key))

	dataset[key] = pd.Series(data=values)

# Same of pricing factor : the more your journey is long, the less you pay per day
keywords = [ "weekly_factor", "monthly_factor" ]

for key in keywords:
	values = []

	for i, row in dataset.iterrows():
		row_data = json.loads(row["pricing"])
		values.append(get_value_of(row_data, key))

	dataset["pricing_" + key] = pd.Series(data=values)

dataset = dataset.drop(["pricing", "pictures", "features", "host_id", "host_name", "host_data"], axis=1)
print(dataset)
dataset.to_csv("clean/listings_final.csv", sep=";")
