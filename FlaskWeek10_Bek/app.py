from flask import Flask, url_for

# instantiate a Flask object
app = Flask(__name__)


# a get route by default
@app.route('/')
@app.route('/home')
def home_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Home</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>Home Page</h1>
            <section>
            <p>Welcome to my first Flask website!</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>
    """


@app.route('/about')
def about_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>About</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>About Page</h1>
            <section>
            <p>This is a very simple Flask website to learn about using html routes and anchor tags for navigating between pages.</p>
            <p>It's not pretty and it's really not practical (lots of duplicated code).</p>
            <p>To be continued...</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>     
    """


@app.route('/portfolio')
def portfolio_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Portfolio</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>Portfolio Page</h1>
            <section>
            <p>Projects...</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>
    """


@app.route('/contact')
def contact_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return f"""
    <!doctype>
    <html>
        <head>
            <title>Contact</title>
            <link rel="stylesheet" href="./static/styles.css">
        </head>
        <body>
            <nav>
                <a href="{home_url}">Home</a>
                <a href="{about_url}">About</a>
                <a href="{portfolio_url}">Portfolio</a>
                <a href="{contact_url}">Contact</a>
            </nav>
            <main>
            <h1>Contact Page</h1>
            <section>
            <p>Contact me...</p>
            </section>
            </main>
            <footer>&copy; Bek &amp; SKY Get Into Tech, 2024</footer>
        </body>
    </html>     
    """

# @app.route('/page1/<name>')
# def simple_html_page(name):
#     # url_for() is a flask method to get url python function
#     home_url = url_for('hello_from_flask')
#     return f"""
#     <!doctype>
#     <html>
#         <head>
#             <title>Page 1</title>
#         </head>
#         <body>
#             <h1>Name Page</h1>
#             <p>Hello {name}!</p>
#             <hr>
#             <a href="{home_url}">Home Page</a>
#         </body>
#     </html>
#     """

# # a get route by default
# @app.route('/bye')
# def goodbye_from_flask():
#     return "Goodbye from Flask :("
#
#
# # brackets means replaceable parameter
# @app.route('/dynamic/<colour>')
# def echo_colour_choice(colour):
#     return f"You like the colour {colour}"
#
#
# @app.route('/dynamicname/<name>')
# def hello_name(name):
#     return f"Hello {name}"
#
#
# @app.route('/square/<int:number>')
# def square(number):
#     squared = number ** 2
#     message = "Your number squared is " + str(squared)
#     return message

if __name__ == "__main__":
    app.run(debug=True)