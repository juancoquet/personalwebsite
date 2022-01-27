Author: [[👤 Harry J.W. Percival]]
Type: #book
Genres: #comp-sci #webdev 

---
# Test Driven Development with Python
### 1 Getting Django Set Up Using a Functional Test
- [[The first step of Test Driven Development]]
- [[First Django web app test]]

### 2 Extending our Functional Test Using the `unittest` Module
- [[Functional tests]]
- [[Using comments]]
- [[Writing a User Story for functional testing]]

### 3 Testing a Simple Home Page with Unit Tests
- [[Unit Tests vs Functional Tests]]
- [[TDD workflow]]
- [[Django's workflow]]
- [[`django.urls` `resolve` function]]

### 4 What Are We Doing with All These Tests? (And, Refactoring)
- [[Why trivial tests are important]]
- [[Testing template used]]
- [[Don't change functionality while refactoring]]

### 5 Saving User Input: Testing the Database
- [[Debugging unexpected functional test errors]]
- [[Testing a POST request]]
- [[What are Django migrations?]]
- [[Creating a new database entry without calling `save()`]]
- [[The purpose of a view function]]

### 6 Improving Functional Tests: Ensuring Isolation and Removing Voodoo Sleeps
- [[Using `LiveServerTestCase` for Django functional tests]]
- [[Accessing `LiveServerTestCase` server with selenium]]
- [[Ensure test isolation]]

### 7 Working Incrementally
- [[Big Design Up Front vs Agile and Minimum Viable Application]]
- [[Testing Django view context items]]

### 8 Prettification: Layout and Styling, and What to Test About It
- [[Testing aesthetics]]
- [[Getting web element position and size]]
- [[Loading static files]]
- [[Using `collectstatic`]]

### 9 Testing Deployment Using a Staging Site
- [[Setting up a staging server for tests]]

### 11 Automating Deployment with Fabric
- [[Using `fabric` to automate deployment]]

### 12 Splitting Our Tests into Multiple Files, and a Generic Wait Helper
- [[Generic explicit wait helper function for testing]]
- [[Put unit tests in a `tests` directory]]

### 13 Validation at the Database Layer
- [[Test that errors are properly raised]]
- [[Django's `reverse` function]]
- [[Defining `get_absolute_url` for a Django model]]
- [[Validate data at the lowest possible level, ideally at the database]]

### 14 A Simple Form
- [[A complex Django view is a code smell]]
- [[Creating Django ModelForms]]
- [[Testing forms]]
- [[Testing that a form is used in a view]]
- [[Using `grep` in the command line]]
- [[Using a Django form in a view]]
- [[Django forms and HTML5]]

### 15 More Advanced Forms
- [[View testing checklist]]

### 16 Dipping Our Toes, Very Tentatively, into JavaScript
- [[Setting up a JavaScript test runner]]
- [[Using jQuery]]

### 18 User Authentication, Spiking, and De-Spiking
- [[Testing sent emails]]
- [[Creating a custom user model]]
- [[Driving Django models with TDD]]

### 19 Using Mocks to Test External Dependencies or Reduce Duplication
- [[Mocking sending an email]]
- [[What is a Mock object?]]
- [[Using `@patch` for mocking]]

### 20 Test Fixtures and a Decorator for Explicit Waits
- [[How do Django sessions work?]]
- [[Creating a `@wait` decorator]]

### 22 Finishing "My Lists": Outside-In TDD
- [[Logging in a user through the Django test client]]
- [[Outside-In testing]]

### 23 Test Isolation, and "Listening to Your Tests"
- [[Don't work on lower level code with failing tests in the upper layers]]
- [[Use helper methods to keep ORM calls in the model layer]]

### 26 Fast Tests, Slow Tests, and Hot Lava
- [[When to use isolated tests vs integrated tests]]