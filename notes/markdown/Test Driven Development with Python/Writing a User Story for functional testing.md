Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch2 p16

---
# Writing a User Story for functional testing
It is a good idea to write a *User Story* when creating your functional test to describe the intended user experience. This will act as a specification, criteria for you tests to meet. You can write your user story by using comments in your functional testing file.
```python
from selenium import webdriver


browser = webdriver.Firefox()

# Edit has heard about a new web app to track her to-dos. She visits the
# homepage.
browser.get('http://localhost:8000')

# She notices that the page title and header mention to-do lists.
assert 'To-Do' in browser.title

# She is invited to enter a to-do straight away.

# She types "Buy peacock feathers" into a text box.

# When she hits enter, the page updates and displays
# "1: Buy peacock feathers" as an item in the to-do list.

# There is still a text box inviting her to add another item. She enters
# "Use feathers to make a fly".

# The page updates, and now shows both items.

# Edith wonders whether the site will remember her list. Then she sees # that
# the site has generated a unique URL for her -- there is some explanatory text
# to that effect.

# She visits that URL - her to-do list is still there. # Satisfied, she goes
# back to sleep.

browser.quit()
```

---
### See also:
- [[Functional tests]]