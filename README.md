![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Threadme4T
A python bot that uses twitter API to GET mentioned tweets and send them as Direct messages to the one who tagged the bot. This project uses the tweepy library, also since tweepy doesnt support the Twitter API V2 we sometimes used the Twitter API directly without any Libraries.

## Team members
1. <a href="https://github.com/ShunKaido">Mohammed Nihad</a> 
2. <a href="https://github.com/ilyazjasim">Mohammed illias Jasim V</a> 
3. <a href="https://github.com/Nihadk117">Abdul Nihad K</a> 

## Team Id
BFH/recdnAxglgpWDXQon/2021

## Link to product walkthrough
<a href="#"><!-- href="https://drive.google.com/file/d/1eRlSoTpMNATVI1M24aSZvIhH2i97YeCW/view?usp=sharing"-->Click here (Removed)</a>

## How it Works ?
<ul>
 <li>The bot is hosted on <a href="https://www.pythonanywhere.com/">Pythonanywhere</a></li>
<li>The bot authenticates with Twitter API using the developer keys</li>
<li>it checks for mentions every 5 minutes</li>
<li>if it finds, it executes a function to get data on both the user and the thread it is tagged in</li>
<li>then the thread data is sent to the user by Direct Message</li>
</ul>that's the basic idea of it, looking deeply there are things like creating a log and saving already processed data into it so the program wont repeatly resend tweets into already sent users everytime the program restarts, accessing the Secret Keys stored in a file etc, functions to send direct message to users, basic API Authentication etc... etc... <br>We also access the Twitter API without using the tweepy library since tweepy's current version doesnt support twitter v2 API, the v2 version of twitter API was needed to get the 'conversation_id' of tweets so we can access threads in twitter more easily.<br> we coudnt get the end result we wanted, the replies are also send along with the threads. We advice not to test this bot on large threads since the bot is freely hosted <br>About hosting : its hosted on Pythonanywhere under the free user plan and the bot cannot run for more than a few hours under this plan thus we need to manually start the bot every few hours for it to work continuously<br>To use the bot simply tag @Threadme4T on any thread<br>
We have referenced google , twitter API official documentations from different sites , Tweepy official documentation and all other good sites<br>

## Libraries used
<ul>
<li>Tweepy - 3.10</li>
<li>requests - 2.25.1</li>
</ul>

## How to configure
<ul>
 <li>Get your API keys from developer.twitter </li>
<li>Clone github repository</li>
<li>Create virtualenv and activate it</li>
<li>Installing required libraries using pip</li>
</ul>

## How to Run
 <ul> <li>Insert your API access keys in config.json</li>
  <li>Simply run the twitter_tagging_bot.py </li></ul>
   
