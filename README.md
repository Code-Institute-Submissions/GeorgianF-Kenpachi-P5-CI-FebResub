# **Kenpachi eStore**
The website is a online platform that allows users to purchase high quality katanas, tantos, wakazashis.\ 
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
      * [**Landing page**](#landing-page)
      * [**Story page**](#story-page)
      * [**Contact Us page:**](#contact-us-page)
      * [**Store:**](#store-page)
      * [**Cart page:**](#cart-page)
      * [**Checkout page:**](#checkout-page)
      * [**Login page:**](#login-page)
      * [**Logout page:**](#logout-page)
      * [**Reset password page:**](#reset-password-page)
      * [**User profile page:**](#user-profile-page)
      * [**View order (by ID) page:**](#view-order-page)
      * [**Admin page:**](#admin-page)
      * [**Add product (admin) page:**](#admin-page)
      * [**View Message (admin) page:**](#admin-page)
    * [**Database schema**](#database-schema)
    * [**Color scheme**](#color-scheme)

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
  * ... **receive a email confirmation** so that I can **verify if my account has been successfully created**
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
**Landing page:**
------------------
<img width="751" alt="Screenshot 2023-01-08 at 14 46 55" src="https://user-images.githubusercontent.com/91877102/211199550-e149886a-319f-4a55-9c54-b0875aa09993.png">

**Story page**
------------------
![Screenshot 2023-01-08 at 15 01 45](https://user-images.githubusercontent.com/91877102/211200331-584096fb-bdc8-4a97-9729-3fba6a5f1144.png)

**Contact Us page**
------------------
![Screenshot 2023-01-08 at 15 07 28](https://user-images.githubusercontent.com/91877102/211200660-51eb093d-c5c4-4303-a735-6a7b9aa67eb9.png)

**Store page**
------------------
![Screenshot 2023-01-08 at 15 15 20](https://user-images.githubusercontent.com/91877102/211201073-a825d0ba-50e8-478e-8fab-8027deda83b6.png)

**Cart page**
------------------
![Screenshot 2023-01-08 at 15 19 11](https://user-images.githubusercontent.com/91877102/211201292-0e611744-4f9c-4aa3-a503-a5215e29e2eb.png)

**Checkout page**
------------------
![Screenshot 2023-01-08 at 15 22 13](https://user-images.githubusercontent.com/91877102/211201417-9c7c976c-64bf-40df-b71d-66872d13a2f8.png)

**Login page**
------------------
![Screenshot 2023-01-08 at 15 27 14](https://user-images.githubusercontent.com/91877102/211201681-0933c8d3-1ed0-448f-b6a0-cfa44f67b14f.png)

**Logout page**
------------------
![Screenshot 2023-01-08 at 15 29 01](https://user-images.githubusercontent.com/91877102/211201783-e8a01cce-f436-4b4f-9c29-c3e287c9730a.png)

**Reset password page**
------------------
![Screenshot 2023-01-08 at 15 30 43](https://user-images.githubusercontent.com/91877102/211201892-fcacdfb2-cae5-4964-b72d-5d06e100edc9.png)

**User profile page**
------------------
![Screenshot 2023-01-08 at 15 33 41](https://user-images.githubusercontent.com/91877102/211202074-f24de57b-1813-4a2f-977e-b968020f20aa.png)

**View order (by ID) page**
------------------
![Screenshot 2023-01-08 at 15 36 39](https://user-images.githubusercontent.com/91877102/211202217-8328762a-61c2-43ab-9dd6-79673255c750.png)

**Admin page**
------------------
![Screenshot 2023-01-08 at 15 40 58](https://user-images.githubusercontent.com/91877102/211202435-eba58cc0-555c-4703-b95f-65159a37d9e8.png)

**Add product (admin) page**
------------------
![Screenshot 2023-01-08 at 15 44 36](https://user-images.githubusercontent.com/91877102/211202605-ca9eeeca-26a4-465d-b4b7-c41850dd0159.png)

**View Message (admin) page**
------------------
![Screenshot 2023-01-08 at 15 47 00](https://user-images.githubusercontent.com/91877102/211202724-fa550b38-8d14-434a-95fb-e27f3034a486.png)
