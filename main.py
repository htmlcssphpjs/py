from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "
      <html>
        <head>
          <title>Home Page</title>
        </head>
        <body>
          <h1>Hello</h1>
        </body>
      </html>
     "
     
if __name__ == "__main__":
    app.run(debug=True)
