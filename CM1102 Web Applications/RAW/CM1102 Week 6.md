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
