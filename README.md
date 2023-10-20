# Fresh Cakes
(Developer: Selam Yigezu)
 The Fresh-cakes app is a simple app developed for a cake shop which accept the name of the person who manage the shop and accept the sold values and  calculate the amount of cakes which needs to be baked for the next market.
 ![Mockup image](assets/image/responsive.png)
 [Live Website](https://fresh-cakes-1092920ed094.herokuapp.com/)

# User Experience (UX)

## Business Goals

### User Goals
- To save the data of the sold cakes
- easy to use
- Possibility to restart the app
- update the googel worksheet of the data


### Website Owner Goals
- Deliver easy-to-use stock managment system for cafe
- calculate the amount of data needed for the next market and minimize waste
- To save stock values on googel spread sheet

### Target Audience
- for all cafe owners 


### User Expectations
- Smooth and easy to use app
- Appealing design
- Accessibility


### Features Left to Implement
-  validating name value


## Validator Testing 

- This project has been tested with (https://pep8ci.herokuapp.com/) and no error is detected
 ![Mockup image](assets/image/test.png)

- All possible user input points have been tested to ensure error on my vs code terminal

### Unfixed Bugs
- all bugs are fixed

# Deployment

[Click Here To See The Live Website](https://fresh-cakes-1092920ed094.herokuapp.com/)


### Deploy
This website has been deployed using Heroku.

Instructions to deploy using Heroku:

1 - Log in to Heroku, navigate to dashboard and then click on the new button in the top right corner choosing: create new app.

2 - Give a name for the app (this name will need to be unique) and choose the correct region for where you are located. Click create app.

3 - The app has been created, now click on the settings tab.

4 - _Then Click reveal config vars to add keys the application will need. I have added the api credentials for my spreadsheet. a key of CREDS and a value of 8000 to a key of PORT.

5 - Click add buildpack to install interdependecies needed. For this project I installed 'python' and 'nodejs'.

6 - Click on deploy tab. Select deploy method, in this case Git Hub. Confirm connection to git hub by searching for the correct repository and then connect to it.

7 - To manually deploy project click 'Deploy Branch'. Once built a message will appear saying: Your app was successfully deployed. Click the view button to view the deployed page making a note of it's url.

### Cloning the repository
Instructions to clone the repository:

1 - On the GitHub repository, click on the green code button.

2 - Copy the link.

3 - In your IDE or local coding environment use the link to open the repository.

On VScode

click on 'Clone Git Repository which will bring up a box in which to paste the link.
save the repo and You will be set up ready to work on the repository.

On CodeAnywhere

Click on 'Add new workspace'
Click on 'Create from your project repository' and a box in which to paste the link
CodeAnywhere will open a new workspace containing the repo.

# Technologies Used

### Languages
The following languages were used to develop the website:
- Python language and gspread libraries

### Resources and Tools
The following resources and tools were used to develop the website:
- Git
- Github
- Gitpod
- Heroku
- CI Python Linter: Used to validate Python code
- Codecademy
- Stack Overflow
- VS code

# Credits

A list of references and tutorials used for t:

* Love Sandwiches Walkthrough Project
* tutorial support from student support: as i was having problem with deploying my project on heroku i have got a good support from student support
* w3school (https://www.w3schools.com/python/)


# Acknowledgements

I would like to take this opportunity to acknowledge and thank the following people:

- I would really acknowledge the Love Sandwiches Walkthrough Project for helping me understand python and make this project.
- Thank you for everybody on Code Institute's Slack Channels.
- tutor from Code Institue. Thank you for the help.
- My loved husband, David , who helped me with taking care of my child.
- My Daughter Mikaela even if she was messing up my code by touching the keyboard suddenly and creating errors she was always there with me.
