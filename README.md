# **Kenpachi eStore**
The website is a online platform that allows users to purchase high quality katana, tanto, wakazashi.\
The name of the store is based on the characted on Zaraki Kenpachi, from the anime [Bleach](https://bleach.fandom.com/wiki/Kenpachi_Zaraki)\
Although he is known to be a violent fighter, Zaraki's actions tend to be for the best.\
Zaraki lives for battle, and enjoys a good fight more than anything. He even holds back in an effort to make any fight last longer.\
He claims injury and death are nothing but the price one pays for a good fight.\
Despite his tendency to be brutal, Zaraki usually stops a fight if his opponent is too injured to fight back, not interested in fighting "weaklings who can't fight anymore", and he does not feel obligated to deal a death blow to anyone who cannot fight any longer.\
However, he will unhesitatingly kill his opponent if they refuse to stop fighting.

![Screenshot 2023-01-08 at 13 31 27](https://user-images.githubusercontent.com/91877102/211196170-85e027bf-fac1-42c8-bf5e-e032d6c33c44.png)

Deployed site can be found here: [Kenpachi eStore](https://kenpachi-estore.herokuapp.com/)

# **Table Of Contents**
* [**Planning Phase**](#planning-phase)
  * [**Site Objectives**](#site-objectives)
    * [**Feasibility study**](#feasibility-study)
  * [**Structure**](#structure)
    * [**User Stories**](#user-stories)
  * [**Backbone**](#backbone)
    * [**Wireframes**](#wireframes)
      * [**WF Landing**](#wf-landing)
      * [**WF Story**](#wf-story)
      * [**WF Contact Us**](#wf-contact-us)
      * [**WF Store**](#wf-store)
      * [**WF Cart**](#wf-cart)
      * [**WF Checkout**](#wf-checkout)
      * [**WF Login**](#wf-login)
      * [**WF Logout**](#wf-logout)
      * [**WF Reset password**](#wf-reset-password)
      * [**WF User profile**](#wf-user-profile)
      * [**WF View order (by ID)**](#wf-view-order-by-id)
      * [**WF Admin**](#wf-admin)
      * [**WF Admin Add product**](#wf-admin-add-product)
      * [**WF Admin View Message**](#wf-admin-view-message)
    * [**Database schema**](#database-schema)
    * [**Color scheme**](#color-scheme)
* [**Features**](#features)
  * [**Site Navigation**](#site-navigation)
    * [**Navbar**](#navbar)
    * [**Footer**](#footer)
    * [**Home page**](#home-page)
    * [**Contact page**](#contact-page)
    * [**Story page**](#story-page)
    * [**Store page**](#store-page)
    * [**Cart page**](#cart-page)
    * [**Checkout page**](#checkout-page)
      * [**success page**](#success-page)
      * [**canceled page**](#canceled-page)
    * [**Login page**](#Login-page)
    * [**Logout page**](#logout-page)
    * [**Reset password page**](#reset-password-page)
    * [**User profile page**](#user-profile-page)
    * [**View order (by ID) page**](#view-order-by-id-page)
    * [**Admin page**](#admin-page)
    * [**Admin Add page**](#admin-page)
    * [**Admin View Message page**](#admin-page)
    * [**Admin Edit and Delete*](#admin-page)

# **Planning Phase**
## **Site Objectives:**
The online webshop wants to inform the visitors about craftmanship of the products.
All products are hand made from the best available materials.
It's using local source products, and each product is unique do to it's manufacturing process.

## Feasibility study

Kenpachi eStore | Importance | Feasibility
---|---|---
User can make orders | 5 | 5
User can cancel orders | 5 | 5
User can update cart items | 5 | 5
User profile | 5 | 5
Order history | 5 | 5
User log in/log out | 5 | 5
User reset password | 5 | 5
Landing page simple and a clear message | 5 | 5
Manually add/edit/delete products into the store (admin) | 5 | 5
Contact form  | 5 | 5
View products (available and out of stock) | 4 | 5 
Manufacturing process | 2 | 4
Secure payments | 5 | 5 
----------------------------------------|----|----
Totals | 61 | 64

## **Structure**   
The structure of the website is simple, easy to follow for every user, from the nav bar or from the footer.
When developing the website, I have put myself in the shoes of the visitor, and organized the page, so it can be easy to reach.

### **User Stories:**  

* As a **User/Shopper** I can ...
  * ... **register for an account** so that I can **view my profile**
  * ... **receive a order confirmation after payment** so that I can **be sure that the payment was realized and the order was processed**
  * ... **recover my password** so that I can **access my account in case I forgot my password**
  * ... **easy login or logout** so that I can **access my account**
  * ... **click on the nav bar** so that I can **easily navigate to the page of interest**
  * ... **click on the social link** so that I can **visit the social pages**
  * ... **add and see items in the shopping cart** so that I can **identify the total items for the purchase**
  * ... **to see that my card details are safe and secure** so that I can **be safe making the payment**
  * ... **select the quantity** so that I can **make a clear selection**
  * ... **easily add payment details** so that I can **proceed with the payment without hassle**
  * ... **adjust the items in the cart** so that I can **easily change items at checkout**
  * ... **easily view the total of my purchases** so that I can **check regularly my total**
  * ... **see my account** so that I can **view my personal order history**
  * ... **sort the list of products by category** so that I can **find the products in a set category**
  * ... **sort the list of available products** so that I can **easily identify products**
  * ... **search items** so that I can **see if a item is in the store**
  * ... **search products by name or description** so that I can **find a product fast**
  * ... **receive a confirmation with the order** so that I can **have all the details of the order**

* As a **Unregistered User** I can ...
  * ... **send a form** so that I can **send/request information to/from the store**

* As a **Admin** I can ...
  * ... **edit/update items** so that I can **easily adjust the items in the store**
  * ... **add a product** so that I can **add new items to the store**
  * ... **delete an item** so that I can **remove items that are no longer for sale**
  * ... **decrease the stock** so that I can **easily manage the store**
  * ... **search the Customer model** so that I can **easily find customers**
  * ... **filter and search the orders** so that I can **identify them**
  * ... **filter and search the products model** so that I can **check the stock and availability**
  * ... **filter and search the contact us form model** so that I can **see what new messages are sent into the store**
  * ... **delete messages sent to the store** so that I can **avoid having a full inbox/or spams**

## **Backbone**

### **Wireframes**:
**WF Landing**
------------------
<img width="751" alt="Screenshot 2023-01-08 at 14 46 55" src="https://user-images.githubusercontent.com/91877102/211199550-e149886a-319f-4a55-9c54-b0875aa09993.png">

**WF Story**
------------------
![Screenshot 2023-01-08 at 15 01 45](https://user-images.githubusercontent.com/91877102/211200331-584096fb-bdc8-4a97-9729-3fba6a5f1144.png)

**WF Contact Us**
------------------
![Screenshot 2023-01-08 at 15 07 28](https://user-images.githubusercontent.com/91877102/211200660-51eb093d-c5c4-4303-a735-6a7b9aa67eb9.png)

**WF Store**
------------------
![Screenshot 2023-01-08 at 15 15 20](https://user-images.githubusercontent.com/91877102/211201073-a825d0ba-50e8-478e-8fab-8027deda83b6.png)

**WF Cart**
------------------
![Screenshot 2023-01-08 at 15 19 11](https://user-images.githubusercontent.com/91877102/211201292-0e611744-4f9c-4aa3-a503-a5215e29e2eb.png)

**WF Checkout**
------------------
![Screenshot 2023-01-08 at 15 22 13](https://user-images.githubusercontent.com/91877102/211201417-9c7c976c-64bf-40df-b71d-66872d13a2f8.png)

**WF Login**
------------------
![Screenshot 2023-01-08 at 15 27 14](https://user-images.githubusercontent.com/91877102/211201681-0933c8d3-1ed0-448f-b6a0-cfa44f67b14f.png)

**WF Logout**
------------------
![Screenshot 2023-01-08 at 15 29 01](https://user-images.githubusercontent.com/91877102/211201783-e8a01cce-f436-4b4f-9c29-c3e287c9730a.png)

**WF Reset password**
------------------
![Screenshot 2023-01-08 at 15 30 43](https://user-images.githubusercontent.com/91877102/211201892-fcacdfb2-cae5-4964-b72d-5d06e100edc9.png)

**WF User profile**
------------------
![Screenshot 2023-01-08 at 15 33 41](https://user-images.githubusercontent.com/91877102/211202074-f24de57b-1813-4a2f-977e-b968020f20aa.png)

**WF View order by ID**
------------------
![Screenshot 2023-01-08 at 15 36 39](https://user-images.githubusercontent.com/91877102/211202217-8328762a-61c2-43ab-9dd6-79673255c750.png)

**WF Admin**
------------------
![Screenshot 2023-01-08 at 15 40 58](https://user-images.githubusercontent.com/91877102/211202435-eba58cc0-555c-4703-b95f-65159a37d9e8.png)

**WF Admin Add product**
------------------
![Screenshot 2023-01-08 at 15 44 36](https://user-images.githubusercontent.com/91877102/211202605-ca9eeeca-26a4-465d-b4b7-c41850dd0159.png)

**WF Admin View Message**
------------------
![Screenshot 2023-01-08 at 15 47 00](https://user-images.githubusercontent.com/91877102/211202724-fa550b38-8d14-434a-95fb-e27f3034a486.png)

### **Database Schema**:
TODO:

### Color scheme:
I wanted to keep the color scheme as simple as possible, because within the website there are a lot of pictures with the katanas, that I want to showcase.\
The more vibrant colors I did't consider that will add value, and will take away from the objective of the webstore, that is chaftmanship.
I have used for reference the website: [coolers.co](https://coolors.co) after looking for some color pallets into the website 
[shutterstock.com](https://www.shutterstock.com/blog/color-palettes-for-websites) and decided that #24.Fearless Fitness will be a good fit 

In the end I have used the following colors:
- #F5F7F7
- #EDB518
- #79031D
- #000407

![Screenshot 2023-01-08 at 16 04 22](https://user-images.githubusercontent.com/91877102/211204066-5ecd2ea6-e9e1-49e0-ae9f-504f2a3fb3b2.png)

### Typography:
I have user only one font Bangers (uppercase) because it provided the **anime look** that I wanted to achieve.

## Agile Development Process
I have use GitHub to keep track of my progress.
All of the user stories have been logged on **Github** [here](https://github.com/users/GeorgianF/projects/3/views/1)

# **Features**

## **Site Navigation**

### **Navbar**
The menu it's hidden from the view and it can be found by clicking the **MENU** on the left side of the screen
Once the button is clicked, the menu will appear
![Screenshot 2023-01-08 at 16 53 34](https://user-images.githubusercontent.com/91877102/211206283-a6217cd3-d317-4e2d-83ae-1833cebbcbf5.png)
The user has full freedom on the page that he wants to visit, and everything is easy to reach.

### **Footer**
The footer in present throughout the website and it includes the option to subscribe to the newsletter.\
It's including also a few option to quick navigate through the website.

![Screenshot 2023-01-08 at 18 35 24](https://user-images.githubusercontent.com/91877102/211210530-4b24f42b-9d83-44d3-a266-a844ceb41974.png)

The user can find in the footer also the Privacy Policy

The only links that are working into the footer is the [Privacy Policy](https://www.privacypolicygenerator.info/live.php?token=dxge6NpmlPRoOHxFIJMFZxD00w1A3jf8)

![Screenshot 2023-01-08 at 18 37 21](https://user-images.githubusercontent.com/91877102/211210623-8ff025af-9b06-43b3-9ada-1cf0ea113803.png)

Also the user can find the social links, where he can be redirected to the custom [FaceBook page](https://www.facebook.com/profile.php?id=100088979418667)

### **Home page**
The user is greeted with the image of a blacksmith and a video that plays only when the user clicks on the play button.\
A small introduction to the webstore, and a main call to action button, to go to store.
![Screenshot 2023-01-08 at 16 55 52](https://user-images.githubusercontent.com/91877102/211206388-241aae40-239c-4e8e-9348-c2847a790abd.png)

### **Contact page**
From the hidden menu, the user can go to the contact page, where he can find a contact form that he can submit.

![Screenshot 2023-01-08 at 16 58 56](https://user-images.githubusercontent.com/91877102/211206549-c4a16844-d311-44da-b45d-7a34a8c4a010.png)

All fields are required, and a modal pops up upon submission to inform the user of the action:

![Screenshot 2023-01-08 at 17 00 29](https://user-images.githubusercontent.com/91877102/211206605-f4a2fe68-05ed-4e86-941f-8c736f558a9c.png)

A success message appears if the order is succesfull, otherwise a error one appears.

![Screenshot 2023-01-08 at 17 00 58](https://user-images.githubusercontent.com/91877102/211206694-a00b176c-aeb3-479f-8f99-0252945b1849.png)

### **Story page**
From the Menu, the user can navigate to the **Our Story** page, where he can find some short information on how the end product is obtained and what is the process is which the blade is forged.
The are 3 .mp4 videos with the process, for better understanding.

### **Store page**
Here the user can find all the available product in the store.
He has the option to:
- View products (6 at the time, due to pagination)
- Search for products
- Filter by categories
- Move to different pages on the store
- Add to cart
- View individual product

![Screenshot 2023-01-08 at 19 00 04](https://user-images.githubusercontent.com/91877102/211211530-f6b02f84-27f2-4aaf-8357-8c7285b0463e.png)

If an item has stock 0, the button to Add to cart is disabled and a tag "No stock" is displayed

![Screenshot 2023-01-08 at 19 01 10](https://user-images.githubusercontent.com/91877102/211211581-57b01efd-67ba-4a73-a7f2-573199726c3f.png)

If the user is **NOT** logged in, if he tries to add a product into the cart, he will be notified with an alert, but the item will still be added into the cart. If the user creates an account, the cart will then reset.

![Screenshot 2023-01-08 at 19 03 06](https://user-images.githubusercontent.com/91877102/211211680-8b0a47fa-4686-4ab3-881f-ff23155f578c.png)

### **Cart page**
Once the user starts adding items to the cart, he can click on the cart icon and he will be redirected to the cart page.
He can easily check the items that are added into the cart (along with the cart and item total)\
The cart details will contain:
- Image of the product
- Name of the product
- Quantity
- Item price
- Total (the total is per line item)

![Screenshot 2023-01-08 at 19 09 07](https://user-images.githubusercontent.com/91877102/211211902-a80bf067-96ad-44a7-a05d-590816828d85.png)

He/she can easily adjust the quantity, by clicking the icons to increase and decrease the quantity.\
If the quantity of the product is 0, it will be deleted from the cart.\
If the user is ok proceeding with the order, he can click the button to continue to the checkout page.

### **Checkout page**
On the checkout page, the user can see a short Order Summary, with the total to be paid.\
The shipping is free on all orders.\
Payment is managed by Stripe and it has the button to Finish the Order.\
The **shipping details** will be collected onto the next step.
If the user is **Anonymus**, and he click on the button to finish the order, he will be redirected to Sign Up page.

![Screenshot 2023-01-08 at 19 11 16](https://user-images.githubusercontent.com/91877102/211212120-b613cc62-5486-4edb-bdce-3b9eba6c8ae2.png)

I have used the Stripe Checkout to manage the payments, and the email address of the user is autocompleted.\
At this step it will require to enter the shipping details and credit card information

![Screenshot 2023-01-08 at 19 19 33](https://user-images.githubusercontent.com/91877102/211212329-ebf95686-7852-4d4f-8f81-2ad295c0ac87.png)

Once the payment is completed, the user will be redirected to the success page, and the items in the cart are set to 0.

#### **success page**
It can be viewed only of the user has made a successful payment on the previous step.\
Here he has the option to view the order details, or go back to the store. 

![Screenshot 2023-01-08 at 19 20 48](https://user-images.githubusercontent.com/91877102/211212371-80d01ae4-9339-4267-971e-2c6c13989e54.png)

The user is notified also via email with the details of the order:

![Screenshot 2023-01-08 at 19 54 45](https://user-images.githubusercontent.com/91877102/211213726-59b1c4a6-1d0f-4e31-a48e-e11b912eba85.png)


#### **canceled page**
It can be viewed only of the user has cancelled the payment on the previous step.\
A .gif from [The Office](https://www.imdb.com/title/tt0386676/) informs the user that the operation failed.
The cart is **NOT** reset, and he will have the option to redo the payment

![Screenshot 2023-01-08 at 19 26 19](https://user-images.githubusercontent.com/91877102/211213344-59d984ce-1f72-4528-975f-92687896a466.png)

### **Sign up page**
The login page can be accessed from the main navbar that is hidden from the view of the user:

![Screenshot 2023-01-09 at 17 51 00](https://user-images.githubusercontent.com/91877102/211362791-9bb3d218-eb42-4707-8645-fc1ccedc07cb.png)

Or the user can log in from the store, cart, checkout page from the Login Button, next to the cart icon.\

![Screenshot 2023-01-09 at 17 52 04](https://user-images.githubusercontent.com/91877102/211363070-9f9268bd-599e-47f9-9800-049fdad6b955.png)

Once the user initiates the action to log into the account, he will find the login form, where he can sign up to a new account:

![Screenshot 2023-01-09 at 17 58 27](https://user-images.githubusercontent.com/91877102/211364309-2d13ece9-911c-4383-a7bd-c015a9310d2d.png)

All information are required, and once the process is complete, the user will be logged into the account.
A toast Success message will be displayed:

![Screenshot 2023-01-09 at 18 01 40](https://user-images.githubusercontent.com/91877102/211364948-0ebdde26-1405-4896-a96b-b0b7b8fb99e8.png)


### **Login page**
The login page can be accessed from the main navbar that is hidden from the view of the user:

![Screenshot 2023-01-09 at 17 51 00](https://user-images.githubusercontent.com/91877102/211362791-9bb3d218-eb42-4707-8645-fc1ccedc07cb.png)

Or the user can log in from the store, cart, checkout page from the Login Button, next to the cart icon.

![Screenshot 2023-01-09 at 17 52 04](https://user-images.githubusercontent.com/91877102/211363070-9f9268bd-599e-47f9-9800-049fdad6b955.png)

Once the user initiates the action to log into the account, he will find the login form:

![Screenshot 2023-01-09 at 17 53 09](https://user-images.githubusercontent.com/91877102/211363272-31f79042-23ba-4891-b920-a0a92625fe87.png)

It's a form based on the Django Allauth, and it a simple form, where the user needs to input the username and password that was previously created in the signup form.

### **Logout page**
If the user is logged in, and he wants to log out of the account, all that he needs to do is to click on the logout button next to the profile icon and cart icon:

![Screenshot 2023-01-09 at 18 03 07](https://user-images.githubusercontent.com/91877102/211365332-9b374a67-e42a-4c7e-8230-ab21bd356f19.png)

Or from the hidden navbar:

![Screenshot 2023-01-09 at 18 04 38](https://user-images.githubusercontent.com/91877102/211365431-9b716069-fb00-4e49-8007-34a688ffc7ae.png)

If the option is to log out, the user will be redirected to a page to confirm the action.\

![Screenshot 2023-01-09 at 18 06 08](https://user-images.githubusercontent.com/91877102/211365699-3eca1477-7d9e-4473-b9f2-6b98ca4cc8c9.png)

### **Reset password page**
If the user has forgotten the password, he can easily ask to reset it.\
From the previously described, login page, the user can find the button to reset the password.\
He will need to enter the email address of the account and confirm the action:

![Screenshot 2023-01-09 at 18 08 52](https://user-images.githubusercontent.com/91877102/211366545-471cf9a3-1038-44eb-a1ae-bbf34486fdf3.png)

The user will receive and email from the store:

![Screenshot 2023-01-09 at 18 11 57](https://user-images.githubusercontent.com/91877102/211366863-0b97e5e5-8db9-43d8-a7e4-1e6b9ca55565.png)

![Screenshot 2023-01-09 at 18 12 22](https://user-images.githubusercontent.com/91877102/211366925-3c58b759-7d9b-45ee-810f-5fa17a7c9d7d.png)

The user is required to click on the link from the email to reset the password:

![Screenshot 2023-01-09 at 18 12 45](https://user-images.githubusercontent.com/91877102/211367218-d879553c-b825-4e5e-9943-954bcf3a6283.png)

Once the password is correctly entered 2 times, he will be redirected to the password success page:

![Screenshot 2023-01-09 at 18 12 58](https://user-images.githubusercontent.com/91877102/211367347-30509263-4410-4c4c-8dc2-49da26ac8bab.png)
![Screenshot 2023-01-09 at 18 15 25](https://user-images.githubusercontent.com/91877102/211367581-305e7e03-a2de-4213-9f3d-e03c32c9d33f.png)

### **User profile page**
The user has the option to view his order history from within the profile page, that can be accessed from the profile icon, next to the cart icon

![Screenshot 2023-01-09 at 18 19 54](https://user-images.githubusercontent.com/91877102/211368450-5a9f620b-74bb-4b86-9603-c37aefd2c48e.png)

Here he can check his order history, and click on the order number that he wants to see, or go back to the store.\

![Screenshot 2023-01-09 at 18 20 31](https://user-images.githubusercontent.com/91877102/211368647-6e116cc6-59a8-45f4-ab0b-1b74701d3c3d.png)

### **View order (by ID) page**
If the user chooses to see the order details, he needs to click on the button with the transaction number.\
Here he can get all of the details of the order:
- shipping address
- date ordered
- transaction id
- items ordered (image, name, quantity, price)

![Screenshot 2023-01-09 at 18 22 41](https://user-images.githubusercontent.com/91877102/211369248-c9fa2d1c-1194-46ba-857b-de4116e93a19.png)

### **Admin page**
The admin panel can be acessed from the profile icon, in the corner right of the screen, next to the cart icon:

![Screenshot 2023-01-09 at 18 31 28](https://user-images.githubusercontent.com/91877102/211370549-9caff106-c165-4555-b336-de51fc49234e.png)

Here the admin has a few options available:
- go back to the store
- add a product to the store
- edit a product
- delete a product
- view messages incoming from the contact us form

![Screenshot 2023-01-09 at 18 31 56](https://user-images.githubusercontent.com/91877102/211370834-82c1a3a8-fd5f-4693-8627-67e03086e39c.png)

### **Admin Add page**
If the admin wishes to add a product into the store, he can click on the Add a Product button, from within the Admin Panel.\
A form will open, where he can add all of the details of the new item.
If the form is valid, the product will be added to the store:

![Screenshot 2023-01-09 at 18 37 44](https://user-images.githubusercontent.com/91877102/211371720-c1e327ad-c80e-4880-87ef-4ec12075a600.png)

If the form is invalid, the product won't be added to the store, and a toast error message will be displayed, along side with the box that is not entered correctly, and a helper text:
![Screenshot 2023-01-09 at 18 37 22](https://user-images.githubusercontent.com/91877102/211371920-d1ea35c2-6d78-4efd-bcc9-52ff80b5a410.png)
![Screenshot 2023-01-09 at 18 37 29](https://user-images.githubusercontent.com/91877102/211371957-7092c1c4-9575-4b45-bf51-69438770ccd9.png)

Of course, all of these actions will need to be confimed via a modal:

![Screenshot 2023-01-09 at 18 37 14](https://user-images.githubusercontent.com/91877102/211372107-ee799e91-bb61-440a-bbc3-bf1b3cd4c307.png)

If the product is added succesfully to the store, the admin and all of the visitors of the website can imediatly view the item and added to the cart, and finally, order it.

![Screenshot 2023-01-09 at 18 41 29](https://user-images.githubusercontent.com/91877102/211372414-8cdc4312-500a-47a1-a8f7-9215eaf26d40.png)

### **Admin Edit and Delete**
These 2 options are available directly into the store, next to the item that needs to be adjusted or deleted
There are 2 icons:
- a pencil icon: to edit
- a trash icon: to delete

If the actions is to **Edit** the product into the store, the admin needs to click on the pencil icon, and a toast message is displayed:

![Screenshot 2023-01-09 at 18 44 06](https://user-images.githubusercontent.com/91877102/211372997-814fe847-2a1b-423e-a098-d784e3441e79.png)

All of the details of the product are prepoluated with the data from the database.
Once all of the changes to the product have been added/adjusted, the admin needs to click on the button to Save the Product, and a modal will be triggered to confirm the change:

![Screenshot 2023-01-09 at 18 45 28](https://user-images.githubusercontent.com/91877102/211373428-7e32a5dd-72c3-4904-a3ef-d6befcc51ed9.png)

If the form is valid, the item will be saved into the database, and he will be informed about the action:

![Screenshot 2023-01-09 at 18 47 17](https://user-images.githubusercontent.com/91877102/211373555-46f5ba7e-fe0c-4c83-963e-d4b80249071f.png)

If the form is invalid, the item will not be saved into the database, and a toast error message will be displayed, along side with the box that is not entered correctly, and a helper text:

![Screenshot 2023-01-09 at 18 37 22](https://user-images.githubusercontent.com/91877102/211371920-d1ea35c2-6d78-4efd-bcc9-52ff80b5a410.png)
![Screenshot 2023-01-09 at 18 37 29](https://user-images.githubusercontent.com/91877102/211371957-7092c1c4-9575-4b45-bf51-69438770ccd9.png)

If the actions is to **Delete** the product into the store, the admin needs to click on the trash icon, and a modal message is displayed:

![Screenshot 2023-01-09 at 18 49 51](https://user-images.githubusercontent.com/91877102/211374065-7b342c8c-d4b2-437b-b659-e1831bc43bda.png)

If the admin confirms the action, the product will be deleted from the database:\

![Screenshot 2023-01-09 at 18 50 40](https://user-images.githubusercontent.com/91877102/211374271-5ea195a6-fc19-4c5c-9943-5fb39f8476b3.png)

### **Admin View Message page**
In the Admin profile, the Admin can view all the messages that are received through the Contact Form, from the Contact Us page.

![Screenshot 2023-01-09 at 18 52 37](https://user-images.githubusercontent.com/91877102/211374571-463ad328-2682-438e-bd7e-178d7539318b.png)

Here there are some basic information about the message:
- Contact name
- Email
- Date
- Status
- View button
- Delete button

If the actions is to View the message, all of the details of the message that was sent will be prepopulated.
If the actions is to Delete the message, the admin will need to confirm the action from the modal that was triggered:

![Screenshot 2023-01-09 at 18 59 39](https://user-images.githubusercontent.com/91877102/211375864-83197f32-b94d-479c-9e07-9eeeb2def91e.png)

If the actions is confirmed, the message will be delete.
Currently there isn't the option to reply directly from the admin panel, nor to change the status of the email.
This will be a future enhancement, to give more options.
The status of the message can be change, currently, from the Django Admin panel.




