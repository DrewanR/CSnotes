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