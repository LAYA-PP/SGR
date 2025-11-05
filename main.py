from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the routes for all your pages
@app.route('/')
def index():
    # Renders the index.html file inside the 'templates' folder
    return render_template('index.html')

@app.route('/yes')
def yes():
    return render_template('yes.html')

@app.route('/no1')
def no1():
    return render_template('no1.html')

@app.route('/no2')
def no2():
    return render_template('no2.html')

@app.route('/no3')
def no3():
    return render_template('no3.html')

# This is needed if you want to run the app locally
if __name__ == '__main__':
    # Setting host='0.0.0.0' is good practice for deployment like Render
    app.run(host='0.0.0.0', port=5000, debug=True)

# For Render deployment, you will only need the 'app' variable, 
# as they will handle the server start-up.
