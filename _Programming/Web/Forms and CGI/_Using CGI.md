Place file inside `cgi-bin/` directory
## CGI with [[Python]]
```python
form = cgi.FieldStorage()         # Gets the form
num1 = form.getvalue('theNumber') # Returns the string specified by the value

# Python typically uses the print statement to generate a new html page
```
#### Example
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8"/>
	<title>square a number</title>
</head>
<body>
	<form action="cgi-bin/NumSquared.py" method="GET">
		<label for="theNumber">Enter a number to be squared</label>
		<input type="text" id="theNumber" name="theNumber"/> <br/>
		<input type="submit" value="submit"/>
	</form>
</body>
</html>
```
```python
#!/usr/bin/python3
import cgi, cgitb
form = cgi.FieldStorage()
num1 = form.getvalue('theNumber')
squared = float(num1)**2
print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Python script to output the square of a number </title> </head>')
print('<body>')
print('<p>')
print('The square of %s is %g' % (num1, squared))
print('</p>')
print('</body>')
print('</html>')
```