from faker import Faker
import pandas as pd
import uuid
import re
import random

fake = Faker()

def validate_email(email):
    """Simple email validation using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def generate_column(col_type):
    """Generate a single column value based on the data type."""
    # Personal
    if col_type == "name":
        return fake.name()
    elif col_type == "first_name":
        return fake.first_name()
    elif col_type == "last_name":
        return fake.last_name()
    elif col_type == "age":
        return random.randint(1, 100)
    elif col_type == "gender":
        return random.choice(["Male", "Female", "Other"])
    elif col_type == "job":
        return fake.job()
    
    # Contact
    elif col_type == "email":
        return fake.email()
    elif col_type == "phone":
        return fake.phone_number()
    
    # Location
    elif col_type == "address":
        return fake.address()
    elif col_type == "city":
        return fake.city()
    elif col_type == "state":
        return fake.state()
    elif col_type == "country":
        return fake.country()
    elif col_type == "zipcode":
        return fake.zipcode()
    elif col_type == "latitude":
        return fake.latitude()
    elif col_type == "longitude":
        return fake.longitude()
    
    # Date/Time
    elif col_type == "date":
        return fake.date()
    elif col_type == "time":
        return fake.time()
    elif col_type == "datetime":
        return fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
    elif col_type == "year":
        return fake.year()
    elif col_type == "month":
        return fake.month_name()
    elif col_type == "day":
        return fake.day_of_month()
    
    # Financial
    elif col_type == "credit_card":
        return fake.credit_card_number()
    elif col_type == "currency":
        return fake.currency()[1] + str(round(random.uniform(1, 1000), 2))
    elif col_type == "price":
        return round(random.uniform(0.01, 1000.00), 2)
    
    # Text
    elif col_type == "text":
        return fake.sentence()
    elif col_type == "paragraph":
        return fake.paragraph()
    elif col_type == "word":
        return fake.word()
    
    # Miscellaneous
    elif col_type == "boolean":
        return random.choice([True, False])
    elif col_type == "uuid":
        return str(uuid.uuid4())
    elif col_type == "color":
        return fake.color_name()
    elif col_type == "ip_address":
        return fake.ipv4()
    elif col_type == "url":
        return fake.url()
    elif col_type == "company":
        return fake.company()
    
    else:
        return "N/A"

def generate_preview(col_names, col_types, row_count=3):
    """Generate a preview of the first 5 rows."""
    data = []
    for _ in range(min(row_count, 3)):
        row = {col_names[i]: generate_column(col_types[i]) for i in range(len(col_names))}
        data.append(row)
    
    # Add email validation for preview
    for row in data:
        for col_name in col_names:
            if col_types[col_names.index(col_name)] == "email":
                email = row[col_name]
                row[f"{col_name}_valid"] = validate_email(email)
    
    return data

def generate_dataset(col_names, col_types, row_count, file_format="csv", file_name="dataset"):
    """Generate the full dataset and save it to a file."""
    data = []
    for _ in range(row_count):
        row = {col_names[i]: generate_column(col_types[i]) for i in range(len(col_names))}
        data.append(row)

    df = pd.DataFrame(data)
    filename = f"{file_name}_{uuid.uuid4().hex}.{file_format}"

    if file_format == "csv":
        df.to_csv(filename, index=False)
    elif file_format == "json":
        df.to_json(filename, orient="records", lines=True)

    return filename