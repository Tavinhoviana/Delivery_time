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

# 🧠 METRICS
slowest = df.iloc[0]
fastest = df.iloc[-1]
avg = df["avg_delivery_time"].mean()

print("\n📈 SYSTEM OVERVIEW:")
print(f"Average delivery time: {avg:.2f}")
print(f"Fastest hub: {fastest['hub_id']} ({fastest['avg_delivery_time']:.2f})")
print(f"Slowest hub: {slowest['hub_id']} ({slowest['avg_delivery_time']:.2f})")

# 🚨 INSIGHT 1 - IMBALANCE DETECTION
if slowest["avg_delivery_time"] > avg * 1.2:
    print("\n🚨 ALERT: Significant performance imbalance detected across hubs")

# 📊 INSIGHT 2 - PERFORMANCE GAP
gap = slowest["avg_delivery_time"] - fastest["avg_delivery_time"]

print("\n📊 PERFORMANCE GAP ANALYSIS")
print(f"Gap between best and worst hub: {gap:.2f}")

# 🧠 INSIGHT 3 - BUSINESS INTERPRETATION
print("\n🧠 BUSINESS INSIGHT")

if gap > avg * 0.5:
    print("⚠️ Operational inconsistency detected")
    print("👉 Recommendation: investigate routing, staffing or demand distribution")
else:
    print("✅ Delivery system is relatively balanced")
