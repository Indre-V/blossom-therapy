# Blossom Therapy Insights

This website is aimed as a comprehensive gardening blog designed for both novice and experienced gardeners. Blossom Therapy Insights offers a wealth of information through its post section, called Insights, where users can find expert advice, detailed guides, and inspiring stories about all things gardening. In addition to the rich content provided in the Insights section, the blog also features a Developer Profile tab. This tab showcases the profile of the developer behind Blossom Therapy Insights, allowing visitors to learn more about expertise, view portfolio, and connect with the developer. With a focus on delivering high-quality content and fostering a community of garden enthusiasts, Blossom Therapy Insights is your go-to resource for cultivating a thriving garden. 



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



## Agile Methodology

### Overview

Agile methodology is a project management approach that emphasizes flexibility, collaboration, and iterative progress towards a well-defined goal. It is particularly effective in software development where requirements and solutions evolve through the collaborative effort of self-organizing cross-functional teams. Agile methodologies aim to deliver small, incremental changes in a product to improve quality and adaptability to changing needs.


### MoSCoW Prioritization

The MoSCoW prioritization technique is used to determine the importance of various features and tasks in a project. This method categorizes features into four groups: Must Have, Should Have, Could Have, and Won't Have. This helps in effective time management and ensures that the most critical functionalities are delivered first.

### GitHub Projects

Using GitHub Projects, tasks are managed and prgress tracked through project boards. Each board will represent an EPIC, with columns for tasks, their statuses (To Do, In Progress, On Hold, Done, Future Features/Uresolved). Issue labels include the user, prioritization and sprints.

![Kanban Board](/docs/readme.md/kanban-board.png)

### EPICS

Epic is a large body of work that is broken down into user stories. Each Epic in this project represents a key aspect of the platform's development and ensures comprehensive coverage of the required functionalities.

- EPIC 1: Design Planning
- EPIC 2: Development Environment Setup
- EPIC 3: User Account Management
- EPIC 4: User Engagement
- EPIC 5: Admin Content Management
- EPIC 6: User Experience Optimization
- EPIC 7: Developer Profile
- EPIC 8: Quality Assurance and Documentation

### User Stories

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

- I want to **provide feedback, report issues, and suggest improvements through a contact form,** so that I can **actively participate in improving the platform and receive support when needed**.

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


### Admin User Stories

As an **admin user**:

- As an **admin user**, I want **the ability to perform all CRUD (Create, Read, Update, Delete) operations** so that **manually manage, control and edit content**.

- As an **admin user**, I want to **approve comments and posts** so that **I can ensure content quality and appropriateness before it is published**.

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

This color scheme aims to create a harmonious balance between the vibrant, nature-inspired elements of the gardening insights and the professional, reliable tone needed for the about section. By combining these carefully chosen colors, I aim to deliver a visually appealing and user-friendly experience that resonates with both gardeners and potential customers. 

![Coolors Scheme](/readme/docs/color-scheme.png)

# Color Palette

| Color             | Hex Code   | Usage                                                                                                                                         |
|-------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Primary Color     | #FF6347    | This color is used for the navbar background and gradients. It is a vibrant and eye-catching color that draws user attention and creates a lively atmosphere.                  |
| Secondary Color   | #46626d    | Applied to icons and other secondary text elements, this color provides good contrast without being too harsh, maintaining readability and a balanced design.                    |
| Background Color  | #FCF7F2    | Used as the background color for the entire body to create a soft and clean look. This color is light and pleasant, ensuring that text and other elements stand out clearly against it. |
| Light Orange      | #EDD0B3    | Applied to the footer background and as a hover effect for buttons. This color adds warmth and highlights important interactive elements, drawing user attention effectively.          |
| Powder Blue       | #B0D3E6    | Used for button backgrounds and various highlights. This color is calming and soft, ensuring that buttons are noticeable but not overwhelming. It complements the other colors well, adding to the overall aesthetic.         |

### Images

