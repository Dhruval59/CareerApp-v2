from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://root:H$&bZF?d;g[Kh;tr@34.66.54.147/DEMO"
engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        # print(result.all())
        result_all = result.all()

        jobs = []
        for row in result_all:
            jobs.append(dict(row))
        return jobs
        