from src.models.sqlite.repository.orders_repo import OrdersRepository
from src.models.sqlite.settings.connection import SqLiteConnectionHandler
import pandas as pd

conn = SqLiteConnectionHandler().connect()
repo = OrdersRepository(conn)

# 📊 DATA
data = repo.get_avg_delivery_time_per_hub()
df = pd.DataFrame(data, columns=["hub_id", "avg_delivery_time"])
df = df.sort_values("avg_delivery_time", ascending=False)

print("\n📊 DELIVERY PERFORMANCE REPORT\n")
print(df)

# 🧠 INSIGHT 1 - HUB MAIS LENTO
slowest = df.iloc[0]
avg = df["avg_delivery_time"].mean()

print("\n⚠️ SLOWEST HUB:")
print(f"Hub ID: {slowest['hub_id']}")
print(f"Avg delivery time: {slowest['avg_delivery_time']:.2f}")

# 🧠 INSIGHT 2 - ANOMALIA
if slowest["avg_delivery_time"] > avg * 1.2:
    print("\n🚨 ALERT: Performance imbalance detected between hubs")

# 🧠 INSIGHT 3 - VISÃO GERAL
print("\n📈 SYSTEM OVERVIEW:")
print(f"Average delivery time: {avg:.2f}")
print(f"Best hub performance gap: {slowest['avg_delivery_time'] - avg:.2f}")
