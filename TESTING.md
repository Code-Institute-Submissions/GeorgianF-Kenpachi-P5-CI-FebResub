# **Testing**

## **Validators**

### **W3 Validator @ https://validator.w3.org/**
------------

To able to succesfully test all the pages for errors I had to change the Django templating language from the html,\
For example {% url 'something' %} had to change it to "#". Otherwise it would throw an error as Bad Value.

![Screenshot 2023-01-10 at 19 37 25](https://user-images.githubusercontent.com/91877102/211634559-1ce91656-d4a7-43ce-885d-759f973c0de6.png)

After all the modification have been done, to show a basic html document, I got the following result:

![Screenshot 2023-01-10 at 19 32 41](https://user-images.githubusercontent.com/91877102/211634626-5d0156fd-5124-442e-9ff0-eee9fe50c577.png)

### **CSS Validator** @ https://validator.w3.org/

![Screenshot 2023-01-10 at 19 41 19](https://user-images.githubusercontent.com/91877102/211635165-9e41e65b-5d78-44d0-b8ff-0d6577dd9277.png)

### **PEP8 online** @ http://pep8online.com/
Due to the deprecations on pep8 online i have used the **pycodestyle** linter to check my code throughout development,\ 
as per anouncement made on Slack, [here](https://code-institute-room.slack.com/archives/CPCT0MBKL/p1664380977854349)
No error can be found within the my code

I have also check on the PEP8 developed by Code Institute, the link can be found [here](https://pep8ci.herokuapp.com/#)
All my custom pages had the following result:

![Screenshot 2023-01-10 at 19 56 54](https://user-images.githubusercontent.com/91877102/211637903-1dc8e5c1-433d-4b64-aac9-aba8b20b4bfa.png)

### **JS Validor** @ [https://validator.w3.org/](https://jshint.com/)

No errors:

![Screenshot 2023-01-10 at 20 04 55](https://user-images.githubusercontent.com/91877102/211639270-0eee795e-6eaa-4c0a-8a9c-2708cd1492f5.png)
