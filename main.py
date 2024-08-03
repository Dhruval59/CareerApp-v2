from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 1000000
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Pune, India',
        'salary': 800000
    },
    {
        'id': 3,
        'title': 'Business Analyst',
        'location': 'Ahmedabad, India',
        'salary': 900000
    },
    {
        'id': 4,
        'title': 'Software Developer',
        'location': 'Remote'
    }
]

@app.route('/')
def hello_app():
    return render_template('home.html', jobs=JOBS, companyName="Build Career")

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
