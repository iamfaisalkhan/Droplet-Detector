# Detecting Droplets using Computer Vision

## Introduction

A currently under development robotic sample changer at sector [12-ID-I](http://12id.xray.aps.anl.gov/) of Advanced Photon Source need to align the sample, in this case a tiny droplet dispensed from a pipette, that needs to centered with respect to the X-ray beam. This project automates that step by using Computer Vision based image segmentation approaches to automatically segment the shape and size of the droplet. This information is then used to compute the position of the dropet.

## Input Samples

The droplet is zoomed to 5-15x times of the original size using zoom lens. The first image shows the droplet no fully formed. The second image shows the droplet fully formed. 

<p align=center>
	<img src=samples/droplet_up_nolabel.jpg/>
</p>

<p align=center>
	<img src=samples/full_droplet_1.jpg/>
</p>

## Equipment

<p align=center>
	<img src=./equipment.jpg/>
</p>



## Results

<p align=center>
	<img src=./ellipse_Fit.png/>
</p>
