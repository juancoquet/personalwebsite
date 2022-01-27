Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch8 p137

---
# Getting web element position and size
You can find the position of an element with Selenium by first using a `find` method to look for the element, then using the `location` attribute, which is a dictionary that contains x and y coordinates.
```python
# assume we have selenium browser set up as the namespace browser

my_el = browser.find_element_by_id('id_my_el')
location = my_el.location['x']		# Returns horizontal position
```

To find the size of an element, use the `size` attribute, which is also a dictionary with the keys `'width'` and `'height'`.
```python
width = my_el['width']		# Returns width of the element
```

---
### See also:
- [[Testing aesthetics]]