from fabric.api import local, lcd   #lcd: local change dir

def hello():
    print ("Executing Hello")
    local("python --version")

def clone (day=""):
    print ("day " + day)
    if day == "":
        print ("Please specify a day")
    else:
        url_to_clone = "https://bala_prasanna@bitbucket.org/bala_prasanna/pydot-day"
        print url_to_clone
        work_dir = 'D:\\tmp\\NUS\\bala_prasanna-pydot4_day05-32cf70979102\\fabric\\'
        with lcd(work_dir):
            local ("git clone " + url_to_clone)

def startnb():
    work_dir = 'D:\\tmp\\NUS\\bala_prasanna-pydot4_day05-32cf70979102\\'
    with lcd(work_dir):
        local ("activate pydot4" )
        local ("jupyter notebook")

def call_api():
    local("python app.py &")
