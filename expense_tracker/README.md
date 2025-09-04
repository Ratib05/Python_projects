# 🧾 Simple Expense Tracker

A desktop application built in **Python** using **Tkinter** and **SQLite** to track daily expenses, manage categories, and visualize spending with charts.

---

## 📌 Features

* **Add, Edit, Delete Expenses**
  Record expenses with amount, category, note, and date.
* **Expense List View**
  Sortable table showing all expenses.
* **Category Management**
  Add, rename, or remove categories.
* **Summary Totals**
  Quick view of Today, This Week, and This Month totals.
* **Visualization**
  Pie/Bar charts of spending by category using Matplotlib.
* **Persistent Storage**
  Uses SQLite database (`expenses.db`) to store all data.

---

## 🖼 Example UI

![Expense Tracker UI](A_2D_digital_image_displays_a_user_interface_\(UI\)_.png)

---

## 🛠 Tech Stack

* **Python 3.x**
* **Tkinter** – GUI framework
* **SQLite3** – local database
* **Matplotlib** – data visualization

---

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. **Install dependencies**

   ```bash
   pip install matplotlib
   ```

   (Tkinter and sqlite3 come with Python)

3. **Run the app**

   ```bash
   python app.py
   ```

---

## 📂 Project Structure

```
expense_tracker/
├─ app.py                 # Main Tkinter app
├─ db.py                  # SQLite connection and queries
├─ models.py              # Expense and Category dataclasses
├─ views/                 # Tkinter views: dashboard, dialogs
├─ charts.py              # Matplotlib charts
├─ utils.py               # Helpers (formatting, validation)
└─ expenses.db            # Created at runtime
```

---

## 🧩 Future Enhancements

* 🔹 CSV Import/Export
* 🔹 Monthly budgets per category
* 🔹 Dark mode with themed Tkinter styles
* 🔹 Recurring expenses (e.g., subscriptions, rent)

---

## 📜 License

MIT License © 2025 Your Name

---

Do you want me to also make a **LinkedIn project post draft** (like you did for your BMI calculator) so you can showcase this?