Combination of images sourced from [Leonardo](https://leonardo.ai/ "Leonardo AI"), and those taken by the developer contributes to a visually compelling and cohesive website design that effectively communicates the message and values of the gardening blog and developer section. All images sourced from Unsplash and Leonardo AI are available under free licenses, allowing for their use in commercial projects without attribution. This ensures compliance with copyright laws and provides assurance regarding the legal usage of the images on the website.


### Responsiveness

My website is responsive to different layouts depending on the size of the viewport have been included in the CSS media queries. This allows visitors to experience the website as I intended on device types and screen sizes. The breakpoints I am using are from Bootstrap.

![Breakpoints](/readme/docs/media-queries.png)

[Back to top](#contents)

## Security Measures and Protective Design

### User Authentication
- Django's `LoginRequiredMixin` is used to ensure that any requests to access secure pages by non-authenticated users are redirected to the login page.
- Django's `UserPassesTestMixin` is used to limit access based on certain permissions, ensuring users can only edit/delete content they authored. If the user doesn't pass the test, they are shown an HTTP 403 Forbidden error.

### Password Management

- Use Django's built-in password management tools to ensure passwords are hashed and stored securely.
- Enforce strong password policies to enhance user account security.

### Form Validation
If incorrect or empty data is added to a form, the form won't submit, and a warning will appear to the user informing them which field raised the error.


### Database Security

- The database URL and secret key are stored in the `env.py` file to prevent unwanted connections to the database. This setup was implemented before the first push to GitHub.
- Cross-Site Request Forgery (CSRF) tokens are used on all forms throughout the site to enhance security.

## Features

### Header

![Visitor Large Screen](/readme/docs/header-visitor-ml-screen.png)

The header of the Blossom Therapy Insights page is designed to be visually appealing and user-friendly, featuring a prominent logo, a navigation menu, user authentication links, and a search bar. It uses a cohesive color scheme with primary, secondary, and background colors, and ensures accessibility with good color contrast and ARIA labels. The responsive design adapts well to both desktop and mobile devices, maintaining functionality and ease of navigation across all screen sizes. The use of 'Merriweather' font and consistent font sizes enhances readability, contributing to a seamless user experience. Once the user is logged in more options become available. For generic authorised users, 'Add Insight' option appears. Superusers have an extra option to approve pending posts.

<details><summary><b>Header - User View</b></summary>
![User Large Screen](/readme/docs/header-user-ml-screen.png)
![Admin Large Screen](/readme/docs/header-admin-ml-screen.png)

</details><br/>

### Footer

![Footer](/readme/docs/footer-ml-screen.png)

The footer maintains consistency with the overall site design, featuring the same font and color scheme, and is fully responsive to adapt to various screen sizes. This attention to detail helps reinforce the site's branding and enhances the user experience by providing clear and accessible navigation options at the bottom of the page. Media links are included. Also, users can contact site owner by clicking on the :envelope: icon is they wish to do so. 

**Contact Form:**

This contact form is designed to facilitate user communication with developers in a streamlined and secure manner. All Contact submitted via the form can be viewed in Django Admin Portal.

<details><summary><b>Contact Form</b></summary>

![Contact Modal](/readme/docs/contact-modal.png)
![Contact List](/readme/docs/contact-list.png)

</details><br/>


**About Section:**

Showcases detailed information about website developer in a visually appealing format. Profile card includes a profile picture, name, location, languages spoken, skills, and a brief bio. Links to the developer’s GitHub, LinkedIn, and resume are also provided, along with a button to contact the developer via email. Additional cards highlight the developer’s coding philosophy, design enthusiasm, and educational background. This comprehensive and user-friendly layout allows for easy navigation and access to important information about the developer involved in the project.
The data is managed via the Django Admin Portal. 


<details><summary><b>About Section</b></summary>

![About Section](/readme/docs/about-page-view.png)

</details><br/>


### Landing Page

The landing page is designed to captivate visitors with its vibrant and welcoming aesthetic. Dominated by a primary color palette of floral white, light orange, and powder blue, it sets a calming yet engaging tone. The hero section prominently features a headline complemented by an inviting image that spans the width of the page. For authenticated users, a clear call-to-action button encourages adding insights, while new visitors are prompted to join the community. The layout is clean and organized, ensuring that content is easily readable and visually appealing, thereby enhancing user engagement from the first interaction.

<details><summary><b>Landing View Large Screen</b></summary>

![Landing View Large Screen](/readme/docs/landing-view-ml-screen.png)

</details><br/>

### User Account Pages

THe user account pages ensure a smooth and secure process for managing user access, enhancing the overall user experience on Blossom Therapy Insights.

**Sign Up Page:**

The Sign Up page features a clean and intuitive form where users can create an account by entering their username, first name, last name, email, and password. The form uses a responsive design, ensuring accessibility and ease of use across devices. By prioritizing user-friendly design, the Sign Up page helps facilitate quick and easy registration, encouraging new users to join the community and start their gardening journey.

<details><summary><b>Register View</b></summary>

![Register](/readme/docs/register-small-screen.png)

</details><br/>

---

**Log In Page:**

The Log In page offers a straightforward and secure way for existing users to access their accounts. The page includes fields for the username and password, with clear labels and a prominent login button. The page maintains consistency with the site's overall aesthetic, ensuring a cohesive user experience. The focus on simplicity and security helps users quickly and confidently access their accounts to engage with the Blossom Therapy community.

<details><summary><b>Log In view</b></summary>

![Log In](/readme/docs/login-small-screen.png)

</details><br/>

---

**Log Out Page:**

The Log Out page provides users with confirmation of a successful logout from their account. It features a brief message indicating that the user has been logged out. The design is minimalistic, reinforcing the action taken and providing a clear path to continue exploring the site or logging in again.

<details><summary><b>Log Out View View</b></summary>

![Log Out View](/readme/docs/logout-small-screen.png)

</details><br/>

---

### Profile Page

The Profile Page on Blossom Therapy Insights serves as a personalized view for users to manage and showcase their gardening insights and track engagement. 

![Personal Profile View](/readme/docs/personal-view-sm-screen.png)

**Profile Image**

![Profile Image](/readme/docs/profile-image.png)

The view prominently displays the user’s profile picture. If no picture is uploaded, a placeholder image is shown instead, ensuring a visually consistent layout.

**Profile Details**

User full name, location and bio displayed publicly to all visitors of the page. They can be updated at anytime. 

![Profile Details](/readme/docs/profile-details.png)

**Navigation and Interaction:**

![Navigation](/readme/docs/navigation.png)

Users can easily navigate to their insights, drafts, and favorite posts using intuitive buttons displayed on the left column. These buttons provide direct access to specific sections of the user’s profile based on their interactions within the platform. Users can remove favourites from the list. Edit, publish or delete the insights. 

<details><summary><b>User Content Summary View</b></summary>

![Profile Insights](/readme/docs/profile-insights-sm-screen.png)
![My Drafts](/readme/docs/my-drafts-ml-screen.png)
![My Favourites](/readme/docs/my-favourites-ml-screen.png)

</details><br/>


**Insights Statistics:**

![Insights Statistics](/readme/docs/insights-statistics.png)

Users can view insightful statistics related to their posts, including total likes and favorites received. These metrics provide feedback on the impact and popularity of their contributions within the community.

**Interactive Actions:**

![Interactive Actions](/readme/docs/interactive-actions.png)

For authenticated users who own the profile, actionable buttons are provided at the bottom for updating the profile, changing passwords, and deleting the account. These actions are centrally located for ease of access and management.

<details><summary><b>Actions Summary View</b></summary>

![Update View](/readme/docs/update-profile-sm-screen.png)
![Change Password View](/readme/docs/change-password-ml-screen.png)
![Delete Account](/readme/docs/delete-account-ml-screen.png)

</details><br/>

**Public Profile View:**

![Public Profile View](/readme/docs/public-profile-view.png)

Visitors can click on the insight author's username and access their public profile. View excludes actions, favourites and drafts to protect the author's privacy.

### Add Insight

The "Add Insight" page features a user-friendly form, allowing users to easily submit new insights to the platform. The page includes a clear title, informative instructions, and a form styled with Crispy Forms for enhanced usability. Users can enter their post details, attach images, and submit their insights, with all submissions by generic users pending admin approval. Additionally, there is an option to save insights as drafts in the user profile section. The design prioritizes simplicity and functionality. Superusers have also an option to 'Publish' the Insight instantly. 

<details><summary><b>Add Insight Form</b></summary>

![Update View](/readme/docs/add-insight-sm-screen.png)

</details><br/>

### Edit Insight

The "Edit Insight" page allows users to modify existing insights. The page displayes the same fields and overall look as *Add Insight*.  Users can update insight details directly within the form, with a submit button for applying changes securely. Additionally, a cancel button is provided to return users to the detailed view of the insight, ensuring straightforward navigation and editing capabilities.

<details><summary><b>Edit Insight Form</b></summary>

![Edit View](/readme/docs/edit-insight-sm-screen.png)

</details><br/>

### Delete Insight

Trash can icon that triggers the delete modal when clicked by the user on the Insight card. Inside the modal, the insight's title is displayed in the header, confirming the deletion action. Users are warned that this action is irreversible in the modal body. The modal footer offers a cancel button to dismiss the modal without deleting the insight. 

<details><summary><b>Delete Insight Modal</b></summary>

![Delete Modal](/readme/docs/delete-insight-sm-screen.png)

</details><br/>

### Pending Approvals

This option is only available to superusers. They are instructed on how to manage pending insights, including approval, viewing content, deletion, editing, and changing status to publish or saving to drafts. If there are pending records, they are displayed in a table format showing details author, title (linked to the insight details), creation date, and an action column with a button to approve each post. If no posts are pending, message informs that there are no pending posts.

<details><summary><b>Delete Insight Modal</b></summary>

![Pending Approvals](/readme/docs/pending-approvals-sm-screen.png)

</details><br/>

### Insight Card

![Insight Card](/readme/docs/insight-card-sm-screen.png)

Insight card layout for each post, features the post's title, featured image, category, author details, publication date, interactive elements based on the user status. It begins with the post's featured image, which links to the detailed view of the post. The card also includes the post's title, category with a link to related posts, and details about the author, including their profile picture and username with a link to their public profile page. For authorized users (author or superuser), edit and delete buttons are provided.
For published posts it includes like and favorite buttons with counts, and the number of comments. If the posts is pending approval or a draft it displays the status.

<details><summary><b> Insight Status Display</b></summary>

![Status Draft Display](/readme/docs/status-draft-sm-screen.png)
![Status Pending Display](/readme/docs/status-pending-sm-screen.png)

</details><br/>

### Browse Insights

 It features a sidebar for easy navigation through different categories, enhancing the user’s ability to filter content. The page dynamically adjusts its heading to display search results or the selected category. In the event that no insights match the user's search or category selection, a prompt encourages users to add new insights. Additionally, the inclusion of a pagination component ensures smooth navigation through multiple pages of insights, making the browsing experience seamless and efficient. Category list is managed by the superuser in Django Admin Portal.

 <details><summary><b> Insight Status Display</b></summary>

![Sidebar](/readme/docs/sidebar.png)
![Insights List View](/readme/docs/Insights-list-view-sm-screen.png)
![Search Results](/readme/docs/search-results-sm-screen.png)
![Category Search](/readme/docs/category-search-sm-screen.png)
![No Records](/readme/docs/no-records-sm-screen.png)

</details><br/>

### Insight Details

It dynamically displays insight card followed by the content of the post which is securely rendered using the safe filter to ensure HTML tags are displayed correctly. 
Additionally, depending on the post status, a comment section with an interactive form allows users to contribute comments. This structured approach ensures a user-friendly interface for reading and interacting with posts on the platform.


<details><summary><b> Insight Details Display</b></summary>

![Insight Details Display](/readme/docs/insight-details-sm-screen.png)

</details><br/>

### User Interactions

![Interactions Display](/readme/docs/interactions-snippet.png)

**Insight Like and Unlike:**

Application allows users to like and unlike insights. This functionality is available for all published posts.  If the user has already liked the post, the like is removed. If the user has not liked the post, the like is added. The total of likes is displayed in the author profile section. The post to be liked or unliked is identified by its unique slug, which is passed in the URL.
After the like or unlike action, the user is redirected back to the page they came from, maintaining their navigation context.

<details><summary><b>Like Functionality</b></summary>

![Like Message](/readme/docs/like-message.png)
![Liked Insight View](/readme/docs/liked-insight.png)
![Unliked Message](/readme/docs/unlike-message.png)

</details><br/>

**Favourite and Unfavourite Insight:**

Application allows users to add or remove insights from their favourites. If the user has already favourited the post, the favourite is removed. If the user has not favourited the post, the favourite is added. After an action (favourite or unfavourite), the user receives a success message indicating whether the insight was added to or removed from their favourites. After the favourite or unfavourite action, the user is redirected back to the page they came from, maintaining their navigation context. 

<details><summary><b>Favourite Functionality</b></summary>

![Like Message](/readme/docs/like-message.png)
![Liked Insight View](/readme/docs/liked-insight.png)
![Unliked Message](/readme/docs/unlike-message.png)

</details><br/>

**Comments:**

Authenticated users can add comments to insights. Comments are displayed in the insight details view accompanied by user profile image and name. The comment date is displayed using `Humanize` built-in Django model to make the date more user friendly. There is no requirement for the comments to be approved by admin. However, all superusers and comment authors can edit and delete comments within the insight details view. If user is not logged in, the message is displayed with log in link. Comment creation, deletion and editing functionalities have coded in user feedback messages that are displayed in the notification modal. After successful action, users are redirected to the detail view of the post associated with the comment. If the comment form field is left empty, the standard error message is displayed.

<details><summary><b>Comments View</b></summary>

![Comment Form](/readme/docs/comment-form.png)
![Comment Edit](/readme/docs/comment-edit.png)
![Comment Delete](/readme/docs/comment-delete.png)
![Comment Add Success Message](/readme/docs/comment-add.png)
![Comment Add Edit Message](/readme/docs/comment-add.png)
![Comment Add Success Message](/readme/docs/comment-add.png)

</details><br/>


### Custom Error Pages

- **400 Bad Request** - The platform is unable to process this request.
- **403 Page Forbidden** - It seems user trying to access restricted content. Please log out and sign in to the appropriate account.
- **404 Page Not Found** - The page user is looking for doesn't exist.
- **500 Server Error** - The platform is currently experiencing technical difficulties and cannot process this request.

<details><summary><b>Error View</b></summary>

![Error 400](/readme/docs/error-400.png)
![Error 403](/readme/docs/error-403.png)
![Error 404](/readme/docs/error-404.png)
![Error 500](/readme/docs/error-500.png)
</details><br/>

[Back to top](#contents)

## Deployment

### To deploy the project to Heroku

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

### To fork the project

Forking the **GitHub** repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.


- Log in to **GitHub**.

- Locate the repository.

- Click to open it.

- The fork button is located on the right side of the repository menu.

- To copy the repository to your **GitHub** account, click the button.

  
### To clone the project

- Log in to **GitHub**.

- Navigate to the main page of the repository and click **Code**.

- Copy the **URL** for the repository.

- Open your local **IDE**.

- Change the current working directory to the location where you want the cloned directory.

- Type git clone, and then paste the **URL** you copied earlier.

- Press **Enter** to create your local clone.
  

_Any changes required to the website, they can be made, committed and pushed to GitHub._

[Back to top](#contents)

## Testing

Blossom-Therapy website underwent an extensive testing process to ensure its functionality, accessibility, and performance. This involved validating the code, assessing accessibility, conducting performance tests, performing cross-device testing, verifying browser compatibility, evaluating user stories, and incorporating user feedback to improve the overall user experience
Testing summary and results can be found in [TESTING.md](TESTING.md) file.

## Future Features

## Technology

###  Languages

- [Python](https://www.python.org/) 
- [Markdown](https://en.wikipedia.org/wiki/Markdown)
- [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML5 "HTML")
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS")
- [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript "JS")


### Python Libraries

- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Authentication library used to create user accounts, providing features such as registration, login, and social authentication.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Used to manage Django forms, making form rendering in templates simpler and more elegant.

### Frameworks

- [Django](https://www.djangoproject.com/): Django is the main Python framework used in the development of this project. It provides a robust and scalable architecture for building web applications.

### Programs

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
 

[Back to top](#contents)


## Credits

- Feedback, advice and support:

  - [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

- Code inspiration and learning content:

* YouTube Channels for platform functionality: 

## Disclaimer