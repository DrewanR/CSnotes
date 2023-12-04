---
aliases: []
---
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

View [[__Using HTML|using HTML]] for explanations
View [[__HTML 5]] for things specific to it

---
### HTTP
***HyperText Transfer Protocol***
A protocol that governs how the browser communicates with the server ^155345

Uses [[Plain Text]]
Is made up of markup tags to indicate special formatting:

```html
HTML uses markup tags to indicate structure or special formatting. <i>This text is displayed in italics</i> whereas <b>this text is displayed bold.</b>
```
HTML uses markup tags to indicate structure or special formatting. <i>This text is displayed in italics</i> whereas <b>this text is displayed bold.</b>

```html
HTML uses markup tags to indicate structure or special formatting. <em>This text is to be emphasized</em> whereas <strong>this text is to be strongly emphasized.</strong>
```
HTML uses markup tags to indicate structure or special formatting. <em>This text is to be emphasized</em> whereas <strong>this text is to be strongly emphasized.</strong>

---
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

---
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