Cascading Style Sheets
Specify how to display the HTML document
view [[_Using CSS]]
## Why
Cascading Style Sheets (CSS) are used to set how web content is displayed. This includes:
-  fonts, colours, backgrounds, borders, etc.
-  layout of content on a page (position, sizing, etc.)
-  Some aspects of interaction with elements (e.g. what happens on mouse-clicks)
# CSS Style Rules
```css
selector {
	property: value;
	property: value;
	property: value;
}
```

Consists of two parts:
	*A selector, A set of declarations*
## The selector
specifies which HTML element the style should be applied to
## The declarations
Specify how the selected elements should be displayed
consists of: *a property and a value*

EXAMPLE
```css
h1 {
	color: red;
	background-color: white;
}

p {
	color: blue;
	font-family: sans-serif;
}
```

