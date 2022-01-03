 # Sales Route Planner

## Data Set

[Data Test - Sheet1.csv](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/663c9334-6fcd-4c30-9a16-51a73235bc58/Data_Test_-_Sheet1.csv)
## Problem Statement
## Task

- A Data Set with a few Cafes, Yoga Studios and Salons has been given, a Sales person would be visiting each of these locations to pitch our product to them
- Create an algorithm that can ingest all this data, and give out a daily route for the salesperson about which stores they should visit. Optimise for following attributes
    - Less Distance travelled
    - Most Stores Covered
    - (Feel free to choose other attribute you want to optimize on)
- A Sales Person cannot visit more than 12 stores a day
- The output of the list should be displayed on a web app, you can  use [https://github.com/keplergl/kepler.gl](https://github.com/keplergl/kepler.gl) or any other open source project (Bonus points if you make your own frontend!)
- Add any analysis you think might be relevant and help our sales team!
- The output of this task should be a public URL that should be emailed to careers+dstfi@omniflo.in
- In the email mention a short paragraph about the approach you took to solve the problem
- Attach your CV with the email

## Notes

- You're not allowed to share the data set to any third parties or companies, or distribute the output to any company

# my solution 

[Public Url](https://sales-route.herokuapp.com/)

# Actions
Firstly I plotted the latitude and longitudes from the given data and found there are some values that were in Slovakia so I removed them and then I used the Nearest neighbor clustering algorithm to obtain the 11 nearest places from a particular place we choose. then I used Streamlit to create the app. the app can accept any other CSV file with the same format and process it. I have also added two select boxes to filter and find a company so that the app will show the 11 nearest companies that you can go and pitch. the program will write the output as a CSV file which can be used to visualize in the Keplergl platform. Deployed the app using Heroku.

