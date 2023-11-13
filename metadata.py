from neuromorpho_api import requestor as requests
import csv
import sys

endpoint = "https://neuromorpho.org/api/"
# r = requests.get(endpoint + "neuron/id/1")
# # Check that the status_code is 200 and raise if not
# r.raise_for_status()
# data = r.json()
# print(data)

# Neuron name - note the `*` wildcard to select all neurons whose name matches
# this pattern
# siegert_dataset = "CB_CKp25_2w_F_Animal01_*"
pmid = sys.argv[1]


# The GET parameters
query_params = {"q": f"reference_pmid:{pmid}"}

r = requests.get(endpoint + "neuron/select/", params=query_params)
# We let requests handle the URL construction

r.raise_for_status()  # Make sure the request was successful
data = r.json()["_embedded"]["neuronResources"]

# Individual neuron names
sorted(record["neuron_name"] for record in data)
data = [record for record in data if (record["species"] == "human" and record["age_classification"] != "fetus")]
print(data)

filename = 'metadata.csv'
fieldnames = list(data[0].keys())

with open(filename, 'a+', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in data:
        writer.writerow(record)
