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