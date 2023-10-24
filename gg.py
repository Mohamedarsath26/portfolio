from flask import Flask
from flask import render_template,request,redirect
import csv

app = Flask(__name__)

@app.route('/index.html')
def home():
    return render_template('index.html')
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_csv(data):
    with open("database2.csv",mode='a',newline='') as database2:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',lineterminator='\n', quotechar='|', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv(data)
        return redirect('/thankyou.html')
    else:
        return "something wentwrong"

if __name__ == '__main__':
    app.run(debug=True)
