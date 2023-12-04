## Video & Audio
### Video
`<video>` and `<audio>` tags replace the need for 3rd party plugins.
```html
<video controls>
	<source src="CuteCat.mp4" type="video/mp4" />
	<source src="CuteCat.webm" type="video/webm" />
	<source src="CuteCat.ogv" type="video/ogg" />
</video>
```

You can insert multiple source files when embedding a video to get around compatibility issues.
File formats such as:
	MPEG4 (.[[MP4]]), WebM (.[[webm]]), OGG (.[[ogg]]), Flash (.[[flv]]) and AVI (.[[avi]])
are containers for a
1. Video track (or stream)
2. Audio track (or stream)
3. Metadata about the tracks

> **CODECS**
> Many ways to encode and decode video and audio (between analog and digital). Often includes lossy (or less likely) lossless compression
> *Video* H.264, Theora, VP8
> *Audio* MP3, Vorbis, AAC

| MPEG-4 (.mp4) | H.264 + AAC     | [[Chrome]], [[Firefox]], [[Internet Explorer]], [[Opera]], [[Safari]] |
| ------------- | --------------- | --------------------------------------------------------------------- |
| OGG           | Theora + Vorbis | [[Chrome]], [[Firefox]], [[Opera]]                                    |
| WebM          | VP8 + AAC       | [[Chrome]], [[Firefox]], [[Opera]]                                    | 

```html
<video src="CuteCat.webm"
	   type="video/webm"
	   width="500" height="480" controls >
</video>
```
`Width` and `height` self explanatory
`Controls` provides the control buttons
`Autoplay` determines whether the video will play automatically
`Type` Tells the browser the format
### Audio
```html
<audio controls>
	<source src="DogBarking.mp3" type="audio/mp3" />
	<source src="DogBarking.ogv" type="audio/ogg" />
</audio>
```