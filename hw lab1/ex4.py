import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot
from pymongo import MongoClient
# Connect to database sever

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
# Select Database

db = client.get_database()

# Select Collection
customers_collection = db["customers"]

# Count Number Of Customers Group
event = customers_collection.count_documents({"ref": "events"})
wom = customers_collection.count_documents({"ref": "wom"})
ads = customers_collection.count_documents({"ref": "ads"})

refs_counts = [event, wom, ads]
refs_types = ["Events", "Wom", "Ads"]

# Draw A Pie Chart
pyplot.pie(refs_counts, labels=refs_types, autopct="%.1f%%", explode=[0, 0.1, 0])
pyplot.title("REFERENCES")
pyplot.axis("equal")

pyplot.show()

# Close connection
client.close()