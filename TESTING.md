
  # Testing

Return back to the [README.md](README.md) file.


- [Testing](#testing)
  * [Bugs Fixed](#bugs-fixed)
  * [Responsiveness Tests](#responsiveness-tests)
  * [Code Validation](#code-validation)
    + [HTML](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Python](#python)
  * [User Story Testing](#user-story-testing)
  * [Feature Testing](#feature-testing)
  * [Accessibility Testing](#accessibility-testing)
  * [Lighthouse Testing](#lighthouse-testing)
  * [Browser Testing](#browser-testing)

## Responsiveness Tests

To test the responsiveness, I have launched the website very early on. I followed the mobile-first strategy and verified all of my modifications using the DevTools browsers for Google Chrome and Microsoft Edge. Deployed versions were tested using the external website [Responsive Design Checker](https://responsivedesignchecker.com/ "Responsive Design Checker"). The [Am I Responsive](https://ui.dev/amiresponsive "Am I responsive") website was another external source that was used to obtain a unified view of different device breakpoints.

I have also used Google Chrome's Mobile Simulator extension to evaluate the responsiveness of even more specialized devices. Device samples were examined for navigation, element alignment, content layout, and functionality concerns at different breakpoints.

Final Test Results:

| Size | Device Example     | Navigation | Element Alignments | Content Placement | Functionality | Notes                             |
| ---- | ------------------ | ---------- | ------------------ | ----------------- | ------------- | --------------------------------- |
| sm   | Samsung Galaxy S20 | &check;    | &check;            | &check;           | &check;       |                                   |
| sm   | iPhone 11 PRO      | &check;    | &check;            | &check;           | &check;       |
| sm   | iPhone 13 PRO MAX  | &check;    | &check;            | &check;           | &check;       |
| md   | iPad MINI          | &check;    | &check;            | &check;           | &check;       |                                   |
| md   | Galaxy Tab S7      | &check;    | &check;            | &check;           | &check;       |                                   |
| md   | iPad Air           | &check;    | &check;            | &check;           | &check;       |                                   |
| lg   | iPad Pro           | &check;    | &check;            | &check;           | &check;       | Update About section image sizing |
| xl   | Mackbook Air       | &check;    | &check;            | &check;           | &check;       |                                   |
| xl   | HP Stream Laptop   | &check;    | &check;            | &check;           | &check;       |                                   |
| xxl  | Dell Lattitude     | &check;    | &check;            | &check;           | &check;       |                                   |
| xxl  | Desktop            | &check;    | &check;            | &check;           | &check;       |                                   |

[Back to top](#contents)


## Code Validation

### HTML

### CSS

The [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) tool, provided by the W3C, enables to validate and verify the correctness of CSS code. It ensures that your web pages adhere to W3C standards, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|CSS file | No errors |<details><summary>Result Summary</summary>![Result](docs/testing.md/validations/css-test.png)</details>| ✅


### JavaScript

### Python

The python files have all been passed through [PEP8 CI Online](https://pep8ci.herokuapp.com/)

<details><summary><b>PEP8 Test Results</b></summary>

**run.py:**

![run.py](docs/pep8-run-py-result.png)

</details><br/>

## Automated Testing



### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal:

`python manage.py test`

## Defensive Programming Testing

Defensive programming testing involves verifying that the defensive measures implemented in the code are effective. 


- Negative Testing: Provide invalid or unexpected inputs to the application to see how well it handles errors and exceptions.

### Role-based restrictions

## Bugs Fixed

## Browser Compatibility

The deployed project was tested on the most popular browsers for compatibility issues.
No major issues identified. 

[Browser Testing Results](/docs/testing.md/browser-testing.pdf)

## User Story Testing

**Developer User Stories**


| User Story                                                                                                     | Acceptance Criteria Complete | Notes                                                                                                            |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Adopt Agile Methodology](https://github.com/Indre-V/blossom-therapy/issues/9#issue-2302892613)                | ✅                            | Documented in README.md                                                                                          |
| [Design Database Schema](https://github.com/Indre-V/blossom-therapy/issues/10#issue-2302944970)                | ✅                            | Database design documented in README.md                                                                          |
| [Create Wireframes](https://github.com/Indre-V/blossom-therapy/issues/11#issue-2302950413)                     | ✅                            | Wireframes documented in README.md                                                                               |
| [Design Visuals](https://github.com/Indre-V/blossom-therapy/issues/12#issue-2303047004)                        | ✅                            | Design process documented in README.md                                                                           |
| [Create Django Project](https://github.com/Indre-V/blossom-therapy/issues/14#issue-2303105943)                 | ✅                            | Git commit [548ffe2](https://github.com/Indre-V/blossom-therapy/commit/548ffe2c2b877163958e9e8c22e90f9ed1afc997) |
| [Initial Deployment to Heroku](https://github.com/Indre-V/blossom-therapy/issues/15#issue-2303122957)          | ✅                            | Git commit [8c7d0f4](https://github.com/Indre-V/blossom-therapy/commit/8c7d0f44072c5897084b06c738a39a6eed9f4037) |
| [Update Developer Profile](https://github.com/Indre-V/blossom-therapy/issues/51#issue-2308275825)              | ✅                            | Available in Django Admin Panel                                                                                  |
| [Performance Optimization](https://github.com/Indre-V/blossom-therapy/issues/41#issue-2304290974)              | ✅                            | Results documented in TESTING.md                                                                                 |
| [Code Validation](https://github.com/Indre-V/blossom-therapy/issues/44#issue-2304298110)                       | ✅                            | Results documented in TESTING.md                                                                                 |
| [Comprehensive Project Documentation](https://github.com/Indre-V/blossom-therapy/issues/45#issue-2304301021)   | ✅                            | Comprehensive README.md and TESTING.md                                                                           |
| [User Story Testing](https://github.com/Indre-V/blossom-therapy/issues/46#issue-2304303369)                    | ✅                            | Results documented in TESTING.md                                                                                 |
| [Heroku Deployment](https://github.com/Indre-V/blossom-therapy/issues/47#issue-2304304912)                     | ✅                            | Git commit [23f1988](https://github.com/Indre-V/blossom-therapy/commit/23f1988a49387c9e13add7e08afa4e5b6769dc7c) |
| [Performance and Accessibility Testing](https://github.com/Indre-V/blossom-therapy/issues/48#issue-2304308035) | ✅                            | Results documented in TESTING.md                                                                                 |

**Visitor User Stories**

| User Story                                                                                                        | Acceptance Criteria Complete | Screenshot/Notes                                                                                                |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [User Registration](https://github.com/Indre-V/blossom-therapy/issues/17#issue-2303311873)                        | ✅                            |  <details><summary>Screenshot</summary>![Registration](/docs/testing.md/userstories/user-reg.png)</details>     |
| [Display Filter](https://github.com/Indre-V/blossom-therapy/issues/37#issue-2304284083)                           | ✅                            |  <details><summary>Screenshot</summary>![Filter](/docs/testing.md/userstories/filter.png)</details>             |
| [View Developer Profile](https://github.com/Indre-V/blossom-therapy/issues/50#issue-2308263786)                   | ✅                            |  <details><summary>Screenshot</summary>![About](/docs/testing.md/userstories/about.png)</details>               |
| [Access Developer's Resume](https://github.com/Indre-V/blossom-therapy/issues/52#issue-2308280758)                | ✅                            |  <details><summary>Screenshot</summary>![CV-Link](/docs/testing.md/userstories/cv-link.png)</details>           |
| [Navigate to Developer's GitHub Portfolio](https://github.com/Indre-V/blossom-therapy/issues/53#issue-2308294861) | ✅                            |  <details><summary>Screenshot</summary>![About-Footer](/docs/testing.md/userstories/about-footer.png)</details> |
| [Implement Navigation Experience](https://github.com/Indre-V/blossom-therapy/issues/38#issue-2304286025)          | ✅                            | Summary documented in README.md                                                                                 |
| [Visual Consistency](https://github.com/Indre-V/blossom-therapy/issues/39#issue-2304287983)                       | ✅                            | Summary documented in README.md                                                                                 |
| [Accessibility Enhancement](https://github.com/Indre-V/blossom-therapy/issues/40#issue-2304289636)                | ✅                            | Test results documented in TESTING.md                                                                           |
| [Developer Feedback and Support](https://github.com/Indre-V/blossom-therapy/issues/34#issue-2304132868)           | ✅                            |  <details><summary>Screenshot</summary>![Contact-Form](/docs/testing.md/userstories/contact-form.png)</details> |


**Registered User Stories**

| User Story                                                                                                   | Acceptance Criteria Complete | Screenshot                                                                                                              |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [User Login and Logout Functionality](https://github.com/Indre-V/blossom-therapy/issues/18#issue-2303341463) | ✅                            |  <details><summary>Screenshot</summary>![Log](/docs/testing.md/userstories/login.png)</details>                         |
| [Password Reset](https://github.com/Indre-V/blossom-therapy/issues/19#issue-2303364772)                      | ✅                            |  <details><summary>Screenshot</summary>![Password-Reset](/docs/testing.md/userstories/password-reset.png)</details>     |
| [Profile Management](https://github.com/Indre-V/blossom-therapy/issues/20#issue-2303381892)                  | ✅                            |  <details><summary>Screenshot</summary>![Profile](/docs/testing.md/userstories/profile-view.png)</details>              |
| [Create New Insight](https://github.com/Indre-V/blossom-therapy/issues/22#issue-2304082436)                  | ✅                            |  <details><summary>Screenshot</summary>![Add-Insight](/docs/testing.md/userstories/add-insight.png)</details>           |
| [Manage Insight](https://github.com/Indre-V/blossom-therapy/issues/23#issue-2304088784)                      | ✅                            |  <details><summary>Screenshot</summary>![Manage-Insight](/docs/testing.md/userstories/manage-insight.png)</details>     |
| [Add a Comment](https://github.com/Indre-V/blossom-therapy/issues/24#issue-2304095247)                       | ✅                            |  <details><summary>Screenshot</summary>![Add-Comment](/docs/testing.md/userstories/add-comment.png)</details>           |
| [Manage Comments](https://github.com/Indre-V/blossom-therapy/issues/25#issue-2304099460)                     | ✅                            |  <details><summary>Screenshot</summary>![Manage-Comment](/docs/testing.md/userstories/manage-comment.png)</details>     |
| [User Interaction with Posts](https://github.com/Indre-V/blossom-therapy/issues/29#issue-2304113934)         | ✅                            |  <details><summary>Screenshot</summary>![User-Interaction](/docs/testing.md/userstories/user-interaction.png)</details> |
 

**Admin User Stories**

| User Story                                                                                           | Acceptance Criteria Complete | Notes                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [User Content Approvals](https://github.com/Indre-V/blossom-therapy/issues/28#issue-2304109153)      | ✅                            | Comments can be edited and deleted by admin in front end. The same functionality is available in backend admin panel as well. There is an extra tab for superusers in navigation to view and manage pending posts. |
| [Administration Content CRUD](https://github.com/Indre-V/blossom-therapy/issues/27#issue-2304105029) | ✅                            | Superusers can manage user profiles via admin portal. Insights and Comments can also be managed in front and backend. Admin users have an extra option to post insights without requiring an approval.             |


## Lighthouse Testing

Blossom-Therapy was tested in the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and [Microsoft Edge Dev Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/open/?tabs=cmd-Windows) using Lighthouse Testing tool which inspects and scores the website for the following criteria:

* Performance - how quickly a website loads and how quickly users can access it.
* Accessibility - test analyses how well people who use assistive technologies can use your website.
* Best Practices - checks whether the page is built on the modern standards of web development.
* SEO - checks if the website is optimised for search engine result rankings.

Initial Lighthouse tests returned an error *Background and foreground colors do not have a sufficient contrast ratio.*. This was due to the button font in the Profile Section. Once the font was updated, the Accessibility score returned 100.

<details><summary><b>Lighthouse Test Results</b></summary>

| Page                 | Status          | Size    | Screenshot                                                                     | Notes                                             |
| -------------------- | --------------- | ------- | ------------------------------------------------------------------------------ | ------------------------------------------------- |
| Home                 | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/logged_out_home_desktop.png )        |                                                   |
| Home                 | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/logged_in_home_desktop.png )         |                                                   |
| Home                 | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/logged_out_home_mobile.png )         |                                                   |
| Home                 | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/logged_in_home_mobile.png )          |                                                   |
| Insights             | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_insights_desktop.png )       |                                                   |
| Insights             | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_insights_desktop.png )      |                                                   |
| Insights             | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_insights_mobile.png )        |                                                   |
| Insights             | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_insights_mobile.png )       |                                                   |
| Add Insight          | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_add_insight_mobile.png )    |                                                   |
| Add Insight          | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_add_insight_desktop.png )   |                                                   |
| Pending Approvals    | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_pending_mobile.png )        |                                                   |
| Pending Approvals    | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_pending_desktop.png )       |                                                   |
| Profile - private    | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_profile_mobile.png )        |                                                   |
| Profile - private    | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_profile_desktop.png )       |                                                   |
| Profile - public     | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_profile_public_mobile.png )  |                                                   |
| Profile - public     | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_prof_public_desktop.png )    |                                                   |
| Profile - public     | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_prof_public_mobile.png )    |                                                   |
| Profile - public     | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_prof_public.png )           |                                                   |
| Profile - Insights   | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_prof_insights_mobile.png )   |                                                   |
| Profile - Insights   | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_prof_insights.png )          |                                                   |
| Profile - Insights   | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_prof_insights.png )         |                                                   |
| Profile - Drafts     | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_prof_drafts.png )           |                                                   |
| Profile - Drafts     | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_prof_drafts_mobile.png )    |                                                   |
| Profile - Favourites | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_prof_favs_desktop.png )     |                                                   |
| Profile - Favourites | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_prof_favs_mobile.png )      |                                                   |
| Profile - Update     | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/prof_update_desktop.png )            |                                                   |
| Profile - Update     | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/prof_update_mobile.png )             |                                                   |
| Change-Password      | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/change_pass_desktop.png )            |                                                   |
| Change-Password      | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/change_pass_mobile.png )             | Accessibility score of 96 due to button contrast. |
| Delete-Account       | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/del_acc_desktop.png )                |                                                   |
| Delete-Account       | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/del_acc_mobile.png )                 | Accessibility score of 95 due to button contrast. |
| Insights-Detail      | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_insights_dets_desktop.png ) |                                                   |
| Insights-Detail      | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_insights_dets_mobile.png )  |                                                   |
| Insights-Detail      | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_insight_dets_desktop.png )   |                                                   |
| Insights-Detail      | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_insight_dets_mobile.png )    |                                                   |
| Edit-Comment         | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_edit_comment_desktop.png )  |                                                   |
| Edit-Comment         | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_edit_comment_mobile.png )   |                                                   |
| Contact-Form         | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_contact_mobile.png )         |                                                   |
| Contact-Form         | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_contact_mobile.png )        |                                                   |
| Contact-Form         | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_contact_desktop.png )        |                                                   |
| Contact-Form         | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_contact_desktop.png )       |                                                   |
| About                | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_about_desktop.png )          |                                                   |
| About                | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_about_desktop.png )         |                                                   |
| About                | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_about_mobile.png )           |                                                   |
| About                | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_about_desktop.png )          |                                                   |
| Search-Results       | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_search_desktop.png )         |                                                   |
| Search-Results       | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_search_desktop.png )        |                                                   |
| Search-Results       | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_search_mobile.png )          |                                                   |
| Search-Results       | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_search_mobile.png )         |                                                   |
| Category-filter      | Visitor         | Desktop | ![screenshot](/docs/testing.md/lighthouse/visitor_cat_filter_desktop.png )     |                                                   |
| Category-filter      | Registered User | Desktop | ![screenshot](/docs/testing.md/lighthouse/reg_user_cat_filter_desktop.png )    |                                                   |
| Category-filter      | Visitor         | Mobile  | ![screenshot](/docs/testing.md/lighthouse/visitor_category_mobile.png )        |                                                   |
| Category-filter      | Registered User | Mobile  | ![screenshot](/docs/testing.md/lighthouse/reg_user_category_mobile.png )       |                                                   |

</details><br/>

[Back to top](#contents)


## Accessibility Testing

[WAVE](https://wave.webaim.org/) online tool was used to check terminal colour contrast.

While building the application, the general principles of accessibility where adhered to: 

- Using clear instructions
- Asking for user input before continuing
- Validating inputs before moving on to the next step
- Testing the game to make sure it does not crash from user input
- Using ARIA labels in the README

![WAVE](/docs/testing.md/summary.png)