## Child Selector
Child selectors apply to the children (direct sub-elements) of a particular element.
```html
<ul> <li> Windows </li>
	<li> <em>Linux</em> </li>
	<li> FreeBSD </li> </ul>
<p> <em>Unix</em> comes in many flavours. </p>
```
```css
li>em {color: red; }
```
![[Pasted image 20231106174553.png]]