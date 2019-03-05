import json
import requests
import markdown2
import sys
import os

def blogsubmitter(title, excerpt, md_file, post_url):
	if not title:
		return "Blog post must have a title."
	if not excerpt:
		return "Blog post must have an excerpt."
	if not md_file:
		return "No markdown file specified to send."
	if "PORTFOLIO_SECRET_KEY" not in os.environ:
		return "Secret key not found for upload."

	try:
		file = open(md_file, 'r')
	except:
		return "Problem opening the file."

	md_string = file.read()
	file.close()

	html_string = markdown2.markdown(md_string)
	
	to_send = json.dumps({
		"post_title": title,
		"excerpt": excerpt,
		"content": html_string,
		"auth": os.environ["PORTFOLIO_SECRET_KEY"]
	})

	try:
		r = requests.post(post_url, to_send)
	except requests.exceptions.RequestException as e:
		return "Error: " + str(e)
	else:
		return r.json()

if __name__ == '__main__':
	if len(sys.argv) < 5:
		print("Invalid arguments. Correct format is:\n$ python3 blogsubmitter <title> <excerpt> <md file> <url>")
	else:
		print(blogsubmitter(sys.argv[1], 
							sys.argv[2], 
							sys.argv[3], 
							sys.argv[4]))