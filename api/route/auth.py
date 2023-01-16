from http import HTTPStatus
from flask import Flask,Blueprint, jsonify, request
from flasgger import swag_from
import pyaes, pbkdf2, binascii, os, secrets
from api.schema.http import HTTP
from api.schema.encryption import Encryption
import requests as req
import config as conf

auth_api = Blueprint('auth',__name__)

@auth_api.route("/login", methods=["POST"])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        
        url = conf.BASE_URL + "users?username=" + str(json['username'])
        response = req.get(url)

        user = response.json()
        user_data = user[0]
        plaintext = str(user_data["id"])
        ciphertext = str(user_data["id"]) 
        HTTP.login_user(plaintext,ciphertext)
        return jsonify({"token": ciphertext, "session":response.json()}), response.status_code


    else:
        return jsonify({"message":"Bad Request"}), 400
     

@auth_api.route("/logout", methods=["POST"])
def logout():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        try:
            decrypt_token = json["token"]
            session_id = HTTP.get_active_user(decrypt_token)
            HTTP.delete_session(str(session_id[0][0]))
            return jsonify({"message":"logout"}), 200
        
        except:
            return jsonify({"message":"Bad Request"}), 400

    else:
        return jsonify({"message":"Bad Request"}), 400