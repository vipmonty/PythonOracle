from flask import Flask, render_template, request, redirect, url_for, flash
import VIPDB_on_flask

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/records')
def records():
    table_name = "CEO_DETAILS"
    columns, records = VIPDB_on_flask.get_all_records()
    return render_template('records.html', table_name=table_name, columns=columns, records=records)

@app.route('/describe_table', methods=['GET', 'POST'])
def describe_table():
    result = None
    if request.method == 'POST':
        table_name = request.form['table_name']
        result = VIPDB_on_flask.describe_table(table_name)
    
    return render_template('describe_table.html', result=result)

@app.route('/display_schema')
def display_schema():
    schema = VIPDB_on_flask.get_schema()
    return render_template('display_schema.html', schema=schema)

@app.route('/add_column', methods=['GET', 'POST'])
def add_column():
    if request.method == 'POST':
        table_name = request.form['table_name']
        column_name = request.form['column_name']
        data_type = request.form['data_type']
        
        if VIPDB_on_flask.add_column(table_name, column_name, data_type):
            flash('Column added successfully', 'success')
        else:
            flash('Error adding column', 'danger')
        
        return redirect(url_for('add_column'))
    
    return render_template('add_column.html')

if __name__ == '__main__':
    app.run(debug=True)
