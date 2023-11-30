also view [[_Using CGI]] for what to do on the python side

![[_Using HTML#`<form>` element]]

```html
<body>
	<form method="POST" action="comments.py">
		<h2>Tell us what you think</h2>
		<!-- etc -->
	</form>
</body>
```

The method attribute specifies the way that form data is sent to the server program
- GET appends the data to the URL
- POST sends the data in body of HTTP message
The action attribute specifies a server program that processes the form data (often as a URL)

---
# Input element

```html
<form method="POST" action="comments.py">
	<h2>Tell us what you think</h2>
	Name <input type="text" name="AName" size="20" /> <br/>
	Address <input type="text" name="address" size="30" />
</form>
```

`Type` attribute specifies the type of user input
`Name` attribute gives an identifier to the input data – used by the server program
`Size` attribute specifies the length of a text input field in characters value attribute specifies an initial value for the input data (optional

<form method="POST" action="comments.py">
	<h3>Tell us what you think</h3>
	Name <input type="text" name="AName" size="20" /> <br/>
	Address <input type="text" name="address" size="30" />
</form>
`example shown above`

## Labels and Input
```html
<form action="feedback.py">
	<h2>Tell us what you think</h2>
	<label for="user">Your name: </label>
	<input type="text" id="user" name="username" size="35"/>
	<label for="address">And address:</label>
	<input type="text" id="address" name="address" size="35"/>
</form>
```

---
## Checkbox `type="checkbox"`
`    Name` used to define a set of check boxes
`   Value` identifies the individual checkbox
` Checked` controls the boxes initial state
```html
<input type="checkbox" name="howheard" id="friend" value="friend" checked="checked"/> A friend told me <br/>
<input type="checkbox" name="howheard" id="dream" value="dream"/> In a dream <br/>
<input type="checkbox" name="howheard" id="link" value="link"/> Followed a link
```

**Note:** The user can click on the label and the checkbox will be checked:
```html
<input type="checkbox" name="howheard" id="friend" value="friend"/> <label for="friend"> A friend told me</label><br/>
```
## Radio `type="radio"`
Similar to check boxes, but only one can be enabled at a time
```html
<input type="radio" name="howheard" id="friend" value="friend" checked="checked"/> A friend told me <br>
<input type="radio" name="howheard" id="dream" value="dream"/> In a dream <br>
<input type="radio" name="howheard" id="link" value="link"/> Followed a link
```
## Button `type="button"`
`  Name:` identifier for the button
` Value:` Gives a label to the button
```html
<h3>Do you want to receive any further information: </h3>
<input type="button" name="yes" value="Yes" />
<input type="button" name="no" value="No" />
```
HTML Forms 11 • Radio buttons are similar to checkboxes, but only one of a set can be selected • To select a button by default, use the checked attribute (for one button only)

Do you want meme? <input type="button" name="yes" value="Yes" /> <input type="button" name="no" value="No" />

---
## Miscellaneous input types
#### `type="submit"`
Clicking this button sends the form data to the program (URL) specified in the action attribute of the form.
#### `type="reset"`
Clicking this button clears all data entered so far
#### `type="password"`
Similar to type="text" except that the input is echoed with asterisks (so not visible).
#### `type=file`
Provides a file dialogue box to specify a file that is sent to the server.
#### `type="hidden"`
similar to text input, but the **value** attribute is used to specify data that is to be sent to the server. Nothing appears on the screen.

---
## Text Area
Used for multi-line textual inputs

Size is specified using the `cols` and `rows` attributes.

Any text placed inside the element appears in the input area (this can be deleted).
Use the `placeholder` attribute for text displayed as temporary suggestions

```html
Please write your comments:<br>
<textarea name="comments" rows="5" cols="20">
	put text here
</textarea>
```
```html
Please write your comments:<br>
<textarea name="comments" rows="5" cols="20" placeholder="put text here"> </textarea>
```
## Select
The select element provides a drop down menu of options
An option can be selected by default using the selected attribute (otherwise the first in the list is initially selected)
```html
In the general scheme of life, how would you rate us?:
<select name="quality">
	<option value="headblowing">head blowing</option>
	<option value="worthadetour">worth a detour</option>
	<option value="somnolent">somnolent</option>
	<option value="thepits">the pits</option>
</select>
```
## Button
![[Pasted image 20231120133241.png]]
*hi dylan*

---
## Additional `<input>` types and attributes
| Element |
| ------- |
| Date    |
| Email   |
| URL     |
| Number  |
| Range   |
| Color   |
| Pattern (regular expression)|

Different browsers may handle each of these differently

| Attribute | use                             |
| --------- | ------------------------------- |
| Required  | Results in automated validation |
| Autocomplete | can be used to specify whether the browser should remember and suggest previously filled in data                                |
