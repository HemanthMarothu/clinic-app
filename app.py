from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#homepage
@app.route('/')
def home():
    return render_template('index.html')

#Appointment page route
@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

#Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    print(f'Appointment booked for {name} on {date}')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)