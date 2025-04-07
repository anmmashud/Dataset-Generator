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