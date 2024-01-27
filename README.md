# Result Tracker

## Description 
> A Django app that utilizes an AWS-RDB hosted PostgreSQL database and a Python web scraper to record results and analyze trends in different ranking systems that allow players to find which ranking system most closely aligns with their performance.  

## About
> In athletics, numerous different sites need to be checked to find rankings, results, and analytics. The process of finding results specifically in tennis is very arduous. With the numerous different systems of ranking as well as the lack of a centralized database, valuable time is spent on finding basic statistics about recent performances.

## Goal: 
>The goal of this app is to create a **centralized website** from which college athletes can analyze all of their matches and also visualize trends in a variety of rankings, all in one area. Furthermore, matches that are currently recorded on paper will be recorded digitally, and scraping of data is done automatically meaning athletes will lose no time in finding statistics.

## **IMPORTANT NOTE**: This app utilizes scraping for non-malicious purposes and is used on a site where data is open normally. The other ranking system requires a subscription which I have personally but can not share publicly. For this reason, some links and code are redacted. Furthermore, this website was hosted using **AWS EC2 on Linux** but was removed at the request of UTR and WTN due to legality reasons

## How the app works

### This app was made for the MIT Men's Varsity Tennis team which I am part of and received permission to collect data from. For this reason, many themes may be MIT-focused.

1. Home page
> <img width="1113" alt="image" src="https://github.com/ShrishChou/Performance-Tracker/assets/91390142/f0a24fd8-14da-41ad-a80f-e547f05d41eb">
> The home page gives users the option to find different data
 2. The **Team Stats** page takes users to all the recent duels which are listed in order of the dates they happened with wins outlined in green and losses in red. This can also be accessed in the navigation bar on any of the other pages
> <img width="1148" alt="image" src="https://github.com/ShrishChou/Performance-Tracker/assets/91390142/a1ea24db-3966-4e05-9b1b-20feb6bc4059">
 3. The **Individual Stats** page gives a list of all players on the team with data on number of wins and games played.
> <img width="1145" alt="image" src="https://github.com/ShrishChou/Performance-Tracker/assets/91390142/1eae4e75-714c-44f3-a720-7bfcb94c22c2">
4. When hovering over the name of a player, the name will turn white and be clickable
><img width="1148" alt="image" src="https://github.com/ShrishChou/Performance-Tracker/assets/91390142/5428c08f-6f5e-423b-a48d-5d9304fc3188">
5.  When clicked the individual profile page of the player will appear
><img width="1147" alt="image" src="https://github.com/ShrishChou/Performance-Tracker/assets/91390142/e4cb69de-4151-48d4-8dc6-472f3cb7e806">
 6. The page given once the name is clicked on is known as the **profile page**. This page visually shows the ranking changes over time for each player. It also gives information about all recent doubles and singles matches along with wins and losses
> **NOTE** page is zoomed out to capture all content so text may look small
7. The **MIT Athletics** page takes you to the official MIT Athletics site for questions or concerns
 8. The Login to report score page ensures that only authorized users are allowed to report match scores
> Once the user has entered the correct information, the home page will change and become:
> <img width="1100" alt="image" src="https://github.com/ShrishChou/Performance-Tracker/assets/91390142/d4cc909c-cd0f-4350-8fc4-835b2b878e55">
9. The **Report Match** page is meant for reporting individual doubles or singles matches against schools in a tournament or other individual event
> <img width="1159" alt="image" src="https://github.com/ShrishChou/Performance-Tracker/assets/91390142/f046977e-f96e-40cd-a63a-1fb1fd34a0fe">
 10. The **Report Duel** is the same as the Report Match page except it has 6 singles and 3 doubles areas due to each duel having 6 singles and 3 doubles.


 ## About the code
 > This app is completely in Django, HTML, and CSS. The app is called Base and includes all information regarding how the views were made, and the models which include the Player, SinglesMatch, DoublesMatch, Ranking, and Duel models which are used in every function. Certain functions require superuser privileges which have the `@loginrequired` tag before them. It is also important to note that the scraper functions rely on Selenium which is being hosted in this case on a Microsoft Edge webdriver which can be changed to meet your requirements.

> Aside from the development of the basic app, there is a scripting function and batch file that allow for the scripting function to run locally on my computer. The scripting information is also within the base app but will not work due to certain parts that have been redacted due to certain privacy and terms. The scripting file runs locally on my computer using the task scheduler which runs the batch file to get ranking data periodically.

Feel free to reach out to me for any questions
