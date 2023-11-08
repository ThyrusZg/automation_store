# The Challenge

## 1. Access https://automationteststore.com/
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

