#CM1102 #raw  #ToNeaten 
## Two Assessments this semester
Coursework (40%), consisting of two parts
-  creating a small static website using HTML and CSS only
-  creating a small dynamic website using HTML, CSS and a Python CGI script
Plus 30 minute test (10%)

Other 50% is done by another lecturer next semester

---
# How the internet came about
`1969` The arpanet
*Created by academics and researchers to make communicating across long distance. This was when computers were massive. Before the only way to send information was to send stuff via mail between the centres.*

*Used phone lines*
![[CM1102_week05_2_background.pdf#page=4|CM1102_week05_2_background, page 4]]
``
`1983` TCP/IP
*Mostly used for emails so was very basic*

`1990s` FTP
*File upload and download*
`1990s` USENET
*Discussion groups were also formed*
`1990s` Gopher
*A texted based information system*
### The internet in the early 1990s
- Mainly text based
- Non-profit
- For the happy few

`1999` World Wide Web
*Created by Tim Berners Lee. Created for easier communication at CERN. Hypertext, which allowed for the creation of web pages*
## Foundations of the internet
[[Packet Switching]]
[[TCP-IP]]
[[Telnet]]
[[FTP]]
[[SMTP]]
[[Hypertext]]
## Building Blocks of the Web
[[HTML]]/[[CSS]]
[[HTTP]]
[[Web Server]]
[[Browser]]

### HTML
```html
<!DOCTYPE html>
<html>
<head>
	<title> Hello There </title>
</head>
<body>
	<h1>Hello There</h1>
	<p> Welcome to the <a href="http://www.w3.org"> Web</a>.
	Some protocols:</p>
	<ul>
		<li> HTTP </li>
		<li> FTP </li>
		<li> SMTP </li>
	</ul> 
</body>
</html>
```
### HTTP
***HyperText Transfer Protocol***
A protocol that governs how the browser communicates with the server
### Web Server
![[CM1102_week05_2_background.pdf#page=25|CM1102_week05_2_background, page 25]]
### Browsers and layout engines
We will be using google chrome for testing stuff, on windows.
![[CM1102_week05_2_background.pdf#page=26&selection=0,0,0,27|CM1102_week05_2_background, page 26]]

---
Netscape is a really old browser
## Current Standards
**[[HTLM 5]]** for specifying the *structure* of a page
[[CSS]] for specifying the *layout* of a page

---
# Web Text File Format
## Plain Text File Format
Each letter has a code.
Example below using [[ASCII]]
![[Pasted image 20231031115939.png]]
![[Pasted image 20231031120056.png]]
## New line conventions
Unix and linux: `LF`
Dos and Windows: `CR+LF`
Apple Mac (up to OS-9): `CR`
![[CM1102_week05_3_textfiles.pdf#page=7|CM1102_week05_3_textfiles, page 7]]

#ToDo 8-Bit from next slide
#ToDo ISO 8859
## Roundup ISO 8859
| Advantages                                                               | Disadvantages                                                                          |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| 1. Does not require any additional space (ascii doesn't use the 8th bit) | 1. what if the same page needs several languages?                                      |
| 2. Relatively simple (once you know the code page)                       | 2. what about languages with more than 128 special characters (Chinese, Japanese, ...) |

## Unicode
Assigns every character a unique number *code point*
`Note:` Numbers 0-255 correspond with ISO 8859-1 character set (which includes ASCII)
Unicode by itself doesn't say anything about how things are encoded at byte level!

UCS-2: just use 2 bytes for each code point (instead of 1 just for ASCII/ISO-8859) Disadvantages:
-  it's not backward compatible with ASCII
-  Unicode now has more than 65t code points
-  it's generally considered obsolete (don't use it!)

UTF-8: use 1 byte if it's an ASCII character and multiple bytes if it's not (using a clever way of encoding that also specifies the length of multiple byte characters)
Advantages:
-  it's backward compatible with ASCII
-  can handle all Unicode code points
-  it's becoming the standard on the Web
![[CM1102_week05_3_textfiles.pdf#page=19&selection=0,23,0,23|CM1102_week05_3_textfiles, page 19]]

## Takeaway
Unicode with UTF-8 is usually the safe option (recommended as default encoding by W3C)

If you're writing your pages in just a single European language, using an ISO 8859 encoding will give you a small efficiency gain (each character is just 1 byte)

If you're planning to use just ASCII characters, it doesn't matter whether you're using ISO 8859 or UTF-8 because it's all the same!

Make sure your editor saves your file in the right format!
# How To Recognise Character Encoding
1) Guessing, based on a statistical analysis of the file contents (not recommended)
2) “Byte Order Mark” at the beginning of the file (like EF BB BF for UTF-8) (not recommended)
3) In the HTTP header: Content-Type:
	`text/html; charset=utf-8`
	(or us-ascii, iso-8859-1, iso-8859-2, etc.)
	*You'd need to configure your web server to do this.*
4) In the HTML file itself:
	`<meta charset=”utf-8”>`
	(or us-ascii, iso-8859-1, iso-8859-2, etc.)
# What plain text does not encode
- Any particular font
- Any particular particular font size
- Any special formatting
- Any particular colouring scheme

**HTML Requires plain text**
it makes use of markup to indicate special formatting:

```html
HTML uses markup tags to indicate structure or special formatting. <i>This text is displayed in italics</i> whereas <b>this text is displayed bold.</b>
```
HTML uses markup tags to indicate structure or special formatting. <i>This text is displayed in italics</i> whereas <b>this text is displayed bold.</b>

```html
HTML uses markup tags to indicate structure or special formatting. <em>This text is to be emphasized</em> whereas <strong>this text is to be strongly emphasized.</strong>
```
HTML uses markup tags to indicate structure or special formatting. <em>This text is to be emphasized</em> whereas <strong>this text is to be strongly emphasized.</strong>

---
# HTML
*HTML: Hypertext Markup Language*
specifies the structure of the document
	(e.g. where do the paragraphs start and end, and what are the section titles)
We use HTML 5 and CSS 3
# CSS
*CSS: Cascading Style Sheets*
specifies how to display the HTML document
	(e.g. use 11pt font size for paragraphs and 18pt font size for section titles)
## Key concepts
### Tags:
`<html>, </html>, <title>, </title>, <br>, …`
### Attributes/values
`<meta charset=”utf-8”>`
### Elements
`<title>An Example Page</title>`
### Nested Elements
`<body><p>Hello World!</p></body>`
### Empty Elements
`<br/> <meta charset=”utf-8”/>`
# Using HTML
```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<title>An Example Page</title>
</head>
<body>
	<p>Hello world!<br/>How are you?</p>
</body>
</html>
```

Note: HTML uses whitespace collapse.
## `<head>`element
Contains meta data about the document such as the character set, the title (to be displayed in the browser tab) the author, etc.
## `<body>` element:
contains the actual contents of the document such as text, hyperlinks, images, tables, etc.

Within the body:
## Block Elements
Block Elements start on a new line, and are preceded and followed by a blank line.

```html
<p> paragraph
<h1> level 1 heading
<h6> level 6 heading
<pre> preserve white space and line breaks
<blockquote> quotation (usually also indented)
<table> table
<form> form to be filled in by user
<div> generic block element
```

`<header>, <footer>, <nav>, <aside>, <section>, <article>` these display the same as `<div>` but are useful for describing the role of the text in the document (HTML 5 semantic elements)
## Inline Elements
Inline Elements continue on the same line
```html
<em> emphasis (usually displayed in italics)
<strong> strong emphasis (usually displayed in bold)
<cite> citation (source of information, usually italics)
<code> computer code (usually monotype spacing)
<q> inline quote
<span> generic inline element
```
more examples (inline explicit style elements):
```html
<b> boldface
<i> italics
<small> smaller than adjacent text (for “fine print”)
<sub> subscript (like H2O)
<sup> superscript (like E=MC2)
```
## Empty Elements
Empty elements do not have a sperate closing tag
```html
<br/> line break
<hr/> horizontal line
<img/> image
```
## Comments
```html
<!-- this is a HTML comment -->
```
## Example
```html
<h1> Chapter 1 </h1>
<h2> Introduction </h2>
	<p> Here comes the introduction. </p>
<h2> Next section </h2>
	<p> Some more text. </p>
<h3> First Subsection </h3>
	<p> Even more text </p>
<h3> Second Subsection </h3>
	<p> Still more text </p>
```
## Lists
```html
<p>Unordered list:</p>
<ul>
	<li> apples </li>
	<li> pears </li>
	<li> bananas </li>
</ul>
```
```html
<p>Ordered Lists:</p>
<ol>
	<li> apples </li>
	<li> pears </li>
	<li> bananas </li>
</ol>
```
Description Lists
![[Pasted image 20231101113450.png]]
Nested Lists
![[Pasted image 20231101113524.png]]
## Images
The `<img/>` element includes an image into a page (this is an empty element, so no closing tag)
```html
<img src="uni_logo.png" alt="Cardiff Uni Logo"/>
```
Required attributes:
1.  `src` attribute specifies the file containing the image
2.  `alt` attribute specifies the text to be displayed if the image is not displayed

You can use the `height` and `width` attributes to specify the image size in pixels.
	Advantage: browser already knows how much space to allocate to the image (so no need to resize after the image is loaded.
	It is possible to use the height and width attributes to display the image bigger or smaller than its actual size. This is usually not a good idea (why?)
```html
<p>Here's the logo of Cardiff University:
<img src="uni_logo.png" alt="Cardiff Uni Logo" Height="100" width="100"/>
</p>
```
### Common image formats
GIF – Graphics Interchange Format (.gif)
-  Pixel based
-  Up to 256 colours (8 bits, not good for photos)
-  Lossless compression (good for drawings) - Options for transparency and animation (GIF89A)
PNG – Portable Network Format (.png)
-  Pixel based - up to 24 bit colours
-  Lossless compression (good for drawings)
JPEG – Joint Photographic Experts Group(.jpg/.jpeg)
-  Lossy compression (image gets “approximated”)
-  Image quality depends on level of compression
-  Suitable for photos, less for drawings
SVG – Scalable Vector Graphics (.svg)
-  Vector based
-  No loss of quality when resizing
## Links
The anchor element (`<a> … </a>`) provides hypertext links between
-  different documents (using a URL)
-  different parts of the same document (using id attribute)
```html
<p> Wales' biggest university is
<a href="http://www.cardiff.ac.uk">Cardiff University</a>.
</p>
```
### Absolute vs Relative Addressing
#### Absolute address:
`href="http://www.cs.cf.ac.uk/index.html"`
*(suitable for links to external sites)*
#### Relative address:
`href="index.html" or href="../index.html"`
*(suitable for links to pages on the same site)*
## Relative linking
![[Pasted image 20231101114825.png]]
## Internal Links
![[Pasted image 20231101114915.png]]

You can, of course, use images for the links
## Thumbnails
Display a small image on a page, and give users the option of displaying a bigger version by clicking on it. `target="_blank"` opens the image (or document) in a new browser window or tab
```html
<a href= "big_version.jpg" target="_blank">
	<img src="small_version.jpg" alt="photo" width="80" height="80" />
</a>
```
## Tables
Tables are divided into rows and columns, cells can contain text, links, images etc.
```html
<table> main element
	<tr> tables row       (inside <table> element)
		<th> table header (inside <tr> element)
		<td> table data   (inside <td> element)
```
### *examples:*
```html
<table border="0"> <tr> <th> </th> <th> area </th> <th> population </th> </tr> <tr> <th> Wales </th> <td> 8t </td> <td> 3.1M </td> </tr> <tr> <th> England </th> <td> 50t </td> <td> 53.0M </td> </tr> <tr> <th> Scotland </th> <td> 30t </td> <td> 5.3M </td> </tr> </table>
```
<table border="0"> <tr> <th> </th> <th> area </th> <th> population </th> </tr> <tr> <th> Wales </th> <td> 8t </td> <td> 3.1M </td> </tr> <tr> <th> England </th> <td> 50t </td> <td> 53.0M </td> </tr> <tr> <th> Scotland </th> <td> 30t </td> <td> 5.3M </td> </tr> </table>

---
```html
<table border="1">
	<tr>
		<th> </th>
		<th scope="col"> area </th>
		<th scope="col"> population </th>
	</tr>
	<tr>
		<th scope="row"> Wales </th>
		<td> 8t </td>
		<td> 3.1M </td>
	</tr>
	<tr> 
		<th scope="row"> England </th>
		<td> 50t </td>
		<td> 53.0M </td>
	</tr>
	<tr>
		<th scope="row"> Scotland </th>
		<td> 30t </td>
		<td> 5.3M </td>
	</tr>
</table>
```
<table border="1">
	<tr>
		<th> </th>
		<th scope="col"> area </th>
		<th scope="col"> population </th>
	</tr>
	<tr>
		<th scope="row"> Wales </th>
		<td> 8t </td>
		<td> 3.1M </td>
	</tr>
	<tr> 
		<th scope="row"> England </th>
		<td> 50t </td>
		<td> 53.0M </td>
	</tr>
	<tr>
		<th scope="row"> Scotland </th>
		<td> 30t </td>
		<td> 5.3M </td>
	</tr>
</table>
`note`: Scope is used for accessibility

---
![[Pasted image 20231101120129.png]]
### Other table elements
the `<caption>` element puts a title above the table

table header row can be wrapped in `<thead>`
table footer row can be wrapped in `<tfoot>`
main part of table can be wrapped in `<tbody>`
`<thead>, <tfoot>` and `<tbody>` are only for semantic annotation and for applying CSS to rows

`<colgroup>` supports applying CSS to several columns its attribute span indicates how many columns

`<col/>` is an empty element, used inside of `<colgroup>` to apply CSS to one or more columns (using attribute span)

`<table border="1">` is old way of setting a border of width 1 around the cells; nowadays people tend to use CSS instead