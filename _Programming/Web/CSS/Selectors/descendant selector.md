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