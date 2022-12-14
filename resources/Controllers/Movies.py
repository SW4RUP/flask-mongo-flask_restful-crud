# from msilib.schema import Directory
from flask import Response, request
from database.Models.Movies import Movie
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class MoviesApi(Resource):


  def get(self):
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)
    

  def post(self):
    try:
      body = request.get_json()
      movie = Movie(**body).save()
      id = movie.id
      return {'id': str(id)}, 200
    except Exception as e:
      return {'error': dict(e)}, 500


class MovieApi(Resource):
  

  def put(self, id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200
  

  def delete(self, id):
    movie = Movie.objects.get(id=id).delete()
    return '', 200
  

  def get(self, id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)
