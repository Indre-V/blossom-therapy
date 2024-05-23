- [Agile Methodology](#agile-methodology)
  * [Overview](#overview)
  * [MoSCoW Prioritization](#moscow-prioritization)
  * [GitHub Projects](#github-projects)
  * [EPICS](#epics)
  * [User Stories](#user-stories)
    + [Developer Stories](#developer-stories)
    + [Visitor Stories](#visitor-stories)
    + [Registered User Stories](#registered-user-stories)
  * [Website Goals and Objectives](#website-goals-and-objectives)
  * [Target Audience](#target-audience)
  * [Wireframes](#wireframes)
  * [Database Schema](#database-schema)
  * [Design Choices](#design-choices)
    + [Typography](#typography)
    + [Colour Scheme](#colour-scheme)
    + [Images](#images)
    + [Responsiveness](#responsiveness)
- [Features](#features)
- [Deployment](#deployment)
  * [To deploy the project to Heroku](#to-deploy-the-project-to-heroku)
  * [To fork the project](#to-fork-the-project)
  * [To clone the project](#to-clone-the-project)
- [Technology](#technology)
  * [Languages used](#languages-used)
  * [Python Libraries](#python-libraries)
  * [Frameworks](#frameworks)
  * [Libraries](#libraries)
  * [Programs](#programs)
  * [Frameworks](#frameworks-1)
- [Credits](#credits)
  * [Disclaimer](#disclaimer)



# Agile Methodology

## Overview

Agile methodology is a project management approach that emphasizes flexibility, collaboration, and iterative progress towards a well-defined goal. It is particularly effective in software development where requirements and solutions evolve through the collaborative effort of self-organizing cross-functional teams. Agile methodologies aim to deliver small, incremental changes in a product to improve quality and adaptability to changing needs.


## MoSCoW Prioritization

The MoSCoW prioritization technique is used to determine the importance of various features and tasks in a project. This method categorizes features into four groups: Must Have, Should Have, Could Have, and Won't Have. This helps in effective time management and ensures that the most critical functionalities are delivered first.

## GitHub Projects

Using GitHub Projects, tasks are managed and prgress tracked through project boards. Each board will represent an EPIC, with columns for tasks, their statuses (To Do, In Progress, On Hold, Done, Future Features/Uresolved). Issue labels include the user, prioritization and sprints.

![Kanban Board](/readme/docs/kanban-board.png)

## EPICS

Epic is a large body of work that is broken down into user stories. Each Epic in this project represents a key aspect of the platform's development and ensures comprehensive coverage of the required functionalities.

- EPIC 1: Design Planning
- EPIC 2: Development Environment Setup
- EPIC 3: User Account Management
- EPIC 4: User Engagement
- EPIC 5: Admin Content Management
- EPIC 6: User Experience Optimization
- EPIC 7: Developer Profile
- EPIC 8: Quality Assurance and Documentation

## User Stories

With an emphasis on delivering a seamless user experience, the goal of this project is to provide a comprehensive platform that serves both visitors and registered users. The platform will allow for the development and maintenance of content, present developer profiles, and provide opportunities for interaction.  The following user stories outline the essential functionalities and the rationale behind them.

*************************************
### Developer Stories

As a **developer**:

- I want to **create wireframes** so that I can **visually represent the layout and structure of the application.**

- I want to **design a database schema**  so that I can **efficiently store and manage platform content, ensuring optimal performance, scalability, and flexibility.**

- I want to **create visually engaging and responsive designs** so that **users can easily navigate the website and access relevant information**.

- I want to **adopt Agile methodology** so that **I can deliver high quality product that meets the needs of the user.**

- I want to **install and add basic configurations to Django** so that **I can create a working app**.

- I want to **deploy to Heroku** so that **I can verify initial set up**.

- I want to **the platform to load quickly and respond swiftly to user interactions** so that **users can have a seamless experience**.

- I want to **ensure that all syntax errors are identified and resolved during the code validation process** so that **the code is free from syntax-related issues**.

- I want to **maintain thorough documentation** so that **code is maintained seamlessly in future**.

- I want to **ensure that user stories are thoroughly tested** so that **they meet acceptance criteria and deliver the expected functionality**.

- I want to **deploy the application to Heroku** so that **it is accessible to users online**.

- I want to **ensure that application meets performance and accessibility standards** so that **provides a seamless experience for all users and performs optimally**.

- I want to **update my profile information** so that **I can keep my information current and accurate**.

*************************************************************
### Visitor Stories

As a **visitor**:

- I want to **visit the developer's GitHub portfolio** so that **I can view their projects and contributions**.

- I want to **download the developer's resume** so that I can **review their qualifications and consider them for a position.**

- I want to **view the developer's profile** so that I can **learn more about the developer, contact them, and access their portfolio.**

- I want the **accessibility features to be improved** so that **to maintain equal access and usability for all users, including those with disabilities.**

- I want to **visual elements across the platform to be consistent** so that **I can have a cohesive and pleasant user interface experience**.

- I want to **navigate through the platform effortlessly,** so that **I can find relevant sections and features intuitively.**

- I want to **utilize advanced display filtering options** so that **content displayed on the platform according to my preferences and requirements.**

- I want to **able to register an account** so **I can create an account**.

****************************************************

### Registered User Stories

As a **registered user**:

- I want to **be able to log in and out of my account** so that **I can use the platform**.

- I want to **to be able to reset my password** so that **I do not loose access to my account**.

- I want to **manage my profile** so that **I have control of the information held on the platform**.

- I want to **create posts** so that **I can upload them on the platform**.

- I want to **edit and delete posts** so that **I can maintain the content up-to-date**.

- I want to **to be able to comment on posts** so that **provide feedback to authors**.

- I want to **to be able to delete and edit comments** so that I can **control my engagement on the platform**.

- I want **the ability to interact with posts and comments by liking, un-liking, and favoriting them,** so that I can **engage with content that resonates with me**.

- I want to **provide feedback, report issues, and suggest improvements through a contact form,** so that I can **actively participate in improving the platform and receive support when needed**.

## Website Goals and Objectives

* Enhance User Experience:
    - Develop a user-friendly interface that is easy to navigate and visually appealing.
    - Ensure the platform is responsive and accessible on all devices.

* Facilitate Developer Showcase:
  - Allow registered users to create, edit, and manage posts and comments.
  -  Implement features that encourage user interaction, such as liking and favoriting content.

* Maintain High Performance and Accessibility Standards:
  - Optimize the platform for fast loading times and swift responses to user interactions.
  - Ensure the platform meets accessibility standards to accommodate all users.

* Support Continuous Improvement and Scalability:
  - Adopt Agile development practices to continuously deliver high-quality features.
  - Design the database and infrastructure to handle growth and increased user activity.

* Ensure Security and Reliability:
  - Implement robust authentication and authorization mechanisms.
  - Regularly validate and test the code to maintain a stable and secure application.

* Encourage Community and Feedback:
  - Provide mechanisms for users to give feedback, report issues, and suggest improvements.
  - Actively engage with user feedback to improve the platform continuously.

## Target Audience

- Developers
- Potential Employers and Recruiters
- General Visitors
- Families and Educators
- Enthusiasts

[Back to top](#contents)


## Wireframes

The wireframes for the platform provide a visual representation of the layout and structure of the application. They outline the placement of key elements such as navigation menus, user profiles, content areas, and interactive features. The wireframes ensure a cohesive and intuitive user interface, guiding the design and development process. After the extensive testing was conducted, naturally there are some deviations from wireframes in the live version of the platform.

 [Mobile Wireframes](/readme/docs/mobile-wireframes.pdf "Mobile Wireframes")

[Desktop Wireframes](/readme/docs/desktop-wireframes.pdf "Desktop Wireframes")



[Back to top](#contents)

## Database Schema

The database schema outlines the structure and relationships between key tables for the platform. The **User** table stores basic user information and authentication details. The **Profile** and **DeveloperProfile** tables extend user details with personal information, bios, and links. The **Category** table categorizes content, while the **Post** table manages user-generated content with fields for title, content, author, and metadata. The **InsightComment** table handles comments on posts, including author information and approval status. These tables are designed to ensure efficient data management and robust user interactions on the platform.

![Database Schema](/readme/docs/database-schema.png)

## Design Choices

### Typography

 [Merriweather](https://fonts.google.com/specimen/Merriweather?query=merri) was chosen as the primary font to enhance the reading experience and align with the blog's nature-themed aesthetic. Its design features make it highly legible on both screens and printed materials, which is crucial for ensuring that readers can comfortably engage with the content, whether they are viewing detailed plant care guides or inspirational gardening stories.This font's traditional yet modern feel complements the natural, earthy tones of our color palette, creating a cohesive and inviting atmosphere that reflects the beauty and tranquility of gardening. By using Merriweather, I aim to deliver content that is not only visually appealing but also easy to read, thereby enhancing the overall user experience.

### Colour Scheme

This color scheme aims to create a harmonious balance between the vibrant, nature-inspired elements of the gardening insights and the professional, reliable tone needed for the developer section. By combining these carefully chosen colors, I aim to deliver a visually appealing and user-friendly experience that resonates with both gardeners and potential customers. 

![Coolors Scheme](/readme/docs/color-scheme.png)

| Color | Description |
|-------|-------------|
| **Primary Color:** | Tomato (#FF6347) |
| | Tomato is a warm, energetic color that evokes the vitality and freshness of a garden in full bloom. Its boldness grabs attention, making it perfect for call-to-action buttons and important highlights. This lively hue reflects the passion and enthusiasm of gardening enthusiasts, adding a sense of excitement to the blog. |
| **Secondary Color:** | Steel Blue (#4682B4) |
| | Steel Blue provides a calming and reliable counterpoint to the vibrant primary color. It symbolizes trust, stability, and depth, making it an ideal choice for the developer section, where clarity and reliability are paramount. This color helps create a serene environment that encourages focus and productivity. |
| **Accent Color:** | Gold (#FFD700) |
| | Gold is used as an accent color to add a touch of elegance and sophistication. It represents achievement and high quality, which can enhance the perceived value of the content. Gold is versatile and works well for highlighting key information, links, and decorative elements, providing a cohesive look across both sections of the site. |
| **Supporting Colors:** | |
| | **Peach Puff (#FFDAB9):** This soft, warm color complements the primary color, creating a gentle and inviting atmosphere. It can be used for backgrounds, secondary buttons, and subtle highlights, enhancing the site's overall warmth and friendliness. |
| | **Powder Blue (#B0E0E6):** A lighter shade of blue, Powder Blue provides a refreshing and airy feel. It is perfect for background elements and less critical components, maintaining the site's clean and spacious look without overwhelming the user. |
| | **Ivory (#FFFFF0):** Ivory is used as an alternative background color to add warmth and softness. It can be applied to sections that need a gentle, neutral backdrop, ensuring that the content remains the focal point. |
| **Background and Text Colors:** | |
| | **Background Color:** White (#ffffff): White serves as the main background color, offering a clean, minimalist canvas that enhances readability and makes other colors stand out. |
| | **Text Color:** Dark Gray (#222020): Dark Gray is chosen for the text color due to its excellent legibility and modern appearance. It provides a strong contrast against the white background, ensuring that the text is easy to read without being as stark as black. |

### Images

Combination of images sourced from [Unsplash](https://unsplash.com/), [Gencraft](https://gencraft.com/ "Gencraft"), and those taken by the developer contributes to a visually compelling and cohesive website design that effectively communicates the message and values of the gardening blog and developer section. All images sourced from Unsplash and Gencraft AI are available under free licenses, allowing for their use in commercial projects without attribution. This ensures compliance with copyright laws and provides assurance regarding the legal usage of the images on the website.


### Responsiveness

My website is responsive to different layouts depending on the size of the viewport have been included in the CSS media queries. This allows visitors to experience the website as I intended on device types and screen sizes. The breakpoints I am using are from Bootstrap.

![Breakpoints](/readme/docs/media-queries.png)

[Back to top](#contents)

# Features




[Back to top](#contents)

# Deployment

## To deploy the project to Heroku

Follow these steps to deploy your Django project to Heroku from VS Code:
| ||
| --- | --- |
| **Step 1** Create a New Heroku App |
| - Access the Heroku Dashboard: Log in to your Heroku account and access the dashboard. |
| - Create a New App: Click on the New button in the top-right corner of the dashboard and select Create new app from the dropdown menu. |
| - App Name and Region: Enter a unique name for your app and choose a region closest to you (EU or USA). Click Create App to create the app. |
| **Step 2** Configure Environment Variables |
| - Reveal Config Vars: From the new app Settings, click Reveal Config Vars. |
| - Set Environment Variables: Set your environment variables as follows: |
|   - `CLOUDINARY_URL`: Insert your own Cloudinary API key here. |
|   - `DATABASE_URL`: Insert your own ElephantSQL database URL here. |
|   - `DISABLE_COLLECTSTATIC`: Set to 1 for temporary purposes, and remove it for the final deployment. |
|   - `SECRET_KEY`: This can be any random secret key. |
| **Step 3** Prepare the Project for Deployment |
| - Create a `requirements.txt` File: This file lists all the dependencies required by your project. You can install the project's requirements using `pip3 install -r requirements.txt`. If you have your own packages installed, update the `requirements.txt` file using `pip3 freeze --local > requirements.txt`. |
| - Create a `Procfile`: This file specifies the commands Heroku should run to start your app. Create the Procfile using `echo web: gunicorn app_name.wsgi > Procfile`. Replace `app_name` with the name of your primary Django app, which is the folder where `settings.py` is located. |
| **Step 4** Connect Your GitHub Repository to Heroku |
| - Automatic Deployment: Select Automatic Deployment from the Heroku app settings to automatically deploy your app whenever you push changes to your GitHub repository. |
| - Manual Deployment: Alternatively, you can connect your GitHub repository to Heroku manually using the Terminal/CLI: |
|   - Login to Heroku: Run `heroku login -i` to log in to your Heroku account. |
|   - Set the Remote for Heroku: Run `heroku git:remote -a app_name` to set the remote for Heroku. Replace `app_name` with your app name. |
|   - Push to Heroku: After performing the standard Git add, commit, and push to GitHub, you can now type `git push heroku main` to deploy your app. |
| **Step 5**  Verify Your Deployment |
| - Open App: Once your app is deployed, you can open it by clicking on the Open App button in the Heroku dashboard. This will open your app in a web browser. |
| - Verify App: Verify that your app is running correctly by checking for any errors or issues. |


[Back to top](#contents)

## To fork the project

  
Forking the **GitHub** repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.


- Log in to **GitHub**.

- Locate the repository.

- Click to open it.

- The fork button is located on the right side of the repository menu.

- To copy the repository to your **GitHub** account, click the button.

  
## To clone the project

  
- Log in to **GitHub**.

- Navigate to the main page of the repository and click **Code**.

- Copy the **URL** for the repository.

- Open your local **IDE**.

- Change the current working directory to the location where you want the cloned directory.

- Type git clone, and then paste the **URL** you copied earlier.

- Press **Enter** to create your local clone.
  

_Any changes required to the website, they can be made, committed and pushed to GitHub._

[Back to top](#contents)

# Technology

##  Languages used

-   [Python](https://www.python.org/) - high-level, general-purpose programming language.
-   [Markdown](https://en.wikipedia.org/wiki/Markdown) - markdown language used to write README and TESTING documents.
- [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML5 "HTML") - the standard markup language for creating Web pages.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS") - a stylesheet language used for styling of a document written in a markup language.
- [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript "JS") - programming language that allows developer to implement complex features on web pages.


## Python Libraries

- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Authentication library used to create user accounts, providing features such as registration, login, and social authentication.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Used to manage Django forms, making form rendering in templates simpler and more elegant.

## Frameworks
- [Django](https://www.djangoproject.com/): Django is the main Python framework used in the development of this project. It provides a robust and scalable architecture for building web applications.

## Libraries
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Django-allauth is an authentication library used to create user accounts, providing features such as registration, login, and social authentication.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Crispy Forms is used to manage Django forms, making form rendering in templates simpler and more elegant.

## Programs

- [Balsamiq](https://balsamiq.com/): Wireframing tool used to generate wireframe images, allowing for quick and easy visualization of the application's layout and design.
- [Bootstrap 5](https://getbootstrap.com/docs/45/getting-started/introduction/): CSS framework used for developing responsiveness and styling, offering a wide range of pre-designed components and utilities.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/): Used for overall development and tweaking, including testing responsiveness, debugging, and performance profiling.
- [Cloudinary](https://cloudinary.com/): Image hosting service used to upload and manage images, providing features such as image optimization, transformation, and delivery.
- [Coolors](https://coolors.co/): Used to create a color palette, offering tools for generating, exploring, and customizing color schemes for web design.
- [Database Schema](https://dbdatabase.io/): dbdatabase.io is a database management tool used for creating and managing databases, providing features such as schema design, data modeling, and SQL querying.
- [Favicon](https://favicon.io/): Used to create the favicon, providing a simple tool for generating favicons for web applications.
- [Font Awesome](https://fontawesome.com/): Used for icons in the information bar, providing a wide range of high-quality, customizable icons for web development.
- [GitHub](https://github.com/): Used for version control and as an agile tool, facilitating collaborative development, code review, and project management.
- [Google Fonts](https://fonts.google.com/): Used to import and alter fonts on the page, offering a vast collection of free, open-source fonts for use in web projects.
- [Heroku](https://dashboard.heroku.com/login): Cloud-based platform used for deploying web applications. It offers easy deployment, scaling, and management of applications in the cloud environment.
- [Jshint](https://jshint.com/): Used to validate JavaScript code, helping identify potential errors and maintain code quality.
- [PEP8 Online](http://pep8online.com/): PEP8 Online is used to validate all Python code against the PEP 8 style guide, promoting code readability and consistency.
- [PostgreSQL](https://dbs.ci-dbs.net/): CI designed the database tool for this project. It is a powerful relational database management system.
- [Summernote](https://summernote.org/): WYSIWYG editor used to allow users to edit their posts, providing a rich text editing experience.
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert Excel testing tables to Markdown format, simplifying the process of creating and formatting tables for documentation purposes.
- [TOC Generator](https://ecotrust-canada.github.io/markdown-toc/): Used to generate table of contents for Markdown files, providing a convenient way to organize and navigate large documents.
- [W3C](https://www.w3.org/): Used for HTML & CSS validation, ensuring that the project's code complies with web standards and is error-free.
- [WAVE](https://webaim.org/resources/contrastchecker/): Used for accessibility testing, providing tools to check for accessibility issues such as color contrast and semantic structure.
 

## Frameworks

- [Django](https://www.djangoproject.com/): The main Python framework used in the development of this project. It provides a robust and scalable architecture for building web applications.


[Back to top](#contents)


# Credits

- Feedback, advice and support:

  - [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

- Code inspiration and learning content:

* YouTube Channels for platform functionality: 

## Disclaimer