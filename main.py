from flask import Flask, jsonify, render_template, request
from sqlalchemy import text
from database import engine, load_jobs_from_db, load_job_from_db, add_application_to_db, number_of_applicants
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def hello_app():
    jobs = load_jobs_from_db()
    list_applicants = number_of_applicants()
    return render_template('home.html', jobs=jobs, companyName="Build Career", list_applicants=list_applicants )

@app.route('/contactus')
def contact_us():
    return render_template('contactus.html')

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)

@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
   if 'resume_file' not in request.files:
        return 'No file part'
   file = request.files['resume_file']
   if file.filename == '':
        return 'No selected file'
   if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # Check if file already submitted previously
        if os.path.exists(file_path):
            return 'Already submitted!'
        else:
            file.save(file_path)
        
        # Collect form data
        data = {
            'full_name': request.form['full_name'],
            'email': request.form['email'],
            'linkedin': request.form['linkedin'],
            'education': request.form['education'],
            'work': request.form['work']
        }
   job = load_job_from_db(id)

   add_application_to_db(id, data)
   print('File successfully uploaded and data saved to database')
   return render_template('application_submitted.html', application=data, job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
