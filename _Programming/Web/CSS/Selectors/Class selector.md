## Class selectors
Class selectors apply to elements whose class attribute has a particular value.
`Note:` classes ***all*** start with a `.`
```html
<ul> <li class=”win”> MS Windows </li>
	 <li class=”unix”> Linux </li>
	 <li class=”unix”> FreeBSD </li> </ul>
<p class=”unix”> Unix comes in many flavours. </p>
```
```css
li.win { color: red; }
li.unix { color: blue; }
.unix { font-style: italic; } <--- Applies to all .unix elements
```
![[Pasted image 20231106174102.png]]