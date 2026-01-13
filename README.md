# 💸 Keuangan Anak Kos (Student Finance Tracker)(Trial)
<img width="1563" height="851" alt="Screenshot 2026-01-13 113546" src="https://github.com/user-attachments/assets/f9dfd92b-c7ab-438d-8db2-45fff007c2fe" />

A sleek, modern desktop application designed to help students or individuals manage their daily finances. Built with Python and Flet, this app provides a focused interface to track monthly budgets, savings, and emergency funds.

## ✨ Key Features
- **Monthly Budget Management:** Set and update your primary monthly allowance.
- **Real-time Balance Tracking:** Automatically calculates your remaining budget after expenses.
- **Dedicated Saving Pots:** Separate tracking for "Savings" and "Emergency Funds".
- **Expense Logging:** Quickly record daily spending to keep your records up to date.
- **Persistent Storage:** Powered by SQLite to ensure your data is saved locally on your device.
- **Modern Dark UI:** A clean, high-contrast dark mode interface for better user experience.

## 🛠️ Tech Stack
- **Language:** Python
- **UI Framework:** [Flet](https://flet.dev/) (Flutter-based framework for Python)
- **Database:** SQLite3

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Pip (Python package manager).

### Installation
1. **Install Dependencies:**
   ```bash
   pip install flet
2. **Clone the repository:**
   ```bash
   git clone [https://github.com/dwzIo/python-1.git](https://github.com/dwzIo/python-1.git)
   cd python-1
3. **Run The Application:**
   ```bash
   python main.py
# 📁 Project Structure
main.py: Handles the UI logic, state management, and Flet application flow.
database.py: Contains the DBHelper class managing all SQLite CRUD operations.
your_Data.db: Local database file (auto-generated upon first launch).

# 🔧 Database Schema
The application uses two main tables:
Summary: Stores global values for Budget, Emergency Fund, and Savings.
Transaksi: Logs every transaction with a timestamp for history tracking.
