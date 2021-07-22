![Lila Harz Logo](https://imagizer.imageshack.com/v2/320x240q90/924/Dg8shx.jpg)

[View the live project here.](https://lila-harz.herokuapp.com/)

https://responsivedesignchecker.com/

This is the website for Lila Harz, a business project which the owner Remi Collins discovered a passion for creating resin homeware during lockdown in the UK. After craft-fair's and social media interest
Remi is looking for this website to take her business to the next level.

# Table of contents

- [UX](#User-Experience)
    - [Owners Business Goals](#owners-business-goals)
    - [User stories](#user-stories)
        - [First Time User Goals](#first-time-user-goals)
        - [Returning User goals](#returning-user-goals)
        - [Frequent User Goals](#frequent-user-goals)
    - [Design](#design)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
        - [Imagery](#imagery)
    - [Wireframes](#wireframes)
- [Features](#features)
- [Technology Used](#technology-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used)
- [Testing](#testing)
    - [Functionality Testing](#functionality-testing)
    - [Compatibility Testing](#compatibility-testing)
    - [Testing User Stories](#testing-user-stories)
        - [First Time User Testing](#first-time-user-testing)
        - [Returning User Testing](#returning-user-testing)
        - [Frequent User Testing](#frequent-user-testing)
    - [Further Testing](#further-testing)
    - [Known Bugs](#known-bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
     - [Media](#media)
     - [Acknowledgements](#acknowledgements)

## User Experience (UX)


### Owners Business Goals

        1. As the owner of the website, I want this website to be the main hub of Lila Harz and the first place customers go to.
        2. As the owner of the website, I want to be able to present a smart and colourful website. 
        3. As the owner of the website, I want to see engagement with the public to understand what they want from the business.


### User stories

#### First Time User Goals

        1. As a first-time user to the site, I want to understand what products Lila Harz offers.
        2. As a first-time user to the site, I want to be able to easily navigate throughout the site to find content.
        3. As a first-time user to the site, I want social media links to be readily available to broadcast what we sell.

#### Returning User Goals

        1. As a returning user to the site, I want to access quality photos if the products Lila Harz offers. 
        2. As a returning user to the site, I want to know what Lila Harz offers to me as a customer.
        3. As a returning user to the site, I want to understand how to care for my resin pieces 
        4. As a returning user to the site, I want to see discounts 

#### Frequent User Goals

        1. As a frequent user to the site, I want to see of new offers.


### Design

#### Colour Scheme
        -   
#### Typography
        -   
#### Imagery
        -    

-   ### Wireframes

<h2 align="center"><img src="#"></h2>

## Features

## Navigation bar

- 
- Navigation scheme:

    - On left side there is a logo. 
    - Next to the logo there are three links or burger menu which contains:
        - Home
        - Portfolio
        - Contact

## Footer

- The footer is consistent on all pages.  The footer has been utilised for the social media links.
Each link will open in a separate tab in a browser.


## Home

### Hero Image

- 

### About

- 

## Collections

- 

## Contact

- 

## Future Implementations

1. A Shopping Cart for purchases from the site.
2. Colour options for each product.
3. Testimonials section.
4. A more extensive product listing.


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Bootstrap 5.0.:](https://getbootstrap.com/docs/5.0/getting-started/download/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Raleway' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [GitPod:](https://gitpod.io/)
    - GitPod was used for version control by utilizing the Gitpod terminal to commit and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Tinyjgp:](https://tinyjpg.com/)
    - Tinyjpg was used for resizing images
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes]() during the design process.
1. [Chrome DevTools:](https://developers.google.com/web/tools/chrome-devtools)
    - Chrome DevTools have massively assisted me during the build of this site, helping with fixes to my code and positioning of elements.

## Testing

I have completed the project so was unable to test in time

### Functionality Testing 

### Compatibility Testing

### User stories

#### First Time User Testing

1. 
2. 
3. 

#### Returning User Testing

1.    
2.	  
3.    
4.    

#### Frequent User Testing

1. 
2. 
3. 

### Further Testing

-  

### Known Bugs

-   O

## Deployment

### Heroku

[Heroku](https://www.heroku.com) is a Cloud Application Platform that enables developers to build, run, and operate applications in the cloud.

Deployment process is as follows:

Create a **requirements.txt** file to store depenecies of installed packages for the project. In the CLI type `pip freeze --local > requirements.txt`.

Create a file named **Procfile** to declare what commands are run by the application's dynos on the Heroku platform. For this project, run by the app.py file, the Procfile should contain:`web: python app.py`

- Register for a free account on the Heroku [Signup](https://signup.heroku.com/login) page.
- On the Dashboard, click the 'New' button and select 'Create new app'.
- Choose a name and region.
- Under the 'Settings' tab, click on 'Config Vars' to add Configuration Variables from the env.py file. Remember to use your own credentials.
- In your CLI terminal install Heroku by typing `npm install -g heroku`
- Select the 'Deploy' option from the menu.
- Under 'Deployment method' select the GitHub option to connect to your GitHub repository. Ensure GitHub Username is selected and use the search function to find the relevant repository. It is recommended using a 'main' branch as default, due to GitHub depreciating the 'master' branch name.
- Select Automatic deploys from the main branch and click 'Deploy Branch'.
- Click on the 'Open App' button on the top-right to open the deployed app.
- There is no difference between the deployed version and the development version.


To run the project locally, in the terminal type `python app.py`
- This will open a localhost address, which is provided in the CLI.


## Credits

- To complete this project I used Code Institute student template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Ideas and knowledge library:

    - [w3schools.com](https://www.w3schools.com)

    - [getbootstrap.com/docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
        I used code for navbar, jumbotron and cards from Bootstrap.

### Code

-   [Bootstrap4](#).

-   [W3 Validator](#)

-   [W3C CSS Jigsaw](#).

### Content

-   All content was written by the developer.

### Media

-   All images were created by the Nathan Davies.

### Acknowledgements

-   Tutor support at Code Institute for their support.

### Screenshots

## Project screenshots

<h2 align="center"><img src="#"></h2>

<h2 align="center"><img src="#"></h2>

<h2 align="center"><img src="#"></h2>

<h2 align="center"><img src="#"></h2>

<h2 align="center"><img src="#"></h2>

<h2 align="center"><img src="#"></h2>


[Back to Table of contents](#table-of-contents)
