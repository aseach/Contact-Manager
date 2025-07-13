# Command‐Line Contact Manager

A simple Python command‐line application to manage contacts (add, view, edit, delete, search) with persistent CSV storage and automated tests.

---

## 🚀 Features

- **CRUD operations**  
  - Add new contacts (with overwrite prompt if duplicate)  
  - View all contacts in a clean, multi‐line format  
  - Edit any field (name, phone, email, notes, birthday)  
  - Delete contacts by exact name  

- **Regex‐powered Search**  
  - Search by name substring  
  - Search by phone number pattern  
  - Search by email domain  
  - Search by birthday month  

- **Persistent Storage**  
  - Contacts stored in `contacts.csv` via the `csv` module  
  - Loads once on startup; saves on every add/edit/delete  

- **Robust Input Validation & Error Handling**  
  - Menus loop until valid choice  
  - Duplicate‐name overwrite prompts  
  - Field‐format checks (phone/email) via regex  
  - Safe handling of missing CSV file  
  - Invalid regex patterns caught gracefully  

- **Automated Testing**  
  - Pytest suite covering load, add, view, delete, search  
  - `monkeypatch` for simulating user input  
  - `capsys` for capturing and asserting console output  

---

## 📁 Repository Structure

