from flask import Flask,render_template,request,jsonify

app = Flask(__name__)
@app.route("/")
def test():
    return render_template("new.html")

@app.route("/test",methods=["post"])
def test_():
    if request.method=="POST":
        print("--------")
        name=request.form["Name"]
        age=request.form["Age"]
    print("so the name,age is", name,age)
    return "Hello this for test"

if __name__ =="__main__":
    app.run(port=8000)
