#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html\r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="Foodscorner")
cur = con.cursor()
v = cgi.FieldStorage()
uid= v.getvalue("Id")
fid=v.getvalue("fid")
q1="""select Quantity,Price,TotalPrice from cart where Fid='%s' and Uid='%s'"""%(fid,uid)
cur.execute(q1)
res=cur.fetchone()
if res!=None:
    if res[0]==1:
        que="""delete from cart where Fid='%s' and Uid='%s' """%(fid,uid)
        cur.execute(que)
        con.commit()
        con.close()
    if res[0]>1:
        count = res[0] - 1
        price = res[1]
        tp = res[2]-price
        q3 = """update cart set Quantity='%s',TotalPrice='%s' where Fid='%s' and Uid='%s' """ % (count,tp,fid,uid)
        cur.execute(q3)
        con.commit()
        con.close()
print("""
<script>    
    function cart(){
        alert("Product Removed from Cart");
        location.href="usercart.py?Id=%s"
    }
    cart()
</script>
"""%uid)