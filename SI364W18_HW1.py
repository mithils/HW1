## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".



## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications.
# Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask,request
import requests

app = Flask(__name__)
app.debug = True

@app.route('/class')
def hello_to_you():
    return  '<h1>Welcome to SI364</h1>'


@app.route('/movie/<movie>')
def movie_details(movie):
    base_url = "https://itunes.apple.com/search?term={}".format(movie)
    response = requests.get(base_url)

    return response.text

@app.route('/question',methods=["GET","POST"])
def ask_question():
    s = """<br><br>
    <form action="http://localhost:5000/question" method='POST'>
    Number:<br>
    <input type="text" name="number"> Enter a number:
    <br>
    <input type="submit" value="Submit">
    </form>
"""
    if request.method == "POST":
        response = request.form['number']  # request.form.get("phrase","")
        number = int(response) * 2
        return s + "<br><br>" + str(number)
    else:
        return s

@app.route("/f1api",methods=["GET","POST"])
def problem_four():
    form_string = """<br>Historical F1 Driver Season Results<br>
    <form action="http://localhost:5000/f1api" method='POST'>
    <br>

    Enter a season(year):<input type="text" name="year">
    <br>
    <input type="checkbox" name="driver" value="hamilton">Hamilton<br>
    <input type="checkbox" name="driver" value="vettel">Vettel<br>
    <input type="checkbox" name="driver" value="alonso">Alonso<br>
    <input type="checkbox" name="driver" value="perez">Perez<br>
    <input type="submit" value="Submit">
    </form>
"""



    if request.method == 'POST':
        year = request.form['year']
        driver = request.form.get('driver')
        baseurl = "http://ergast.com/api/f1/{0}/drivers/{1}/results".format(year,driver)

        response = requests.get(baseurl)

        return form_string + "<br><br>"+"{0}'s {1} Season Results:".format(driver.upper(),year) + "<br><br>"+response.text
    else:
        return form_string



if __name__ == '__main__':
    app.run()


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL
# 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page.
# For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see
# something like the data shown in the included file sample_ratatouille_data.txt, which contains
# data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data,
# and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question,
# you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form,
# you should then see a web page that says "Double your favorite number is <number>". For example,
# if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4".
# Careful about types in your Python code!
## You can assume a user will always enter a number only.




## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
