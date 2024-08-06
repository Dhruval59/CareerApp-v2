# CareerApp
Build your career

# This web application will help to apply for different roles at Career builder.

Create two different tables in a database: jobs and applications

Jobs fields: id,title,location,salary,currency,responsibilities,requirements
Application fields: job_id,full_name,email,linkedin_url,education,work_experience

Export env variables: USER, PASS, HOSTNAME, DATABASE

# Dockerize the application

docker build -t careerapp:v2 .

docker run -dp 5000:5000 --env-file .env careerapp:v2

Access the web app on localhost:5000

# Attached demo images under Screenshots folder

Reference: https://jovian.com/aakashns/database-driven-web-applications