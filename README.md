# Python-Final-Project

Link to Youtube: https://www.youtube.com/watch?v=Ou89_Ign2hM

Hi, this is our final project called Reddit AITA Analyzer by Ernest Wong and Stela Licheva.

Stela (me):

In this project, I learned how to screenscrape information from Reddit and complete a sentiment analysis then compile everything into a CSV file.
I am an avid AITA reader and have always been curious whether the information could be compiled to get an overall look of the comments rather
than reading them one by one. I learned how to use the Command line to install packages and then how to use PRAW for screenscraping and VADER for
sentiment analysis.

One trouble I had was determining how many comments to take in. The more comments screenscraped, the longer the run time. I also had trouble with the "NAH"
(no assholes here) category. Usually, people text nah as in no, which would be picked up as "NAH" for the count. I am also unsure of whether the
sentiment analysis was effective. Looking at the CSV, it wasn't able to detect the sarcasm in some comments and to whom the negative intonation was 
pointed.

Ernest:

In this project, I learned how to use HTML. We wanted a way to present the output of our python code and I found that the easiest way would 
probably be through using HTML. I learned how you can create a HTML file within python and I also learned how to format what you want to put
in the HTML as well as do things like changing the font size, bolding, etc. I also learned how you can make the html filed be opened when 
you run the python code.

However, one difficulty that I faced was making this work for everyone. In the code I have, it will only work on my computer as it is taking the
file path name and opening the html file through that. However, everyone's file path name will be different so I was unsure of how to make this
work for other people as well when running it on their computer.
