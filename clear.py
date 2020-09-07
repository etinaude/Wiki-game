import json
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(datastore, f)