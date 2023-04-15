https://jovian-careers-website.anoopk7.repl.cofrom flask import Flask
app= Flask(__name__)
@app.route("/")
def hello_world():
  return("hello world")

print("hi")

if __name__  == '__main__' :
  print("hi")
  app.run(host='0.0.0.0',debug='True')
