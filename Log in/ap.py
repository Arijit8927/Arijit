from flask import Flask, request, session, redirect, url_for,render_template

ap = Flask(__name__)
ap.secret_key = "anyrandomsecretkey"   # 🔑 important for session
ap.secret_key = "anyrandomsecr"   # 🔑 important for session
ap.secret_key = "anyrandomsecr"   # 🔑 important for session
@ap.route('/', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request. form.get("password")
        choice=request.form.get("choice")

        if username == "Arijit" and password == "123" and choice == "student":
            session["user"] = username  # store session
            return render_template("student.html") #redirect(url_for("Student"))
        elif username == "Trisha" and password == "124" and  choice == "student":
            session["user"]= username
            return render_template("student.html")
        elif username == "Suresh" and password == "125" and  choice == "student":
            session["user"]= username
            return render_template("student.html")
        elif username == "Shrabani" and password == "126" and  choice == "student":
            session["user"]= username
            return render_template("student.html")
        elif username == "Rimjhim" and password == "127" and  choice == "student":
            session["user"]= username
            return render_template("student.html")
        elif username == "Aindrila" and password == "128" and  choice == "student":
            session["user"]= username
            return render_template("student.html")
        elif username == "Prajna" and password == "129" and  choice == "student":
            session["user"]= username
            return render_template("student.html")
        
        
        elif  username == "at" and password == "145" and choice == "teacher":
            session["user"] = username  # store session
            return render_template("teacher.html") #redirect(url_for("Student"))

            
         
        elif  username == "ap" and password == "187" and choice == "principal":
            session["user"] = username  # store session
            session["user"] =  password  # store session
            session["user"] =  choice  # store session

            return render_template("principal.html") #redirect(url_for("Student"))

            
        else:
            return  "This user or pass are rong! please provied right user or pass enter"
    
    return render_template("login.html")
    

@ap.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    ap.run(debug=True)      