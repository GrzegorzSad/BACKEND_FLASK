from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import posts, tokens, errors, auth

