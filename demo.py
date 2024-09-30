from flask import Flask, render_template, request, redirect, url_for, flash

# Create the Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page with form handling
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Normally, you would process/store the data here (e.g., send email or log it)
        # For now, just flash a success message and simulate storing it
        flash(f"Message from {name} has been received! We'll get back to you shortly.", "success")
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)