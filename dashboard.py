import matplotlib.pyplot as plt
from src.models.sqlite.repository.orders_repo import OrdersRepository
from src.models.sqlite.settings.connection import SqLiteConnectionHandler
import pandas as pd

conn = SqLiteConnectionHandler().connect()
repo = OrdersRepository(conn)

data = repo.get_avg_delivery_time_per_hub()
df = pd.DataFrame(data, columns=["hub_id", "avg_delivery_time"])

df = df.sort_values("avg_delivery_time")

plt.bar(df["hub_id"], df["avg_delivery_time"])
plt.title("Delivery Time per Hub")
plt.xlabel("Hub ID")
plt.ylabel("Avg Delivery Time")
plt.show()
