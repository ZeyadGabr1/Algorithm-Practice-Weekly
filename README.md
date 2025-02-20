
## Short description:
A secure daily task management program that stores data in a JSON file and encrypts all information using Fernet. It provides a flexible experience, allowing users to add, edit, or delete tasks, as well as the option to download tasks as a CSV file.

---

## Requirements:
- Python (version after 3.10)
- json (Built-in)
- os (Built-in)
- pandas
- cryptography
- datetime (Built-in)

---

## How to Run:

### 1. Clone the Repository:
```bash
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME
```

---

### 2. Create a Virtual Environment:
- **On Windows:**
    ```powershell
    python -m venv venv
    .env\Scriptsctivate
    ```
- **On Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

---

### 3. Install Required Libraries:
```bash
pip install -r requirements.txt
```

---

### 4. Run the Application:
```bash
python main_methods.py
```

---

### Notes:
- Make sure you have **Python 3** installed.
- If you encounter any issues with dependencies, manually install them using:
    ```bash
    pip install pandas cryptography
    ```

---

### 5. Exiting the Virtual Environment:
- **On Windows:**
    ```powershell
    deactivate
    ```
- **On Linux:**
    ```bash
    deactivate
    ```

---

## Features:
- Add, Edit, Delete tasks securely.
- Encrypts all task information using Fernet.
- Downloads tasks as a CSV file for easy management.
- Stores data locally in a JSON file.

---

## License:
This project is licensed under the MIT License - see the LICENSE file for details.

---------------------------------

If you like this project, don’t forget to give it a ⭐! Your feedback and contributions are highly appreciated.
