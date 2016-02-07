# animated-win-background
Python script for animated backgrounds on Windows
<h1>Usage</h1>
1. Split animated image into frames. If the image is a GIF, use http://www.ezgif.com/split.
2. Copy images into <i>frames</i> folder of project.
3. Run 'animate.py'

NOTE: If you encounter performances issues, use less frames and/or increase the shuffle interval. To do this, change 0.15 to the amount of seconds you want in <color=blue>animate.py</color>.

<h1>How it works</h1>
It's essentially an implementation of a background shuffler. The methods in <color=blue>background_shuffler.py</color> simply change the background at a given time interval. By reducing this time interval to <1s, an animated background effect is achieved. 
