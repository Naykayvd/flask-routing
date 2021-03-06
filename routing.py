# imports
from flask import Flask, redirect, url_for

app = Flask(__name__)


# user redirect
@app.route('/user/<name>')
def user_page(name):
    if name == "nahum":
        return redirect(url_for('admin_page', name=name))
    else:
        return redirect(url_for('guest_page', name=name))


# admin page
@app.route('/admin/<name>')
def admin_page(name):
    return "I am the admin. My name is %s" % name


# guest page
@app.route('/guest/<name>')
def guest_page(name):
    return "I am on the guest page. My name is %s" % name


if __name__ == '__main__':
    app.debug = True
    app.run()
