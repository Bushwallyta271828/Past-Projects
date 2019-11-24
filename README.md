# Past-Projects
## USACO Sample

These are my submissions to the third USA Computer Olympiad Platinum competition of the 2016-2017 season (when I was a freshman). The problem statements are included in each sub-folder. In this contest I scored a 478. The scores of everyone on this competition can be found at this link: http://www.usaco.org/current/data/feb17_platinum_results.html

## Grid of 1s

This code was written in response to a computer science challenge from David Lerner. The challenge was to take a grid of 0s and 1s and find how many different rectangles were filled only with 1s. I managed to find an algorithm which solved the problem in O(nm) time for an n by m grid.

## Speech Recognition Project

This was a project I once worked on for a friend's brother who was doing psychological research. I was given a large number of sound files of people saying single words and I had to identify the word and identify the milisecond when the word was first spoken. In the end, this proved rather problematic, and I do not believe the most recent version of the code (the one here) is working properly. 

## Schedule Management Code

This is a code project I built myself to try to get control over my schedule. For several years, I recorded in text files every subject I did and when I did it. For example, I could say:

<pre>start Task One @ 13:00
stop Task One @ 15:00
 + 35 minutes Task Two
start Task Three @ 17:00
 - 4 minutes
stop Task Three @ 19:00</pre>

and the program would tell me how many hours I worked that day and on what. In the end, the project got rather elaborate with several tools built to help me analyze my long-term work habits. Sadly, when I changed computer setups, a large part of the funcionality was broken due to badly configured python libraries. 

## Blackrock Castle Observatory Project

This was a project I did at Blackrock Castle Observatory, Cork, sifting through images of stars looking for exoplanet transits. I worked on two algorithms. The first algorihtm tried to intelligently determine which pixels contained light from the star and which were background, while the second algorihtm looked at the light given off by the star over time to try to group the lightcurve into blocks of similar output. The latter I implemented with a dyamic program to improve the runtime by a factor of the number of images. The code for these two algorithms (dynamic aperture and dynamic blocking, respectively) are contained in the other repositories on my github account:

https://github.com/Bushwallyta271828/Dynamic2

https://github.com/Bushwallyta271828/StarTracker

https://github.com/Bushwallyta271828/ClassifierNet

https://github.com/Bushwallyta271828/Classifier

## 2048

For this project, I attempted to write a computer program that would try to earn as many points as possible at 2048. I used a fairly elementary breadth-first-search of the state space combined with a hand-tuned heuristic that evaluated itself on every leaf node. The program would usually make it to the 2048 tile and often beyond, but it was no match for established 2048-playing programs.

## Computer Algebra System

This was a computer algebra system I tried to create, which could manipulate algebraic expressions and solve equations. This project was fairly successful, although its funcionality was limited and of course Wolfram Alpha is way better than it at everything.

## MEEP Project

I started this project to get some sense of how computational electrodynamics simulations work. I tried to find a shape made out of stitched-together cones that would focus light as much as possible from a large opening into a smaller one. I wrote a python function to evolve over the shape of the cone slices, and that python file called a computational electrodynamics simulator called MEEP with an interface in the Scheme language to compute how much light made it though. I was unable to achieve much success through the optimization algorithms, and in retrospect the problem of focusing light could have been better chosen. Still, I learned about how programs like MEEP and other discrete simulation software works and I also gained familiarity with many python optimization libraries.

## Past Papers

I've read most of these papers on machine learning: https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap
