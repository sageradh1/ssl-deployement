from flask import Flask,request,render_template
import os

app= Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))+'/app/static'
@app.route("/",methods=['GET','POST'])
def index():

    if request.method == 'POST':
        newfile = request.files['file']
        print(os.path.abspath(os.path.dirname(__file__))+'/app/static')
        newfile.save(os.path.join(basedir, newfile.filename))
    return render_template('fileupload.html') 

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0',port='4000')
