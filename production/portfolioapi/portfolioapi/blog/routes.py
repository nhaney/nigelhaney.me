from flask import Blueprint, current_app, request

from portfolioapi import limiter, app_mail
from portfolioapi.utils import make_json_response
from portfolioapi.blog.BlogApiHandler import BlogApiHandler


blog = Blueprint('blog', __name__)
blog_api_handler = BlogApiHandler(app_mail, current_app)

@blog.route("/blog/posts", methods=['GET'])
def get_posts_handler():
	# TODO: make get request that returns all post titles, ids, and excerpts
	# This will be used for blog landing page
	result = blog_api_handler.preview_posts()
	return make_json_response(result, result['code'])

@blog.route("/blog/posts/<post_title>", methods=['GET'])
def get_post_handler(post_title):
	result = blog_api_handler.read_post(post_title)
	return make_json_response(result, result['code'])

@blog.route("/blog/posts", methods=['POST'])
@limiter.limit("200/day;100/hour;10/minute;1/second")
def create_post_handler():
	print("here")
	result = blog_api_handler.create_post(request.data)
	return make_json_response(result, result['code'])

@blog.route("/blog/posts", methods=['PUT'])
def update_post_handler():
	result = blog_api_handler.update_post(request.data)
	return make_json_response(result, result['code'])

@blog.route("/blog/posts", methods=['DELETE'])
def delete_post_handler():
	result = blog_api_handler.delete_post(request.data)
	return make_json_response(result, result['code'])

@blog.route("/blog/comments", methods=['POST'])
@limiter.limit("50/day;25/hour;5/minute;1/second")
def create_comment_handler():
	result = blog_api_handler.create_new_comment(request.data)
	return make_json_response(result, result['code'])

@blog.route("/blog/comments/<post_id>", methods=['GET'])
def get_comments_handler(post_id):
	result = blog_api_handler.read_comments_from_post(post_id)
	return make_json_response(result, result['code'])

@blog.route("/blog/comments", methods=['DELETE'])
def delete_comment_handler():
	result = blog_api_handler.delete_comment_by_id(request.data)
	return make_json_response(result, result['code'])