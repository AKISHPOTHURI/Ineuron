from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/", methods=['GET','Post'])
def home():
    return render_template('index.html')

@app.route("/post", methods=['POST'])
def insertdata():
    if(request.method=='POST'):
        car = int(request.form['car'] or 0)
        rice = int(request.form['rice'] or 0)
        bag = int(request.form['bag'] or 0)
        dress = int(request.form['dress'] or 0)
        mobile = int(request.form['mobile'] or 0)
        pouch = int(request.form['pouch'] or 0)

        Total = car + rice + bag + dress + mobile + pouch

        if Total <= 1000:
            discount = 10
            Total = Total*0.1
        elif Total > 1000 and Total <= 2000:
            discount = 20
            Total = Total*0.2
        elif Total > 2000:
            discount = 30
            Total = Total*0.3

        result = "The discount you got is {}% and Your payable amount is {}".format(discount,Total)

        return render_template('results.html',result=result)
        
if __name__ == '__main__':
   app.run()