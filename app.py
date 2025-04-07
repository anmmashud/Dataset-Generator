from flask import Flask, render_template, request, send_file, jsonify
from generator import generate_dataset, generate_preview
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'preview' in request.form:
            # Handle preview request (first 5 rows)
            column_types = request.form.getlist('column_type')
            column_names = request.form.getlist('column_name')
            row_count = int(request.form.get('row_count', 5))
            
            # Validate inputs
            if not column_names or not column_types or len(column_names) != len(column_types):
                return jsonify({'error': 'Invalid column data'}), 400
            if row_count < 1:
                return jsonify({'error': 'Row count must be at least 1'}), 400

            preview_data = generate_preview(column_names, column_types)
            return jsonify({'preview': preview_data})

        # Handle full dataset generation and download
        column_types = request.form.getlist('column_type')
        column_names = request.form.getlist('column_name')
        row_count = int(request.form.get('row_count', 10))
        file_format = request.form.get('file_format', 'csv')
        file_name = request.form.get('file_name', 'dataset')

        # Validate inputs
        if not column_names or not column_types or len(column_names) != len(column_types):
            return render_template('home.html', error='Please define at least one column.')
        if row_count < 1:
            return render_template('home.html', error='Row count must be at least 1.')

        filename = generate_dataset(column_names, column_types, row_count, file_format, file_name)
        return send_file(filename, as_attachment=True)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)