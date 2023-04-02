from flask import Flask, redirect, url_for, make_response, render_template, flash, abort
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from hidden import secret, admin_flag, jwt_secret


app = Flask(__name__)
cookie = "access_token_cookie"

app.config['SECRET_KEY'] = secret
app.config['JWT_SECRET_KEY'] = jwt_secret
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['DEBUG'] = False

jwt = JWTManager(app)


@jwt.expired_token_loader
def my_expired_token_callback():
    return abort(404)


@jwt.invalid_token_loader
def my_invalid_token_callback(callback):
    return abort(404)


@jwt_required(optional=True)
def get_flag():
    if get_jwt_identity() == 'admin':
        return admin_flag
    else:
        return "Anonymous User, Flag not available"


@app.route('/flag')
def flag():
    response = make_response(render_template('main.html', flag=get_flag()))
    response.set_cookie(cookie, create_access_token(identity='anonymous'))
    return response


@app.route('/')
def source():
    return render_template('main.html', flag="Nothing here!")


if __name__ == "__main__":
    app.run("0.0.0.0", 5121, debug=False)
