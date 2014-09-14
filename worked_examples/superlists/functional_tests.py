from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	import pdb
	pdb.set_trace()

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_start_and_retrieve_list(self):
		#self.browser = webdriver.Firefox()
		# Edith heard about a cool new app, she goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the Test!')

		# She is invited to create a to-do item

		# She types in "Buy synthetic feathers" into a text box

		# When she hits enter the page updates and now the page lists
		# 1: "Buy synthetic feathers" as an item in a to-do list

		# There is still another text box inviting her to add another item
		# She enters "Use synthetic feathers to make a fly"

		# The page updates again, and now she has both items in her list

		# She realizes that the site has generated a unique URL for her 
		# and there is some explanatory text to that effect

		# Satisfied, she goes on to bean flicking

if __name__ == "__main__":
	unittest.main()

