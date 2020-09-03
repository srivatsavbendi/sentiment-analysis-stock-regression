# metaaiml.github.io
Crated by Srivatsav Bendi- August 2020

Meta AI is a Machine Learning stock prediction modeling website that uses a polynomial regression, allowing investors to easily predict small changes in the market. 

Inspiration- 
I started noticing that there were a lot of cyclic patterns in stock charts and I did some research and learned that data scientists have used ML regression models and the patterns found in stock charts to predict future stock prices for a couple of years now, and I wanted to create my own models to test if it could be profitable

What It Does- 
Essentially, Meta AI is a website with a database of some of the most trending stock right now. Using python and regression models that I've tuned, the website displays the most recent and accurate polynomial predictions of stock prices for these companies for the next few days

How I Built It- 
There were 3 major parts in building this hack. First, I had to build the actual regression model which was probably the hardest part. I had to research the different types of regression models, choose the one that worked best, and coded the arrays and CSV files that I had of stock data to be plotted on the model. Next, I took the predicted values and placed them in firebase in order to move it to my javascript-based website later. Since I'm well versed in HTML and CSS, the last part of creating the actual website was quite simple. It was just connected to the firebase realtime database for the text and pictures, and I made a quick aesthetic design
