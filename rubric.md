StatsBomb360 event data provides deeper insights into the game's context than traditional event data, allowing us to understand the impact of off-ball players better. Carlon Carpenter, the current lead performance analyst at Manchester United Women, outlined the value of this data and the key insights that can be generated from this data: https://blogarchive.statsbomb.com/articles/soccer/using-statsbomb-360-data-as-a-performance-analyst/

The following article gives you insights into the data and what can be done technically: https://medium.com/@lucascarrasquillaparra/complete-guide-on-working-with-the-statsbomb-open-data-dataset-a57c26d5852b

In this hackathon, we’re looking for new ways to visualise, report, and deliver insights to the coaching staff of teams using this data. We have provided you with StatsBomb 360 data from the 2022 World Cup to explore. 

Your goal: Identify/model Factors that make a Possession more Likely to result in a Shot 

Given the prompt and data at hand, your workflow may look like this:

Defining a possession
Feature engineering (for eg, build features that show space, progression, structure, etc.)
Modeling approach
Output
Creativity is encouraged! Technical complexity is also encouraged, but the best projects will communicate their key points effectively. 

Data Provided
The dataset provides all 64 games from the 2022 World Cup. We have combined it with 360 data for convenience. The penultimate column in the dataset, named ‘freeze_frame’, is a key column. It gives you the coordinates of every player in the visible area and classifies whether they are teammates or not, along with a well-defined goalkeeper. 


While there is no data glossary available for this data, if you have any questions about the data, please approach an E-board member. Although this is a good official resource to look at (last updated in 2019): 

https://github.com/statsbomb/open-data/tree/master/doc

Submission Requirements
By 6 PM, you will be required to submit a Google Drive link containing the following:

A Jupyter Notebook or R Markdown (or equivalent)
A PowerPoint presentation that contains the following:
At least 5 visuals
An explanation of your methodology and architecture
An explanation of the features you engineered
An explanation of how teams can actionably implement your model
The presentation will be approximately 10 minutes in length (8+2 Q&A). This is subject to change. 

Rubric
You will be judged on the following criteria

Sporting Value: How well did you define a possession? Do the factors in your model make “soccer sense”?
Communication: How well have you translated data insights to soccer concepts for your target audience (coaches + data-savvy analysts)? How well did you explain your project from the base principles? Did you check your assumptions?
Technical Complexity: Did you make the most of the time provided? Do the technical choices you made make sense for the evaluation method you chose? 
Reproducibility/Extensibility: Could we plug in a different game(s) from other tournaments and still be able to use the model? What steps would you have to take to scale this project?

Learning Resources
McKay Johns tutorials: https://www.youtube.com/@McKayJohns/videos 
Mplsoccer plotting package: https://mplsoccer.readthedocs.io/en/latest/index.html

About the Judges

Kevin O’Donnell is a data scientist at the US Soccer Federation. He is focused on developing deep learning possession value models and also assists in data-driven match reporting and modeling player load. Before joining US Soccer, he worked as a data scientist for DC United. He has a master's degree in Advanced Analytics from North Carolina State University and a bachelors of statistics from Villanova University.
William Johnson is a data analyst for the New England Revolution, where he has worked since 2022, applying analytics to support team performance and decision-making. A graduate of Colby College with a degree in Computer Science, Will has experience in both professional sports and industry, including a prior data analytics internship at Spectrus. With skills in programming languages like Java and JavaScript, he brings a strong technical foundation to sports analytics, combining data-driven insights with a passion for athletics.
