
import matplotlib.pyplot as plt
 # --- Bar Chart ---
assets = ['A1', 'A2', 'A3', 'A4', 'A5']
days = [30, 45, 20, 25, 18]
 
plt.figure(figsize=(6, 4))
plt.bar(assets, days, color='skyblue')
plt.title("Days Between Failures")
plt.xlabel("Assets")
plt.ylabel("Days")
plt.tight_layout()
plt.show()
 
# --- Pie Chart ---
labels = ['1 failure', '2 failures', '3 failures', '4 failures']
sizes = [2, 4, 2, 2]
 
plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Failure Count Distribution")
plt.axis('equal')
plt.tight_layout()
plt.show()
