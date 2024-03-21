from flask import Flask, url_for

# instantiate a Flask object
app = Flask(__name__)


# a get route by default
@app.route('/')
@app.route('/hi')
def hello_from_flask():
    return "Hello from Flask!"


# a get route by default
@app.route('/bye')
def goodbye_from_flask():
    return "Goodbye from Flask :("


# brackets means replaceable parameter
@app.route('/dynamic/<colour>')
def echo_colour_choice(colour):
    return f"You like the colour {colour}"


@app.route('/dynamicname/<name>')
def hello_name(name):
    return f"Hello {name}"


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    message = "Your number squared is " + str(squared)
    return message


@app.route('/page1/<name>')
def simple_html_page(name):
    home_url = url_for('hello_from_flask')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Page 1</title>
        </head>
        <body>
            <h1>Name Page</h1>
            <p>Hello {name}!</p>
            <hr>
            <a href="{home_url}">Home Page</a>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)