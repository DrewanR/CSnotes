---
tags:
  - Programming
  - HTML
  - Web
Language: "[[HTML]]"
---
#ToNeaten 
## Tables
Tables are divided into rows and columns, cells can contain text, links, images etc.
```html
<table> main element
	<tr> tables row       (inside <table> element)
		<th> table header (inside <tr> element)
		<td> table data   (inside <td> element)
```
### *examples:*
```html
<table border="0">
	<tr>
		<th> </th>
		<th> area </th>
		<th> population </th>
	</tr>
	<tr>
		<th> Wales </th>
		<td> 8t </td>
		<td> 3.1M </td>
	</tr>
	<tr>
		<th> England </th>
		<td> 50t </td>
		<td> 53.0M </td>
	</tr>
	<tr>
		<th> Scotland </th>
		<td> 30t </td>
		<td> 5.3M </td>
	</tr>
</table>
```
<table border="0"> <tr> <th> </th> <th> area </th> <th> population </th> </tr> <tr> <th> Wales </th> <td> 8t </td> <td> 3.1M </td> </tr> <tr> <th> England </th> <td> 50t </td> <td> 53.0M </td> </tr> <tr> <th> Scotland </th> <td> 30t </td> <td> 5.3M </td> </tr> </table>

---
```html
<table border="1">
	<tr>
		<th> </th>
		<th scope="col"> area </th>
		<th scope="col"> population </th>
	</tr>
	<tr>
		<th scope="row"> Wales </th>
		<td> 8t </td>
		<td> 3.1M </td>
	</tr>
	<tr> 
		<th scope="row"> England </th>
		<td> 50t </td>
		<td> 53.0M </td>
	</tr>
	<tr>
		<th scope="row"> Scotland </th>
		<td> 30t </td>
		<td> 5.3M </td>
	</tr>
</table>
```
<table border="1">
	<tr>
		<th> </th>
		<th scope="col"> area </th>
		<th scope="col"> population </th>
	</tr>
	<tr>
		<th scope="row"> Wales </th>
		<td> 8t </td>
		<td> 3.1M </td>
	</tr>
	<tr> 
		<th scope="row"> England </th>
		<td> 50t </td>
		<td> 53.0M </td>
	</tr>
	<tr>
		<th scope="row"> Scotland </th>
		<td> 30t </td>
		<td> 5.3M </td>
	</tr>
</table>
`note`: Scope is used for accessibility

---
![[Pasted image 20231101120129.png]]
### Other table elements
the `<caption>` element puts a title above the table

table header row can be wrapped in `<thead>`
table footer row can be wrapped in `<tfoot>`
main part of table can be wrapped in `<tbody>`
`<thead>, <tfoot>` and `<tbody>` are only for semantic annotation and for applying CSS to rows

`<colgroup>` supports applying CSS to several columns its attribute span indicates how many columns

`<col/>` is an empty element, used inside of `<colgroup>` to apply CSS to one or more columns (using attribute span)

`<table border="1">` is old way of setting a border of width 1 around the cells; nowadays people tend to use CSS instead