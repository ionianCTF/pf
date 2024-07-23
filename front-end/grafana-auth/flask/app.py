from flask import Flask, redirect
import flask
import flask_login

login_manager = flask_login.LoginManager()

# Our mock database.
users = {'people': {'password': 'flows'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user

app = Flask(__name__)
app.secret_key = 'p3OpL3'  # Change this!
login_manager.init_app(app)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if email in users and flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect('/')

    return 'Bad login'

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect('/login')
    # return 'Unauthorized', 401

@app.route("/auth")
def nginx_auth():
    if flask_login.current_user.is_authenticated:
        return "You are logged in! Sweet!"
    else:
        return flask.redirect(flask.url_for('login')), 401
        # return 'Sorry, but unfortunately you\'re not logged in.', 401

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
