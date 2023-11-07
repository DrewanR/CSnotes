## Adjacent Sibling Selector
Adjacent sibling selectors apply to the first sibling (child of the same parent) of a particular element.
```html
<h1> Transport </h1>*
<p> Take bus 11 towards Pengam Green. </p>
<p> Alternatively, just walk. </p>
```
```css
h1+p {color: red; }
```
![[Pasted image 20231106175204.png]]