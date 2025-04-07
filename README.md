this is the previous code. i want its upgrade version:

Thanks for the clarification! Since your project is focused on **a dataset generator web tool**, here’s how we’ll structure your Flask app:

---

## 💡 Goal
A **Flask web app** where users can:
- Define number of rows
- Define column names and types (name, email, address, date, etc.)
- Generate dummy dataset using `Faker`
- Download it as CSV/JSON

---

## 📦 Updated Project Structure

```
project/
├── app.py                  ← Main app controller (the brain)
├── generator.py            ← Core logic to generate dataset (Faker + Pandas)
├── templates/
│   ├── base.html
│   ├── home.html
├── static/
│   └── style.css
└── requirements.txt
```

---

### ✅ `app.py` – The Brain

```python
from flask import Flask, render_template, request, send_file
from generator import generate_dataset
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        column_types = request.form.getlist('column_type')
        column_names = request.form.getlist('column_name')
        row_count = int(request.form.get('row_count', 10))
        file_format = request.form.get('file_format', 'csv')

        filename = generate_dataset(column_names, column_types, row_count, file_format)

        return send_file(filename, as_attachment=True)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
```

---

### ⚙️ `generator.py` – Dataset Generator Logic

```python
from faker import Faker
import pandas as pd
import uuid

fake = Faker()

def generate_column(col_type):
    if col_type == "name":
        return fake.name()
    elif col_type == "email":
        return fake.email()
    elif col_type == "address":
        return fake.address()
    elif col_type == "date":
        return fake.date()
    elif col_type == "phone":
        return fake.phone_number()
    elif col_type == "text":
        return fake.sentence()
    else:
        return "N/A"

def generate_dataset(col_names, col_types, row_count, file_format="csv"):
    data = []

    for _ in range(row_count):
        row = {col_names[i]: generate_column(col_types[i]) for i in range(len(col_names))}
        data.append(row)

    df = pd.DataFrame(data)
    filename = f"generated_{uuid.uuid4().hex}.{file_format}"

    if file_format == "csv":
        df.to_csv(filename, index=False)
    elif file_format == "json":
        df.to_json(filename, orient="records", lines=True)

    return filename
```

---

### 📝 `templates/home.html`

```html
{% extends "base.html" %}
{% block content %}
<h2>Dataset Generator</h2>
<form method="POST">
    <label>Number of Rows:</label>
    <input type="number" name="row_count" value="10" required><br><br>

    <div id="columns">
        <div class="column-group">
            <input name="column_name" placeholder="Column Name" required>
            <select name="column_type">
                <option value="name">Name</option>
                <option value="email">Email</option>
                <option value="address">Address</option>
                <option value="date">Date</option>
                <option value="phone">Phone</option>
                <option value="text">Text</option>
            </select>
        </div>
    </div>
    <br>
    <button type="button" onclick="addColumn()">Add Column</button><br><br>

    <label>File Format:</label>
    <select name="file_format">
        <option value="csv">CSV</option>
        <option value="json">JSON</option>
    </select><br><br>

    <button type="submit">Generate Dataset</button>
</form>

<script>
function addColumn() {
    const container = document.getElementById("columns");
    const newColumn = document.createElement("div");
    newColumn.classList.add("column-group");
    newColumn.innerHTML = `
        <input name="column_name" placeholder="Column Name" required>
        <select name="column_type">
            <option value="name">Name</option>
            <option value="email">Email</option>
            <option value="address">Address</option>
            <option value="date">Date</option>
            <option value="phone">Phone</option>
            <option value="text">Text</option>
        </select>
    `;
    container.appendChild(newColumn);
}
</script>
{% endblock %}
```

---

### 🧩 `templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dataset Generator</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <header>
        <h1>Flask Dataset Tool</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2025 Data Generator App</p>
    </footer>
</body>
</html>
```

---

### 🎨 `static/style.css`

```css
body {
    font-family: Arial;
    background-color: #f8f8f8;
    margin: 0;
    padding: 0;
}

header, footer {
    background-color: #333;
    color: white;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 2rem;
}

input, select, button {
    padding: 0.5rem;
    margin: 5px;
}
```

---

### 📦 `requirements.txt`

```txt
Flask
pandas
faker
```

---

Let me know if you want:
- Advanced validation
- More column types
- Auto-preview before download
- Saving datasets to a server path

Ready to take it to the next level whenever you are 😎