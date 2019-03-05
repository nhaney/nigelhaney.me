import unittest
import sys

sys.path.append("../../portfolioapi")
from portfolioapi.blog.BlogTableHandler import BlogTableHandler

class TestBlogTableHandler(unittest.TestCase):
	"""
	This class unit tests the methods of the TestBlogHandler class
	"""
	
	def test_create_blog_post_success(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"
		temp_excerpt = "My Unit Test"
		temp_content = "Here is some sample content."

		test_result = \
			bth.create_blog_post(temp_title, temp_excerpt, temp_content)

		self.assertEqual((temp_title, temp_excerpt, temp_content), 
						   (test_result['post_title'],
						   	test_result['excerpt'],
						   	test_result['content']))
		bth.delete_blog_post(temp_title)
		return

	def test_create_blog_post_already_exists(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"
		temp_excerpt = "My Unit Test"
		temp_content = "Here is some sample content."

		bth.create_blog_post(temp_title, temp_excerpt, temp_content)

		test_result = \
			bth.create_blog_post(temp_title, temp_excerpt, temp_content)

		self.assertEqual("POST_ALREADY_EXISTS", test_result)
		bth.delete_blog_post(temp_title)
		return

	def test_read_blog_post_success(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"
		temp_excerpt = "My Unit Test"
		temp_content = "Here is some sample content."

		bth.create_blog_post(temp_title, temp_excerpt, temp_content)
		test_result = bth.read_blog_post(temp_title)
		self.assertEqual((temp_title, temp_excerpt, temp_content),
						  (test_result['post_title'],
						  	test_result['excerpt'],
						  	test_result['content']))

		bth.delete_blog_post(temp_title)
		return

	def test_read_blog_post_not_found(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"

		test_result = bth.read_blog_post(temp_title)
		self.assertEqual("POST_NOT_FOUND", test_result)
		return

	def test_update_blog_post_success(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"
		temp_excerpt = "My Unit Test"
		temp_content = "Here is some sample content."
		temp_updated_content = "Here is some updated content."

		init_result = bth.create_blog_post(temp_title, temp_excerpt, temp_content)
		test_result = \
			bth.update_blog_post(temp_title, temp_updated_content)

		self.assertEqual(temp_updated_content, test_result['content'])
		self.assertNotEqual(init_result['last_edited'], test_result['last_edited'])

		bth.delete_blog_post(temp_title)
		return

	def test_update_blog_post_not_found(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"

		test_result = \
			bth.update_blog_post(temp_title, "NEW CONTENT")

		self.assertEqual("POST_NOT_FOUND", test_result)
		return

	def test_delete_blog_post_success(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"
		temp_excerpt = "My Unit Test"
		temp_content = "Here is some sample content."

		bth.create_blog_post(temp_title, temp_excerpt, temp_content)
		test_result = bth.delete_blog_post(temp_title)

		self.assertEqual("POST_DELETED", test_result)
		return

	def test_delete_blog_post_not_found(self):
		bth = BlogTableHandler()
		temp_title = "Unit Testing Create Blog Post"

		test_result = bth.delete_blog_post(temp_title)

		self.assertEqual("POST_NOT_FOUND", test_result)
		return

	def test_preview_delete_blog_posts(self):
		bth = BlogTableHandler()

		bth.delete_all_blog_posts()

		temp_title = "Unit Testing Create Blog Post"
		temp_excerpt = "My Unit Test"
		temp_content = "Here is some sample content."

		bth.create_blog_post(temp_title + '1', temp_excerpt, temp_content)
		bth.create_blog_post(temp_title + '2', temp_excerpt, temp_content)
		bth.create_blog_post(temp_title + '3', temp_excerpt, temp_content)

		test_result = bth.preview_blog_posts()

		self.assertEqual(len(test_result), 3)
		self.assertTrue(all("post_title" in result and \
							"excerpt" in result and \
							"unique_url" in result for result in test_result))

		bth.delete_all_blog_posts()
		return

	def test_preview_delete_blog_posts_empty(self):
		bth = BlogTableHandler()

		bth.delete_all_blog_posts()
		test_result = bth.preview_blog_posts()

		self.assertEqual(test_result, "NO_POSTS_EXIST")

		return




if __name__ == '__main__':
	unittest.main()