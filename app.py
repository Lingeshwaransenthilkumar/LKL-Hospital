from flask import Flask,render_template,url_for,request
import mysql.connector

app=Flask(__name__,template_folder="../FLASK2/template")
db=mysql.connector.connect(
   host="localhost",
   username="lingesh",
   password="Lingesh2002",
   database="hospdb")
cursor=db.cursor()
@app.route('/',methods=['GET'])
def home():
    datatype=type(request.args)
    myargs=request.args
   
    try:  
        if request.args.get('book')=="book":
            name=request.args.get('name')
            number=request.args.get('number')
            email=request.args.get('email')
            appt_date=request.args.get('appt_date')
            sql="insert into appointment(name,number,email,appt_date) values('{0}','{1}','{2}','{3}')".format(name,number,email,appt_date)
            cursor.execute(sql)
            db.commit()
            print(myargs)
            return render_template("appt.html",name=name,number=number,email=email,date=appt_date)
        else:
           return render_template("index (5).html")
    except Exception as e:
       return "provide valid data"
    

@app.route('/slogin')
def slogin():
    return render_template("login.html")

@app.route('/pdetails',methods=['GET'])
def pdetails():
    if request.args.get('register')=="register":
            name=request.args.get('name')
            age=request.args.get('age')
            email=request.args.get('email')
            dob=request.args.get('dob')
            gender=request.args.get('gender')
            address=request.args.get('address')
            bg=request.args.get('Bg')
            disname=request.args.get('dname')
            docname=request.args.get('docname')
            pres=request.args.get('pres')
            phone=request.args.get('mobile')
            remarks=request.args.get('remarks')
            cardno=request.args.get('cardnum')
            advice=request.args.get('advice')
            sql="insert into pat_details(name,dob,age,gender,bg,email,address,mobile,disease_name,doc_name,prescription,remark,cardno,advice) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(name,dob,age,gender,bg,email,address,phone,disname,docname,pres,remarks,cardno,advice)
            cursor.execute(sql)
            db.commit()
            return render_template("success.html")
    else:
        return render_template("reg.html")

 


@app.route('/patlogin',methods=['GET'])
def patlogin():
            if request.args.get('login')=="login":
                name=request.args.get('name')
                cardno=request.args.get('cardnum')
                sql="select * from pat_details where name='{0}' and cardno='{1}'".format(name,cardno)
                cursor.execute(sql)
                db_data=cursor.fetchall()
                print(db_data)
                return render_template("pat.html",pat_data=db_data)
            else:
                return render_template("patlogin.html")



                   
if __name__=="__main__":
    app.run(debug=True)
