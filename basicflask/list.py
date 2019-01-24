from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def dict():
   data=('maths' :80,'dbmi' :20,'cg' :30)
   print data
   return render_template('tmp.html',data=data)

if __name__=="__main__":
    app.run(debug=True)
