# Dataset Generator

A Flask-based web tool to generate and download dummy datasets with customizable columns and data types.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone "https://github.com/anmmashud/Dataset-Generator.git"
cd dataset-generator
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .flask_env
source .flask_env/bin/activate 
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

## Updating Dependencies
To add a new package:
```bash
pip install --upgrade pip
pip freeze > requirements.txt
```

## Project Structure
- `app.py`: Main Flask app.
- `generator.py`: Dataset generation logic.
- `templates/`: HTML templates.
- `static/`: CSS and JavaScript files.
- `requirements.txt`: Project dependencies.

## License
MIT License


## Guidance: 
Creating Environment, Installing `requirements.txt`, and Updating It

### 1. Create a Virtual Environment
A virtual environment isolates your project’s dependencies. Here’s how to create one named `.flask_env` using the Linux terminal:

- Navigate to your project directory:
  ```bash
  cd /path/to/dataset-generator
  ```

- Create the virtual environment:
  ```bash
  python3 -m venv .flask_env
  ```

- Activate the virtual environment:
  ```bash
  source .flask_env/bin/activate
  ```
  Your terminal prompt will change to `(.flask_env)`.

### 2. Install Dependencies from `requirements.txt`
With the virtual environment activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

This installs `Flask`, `pandas`, and `faker` as specified in your `requirements.txt`.

### 3. Update `requirements.txt`
If you install a new package (e.g., `pip install requests`), update `requirements.txt` to include it:

- Install the new package:
  ```bash
  pip install requests
  ```

- Update `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```

This ensures all dependencies are documented for future setups.

---

## Full Code in Markdown

### `README.md`
```markdown
# Dataset Generator

A Flask-based web tool to generate and download dummy datasets with customizable columns and data types.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd dataset-generator
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .flask_env
source .flask_env/bin/activate  # On Windows: .flask_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

## Updating Dependencies
To add a new package:
```bash
pip install <package-name>
pip freeze > requirements.txt
```

## Project Structure
- `app.py`: Main Flask app.
- `generator.py`: Dataset generation logic.
- `templates/`: HTML templates.
- `static/`: CSS and JavaScript files.
- `requirements.txt`: Project dependencies.

## License
MIT License
```

---

## Additional Notes

- **Deactivate the Environment**: When done, deactivate the virtual environment:
  ```bash
  deactivate
  ```

- **Re-activate for Future Sessions**: If you close the terminal, re-activate the environment:
  ```bash
  cd /path/to/dataset-generator
  source .flask_env/bin/activate
  ```

- **Windows Users**: If you’re on Windows, replace `source .flask_env/bin/activate` with:
  ```bash
  .flask_env\Scripts\activate
  ```

This setup ensures your project is well-documented and easy to run for anyone who clones the repository. Let me know if you need further assistance, Mashud! 😊