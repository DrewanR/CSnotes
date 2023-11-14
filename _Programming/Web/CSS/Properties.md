[[#Fonts:|Fonts:]]
[[#Colours and backgrounds for text:|Colours and backgrounds for text:]]
[[#CSS Font Family|CSS Font Family]]
[[#The CSS Box Model|The CSS Box Model]]
[[#Shorthand|Shorthand]]
[[#List Styles]]
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