Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch16 p279

---
# Setting up a JavaScript test runner
To set up a JavaScript test runner, we first need a JavaScript testing framework. We'll be using QUnit, but there are many more to choose from.

To get started with QUnit, its files (one `.js` and one `.css`) need to be downloaded to your directory for testing static files. This can be done from the terminal by navigating to your desired directory and running the command:
`curl -O 'https://code.jquery.com/qunit/qunit-2.15.0.{js,css}'`

The above will download the files for QUnit version 2.15.0, but the numbers towards the end of the download link can be substituted to match the latest available version, or a version of your choice.

Next, create a `tests.html` file in the same directory as the QUnit files, and populate it with the following boilerplate HTML:
```HTML
 <!DOCTYPE html> 
<html>
<head> 
	<meta charset="utf-8">  
	<meta name="viewport" content="width=device-width">
	<title>Javascript tests</title>  
	<link rel="stylesheet" href="qunit-2.0.1.css">
</head>
<body> 
	<div id="qunit"></div>  
	<div id="qunit-fixture"></div> <script src="qunit-2.0.1.js"></script>

	<script>

		QUnit.test("smoke test", function (assert) {
			assert.equal(1, 1, "Maths works!");
		});

	</script>
</body> 
</html>
```

This `tests.html` file can now be opened in your browser to display a window that will be the home of your JS tests.

Each test that we run normally carries state into the next, meaning that if we make any changes to the HTML using jQuery, those changes will be present in the next test. This can affect our tests, so we may want to reset everything back to the original state before moving on to the next test. We can do this manually, but a better way is by defining any elements we want to be reset after each test inside the `qunit-fixture` div. For example:
```HTML
...

	<div id="qunit-fixture">
		<form>
			<input name="text" />
			<div class="has-error">Error text</div>
		</form>
	</div>

...
```

The form specified above will be reset back to the given state after each test runs, even if any changes are made. This is similar behaviour to Python's `unittest` `setUp` and `tearDown` methods.