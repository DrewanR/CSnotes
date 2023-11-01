---
tags:
  - Programming
  - HTML
  - Web
Language: "[[HTML]]"
---
## Images
The `<img/>` element includes an image into a page (this is an empty element, so no closing tag)
```html
<img src="uni_logo.png" alt="Cardiff Uni Logo"/>
```
Required attributes:
1.  `src` attribute specifies the file containing the image
2.  `alt` attribute specifies the text to be displayed if the image is not displayed

You can use the `height` and `width` attributes to specify the image size in pixels.
	Advantage: browser already knows how much space to allocate to the image (so no need to resize after the image is loaded.
	It is possible to use the height and width attributes to display the image bigger or smaller than its actual size. This is usually not a good idea (why?)
```html
<p>Here's the logo of Cardiff University:
<img src="uni_logo.png" alt="Cardiff Uni Logo" Height="100" width="100"/>
</p>
```
### Common image formats
GIF – Graphics Interchange Format (.gif)
-  Pixel based
-  Up to 256 colours (8 bits, not good for photos)
-  Lossless compression (good for drawings) - Options for transparency and animation (GIF89A)
PNG – Portable Network Format (.png)
-  Pixel based - up to 24 bit colours
-  Lossless compression (good for drawings)
JPEG – Joint Photographic Experts Group(.jpg/.jpeg)
-  Lossy compression (image gets “approximated”)
-  Image quality depends on level of compression
-  Suitable for photos, less for drawings
SVG – Scalable Vector Graphics (.svg)
-  Vector based
-  No loss of quality when resizing
## Thumbnails
Display a small image on a page, and give users the option of displaying a bigger version by clicking on it. `target="_blank"` opens the image (or document) in a new browser window or tab
```html
<a href= "big_version.jpg" target="_blank">
	<img src="small_version.jpg" alt="photo" width="80" height="80" />
</a>
```