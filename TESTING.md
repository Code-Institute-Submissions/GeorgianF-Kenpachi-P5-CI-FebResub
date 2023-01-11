# **TESTING**

## **Table Of Contents**
* [**Validators**](#validators)
  * [**W3 Validator**](#w3-validator)
  * [**CSS Validator**](#css-validator)
  * [**PEP8 Python**](#pep8-python-validator)
  * [**JS Validator**](#js-validator)
* [**Lighthouse**](#lighthouse)
* [**Manual testing**](#manual-testing)
* [**Bugs and fixes**](#bugs-and-fixes)


## **Validators**

### **W3 Validator**
------------

Test was done on: https://validator.w3.org/

To able to succesfully test all the pages for errors I had to change the Django templating language from the html,\
For example {% url 'something' %} had to change it to "#". Otherwise it would throw an error as Bad Value.

![Screenshot 2023-01-10 at 19 37 25](https://user-images.githubusercontent.com/91877102/211634559-1ce91656-d4a7-43ce-885d-759f973c0de6.png)

After all the modification have been done, to show a basic html document, I got the following result:

![Screenshot 2023-01-10 at 19 32 41](https://user-images.githubusercontent.com/91877102/211634626-5d0156fd-5124-442e-9ff0-eee9fe50c577.png)

### **CSS Validator**
Test was done on: https://validator.w3.org/

![Screenshot 2023-01-10 at 19 41 19](https://user-images.githubusercontent.com/91877102/211635165-9e41e65b-5d78-44d0-b8ff-0d6577dd9277.png)

### **PEP8 Python Validator**
Due to the deprecations on pep8 online i have used the **pycodestyle** linter to check my code throughout development,
as per anouncement made on Slack, [here].(https://code-institute-room.slack.com/archives/CPCT0MBKL/p1664380977854349) \
No error can be found within the my code.

I have also check on the PEP8 developed by Code Institute, the link can be found [here].(https://pep8ci.herokuapp.com/#) \
All my custom pages had the following results:

![Screenshot 2023-01-10 at 19 56 54](https://user-images.githubusercontent.com/91877102/211637903-1dc8e5c1-433d-4b64-aac9-aba8b20b4bfa.png)

### **JS Validator**

Test was done on: [https://validator.w3.org/](https://jshint.com/)

No errors:

![Screenshot 2023-01-10 at 20 04 55](https://user-images.githubusercontent.com/91877102/211639270-0eee795e-6eaa-4c0a-8a9c-2708cd1492f5.png)

### **Lighthouse**

Test was done on: Google Chrome Dev Tools

#### **Home page**

![home](https://user-images.githubusercontent.com/91877102/211873904-1434c323-b3fa-47fa-808b-b500eb2b0b3e.png)

#### **Contact page**

![contact-us](https://user-images.githubusercontent.com/91877102/211873933-a6c77401-5fbe-46ff-8a0a-4f4517ea3967.png)

#### **Story page**

![story](https://user-images.githubusercontent.com/91877102/211873954-34c39ee0-1fcd-4ba6-87cc-57d44e1092d5.png)

#### **Store page**

![store](https://user-images.githubusercontent.com/91877102/211873990-c7a5152d-95d5-4186-bce4-03cb719a65e4.png)

#### **Cart page**

![cart](https://user-images.githubusercontent.com/91877102/211874015-b90e3dcd-27c5-478a-b0bc-e2333146a7d1.png)

#### **Checkout page**

![checkout](https://user-images.githubusercontent.com/91877102/211874029-6e354688-5ecb-4eb1-8641-b81db3fbde17.png)

#### **Sign In page**

![sign-in](https://user-images.githubusercontent.com/91877102/211874049-4b390194-fffb-41b7-bccd-c3d3f969f67f.png)

#### **Sign Up page**

![sign-up](https://user-images.githubusercontent.com/91877102/211874079-c721dba0-43f9-4fc7-b639-01bb82855f64.png)

#### **Reset password page**

![password-reset](https://user-images.githubusercontent.com/91877102/211874121-8cc973e2-cbf3-45be-8add-3775d7a16736.png)

#### **Sign Out page**

![Screenshot 2023-01-11 at 18 24 51](https://user-images.githubusercontent.com/91877102/211874630-1c4f20bf-e413-4032-b6c7-5d230ff1f40f.png)

#### **User profile page**

![user-profile](https://user-images.githubusercontent.com/91877102/211874156-17f66b71-8599-4d09-8537-3c30d25b25a9.png)

#### **View order (by ID) page**

![Screenshot 2023-01-11 at 18 26 23](https://user-images.githubusercontent.com/91877102/211875000-73bd1227-f872-4ac1-9707-5d0220e56aab.png)

#### **Admin page**

![admin-page](https://user-images.githubusercontent.com/91877102/211874190-5597a6a0-815a-48cd-b885-a691736d5be0.png)

#### **Admin Add page**

![admin-add](https://user-images.githubusercontent.com/91877102/211874270-bd51fafc-0930-40fe-ad9d-fe674f49d05f.png)

#### **Admin View Message**

![Screenshot 2023-01-11 at 18 27 40](https://user-images.githubusercontent.com/91877102/211875932-1514ae62-1035-4aff-bcd6-b35c67770309.png)

## Manual testing
Below is a summary of how I manually tested each user story:
* As a **User/Shopper** I can ...
  * | &check; |... **register for an account** so that I can **view my profile**
  * | &check; |... **receive a order confirmation after payment** so that I can **be sure that the payment was realized and the order was processed**
  * | &check; |... **recover my password** so that I can **access my account in case I forgot my password**
  * | &check; |... **easy login or logout** so that I can **access my account**
  * | &check; |... **click on the nav bar** so that I can **easily navigate to the page of interest**
  * | &check; |... **click on the social link** so that I can **visit the social pages**
  * | &check; |... **add and see items in the shopping cart** so that I can **identify the total items for the purchase**
  * | &check; |... **to see that my card details are safe and secure** so that I can **be safe making the payment**
  * | &check; |... **select the quantity** so that I can **make a clear selection**
  * | &check; |... **easily add payment details** so that I can **proceed with the payment without hassle**
  * | &check; |... **adjust the items in the cart** so that I can **easily change items at checkout**
  * | &check; |... **easily view the total of my purchases** so that I can **check regularly my total**
  * | &check; |... **see my account** so that I can **view my personal order history**
  * | &check; |... **sort the list of products by category** so that I can **find the products in a set category**
  * | &check; |... **sort the list of available products** so that I can **easily identify products**
  * | &check; |... **search items** so that I can **see if a item is in the store**
  * | &check; |... **search products by name or description** so that I can **find a product fast**
  * | &check; |... **receive a confirmation with the order** so that I can **have all the details of the order**

* As a **Unregistered User** I can ...
  * | &check; |... **send a form** so that I can **send/request information to/from the store**

* As a **Admin** I can ...
  * | &check; |... **edit/update items** so that I can **easily adjust the items in the store**
  * | &check; |... **add a product** so that I can **add new items to the store**
  * | &check; |... **delete an item** so that I can **remove items that are no longer for sale**
  * | &check; |... **decrease the stock** so that I can **easily manage the store**
  * | &check; |... **search the Customer model** so that I can **easily find customers**
  * | &check; |... **filter and search the orders** so that I can **identify them**
  * | &check; |... **filter and search the products model** so that I can **check the stock and availability**
  * | &check; |... **filter and search the contact us form model** so that I can **see what new messages are sent into the store**
  * | &check; |... **delete messages sent to the store** so that I can **avoid having a full inbox/or spams**

## **Bugs and fixes**
1. Menu button had full width and every time that you clicked on the same line the menu pops
   **Solution**: Adjusted the width of the button to fit content
2. Top product container buttons were not working
   Tried: adjusting the z-index on the button to put them on top, did not work.
   **Solution**: The nav container had a 100vh, pussing the content to the bottom of the page
3. Line image on the cart was not displaying
   **Solution**: had to adjust the  {{ product.imageURL }} into {{ item.product.imageURL }}
4. Pause image on the home page was not showing in the deployed app
   **Solution**: changed the scr to match the AWS path
5. Image field on the add product form in the admin panel did not upload the file to the correct path.
   **Solution**: I had to modify the Product Model to tell it where to upload, and use the [ClearableFileInput](https://docs.djangoproject.com/en/2.2/ref/forms/widgets/#django.forms.ClearableFileInput) widget in the form.
6. Contact form was displaying “Opps Error…” from the beggining
   **Solution**: I corrected the view, and moved the else statement in the nested if statement and defined the form variable at the top of the function.
   
**NO** other bugs have been identified.
For each issue found, I have created also one in Github Project [here](https://github.com/users/GeorgianF/projects/3)

[Back to Readme](README.md)

