# animated-win-background
Python script for animated backgrounds on Windows
<h1>Usage</h1>
After downloading the project:

1. Split animated image into frames. If the image is a GIF, use http://www.ezgif.com/split.
2. Delete images in <i>frames</i> folder of project (sample images).
3. Copy frames into <i>frames</i> folder of project.
4. Run <b>animate.py</b>
5. To stop the animation, close the script. 

If you don't have Python installed, you can download it [here](https://www.python.org/downloads/).

NOTE: If you encounter performances issues, use less frames and/or increase the shuffle interval. To do this, change 0.15 to the amount of seconds you want in <b>animate.py</b>.

<h1>How it works</h1>
It's essentially an implementation of a background shuffler. The methods in <b>background_shuffler.py</b> simply change the background at a given time interval. By reducing this time interval to <1s, an animated background effect is achieved. 

<h1>See it in action</h1>
http://i.imgur.com/muPAAEs.gif

<h1>Sample GIFs</h1>
Here are some .gif files that make for good backgrounds. Feel free to add any.

1. [Pixel art backgrounds](http://imgur.com/gallery/GPlx4)
2. [Dancing cat](http://24.media.tumblr.com/34236728900b726b198ab8e802182513/tumblr_mfxf0w364J1rqb8h7o1_500.gif)
