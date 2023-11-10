# The Challenge

## 1. Access https://automationteststore.com/
- Click on the link above
## 2. Create a Test Coverage Plan:
- a. Analyze the website and document 3 major user scenarios.
- b. Based on these scenarios, create a test coverage plan 
detailing how you’d approach testing each scenario.

## Answer:
### a. Analyze the website and document 3 major user scenarios.
### 1. Create account and login 
This scenario is designed to check basic account creation and usability of newly created account

In this scenario user will do following:
- User navigates to account/login page
- User selects 'I am a new customer'
- User creates new account on account/create page
- User logs in with newly created account on account/login page

### 2. Search for specific product and add it to cart
This scenario is designed to check that home page is accessible, that user can search for specific product , that user
can search for product in different category and finally add found product to cart

In this scenario user will do following:
- User navigates to home page (/)
- User searches for specific product in specific product category
- User adds product to the cart

### 3. Checkout and finalizing payment

This scenario is designed to check that user can successfully click on checkout page and finalize the payment of the
goods. Precondition for this scenario is that user is successfully logged in and that user has product in cart.

In this scenario user will do following:
- User navigates to checkout page
- User adds payment information
- User successfully finishes the payment

### b. Based on these scenarios, create a test coverage plan detailing how you’d approach testing each scenario.

### For account creation and login:
- Testing whole process of user registration with valid credentials
- Testing invalid data such as invalid e-mail format 
- Testing maximum and minimum character length for each input field, weak and strong password testing 
- Testing that error messages are displayed when invalid data is imputed or data that is not satisfying input field
requirements 
- This page does not have e-mail confirmation, but usually also email confirmation or code confirmation is tested
- Test login with valid credentials, whole process
- Test login with invalid credentials such as invalid username or password or non-existing user

### For searching for specific product and adding it to the cart
- Verifying that web page is successfully loading and displaying all required elements and data
- Testing links, buttons, dropdown lists if they lead to correct destinations
- Testing search functionality and checking search results
- Testing different product categories and checking that each product has price, name, image and that if it is available
can be added to the cart
- Testing that each product can be opened in detailed view and that data inside details is matching product
- Testing that each product that is on sale has sale mark and old + new price
- Testing that product that is out of stock can't be added to the cart
- Testing that all products that are added to cart are displayed in correct order and in correct quantity

### For checkout and finalizing payment
- Check that correct data is visible for shipping, payment and items in cart
- Check that shipping info can be edited
- Check that payment infor can be edited
- Check that cart can be edited
- Check that coupon can be applied for discount
- Check that total amount is correct
- Check that each item in cart has correct price
- Usually sites have more payment methods, this one has only pay on delivery so there is no check for payment methods
- Check that order can be confirmed and that success message is displayed

### Additional checks that can be performed 
- Testing website on different browsers (Safari, Chrome, Firefox, Brave browser, Edge) -> Cross browser testing
- Testing website on different devices (Desktop, mobile, tablet) -> Cross device testing
- Performance and load testing -> using tools like k6 or locust to test how well website is handling multiple users
- There are more tests that can usually be executed, but this site does not support such features
(translations, localizations)

## 3. Automation Testing:
### a. Propose an automation testing framework for the website.
- My proposal for automation testing framework is pytest with playwright plugin/library.
- Playwright is user-friendly, easy to learn, and it is well documented. Same goes for pytest.
- Other frameworks that can be used is selenium or cypress. I would use selenium in combination with python.

### b. Design automation test cases for three of the scenarios you’ve identified.
- Automation test cases are located in automation_store/tests.
In Pages there is example of POM (Page object model) where each class represents one page. If there will be time
I will prepare all test cases to work with POM, if not I will only demonstrate that test case is executing.
- How to start test cases is in RunTests.md
- Also check InstallRequirements.md

## 4. Manual Testing:
### a. Highlight 3 areas/features of the website that you believe should primarily be tested manually. 
### b. Justify your choices.
### 1. User Interface (UI)

-  This area of testing is to check that web page visual design, fonts, colors, layouts are looking like they should, 
how it is specified in the documentation. Also, here is tested that all products have correct image, description, price.
UI can be automated, and there are tools that can check if image is correct like "tesseract ocr" but that is expensive
to automate

### 2. User experience and Exploratory testing (UX)

- This area of testing is to check that web page is running smoothly, that transitions are good, that everything that
is hard to detect with automated tests can be checked. Basically this area is for aesthetics and how does it feel in
hands of a human. Exploratory testing is also part of manual testing, where lots of issues can be detected. Usually it
results in some edge case scenarios, but it is important to take care of them.

### 3. Checkout process and payment

- This is for end-to-end testing, checking entire flow of the web page and checking that 
payment can be performed. This is put in both manual and automated test cases because this is the most important part 
of every web page that is supporting payment. If payment does not work, how users will be able to buy ?
Also, usually when websites are supporting more payments methods like bank or PayPal or some other method, confirmation
from bank mobile application or mail confirmation is required. And that usually is checked by hand.

### Why did I select those three areas
- Cost/benefit -> Some areas are hard to automate and expensive to automate and tester can manually check feature in few
seconds, than there is no need to automate it
- Complexity -> Complex scenarios like UI/UX checking, and how some elements react to resizing, how long does it take to
transition... usually complex stuff that is hard to automate is also checked manually
- Exploratory testing -> testers manually can check areas that can be missed by automated tests 
because manual testing is human testing. Humans will be using website, so it is important that tests are executed like
humans would
- By manually testing whole process,flow of the web page from searching product, adding it to cart and payment process,
tester can provide valuable feedback to designers and developers how it can be easier to perform some steps.

## 5. API Testing:
### a. Assume the website has endpoints for product listings, user registration, and order placements.

- /
### b. Propose potential test cases for these API endpoints
### User registration

- Check that user can successfully register when all mandatory data is provided and valid
- Check that response of that api call is unique ID for the user
- Check that response for successful registration will return correct status code
- Check that user cannot register if all mandatory data is not provided
- Check that response contains correct error message
- Check that user cannot register if wrong data type is sent in request
- Check that response contains correct error message for invalid data type
- Check that invalid register will return correct status code
- Check that valid method can create user (POST)
- Check that user cannot register with name that is already taken and that response is containing correct error message
- Check that user cannot register with email that is already taken and that response is containing correct error message

### Product listing

- Check that request will return list of products
- Check that product that are returned are correct (correct data)
- Check that specific product can be returned
- Check that non-existing product will give correct error message and status code
- Check that correct method is used for getting products (GET)
- Check that large number of products can be received

### Order placement

- Check that only user that is logged in can place order
- Check that response for valid order will return user ID of the user which is placing an order
- Check that order placement is using correct method
- Check that order placement data is correct (both request and response)
- Check that order without product cannot be placed
- Check that all responses have valid status code
- Check that all invalid requests have valid/correct error message
- Check that order number is received when order is completed
- Check that unauthorized user cannot place order