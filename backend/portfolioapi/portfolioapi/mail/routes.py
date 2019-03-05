from flask import Blueprint, current_app, request

from portfolioapi import app_mail
from portfolioapi.utils import make_json_response
from portfolioapi.mail.MailListHandler import MailListHandler

mail = Blueprint('mail', __name__)
mail_list_handler = MailListHandler(app_mail, current_app)


@mail.route("/mail/subscribe", methods=['POST'])
def subscribe_to_mail_list():
	result = mail_list_handler.confirmation_email_handler(request.data)
	return make_json_response(result, result['code'])

@mail.route("/mail/confirm/<path:sub_code>")
def confirm_subscription(sub_code):
	return mail_list_handler.subscription_confirmation_handler(sub_code)

@mail.route("/mail/unsubscribe/<path:sub_code>")
def unsubscribe(sub_code):
	return mail_list_handler.unsubscribe_handler(sub_code)