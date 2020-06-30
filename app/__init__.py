from flask import Flask,request,render_template
import os

app= Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))+'/static'
# @app.route("/",methods=['GET','POST'])
# def index():

#     if request.method == 'POST':
#         newfile = request.files['file']
#         print(os.path.abspath(os.path.dirname(__file__))+'/app/static')
#         newfile.save(os.path.join(basedir, newfile.filename))
#     return render_template('fileupload.html') 

@app.route("/",methods=['GET','POST'])
def index():
    return 'api is working fine'