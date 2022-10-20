#載入flask模組
from flask import Flask,request,render_template,redirect,session,url_for

app = Flask(__name__)

#設定 session 密鑰
app.secret_key='tian12345'

@app.route('/')
def index():
    return render_template("signin.html")

#路由-後端-路由-前端
#account=參數名稱/ acc=資料
#session ['參數名稱‘] = ‘資料’
#釐清哪些狀況下會跳轉到成功頁面 1.輸入test 2.曾經有登入紀錄 3.保持登入頁面
#request 要求物件 / request.args.get  
#redirect 導向另一個路徑/也可直接傳送網址
#render_template 導向前端
@app.route('/signin',methods=['POST'])
def signin(): 
    acc = request.form['account']
    # session['account']= acc
    psw = request.form["password"]
    # session['password']= psw
    # 彭彭作業回應: session['enter'] == 'open'以上這個判斷式，後面的部份是多出來的，使用者如果透過表單輸入帳號密碼，就算曾經登入過，輸入帳密若是錯誤，我們也會告訴他是輸入帳密錯誤。未來輸入帳號密碼的使用者也可能會輸入不同組的帳號密碼，所以在登入的判斷上不會加入這樣的邏輯
    if (acc == "test" and psw == "test") or session['enter'] == 'open':
        session['enter'] = 'open'
        return redirect(url_for("member")) 
    elif acc == '' and psw == '' :
        return redirect('http://127.0.0.1:3000/error?message=請輸入帳號密碼') 
    else:
        return redirect(url_for("error")) 

#跳轉到memeber的路由後，如果紀錄保持存在，便會渲染到member.html ，反之跳轉到首頁。 
@app.route('/member')
def member():
    if session['enter'] == 'open':
       return render_template("member.html") 
    else :
       return redirect("/")
    
#跳轉到error的路由後，設定w參數去取得要求物件，
#render_template  可渲染到網址及靜態上，但html無法直接接收參數
@app.route('/error')
def error():
    w=request.args.get('message','帳號、或密碼輸入錯誤')
    return render_template("error.html",w2=w)
#研究討論w2=w 的寫法？？？

#跳轉到signout路由，假設沒有紀錄會跳轉到首頁
@app.route('/signout',)
def signout():
    session['enter'] = 'close'
    return redirect('/')
     
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000,debug=True)