from flask import Flask, render_template,jsonify

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


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOB_LISTING)

@app.route("/api/jobs")
def joblist():
  return jsonify(JOB_LISTING)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
