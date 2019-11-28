#### Visualise snow depth on top of the floating sea ice in Antarctica [1992-2008]

Link to github repo with code: https://github.com/MridulS/antarctica-snow-on-ice

All the stars aligned perfectly and I was able to spend my birthday this year jumping into polar ice water in Antarctica
while some penguins and whales were cheering on the sidelines (not really, but it would have helped). I started reading about Antarctica, the history of exploration, the wildlife and the delicate system of sea ice around the continent.
A lot has been said and written about [effect](https://oceanservice.noaa.gov/facts/sea-ice-climate.html) [of](https://www.climate.gov/news-features/understanding-climate/understanding-climate-antarctic-sea-ice-extent) [climate change](https://www.nature.com/articles/s41467-018-07865-9) on the continent by researchers. I'll do what I like doing, so let's create a tiny little visualisation.

DISCLAIMER: I am not going to do any inference from this data because 1) I can't 2) I have pretty much zero domain knowledge about this so I shouldn't. I am just going to try to make a nice pretty animation of the evolution of *snow* on sea ice around Antarctica.

First thing to do was to collect some data and I stumbled upon https://neptune.gsfc.nasa.gov/csb/index.php?section=52
I chose snow on sea ice there is well detailed visualisation about sea ice available, https://github.com/vannizhang/sea-ice .

Extracting the bytearrays and creating heatmaps using matplotlib gave me this pretty visualisation about snow on sea ice from 1992 - 2008. Click on the image below to play the video.

[![animation](/images/1992001.png)](http://mriduls.github.io/antarctica-snow-on-ice/images/video.mp4)



Maybe a climate scientist can help me make sense of this?


##### Reproduce the video


Data from https://neptune.gsfc.nasa.gov/csb/index.php?section=52

- Download and extract the data. 

- Create images from individual day data using `python create_images.py` [python 3.7, matplotlib 3.1.1]

- Create a gif using `convert -delay 5 -loop 0 *.png animation.gif` in the images directory [tested on MacOS 10.14.5 , ImageMagick 7.0.8-59]

- Optionally create a MP4 video using `ffmpeg -i animation.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" video.mp4` in the images directory [tested on MacOS 10.14.5, ffmpeg version 4.2.1] (10x better compression)
