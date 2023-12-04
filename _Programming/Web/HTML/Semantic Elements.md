## Semantic Elements
```html
<header>  Banner/header at the begining of the page or section of a page
<footer>  Wraps a footer, i.e.
<nav>     A section that contains navigational material
<section> A logically related part of a web page
<article> A relatively independent piece of a content, such as blog entry or news
<aside>   Content seperate from main content, typically a side bar
```
### Time
Specifies a date as `"YYYY-MM-DD"` or `YYYY-MM-DDThh:mm±hh:mm` where `±hh:mm` is a time zone
```html
<time datetime="2012-12-26"> 26th December 2012 </time>
<time datetime="2012-12-26T10.30+00:00">|26th December 2012 at 10.30 GMT</time>
<time datetime="2012-12-26T10.30Z"> 26th December 2012 at 10.30 GMT </time>
```