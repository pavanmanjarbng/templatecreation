# from flask import Flask, render_template, request
from flask import Flask, render_template, request, send_file, flash, redirect, url_for

from scraper import scrape_webinar_details  # Replace with the actual function name
import os

app = Flask(__name__)
app.secret_key = '_g\xa9\x15\xb0T\x88\xba\xc5\x10\xda!\x7f\x83\x94\x8e'  # Replace with your generated key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def index():
    return render_template('form.html')

@app.route('/generate-email', methods=['POST'])
def generate_email():
    url = request.form['url']
    date = request.form['date']
    speaker = request.form['speaker']
    
    # Call your scraping function here and process data
    # For example:
    scraped_data, file_name = scrape_webinar_details(url, date, speaker)
    your_file_directory = 'created/'

    # Assuming the edited_file is being set in your scrape_webinar_details function
    # file_path = os.path.join(your_file_directory, scraped_data["edited_file"])
    file_path = os.path.join(your_file_directory, file_name)

    # Check if file exists
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
        
    else:
        # return "Error: File not found.", 404
        flash('Error: File not found.', 'error')  # 'error' is a category
        return redirect(url_for('index'))
    # Render the email template with scraped data
    # Assuming scraped_data is a dictionary containing necessary information

