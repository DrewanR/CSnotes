# CSS
Cascading Style Sheets
Specify how to display the HTML document
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
# Where to put the CSS
**INLINE** in an individual element using the style attribute.
```html
<p style=”color: blue; font-family: sans-serif;”> example </p>
```

In an **INTERNAL STYLE SHEET** inside of the `<style>` element within the `<head>` of the file.
```html
<style>
	p {color: blue; font-family: sans-serif;}
</style>
```

In an **EXTERNAL STYLE SHEET** in a separate file referenced by a `<link>` element. <-- Bestest
```css
p {color: blue;
   font-family: sans-serif;}
```
## Invoking an external style sheet
CSS is contained within an external file

The HTML file should then contain a link:
```html
<link rel=”stylesheet” type=”text/css” href=”mystylesheet.css”/>
mystylesheet.css is the name of the external file
```
-  `rel` specifies the type of link being used
-  `type` specifies the MIME (Multipurpose Internet Mail Extensions) / IMT (Internet Media Type) of this file
-  `text/css` specifies “cascading style sheets” text
-  `href` specifies where to find the file
# Selectors
Selectors are used for internal and external style sheets (but not for inline CSS) Some of the most useful selectors:
-  type selector `p`
-  class selector `.blah`
-  id selector `\#blah`
-  child selector `p > em`
-  descendant selector `p span`
-  adjacent sibling `h1+p`
-  general sibling `h1~p`

