import requests
from flask import Flask, render_template, request, redirect, url_for
import subprocess  # to run your football.py script
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # reCAPTCHA response token from the form
        recaptcha_response = request.form['g-recaptcha-response']
        
        # Secret key for reCAPTCHA verification
        secret_key = '6LccRSMrAAAAAM4zZMmreYsORSXc_S5OF9Up_xXH'
        
        # Verify the reCAPTCHA response with Google's API
        payload = {
            'secret': secret_key,
            'response': recaptcha_response
        }
        # Send a POST request to Google to verify the reCAPTCHA response
        verification_url = "https://www.google.com/recaptcha/api/siteverify"
        response = requests.post(verification_url, data=payload)
        result = response.json()
        
        if result['success']:
            # After passing CAPTCHA, you can call your football.py script
            subprocess.run(['python', 'football.py'])  # This will run football.py as a separate process
            return redirect(url_for('football'))  # Redirect to the route that opens your football game
        else:
            return "CAPTCHA failed. Try again."
    return render_template('sujithradevi.html')
@app.route('/football')  # New route for opening your football game
def football():
    # You can implement your game logic here or point to where the game opens
    return "Football game is running!"  # or render the page that displays the game
if __name__ == '__main__':
    app.run(debug=True)
