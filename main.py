from flask import Flask, jsonify, render_template
from sqlalchemy import text
from database import engine, load_jobs_from_db

app = Flask(__name__)

@app.route('/')
def hello_app():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, companyName="Build Career")

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
