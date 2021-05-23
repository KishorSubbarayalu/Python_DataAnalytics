# Football Analytics

> [Fifa 2019 Players Dataset](https://www.kaggle.com/karangadiya/fifa19)

> [Various Tasks](https://www.kaggle.com/karangadiya/fifa19/tasks)

### Description
- Detailed attributes for every player registered in the latest edition of FIFA 19 database

### Data Information
- There are 89 attributes available for the FIFA 2019 players in the data collection.The total number of players are roughly 18.2 K
- The dataset has the following attributes like Age, Nationality, Overall, Potential, Club, Value, Wage, Preferred Foot, International Reputation, Weak Foot, Skill Moves, Work Rate, Position, Jersey Number, Joined, Loaned From, Contract Valid Until, Height, Weight, LS, ST, RS, LW, LF, CF, RF, RW, LAM, CAM, RAM, LM, LCM, CM, RCM, RM, LWB, LDM, CDM, RDM, RWB, LB, LCB, CB, RCB, RB, Crossing, Finishing, Heading, Accuracy, ShortPassing, Volleys, Dribbling, Curve, FKAccuracy, LongPassing, BallControl, Acceleration, SprintSpeed, Agility, Reactions, Balance, ShotPower, Jumping, Stamina, Strength, LongShots, Aggression, Interceptions, Positioning, Vision, Penalties, Composure, Marking, StandingTackle, SlidingTackle, GKDiving, GKHandling, GKKicking, GKPositioning, GKReflexes, and Release Clause


:::info
:bulb:Jupyter Notebook was the only tool used to perform these analytics
:::

### <span style="color:Blue">Problem Statements</span>
1. Find the best left foot finisher in each club
2. Categorize the players based on their finishing and show the count for each category using seaborn
3. Top 7 Economical Club, Richest Club, Clubs paying the high wages to their players

### <span style="color:Green">Solutions</span>
:::info
:bulb:To begin, it is critical to comprehend the facts. All of the columns are optional and may not be required to produce the desired output. Choose your columns carefully, and then create a dataframe to do analytics on
:::

:::info
:bulb: Libraries used: <br>
numpy -> Faster array operations if required <br>
pandas -> To work with dataframes <br>
seaborn -> Data visulaization <br>
matplotlib -> Data visulaization, however matplotlib shall be used to configure the minute details of every plot
:::


*Find the best left foot finisher in each club:*
- As previously said, the data set has a huge number of columns
- To select the top finisher, we can use the finishing column having numerical datatype. While playing, a player could finish well with his favoured foot. The data frame having the left foot players is easier to construct because the dataset provides a column that categorizes the players based on their strong/preferred foot
- After creating the dataframe, I kept only four columns for the analysis such as player id, club, finishing and player name
- I made another dataframe with player ids organized by club having highest finishing. Each club will have a larger number of players with varying finishing levels. We can query the records based on the player id who has the highest finishing of each club by following the steps above
- The final result shall be exported in many formats
![](https://i.imgur.com/tGZLoXt.png)

*Categorize the players based on their finishing and show the count for each category using seaborn:*
- The skill level shall be easliy categorized using the finishing levels
- I utilized the above statement's output dataframe to divide the players into four skill levels: professional, advanced, average, and below average
- A plot was created to display the number of players in each category using seaborn count plot
![](https://i.imgur.com/QLd8mAe.png)

*Top 7 Economical Club, Richest Club, Clubs paying the high wages to their players:*
- This is very interesting task where we had to do few data cleaning.
- As we plot will be more inclined to each club, we will remove the rows if any player has no information regarding their club
![](https://i.imgur.com/bVvw3XK.png)
- Secondly, the data type of the columns value and wages are object(i.e.string). We can't perform mathematical functions such as summation, count with this data type. Hence we need to perform some cleaning and convert the data type
- Before Cleaning
![](https://i.imgur.com/YBMB9Ra.png)
- After Cleaning
![](https://i.imgur.com/mGUx8NU.png)
![](https://i.imgur.com/cQVY5Y9.png)
![](https://i.imgur.com/OUGVpSW.png)
- Once the data was cleaned then group by on clubs was performed to obtain the required details. Subsequently the results were plotted
![](https://i.imgur.com/VWTmWkc.png)
![](https://i.imgur.com/lTsTCPc.png)
![](https://i.imgur.com/4RNDLuB.png)


