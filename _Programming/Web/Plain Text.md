Each letter has a code.
Example below using [[Pasted image 20231031120056.png|ASCII]]
![[Pasted image 20231031115939.png]]
## New line conventions
Unix and linux: `LF`
Dos and Windows: `CR+LF`
Apple Mac (up to OS-9): `CR`
![[CM1102_week05_3_textfiles.pdf#page=7|CM1102_week05_3_textfiles, page 7]]

## 8 Bit Encoding
ASCII uses 7-bit codes (128 Characters), because of this ASCII only does English characters.
To fix this, the ISO 8859 standard was invented.

**The Concept:**
Put a language specific encoding atop ASCII to use the full 8 bits, doubling the available characters to 256. Values 0-127 were standard ASCII, and 128-256 were used for the current non-English alphabet. View [[CM1102_week05_3_textfiles.pdf#page=10|Diagram]].
## Roundup ISO 8859
| Advantages                                                               | Disadvantages                                                                          |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| 1. Does not require any additional space (ascii doesn't use the 8th bit) | 1. what if the same page needs several languages?                                      |
| 2. Relatively simple (once you know the code page)                       | 2. what about languages with more than 128 special characters (Chinese, Japanese, ...) |

## Unicode
Assigns every character a unique number *code point*
`Note:` Numbers 0-255 correspond with ISO 8859-1 character set (which includes ASCII)
Unicode by itself doesn't say anything about how things are encoded at byte level!

UCS-2: just use 2 bytes for each code point (instead of 1 just for ASCII/ISO-8859) Disadvantages:
-  it's not backward compatible with ASCII
-  Unicode now has more than 65t code points
-  it's generally considered obsolete (don't use it!)

UTF-8: use 1 byte if it's an ASCII character and multiple bytes if it's not (using a clever way of encoding that also specifies the length of multiple byte characters)
Advantages:
-  it's backward compatible with ASCII
-  can handle all Unicode code points
-  it's becoming the standard on the Web
![[CM1102_week05_3_textfiles.pdf#page=19&selection=0,23,0,23|CM1102_week05_3_textfiles, page 19]]

## Takeaway
Unicode with UTF-8 is usually the safe option (recommended as default encoding by W3C)

If you're writing your pages in just a single European language, using an ISO 8859 encoding will give you a small efficiency gain (each character is just 1 byte)

If you're planning to use just ASCII characters, it doesn't matter whether you're using ISO 8859 or UTF-8 because it's all the same!

Make sure your editor saves your file in the right format!
# How To Recognise Character Encoding
1) Guessing, based on a statistical analysis of the file contents (not recommended)
2) “Byte Order Mark” at the beginning of the file (like EF BB BF for UTF-8) (not recommended)
3) In the HTTP header: Content-Type:
	`text/html; charset=utf-8`
	(or us-ascii, iso-8859-1, iso-8859-2, etc.)
	*You'd need to configure your web server to do this.*
4) In the HTML file itself:
	`<meta charset=”utf-8”>`
	(or us-ascii, iso-8859-1, iso-8859-2, etc.)
# What plain text does not encode
- Any particular font
- Any particular particular font size
- Any special formatting
- Any particular colouring scheme

**HTML Requires plain text**
it makes use of markup to indicate special formatting:

```html
HTML uses markup tags to indicate structure or special formatting. <i>This text is displayed in italics</i> whereas <b>this text is displayed bold.</b>
```
HTML uses markup tags to indicate structure or special formatting. <i>This text is displayed in italics</i> whereas <b>this text is displayed bold.</b>

```html
HTML uses markup tags to indicate structure or special formatting. <em>This text is to be emphasized</em> whereas <strong>this text is to be strongly emphasized.</strong>
```
HTML uses markup tags to indicate structure or special formatting. <em>This text is to be emphasized</em> whereas <strong>this text is to be strongly emphasized.</strong>
