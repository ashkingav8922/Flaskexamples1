from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtfforms import TextField
from wtfforms.validator import Required
app=Flask(__name__)
app.config['Secret_key']='hard to guess string'
bootstrap=Bootstrap(app)
class registration(Form):
    name=TextField('What is your name',validator=[Required()])

@app.route('/',method=['GET','POST'])

def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data()
        form.name.data=" "
    return render_template('index.html',form=form,name=name)
                

