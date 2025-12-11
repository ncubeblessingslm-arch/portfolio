from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
        name="Ncube Blessings Lethubuhle Mary",
        role="Developer | Builder",
        projects=[
           
            {"title": "Login Form System", "tech": "Python, Tkinter", "desc": "GUI authentication project"},
            {"title": "Mini Softwares", "tech": "Python", "desc": "Automation & utilities"}
        ],
        
    
        skills=["Python", "Java",  "Hardware Prototyping"]
    )

if __name__ == "__main__":
    app.run(debug=True)