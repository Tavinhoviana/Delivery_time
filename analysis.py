from src.models.sqlite.repository.orders_repo import OrdersRepository
from src.models.sqlite.settings.connection import SqLiteConnectionHandler
import pandas as pd

conn = SqLiteConnectionHandler().connect()
repo = OrdersRepository(conn)

# 📊 Dados
data = repo.get_avg_delivery_time_per_hub()
df = pd.DataFrame(data, columns=["hub_id", "avg_delivery_time"])

df = df.sort_values("avg_delivery_time", ascending=False)

print("\n📊 Average Delivery Time per Hub:")
print(df)


# 🧠 INSIGHT 1: hub mais lento
slowest_hub = df.iloc[0]

print("\n⚠️ Slowest Hub Detected:")
print(f"Hub ID: {slowest_hub['hub_id']}")
print(f"Avg Delivery Time: {slowest_hub['avg_delivery_time']}")


# 🧠 INSIGHT 2: comparação com média
avg = df["avg_delivery_time"].mean()

print("\n📈 System Overview:")
print(f"Overall average delivery time: {avg:.2f}")

if slowest_hub["avg_delivery_time"] > avg * 1.2:
    print("⚠️ Alert: One hub is significantly slower than average")
