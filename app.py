from flask import Flask, render_template,jsonify
from database import engine
from sqlalchemy import text


app = Flask(__name__)

JOB_LISTING = [{
  'id': 1,
  'title': 'Data scientist',
  "salary": 'Rs 15,00,000',"location": 'Bangalore',
  "link_apply":"https://www.w3schools.com"
}, {
  'id': 2,
  'title': 'Data engineer',
  "salary": 'Rs 12,00,000',"location": 'Chennai',"link_apply":"https://www.w3schools.com/html/html_exercises.asp"
}, {
  'id': 1,
  'title': 'Software developer',
  "salary": 'Rs 14,00,000',"location": 'Hyderabad',"link_apply":"https://www.w3schools.com/cssref/pr_text_text-align.php"
}]

def load_job_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs_table"))
    column_names = result.keys()
    
    result_dicts = []
    
    for row in result.all():
      result_dicts.append(dict(zip(column_names, row)))
  return(result_dicts)

@app.route("/")
def hello_world():
  job_from_db=load_job_db()
  return render_template('home.html', jobs=job_from_db)

@app.route("/api/jobs")
def joblist():
  return jsonify(JOB_LISTING)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
