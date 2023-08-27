from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data=response.json()
    return render_template("index.html", posts=data)

@app.route('/post/<int:n>')
def blog(n):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("post.html", posts=data)

if __name__ == "__main__":
    app.run(debug=True)
