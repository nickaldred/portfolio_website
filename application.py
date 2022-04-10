from flask import Flask, render_template, send_from_directory, redirect
import os

application = app = Flask(__name__)

#Functions for website page rendering 

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route("/test")
def test():
    return(render_template("test.html"))

@app.route("/projects")
def projects():
    return(render_template("projects.html"))

@app.route("/about_me")
def about_me():
    return(render_template("about_me.html"))

@app.route("/cv")
def cv():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/files'
    return send_from_directory(filepath, 'cv.pdf')

@app.route("/mobile_home")
def mobile_home():
    return(render_template("mobile_home.html"))

@app.route("/mobile_about_me")
def mobile_about_me():
    return(render_template("mobile_about_me.html"))

#Functions to redirect to socials - Linked in and Github

@app.route("/linkedin")
def linkedin():
    return redirect("https://www.linkedin.com/in/nicholas-aldred94", code=302)

@app.route("/github")
def github():
    return redirect("https://www.github.com/nickaldred", code=302)


#Functions to redirect to to projects hosted on Heroku

@app.route("/project1")
def project1():
    return redirect("https://project1-portfolio-nick.herokuapp.com")

@app.route("/project1_git")
def project1_git():
    return redirect("https://github.com/nickaldred/Data_Visualisation")

@app.route("/project2")
def project2():
    return redirect("https://sql-log-in.herokuapp.com/")

@app.route("/project2_git")
def project2_git():
    return redirect("https://github.com/nickaldred/sql_log_in_tool")

@app.route("/project3")
def project3():
    return redirect("https://microblog-project-3.herokuapp.com")

@app.route("/project3_git")
def project3_git():
    return redirect("https://github.com/nickaldred/micro_blog")

@app.route("/project4")
def project4():
    return redirect("/")

@app.route("/project4_git")
def project4_git():
    return redirect("https://github.com/nickaldred/portfolio_website")


@app.route("/project5")
def project5():
    pass
    #return redirect("#")

@app.route("/project5_git")
def project5_git():
    return redirect("https://github.com/nickaldred/Webcam_Photo_Viewer")

@app.route("/project6")
def project6():
    return redirect("https://assignment3-web-app.herokuapp.com/")

@app.route("/project6_git")
def project6_git():
    return redirect("https://github.com/nickaldred/web_socket_chat")

@app.route("/project7")
def project7():
    return redirect("https://flatmates-bill-web-app.herokuapp.com/")

@app.route("/project7_git")
def project7_git():
    return redirect("https://github.com/nickaldred/flat-mates-bill")

@app.route("/project8")
def project8():
    return redirect("https://calorie-web-app.herokuapp.com/calorie_form_page")

@app.route("/project8_git")
def project8_git():
    return redirect("https://github.com/nickaldred/calorie_web_app")




app.run(debug=True)