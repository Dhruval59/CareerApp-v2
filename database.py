from sqlalchemy import create_engine, text
import os

username = os.getenv("USER")
password = os.getenv("PASS")
host = os.getenv("HOSTNAME")
database = os.getenv("DATABASE")

db_connection_string = f"mysql+pymysql://{username}:{password}@{host}/{database}?charset=utf8mb3"

engine = create_engine(db_connection_string)
                    #    ,
                    #    connect_args={
                    #        "ssl": {
                    #            "ssl_ca": ""
                    #        }
                    #    })

def load_jobs_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        # print(result.all())
        result_all = result.all()

        jobs = []
        for row in result_all:
            jobs.append(dict(row))
        return jobs
        
def load_job_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs where id = :val"), val=id)
        row = result.all()
        if len(row)==0:
            return None
        else:
            return dict(row[0])

def number_of_applicants():
    with engine.connect() as connection:
        result = connection.execute(text("select job_id, COUNT(id) as number_of_applicants from applications GROUP BY job_id"))
        rows = result.all()
        return rows
    
# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData


def add_application_to_db(job_id, data):
    conn = engine.connect()
    try:
        query = text("""
            INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience)
            VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience)
        """)

        # file = convertToBinaryData(resume_file_path)
        conn.execute(query, 
                     job_id=job_id, 
                     full_name=data['full_name'],
                     email=data['email'],
                     linkedin_url=data['linkedin'],
                     education=data['education'],
                     work_experience=data['work'])
    finally:
        conn.close()