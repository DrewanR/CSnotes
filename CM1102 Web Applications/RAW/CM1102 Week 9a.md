[[linux.pdf]]
### THIS IS ABOUT UNIX, not so much linux
---
![[Pasted image 20231127121450.png]]
![[Pasted image 20231127121506.png]]
# Design Factors
- Freedom
- Performance
- Efficiency
- Security
- Reliability
- Usability
- Control
...
- Modularity, Simplicity, Elegance ... ?
# Monolithic Micro, Hybrid
![[Pasted image 20231127122238.png]]
![[Pasted image 20231127122728.png]]
Dont use telnet

https://refspecs.linuxfoundation.org/fhs.shtml
#ToDo learn to use symbolic links, they sound f###ing amazing

`mount` 
`df` disk free
`du` disk usage

![[Pasted image 20231127124348.png]]
`ls   ` list contents of directory; long (-l); all (-a)
`cd   ` change directory
`pwd  ` print working directory
`cp   ` copy file/directory (-r)
`mv   ` move file
`ln   ` link to file; symbolic link (-s)
`rm   ` remove file; directory (-r); forced (-f)
`mkdir` make directroy; hierarchy (-p)
`cpio ` copy files to/from archives, including between directories (-pdvmua)
`cat  ` concatenate files
`sort ` sort data
`find ` find files
`grep ` show matching lines
`sed  ` stream editor
`awk  ` pattern scanning and processing
`vi   ` visual editor (vim)
`man  ` view manual page `<-- OMG I HAVE BEEN LOOKING FOR THIS FOR SO LONG`

![[Pasted image 20231127125624.png]]
# UNIX philosophy
### Programs should:
> Do one thing
> Do it well
> Work together
> Process text streams
#### Worse is better
> Make it work, not perfect - perfection is usually ill-defined
> Let the user fix it, even if it's complex - they are not dumb
> Share the code freely (not fake openly) - at least it can be fixed
#### UIs
> Shells have a steep learning curve - at least there is one
> Using and programming are equivalent - greed says otherwise
> GUIs can deceive (\*), depend on culture ( ), and mostly fail:
> 	 - limited interoperability, automation, concurrency, accuracy/precision, choice
#### Over-engineering/abstraction/design
> Only creates limits
> Failure of OOP
#### Freedom
> Who controls/owns the box? — your (collective) choice

![[Pasted image 20231127125608.png]]