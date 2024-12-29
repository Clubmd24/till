from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Prepare the data for rendering in the table
cleaned_data = pd.DataFrame({
    "ENTRY DESK": ["FLOAT", 20, 10, 5, 2],
    "GROUND FLOOR BAR": ["FLOAT", 20, 10, 5, 2],
    "ARENA BAR 1": ["FLOAT", 20, 10, 5, 2],
    "ARENA BAR 2": ["FLOAT", 20, 10, 5, 2],
    "ARENA BAR 3": ["FLOAT", 20, 10, 5, 2],
    "OVERALL DATA": ["TOTAL FLOAT", 20, 10, 5, 2],
    "REPLACE FLOAT": [None, 20, 10, 5, 2]
})

# HTML structure with integrated styling and interactivity
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Till Sheet Overview</title>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #555;
        }
        table {
            margin: 0 auto;
            width: 90%;
            border-collapse: collapse;
            background: #ffffff;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        th {
            background-color: #3a7afe;
            color: white;
            padding: 10px;
            text-align: center;
        }
        td {
            padding: 10px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            font-size: 14px;
            color: #888;
        }
    </style>
</head>
<body>
    <h1>Till Sheet Data</h1>
    <table id="data" class="display">
        <thead>
            <tr>
                {% for col in columns %}
                    <th>{{ col }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
                <tr>
                    {% for cell in row %}
                        <td>{{ cell }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
    <script>
        $(document).ready(function() {
            $('#data').DataTable();
        });
    </script>
    <footer>
        <p>Powered by Flask and DataTables.js</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(
        html_template, columns=cleaned_data.columns, data=cleaned_data.values
    )

if __name__ == '__main__':
    app.run(debug=True)
