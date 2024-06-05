#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="Foodscorner")
cur = con.cursor()
v = cgi.FieldStorage()
id = v.getvalue("Id")
fid=v.getvalue("fid")
q1="""select Fid from cart where Fid='%s' and Uid='%s'"""%(fid,id)
cur.execute(q1)
res=cur.fetchone()
if res!=None:
    q2="""select Quantity,Price,TotalPrice from cart where Fid='%s' and Uid='%s' """%(fid,id)
    cur.execute(q2)
    res1=cur.fetchone()
    count=res1[0]+1
    price=res1[1]
    tp=count*price
    q3="""update cart set Quantity='%s',TotalPrice='%s' where Fid='%s' and Uid='%s' """%(count,tp,fid,id)
    cur.execute(q3)
    con.commit()
if res==None:
    q4="""select Actualprice from foods where Fid='%s'"""%(fid)
    cur.execute(q4)
    res2=cur.fetchone()
    q5 = """insert into cart(Fid,Uid,Adminid,Quantity,Price,TotalPrice) values('%s','%s',"11","1",'%s','%s') """ % (fid, id,res2[0],res2[0])
    cur.execute(q5)
    con.commit()
print("""
<script>    
    function cart(){
        alert("Product Added to Cart");
        location.href="userdashboard.py?Id=%s"
    }
    cart()
</script>
"""%(id))