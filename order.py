#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi, cgitb,smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="Foodscorner")
cur = con.cursor()
v = cgi.FieldStorage()
id = v.getvalue("Id")
q1="""select * from cart where Uid='%s'"""%(id)
cur.execute(q1)
res=cur.fetchall()
q2="""select Fid from ordercart where Uid='%s'"""%(id)
cur.execute(q2)
res1=cur.fetchone()
q3="""select Username,Email from details where Id='11' and Role='Admin' """
cur.execute(q3)
res2=cur.fetchone()
q5="""select Username from details where Id='%s' and Role='User' """%(id)
cur.execute(q5)
res3=cur.fetchone()
if res1==None:
        for i in res:
                q4="""insert into ordercart(Fid,Uid,Adminid,Quantity,Price,TotalPrice,PaymentMode) values('%s','%s','%s','%s','%s','%s','%s')"""%(i[0],i[1],i[2],i[3],i[4],i[5],"Cash on Delivery")
                cur.execute(q4)
                con.commit()
        fromadd = "jeevajeevaloganathan977@gmail.com"
        password = "yyyh bgac mlkp yfcm"
        tadd = res2[1]
        subject="Hello {}! New Order".format(res2[0])
        body="Order from {}".format(res3[0])
        msg="""Subject:{} \n{}""".format(subject,body)
        server= smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromadd,password)
        server.sendmail(fromadd,tadd,msg)
        server.quit()
print("""<script> 
function ordercart(){
        alert("Order Placed!");
        location.href="userdashboard.py?Id=%s"
}
ordercart()
</script>""" % (id))