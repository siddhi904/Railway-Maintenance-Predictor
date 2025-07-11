import matplotlib.pyplot as plt

# Dummy data
failures = [2, 1, 3, 2, 4, 2, 1, 3, 2, 4]
days_between = [30, 45, 20, 25, 18, 33, 50, 22, 35, 15]
actual = [15, 25, 10, 12, 9, 16, 28, 11, 17, 7]

# Prediction using simple formula
predicted = []
for f, d in zip(failures, days_between):
    predicted.append(int(f * 2 + d * 0.3))

# Line chart: Actual vs Predicted
plt.figure(figsize=(6, 4))
plt.plot(actual, label='Actual', marker='o')
plt.plot(predicted, label='Predicted', marker='x')
plt.title('Maintenance Forecast')
plt.xlabel('Asset Index')
plt.ylabel('Days Until Next Maintenance')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
