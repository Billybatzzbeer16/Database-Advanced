# Database-Advanced

## How to use
1. Install the following libraries:
You can install these by copy pasting the code between the brackets in your ubuntu terminal.
  - BeautifulSoup (sudo apt-get install python-beautifulsoup)
  - pandas (sudo apt-get install python-pandas)
  - Requests (sudo apt-get install python-requests)
  - Pymongo (sudo apt-get install python-pymongo)
  
2. import the following libraries:
  - BeautifulSoup
  - Pandas
  - Requests
  - Time
  - Pymongo

3. Click run

## Making of
### Week 15/02/2021
I started off with installing a virtual machine and Ubuntu on it. I used VirtualBox for this task because we already used it in information security in the first year. After that I had to install python on the VM which wasn't that difficult. The installation of libraries however was a bit more complicated because I couldn't get pip to work so I had to find a different way to install libraries. After figuring this out I could begin on the actual task. I ran into some troubles with finding the right class to scrape. I thought it was easier to scrape the whole table of things I needed but this wasn't easy at all. I then decided to make different variables for each of the needed values. The problem was that the amount had the same class so I had to split them up by myself. I did this by using a for loop and checked if the value contained the word BTC. If so I putted them in a list of amount in Bitcoin and the others in amount in USD. The problem I ran in to however was that the word of the object would always be appended as well. I Solved  this by appending substrings. After this I placed all this data in a data variable and added it to a pandas data frame. To get the largest amount in USD I sorted the data frame on Amount of BTC because if I did this on Amount of USD the comma's would mess things up. A solution could be to replace the comma's but this would take to much time so I decided to do sort on BTC because if the USD go higher the amount of bitcoin should go up as well. After this I placed all of this in a function and this function in a timer which makes the function run every 60 seconds as requested.

### week 22/02/2021
Things weren't' as difficult as the first time. This was the case because we had the code wee needed to modify already, where as last week we had to start from scratch. Never the less I still had some struggling with the data I had to sent to the mongo database. First I tried to sent the pandas dataframes first line trough butt this wasn't possible. Then I decided to make this same dataframe line into a list. I did this by using a bit of hardcoding just to see if it worked. When I found out it did all I had to do was write a loop to automise the proces and then I was done.
