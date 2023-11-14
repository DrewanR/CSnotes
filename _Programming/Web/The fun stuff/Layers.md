## Layers
The browser maintains a stack of layers, this dictates whats rendered 'above' what.
`z-index` specifies this layer, higher numbers being the above layers.

![[Pasted image 20231113152439.png]]

```html
<body>
<div style="z-index:2; left:100px; top:50px; position:absolute; background-color:red; font-size:30pt">
<p>THIS STUFF IS ON TOP</p>
</div>
	
<div style="z-index:1; left:10px; top:10px; position:absolute; background-color:yellow; font-size:56pt">
<p>BACKGROUND STUFF</p>
</div>
</body>
```

