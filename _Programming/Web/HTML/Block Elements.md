---
tags:
  - Programming
  - HTML
  - Web
Language: "[[HTML]]"
---
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