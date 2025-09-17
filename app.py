from flask import Flask, render_template, request
app = Flask(__name__)
def nhapdulieu(n):
    a=[]
    print('nhap cac phan tu cua day')
    for i in range (n):
        a.append(int(input(f'nhap gia tri thu {i} cua day: '))) 
    maxx = a[0]
    for i in a:
       if maxx < i:
           maxx = i
    return maxx
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            n = int(request.form.get("n"))
            a=[]
            result = nhapdulieu(n)
        except:
            result = "Lỗi nhập dữ liệu!"
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)

    