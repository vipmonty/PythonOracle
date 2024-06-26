from flask import Flask, render_template, request, redirect, url_for, flash
import VIPDB_on_flask

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/records')
def records():
    records = VIPDB_on_flask.get_all_records()
    return render_template('records.html', records=records)

@app.route('/describe_table', methods=['GET', 'POST'])
def describe_table():
    result = None
    if request.method == 'POST':
        table_name = request.form['table_name']
        result = VIPDB_on_flask.describe_table(table_name)
    
    return render_template('describe_table.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
