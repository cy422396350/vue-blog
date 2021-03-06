from flask import Flask
from flask_restful import Api, Resource
from flask import make_response

from category import CategoryModel
from article import ArticleModel

app = Flask(__name__)

api = Api(app)

"""
    cross domain
"""


def allow_cross_domain(fun):
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun


class Category(Resource):
    @allow_cross_domain
    def get(self, category_id=0, page=0):
        return CategoryModel.getAll(category_id, page)
class Categories(Resource):
    @allow_cross_domain
    def get(self):
        return CategoryModel.getCat()
class Article(Resource):
    @allow_cross_domain
    def get(self, id):
        return ArticleModel.getInfo(id)


api.add_resource(Category, '/category/<int:category_id>/<int:page>', '/category/<int:category_id>')
api.add_resource(Categories, '/categories', '/categories/')
api.add_resource(Article, '/article/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
