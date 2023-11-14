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

---
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