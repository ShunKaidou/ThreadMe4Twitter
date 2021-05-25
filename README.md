![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Threadme4T
A python bot that uses twitter API to GET mentioned tweets and send them as Direct messages to the one who tagged the bot. This project uses the tweepy library,also since tweepy doesnt support the Twitter API V2 we sometimes used the Twitter API directly without any Libraries. This isnt working as exactly as we needed(replies are also included along with threads, we coudnt remove it 😢) but everything else looks fine...

## Team members
1. <a href="https://github.com/ShunKaido">Mohammed Nihad</a> 
2. <a href="https://github.com/ilyazjasim">Mohammed illias Jasim V</a> 
3. <a href="https://github.com/Nihadk117">Abdul Nihad K</a> 

## Team Id
BFH/recdnAxglgpWDXQon/2021

## Link to product walkthrough
[link to video]

## How it Works ?
<ul>
 <li>The bot authenticates with Twitter API using the developer keys</li>
<li>it checks for mentions every 5 minutes</li>
<li>if it finds it executes a function to get data on both the user and the thread it is tagged in</li>
<li>then the thread data is sent to the user by Direct Message</li>
</ul>Yup that's the basic idea of it ,looking deeply there are things like creating a log and saving already processed data into it so the program wont repeatly resend tweets into already sent users , accessing the Secret Keys stored in a file etc, working with json  a bit, basic API Authentication etc... etc...
[Embed video of project demo]

## Libraries used
Tweepy - 3.10
requests - 2.25.1 (for accessing twitter API directly)

## How to configure
Clone github repository 
create virtualenv and activate 
install required files
## How to Run
Instructions for running
 