view [[CM1102_week06_1_CSS.pdf#page=7|CSS Part 1, part 7...]] for nicer examples than I can provide here.
## Type selectors
Type selectors apply to a particular type of element (e.g. h1, p or em).
```html
<h1> Main Attractions </h1>
<p> <em>Splott Beach</em> and
	<em>Splott Market</em> are the main attractions in Splott
</p>
```
```css
h1,p { color: red; }
em { color: blue; }
```
![[Pasted image 20231106173651.png]]
## Class selectors
Class selectors apply to elements whose class attribute has a particular value.
`Note:` classes ***all*** start with a `.`
```html
<ul> <li class=”win”> MS Windows </li>
	 <li class=”unix”> Linux </li>
	 <li class=”unix”> FreeBSD </li> </ul>
<p class=”unix”> Unix comes in many flavours. </p>
```
```css
li.win { color: red; }
li.unix { color: blue; }
.unix { font-style: italic; } <--- Applies to all .unix elements
```
![[Pasted image 20231106174102.png]]
## ID Selectors
ID selectors apply to the **unique** element whose ID attribute has a particular value.
```html
<ul> <li id=”win”> MS Windows </li>
	<li id=”linux”> Linux </li>
	<li id=”freebsd”> FreeBSD </li> </ul>
```
```css
#linux {color: red; }
```
![[Pasted image 20231106174403.png]]
## Child Selector
Child selectors apply to the children (direct sub-elements) of a particular element.
```html
<ul> <li> Windows </li>
	<li> <em>Linux</em> </li>
	<li> FreeBSD </li> </ul>
<p> <em>Unix</em> comes in many flavours. </p>
```
```css
li>em {color: red; }
```
![[Pasted image 20231106174553.png]]
## Descendant Selector
Descendant selectors apply to the descendants (children, children’s children, etc) of a particular element.
```html
<ul> <li> Windows </li>
	<li> <em>Linux</em> </li>
	<li> FreeBSD </li> </ul>
<p> <em>Unix</em> comes in many flavours. </p>
```
```css
ul em {color: red; }
```
![[Pasted image 20231106174553.png]]
## Adjacent Sibling Selector
Adjacent sibling selectors apply to the first sibling (child of the same parent) of a particular element.
```html
<h1> Transport </h1>*
<p> Take bus 11 towards Pengam Green. </p>
<p> Alternatively, just walk. </p>
```
```css
h1+p {color: red; }
```
![[Pasted image 20231106175204.png]]
## General Sibling Selector
General Sibling Selectors General sibling selectors apply to any subsequent sibling of a particular element.
```html
<h1> Transport </h1>*
<p> Take bus 11 towards Pengam Green. </p>
<p> Alternatively, just walk. </p>
```
```css
h1~p {color: red; }
```
![[Pasted image 20231106175314.png]]

---
# Properties

## Fonts:
```css
font-family: <family name> [<generic family>]
font-style: normal|italic|oblique
font-weight: normal|bold|bolder|lighter
font-size: small|medium|large|smaller|larger
```
## Colours and backgrounds for text:
```css
color: <value>
background-color: <value> | transparent 
background-image: URL | none
(URL notation: url(“selfie.jpg”)
```
## CSS Font Family
`font-family` can be given multiple alternative values.

`body { font-family: Verdana, Arial, sans-serif;}`
In the above example:
1. The browser first looks for the Verdana font
2. If this is not on the system, it looks for the Arial font
3. Last resort: browser uses a generic sans-serif font
### Generic font classes
<div style = "font-family: serif"> serif </div><div style = "font-family: sans-serif"> sans-serif </div><div style = "font-family: monospace"> monospace </div><div style = "font-family: cursive"> cursive </div><div style = "font-family: fantasy"> fantasy (boo you dont have cool text theme)</div>
`note:` as you can see above, not all of these are universally availiable
## Text
```css
text-decoration: none|underline|overline|line-through
text-transformation: none|capitalize|uppercase|lowercase
text-align: left|right|center|justify
text-indent: length|percentage
```
## Sizing

## The CSS Box Model
```css
margin: width (e.g. 5px or 5%)
padding: width (e.g. 5px or 5%)
border-width: thin|thick|medium (or width units)
border-color: colour name or hex/rgb values
border-style: none|dotted|dashed|solid|double|groove| ridge|inset|outset
```

`margin-top, margin-right, margin-left, margin-bottom` exist as variants upon the margins. `Padding, border-width, border-color and border-style` also have this
![[Pasted image 20231106180611.png]]
# Size units for width
`px`: pixels (e.g. 5px)
`em`: related to font size (so 1em=12pt if the current font size is 12pt)
`ex`: related to font size (height of lowercase x)
`pt`: points (1/72 inch)
`pc`: pica (12 points)
`% `: percentage of the entire box width
## Shorthand
Shorthand for box widths of border, margin and padding:
1 value: all edges
	`margin: 10px;`
2 values: top+bottom, left+right
	`border-width: 10px 15px;`
3 values: top, left+right, bottom
	`padding: 4px 8px 10px; `
4 values: top, right, bottom, left (so clockwise from top)
	`border: 2px 4px 6px 8px;`
# List Styles
The bullets or counters can be set with
	`list-style-type: disc|circle|square|decimal|lower-alpha|upper-alpha| lower-roman|upper-roman`
To use a custom image
	`list-style-image: url(“mybullet.png”);`
To remove bullets or counters entirely:
	`list-style: none;`
# CSS Event Pseudo-Classes
CSS can detect a few basic mouse events. `:hover` and `:active` also work on other non-link elements.
```css
a:link { color: blue; }      Not yet visited
a:visited { color: purple; } Already visited
a:hover {color: green; }     Mouse goes over element
a:action {color: red; }      Element is being clicked
```
# Colour
As well as using hex codes, one can also make use of colour names.
```css
<body style=“background-color:#d2691e”>
<h1 style=“color:rgb(210,105,30)”>
```
```css
<body style=“background-color:gray; color:black;” >
```
http://www.w3schools.com/colors/colors_names.asp
# Multiple style sheets
is possible to specify multiple colour sheets:
```html
<head>
	<title>Stylesheets</title>
	<style>
		@import url(“http://www.abc.com/deptstyles.css”)
		@import url(“mystyles.css”)
	</style>
</head>
```
## *Cascading* style sheets
```
– mainstyles.css – the company's stylesheet
– deptstyles.css – the department's stylesheet
– mystyles.css   – the user's stylesheet
```
In the above example, when there are conflicting declarations, the user's style declarations (in `mystyles.css`) with override the previously declared two. This can result in the document being a mix of the 3 style sheets.

#### Other priorities
Highest
1. Inline styles (using the `style="..."` attribute in the html body)
2. Internal style sheets (in the `<style>` element)
3. External style sheets (note: later declarations override previous ones)

---
# HTML returns
## Divisions and spans
Rather than applying styles to an element itself, we wrap one or more elements in
-  a `div` (division) element (usually for block elements), or
-  a `span` element (usually for inline elements – part of a piece of text)

Any required formatting can then be applied to the `<div>` or `<span>` element.
-  each can have `class` and `id` attributes

The [[HTML5]] elements of `header, nav, article, section, aside, footer` can be regarded as divs with particular semantics.
# Divisions
Styles can be applied to blocks of HTML code using divisions.
```html
<head>
	<style> .myclass {
		color: blue;
		background: cyan;
		text-decoration: underline;
		border: thin groove red;
	}
	</style>
</head>
<body>
	<div class="myclass">
		<h2>A Simple Heading</h2>
		<p>some text . . . </p>
	</div>
</body>
```
<head>
	<style> .myclass {
		color: blue;
		background: cyan;
		text-decoration: underline;
		border: thin groove red;
	}
	</style>
</head>
![[Screenshot_20231113_150540.png]]
# Spans
Spans usually refer to a selected piece of text (inline).
```html
<head>
	<style> .myclass {
	color: red;
	background: cyan;
	text-decoration: none;
	}
	</style>
</head>
<body>
	<p>some text with <span class=“myclass”>an important bit</span>
	and the not so exciting stuff…
	</p>
</body>
```
![[Pasted image 20231113150730.png]]
# Positioning
```html
<style>
#mypara {position: absolute; <-- replace with psotioning type
	top: 5px;
	left: 5px;}
</style>
... ... ...
</head>
<body>
	<h1 class="headers"> Header number 1</h1>
	<p id="mypara"> here is a paragraph with some text </p>
```
#### `Absolute`
The values left and top are distances horizontally and vertically from the ***top left corner of the containing element.***
![[Pasted image 20231113151018.png]]
#### `Relative`
Values are relative to the top left of where the element would have been placed otherwise (with normal flow)
![[Pasted image 20231113151431.png]]
#### Note:
The values of top and left are relative to the containing element that has a position property set (other than to static).

By default the containing element is the `<body>` element.

To position relative to an element that is contained in the body or at some lower hierarchical level, the parent element must be given a position property, (irrespective of whether top or left are set):

`{position: relative; }`
# Layers
The browser maintains a stack of layers, this dictates whats rendered 'above' what.
`z-index` specifies this layer, higher numbers being the above layers.

![[Pasted image 20231113152439.png]]

```html
<body>
<div style="z-index:2; left:100px; top:50px; position:absolute; background-color:red; font-size:30pt">
<p>THIS STUFF IS ON TOP</p>
</div>
	
<div style="z-index:1; left:10px; top:10px; position:absolute; background-color:yellow; font-size:56pt">
<p>BACKGROUND STUFF</p>
</div>
</body>
```

# nth child
[[CM1102_week06_2_CSS.pdf#page=18&selection=0,25,2,14|CM1102_week06_2_CSS, page 18]]
# Columns
## 2 Columns
Left Column `nav`: fixed width W and floats left
Content Column `div`: liquid, i.e. no width specified (but has min width) - has left margin >= W

Both contained in Wrapper `div`

`<body>` set to have no margin or padding
```html
<header>
	<h1>Well Hello There</h1>
</header>
<div id="wrapper">
	<nav id="leftNavigation">
		<h2>Navigational</h2>
		<ul>
			<li>item 1</li>
			<li>item 2</li>
			<li>item 3</li>
			<li>item 4</li>
		</ul>
	</nav>
	<div id="contentcol">
		<h2> This really is the real thing< /h2>
		<p> somethingystuff about bla somethingystuff about bla…….. </p>
	</div>
</div>
```
```css
body { margin: 0; padding: 0;}

h1, h2 {font-family: Arial, sans-serif;}

#wrapper { width: 100%;}

header {
	width 100%;
	border: red 2px solid;
	background-color: #ffffaa;}

#leftNavigation {
	width: 10em;
	float: left;
    border: dashed silver 2px;
    padding:0;}

#contentcol {
	padding: 0;
	margin-left: 10em;
    border: dashed silver 2px;
    min-width: 10em;}
```
![[Pasted image 20231114110421.png]]
## Float property
The `float` property causes an element to move to the left or right of its containing element.

Text that follows the floating element will wrap around it.

A block element that follows a floating element will not force a new line (unless the clear property is set)
```html
<header>
	<h1>Well Hello There</h1>
</header>
<div id="wrapper">
	<nav id="leftNavigation">
		<h2>Navigational</h2>
		<ul>
			<li>item 1</li>
			<li>item 2</li>
			<li>item 3</li>
			<li>item 4</li>
		</ul>
	</nav>
	<div id="rightCol">
		<h2> I am Right </h2>
		Most interesting material of
		...
	</div>
	<div id="contentcol">
		<h2> This really is the real thing</h2>
		<p> somethingystuff about bla somethingystuff about blah</p>
		...
	</div>
</div>
```
```css
body { margin: 0; padding: 0;}
h1, h2 {font-family: Arial, sans-serif;}
header {width 100%; border: red 2px solid; background-color: #ffffaa;}

#wrapper{
	float: left;
	min-width: 30em;}
	
#leftNavigation {
	width: 10em;
	float: left;
	border: dashed silver 2px;
	padding:0 1em;}
	
#rightCol {
	width: 10em;
	float: right;
	border: dashed silver 2px;
	padding: 0 1em;}

#contentcol {
	background-color: #ccffff;
	padding: 0 1em;
	margin: 0 12em 0 12em;
	border: dashed silver 2px;
	min-width: 5em;}
```
Here left and right columns are fixed width left floats to left; right floats to right 

Content column liquid with min-width (could also be fixed) its left and right margins extend across full width of the left and right columns

**IMPORTANT:** *the floating div elements for the left and right columns must appear in the HTML doc **before** the content div – so that they can claim their space.*
![[Pasted image 20231114112139.png]]
