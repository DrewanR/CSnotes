## Positioning
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