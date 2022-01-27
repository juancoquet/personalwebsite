Note Type: #litnote
Source: [[📖 Test Driven Development with Python]] ch16 p282

---
# Using jQuery
The first step to using jQuery is to download it as a file from their website, https://jquery.com. You should download it to wherever your static tests are located (see [[Setting up a JavaScript test runner]]). This will download a `jquery-x.x.x.js`, with the `x.x.x` part being the version number.

To start using jQuery in your testing HTML file, it must be loaded as a script, giving the `src` the relative path to the jQuery file.
```HTML
<!-- tests.html -->
...

	<script src="../jquery-3.6.0.js"></script>
	
...
```

Once jQuery is loaded in, we use the `$` sign as a kind of jQuery Swiss Army knife—it's used to find bits of the DOM. Below, we use it to find a CSS selector—we tell it to find all the elements that have the class name `has-error` (we use `.` in CSS to select classes).
```HTML
<!-- tests.html -->
...

	<script>
		QUnit.test("my test", function (assert){
			assert.equal($('.has-error').is(':visible'), true);
			$('.has-error').hide();
		})
	</script>

...
```

The `$` returns an object that represents one or more DOM elements, which has various useful methods that allow us to manipulate or get information about those elements. We use one of these methods — `.is` — which tells us whether an element matches a given CSS property. Here we use it to find out if it matches the `:visible` property, which tells us if the element (or elements) is displayed or hidden. We assert that this returns `true`.

We then access the element(s) again and call the `.hide` method on them, which changes the `style` property of the element to `style="display: none"` behind the scenes.

We can access `input` elements by using the following syntax:
```HTML
$('input[name="text"]')
```

This retrieves any `input` elements that have the property `name="text"`. We can then call methods on this element, one of which is `.trigger`, which allows us to trigger JavaScript DOM events on the element(s). Here we trigger a *keypress* event, which is what the browser does behind the scenes any time a user types something into an input element.
```HTML
$('input[name="text"]').trigger('keypress');
```