from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    emails = Email.get_all()
    print(emails)
    return render_template('results.html', emails=emails)

@app.route('/saveEmail', methods=['POST'])
def save_email():
    if not Email.validate_email(request.form['email']):
        print('working')
        return redirect('/')
    else:
        data = {
            'email': request.form['email']
        }
        Email.save(data)
        return redirect('/results')

@app.route('/delete/<int:email_id>')
def delete_email(email_id):
    data = {
        'id': email_id
    }
    Email.delete_email(data)
    return redirect('/results')