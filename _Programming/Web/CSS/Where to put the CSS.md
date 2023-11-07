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