import tkinter as tk

def predict():
    try:
        f = int(entry1.get())
        d = int(entry2.get())
        # Dummy formula: just for demo
        result = f * 2 + d // 3
        label_result.config(text=f"Estimated Maintenance in: {result} days")
    except ValueError:
        label_result.config(text="Enter valid numbers")

root = tk.Tk()
root.title("Simple Maintenance Form")

tk.Label(root, text="Failures Count").grid(row=0)
tk.Label(root, text="Days Between Failures").grid(row=1)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

tk.Button(root, text="Predict", command=predict).grid(row=2, column=0, columnspan=2, pady=10)
label_result = tk.Label(root, text="", fg="blue")
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()
