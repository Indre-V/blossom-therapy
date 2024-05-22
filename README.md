[Contents](#contents)
  * [User Stories](#user-stories)
  * [Website Goals and Objectives](#website-goals-and-objectives)
  * [Wireframes](#wireframes)
  * [Database Schema](#database-schema)
  * [Design Choices](#design-choices)
    + [Typography](#typography)
    + [Colour Scheme](#colour-scheme)
    + [Images](#images)
    + [Responsiveness](#responsiveness)
- [Agile Methodology](#agile-methodology)
    + [Overview](#overview)
    + [EPICS](#epics)
    + [User Stories](#user-stories)
    + [MoSCoW prioritization](#moscow-prioritization)
    + [GitHub Projects](#github-projectskanban)
- [Features](#features)
  * [Existing Features](#existing-features)
    + [Header](#header)
    + [Footer](#footer)
  * [Future Enhancements](#future-enhancements)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Libraries & Framework](#libraries---framework)
  * [Python Modules](#python-modules-imported)
  * [Tools](#tools)
- [Deployment](#deployment)
  * [To deploy the project](#to-deploy-the-project)
  * [To fork the project](#to-fork-the-project)
  * [To clone the project](#to-clone-the-project)
- [Credits](#credits)



## User Stories

With an emphasis on delivering a seamless user experience, the goal of this project is to provide a comprehensive platform that serves both visitors and registered users. The platform will allow for the development and maintenance of content, present developer profiles, and provide opportunities for interaction.  The following user stories outline the essential functionalities and the rationale behind them.

*************************************
### Developer Stories

As a **developer**, I want to **create wireframes** so that I can **visually represent the layout and structure of the application.**

As a **developer**, I want to **design a database schema**  so that I can **efficiently store and manage platform content, ensuring optimal performance, scalability, and flexibility.**

As a **developer**, I want to **create visually engaging and responsive designs** so that **users can easily navigate the website and access relevant information**.

As a **developer**, I want to **adopt Agile methodology** so that **I can deliver high quality product that meets the needs of the user.**

As a **developer**, I want to **install and add basic configurations to Django** so that **I can create a working app**.

As a **developer**, I want to **deploy to Heroku** so that **I can verify initial set up**.

As a **developer**, I want to **the platform to load quickly and respond swiftly to user interactions** so that **users can have a seamless experience**.

As a **developer**, I want to **ensure that all syntax errors are identified and resolved during the code validation process** so that **the code is free from syntax-related issues**.

As a **developer**, I want to **maintain thorough documentation** so that **code is maintained seamlessly in future**.

As a **developer**, I want to **ensure that user stories are thoroughly tested** so that **they meet acceptance criteria and deliver the expected functionality**.

As a **developer**, I want to **deploy the application to Heroku** so that **it is accessible to users online**.

As a **developer**, I want to **ensure that application meets performance and accessibility standards** so that **provides a seamless experience for all users and performs optimally**.

As a **developer**, I want to **update my profile information** so that **I can keep my information current and accurate**.

*************************************************************
### Visitor Stories

As a **visitor**, I want to **visit the developer's GitHub portfolio** so that **I can view their projects and contributions**.

As a **visitor**, I want to **download the developer's resume** so that I can **review their qualifications and consider them for a position.**

As a **visitor**, I want to **view the developer's profile** so that I can **learn more about the developer, contact them, and access their portfolio.**

As a **visitor**, I want the **accessibility features to be improved** so that **to maintain equal access and usability for all users, including those with disabilities.**

As a **visitor**, I want to **visual elements across the platform to be consistent** so that **I can have a cohesive and pleasant user interface experience**.

As a **visitor**, I want to **navigate through the platform effortlessly,** so that **I can find relevant sections and features intuitively.**

As a **visitor**, I want to **utilize advanced display filtering options** so that **content displayed on the platform according to my preferences and requirements.**

As a **visitor**, I want to **able to register an account** so **I can create an account**.

****************************************************

### Registered User Stories

As a **registered user**, I want to **be able to log in and out of my account** so that **I can use the platform**.

As a **registered user**, I want to **to be able to reset my password** so that **I do not loose access to my account**.

As a **registered user**, I want to **manage my profile** so that **I have control of the information held on the platform**.

As a **registered user**, I want to **create posts** so that **I can upload them on the platform**.

As a **registered user**, I want to **edit and delete posts** so that **I can maintain the content up-to-date**.

As a **registered user**, I want to **to be able to comment on posts** so that **provide feedback to authors**.

As a **registered user**, I want to **to be able to delete and edit comments** so that I can **control my engagement on the platform**.

As a **registered user**, I want **the ability to interact with posts and comments by liking, un-liking, and favoriting them,** so that I can **engage with content that resonates with me**.

As a **registered user**, I want to **provide feedback, report issues, and suggest improvements through a contact form,** so that I can **actively participate in improving the platform and receive support when needed**.

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

[Back to top](#contents)

## Database Schema

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