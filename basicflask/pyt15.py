from flask import Flask
app=Flask(__name__)

@app.route("/hi/<int:var>")
def hello_name(var):
    return "Hello" +var

if __name__=="__main__":
    app.run(debug=True)
