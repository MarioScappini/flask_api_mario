from http import HTTPStatus
from flask import Flask,Blueprint, jsonify, request
from flasgger import swag_from
import requests as req
from api.schema.http import HTTP

import config as conf

posts_api = Blueprint('posts',__name__)

@posts_api.route("/", methods=["GET", "POST","DELETE","PUT"])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Starter Kit'
        }
    }
})
def posts():
    if request.method == "GET":
       return get_posts()

    elif request.method == "POST":
        return create_post()

    elif request.method == "DELETE":
        return delete_post()

    elif request.method == "PUT":
        return updated_post()

    else:
        return jsonify({"message":"Method not supported"}), 405



def get_posts():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        
        try:
            userId = userValidation(json["token"])
            
            url = conf.BASE_URL + "posts?userId=" + str(userId[0]) 
            
            response = req.get(url)
            return jsonify({"posts":response.json()}), response.status_code
        except:        
            return jsonify({"message":"Bad Request"}), 400

    else:
        return jsonify({"message":"Bad Request"}), 400

    



def create_post():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        
        try:
            userId = userValidation(str(json['token']))

            url = conf.BASE_URL + "posts" 
            response = req.post(url, data={
                'title': str(json['title']),
                'body': str(json['body']),
                'userId': userId[0]
            })
            return response.json(), response.status_code

        except:
            return jsonify({"message":"Bad Request"}), 400

    else:
        return jsonify({"message":"Bad Request"}), 400


def delete_post():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        
        try:
            userId = userValidation(str(json['token']))
            
            url = conf.BASE_URL + "/posts/" + str(json["postId"]) 
            response = req.delete(url)
            return jsonify({"message":"Deleted"}), response.status_code

        except:
            return jsonify({"message":"Bad Request"}), 400

    else:
        return jsonify({"message":"Bad Request"}), 400

def updated_post():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        
        try:
            userId = userValidation(str(json['token']))

            url = conf.BASE_URL + "posts/" + str(json['id'])
            response = req.put(url, data={
                "id": str(json['id']),
                'title': str(json['title']),
                'body': str(json['body']),
                'userId': userId[0]
            })
            return response.json(), response.status_code

        except:
            return jsonify({"message":"Bad Request"}), 400

    else:
        return jsonify({"message":"Bad Request"}), 400

def userValidation(token):
    plaintext_token = token
    active_user = HTTP.get_active_user(plaintext_token)
    if len(active_user) < 0:
        return "", 401
    
    return active_user[0]