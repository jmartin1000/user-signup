from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/")
def index():
    encoded_error1= request.args.get("error1")
    encoded_error2= request.args.get("error2")
    encoded_error3= request.args.get("error3")
    encoded_error4= request.args.get("error4")
    name = request.args.get("name")
    name = "" if name is None else name
    email = request.args.get("email")
    email = "" if email is None else email
    return render_template('signup.html', name=name, email=email,
        error1=encoded_error1, error2=encoded_error2, 
        error3=encoded_error3, error4=encoded_error4)

@app.route("/welcome", methods=['POST'])
def sign_up():
    #pull user info out of form
    user_name = request.form['name']
    email = request.form['email']
    password = request.form['pswd']
    password_verify = request.form['pswd_verify']
    #verify user name
    if (not user_name) or (user_name.strip() == "") or (user_name == "None"):
        error1 = "No username submitted"
        user_name = ""
        return redirect("/?error1=" + error1 + "&email="+email)

    if len(user_name) > 20 or len(user_name) < 3:
        error1 = "Username must be between 3 and 20 characters"
        return redirect("/?error1=" + error1 + "&name="+user_name + "&email="+email)
    
    if " " in user_name:
        error1 = "Username cannot contain any spaces"
        return redirect("/?error1=" + error1 + "&name="+user_name + "&email="+email)

    #verify password
    if (not password) or (password.strip()==""):
        error2 = "No password submitted"
        return redirect("/?error2=" + error2 + "&name="+user_name + "&email="+email)

    if len(password) > 20 or len(password) < 3:
        error2 = "Password must be between 3 and 20 characters"
        return redirect("/?error2=" + error2 + "&name="+user_name + "&email="+email)

    if " " in password:
        error2 = "Password cannot contain any spaces"
        return redirect("/?error2=" + error2 + "&name="+user_name + "&email="+email)

    if password != password_verify:
        error3 = "The passwords do not match"
        return redirect("/?error3=" + error3 + "&name="+user_name + "&email="+email)
    
    #validate email
    # for future use regex expression '/[^@]+@[^\.]+\..+/g'
    if email != '':
        if len(email) > 20 or len(email) < 3:
            error4 = "email must be between 3 and 20 characters"
            return redirect("/?error4=" + error4 + "&name="+user_name + "&email="+email)

        criteria1 = email.count("@")
        criteria2 = email.count(".")
        criteria3 = email.count(" ")
        if criteria1 != 1 or criteria2 != 1 or criteria3 != 0:
            error4 = "this email does not appear to be valid"
            return redirect("/?error4=" + error4 + "&name="+user_name + "&email="+email)
                           

    # now that everything is valid
    return render_template('welcome.html', name=user_name)




app.run()
