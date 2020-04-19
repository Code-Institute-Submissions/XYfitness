# XYfitness

[![Build Status](https://travis-ci.org/brianscan14/XYfitness.svg?branch=master)](https://travis-ci.org/brianscan14/XYfitness)

This Django website was created as a means for an aspiring personal fitness or "PT" trainer to display their talents or capabilities to the general public, and potentially attract new clients. Whether this results in them purchasing a plan for exercise or routine to follow, or even if they purchase an item of clothing. This results in a revenue stream for the PT and means of getting their product out on the market and their clientele growing in stature. 

Users are encouraged to sign up to the website in order to create a profile, this will allow them to purchase products, leave reviews and the usual profile features by being able to edit their picture, password and add additional details such as first name, email, etc. However the user can still browse many parts of the page freely without needing an account, this is the encourage freedom of the site and to get the user to browse it more and get a feel for it, without being put off by having to sign in straight away. In order to purchase any products the user will then need to create an account. 

## UX

The main goal of the website is to convince customers that this is the PT that they need, and that his plans are the best ones to get on the market. This is accomplished by a combination of a sleek, professional design and many reviews and testimonials from current customers to persuade the user to use this PT. The pages are kept sleek and interactive so as to allow the user to easily navigate around the site.  The navbar at the top enkeeps with this theme and allows the users to navigate to each page with ease, decreasing to a menu icon on smaller screen sizes.

The hero image on the index page take up the entire and lets the user know the purpose of the site straight away, grabbing their attention. If the user just wants to search a product quickly then they can utilise the search icon in the nav bar which calls an overlay that has a search bar, which searches the DB for names matching the string inputted by the user. The user can also easily navigate to the about or contact page, if they want to find out more about the PT. All products also have a review rating from customers, if they have left one. And the testimonials page shows previous customers experiences and even before and after pics if they have left one.

### User Stories

1. As a new visitor to the website, I want to be easily navigate the site and find information I was looking for in one or two clicks.
2. As a new visitor, when browsing the site I want the site to be coherent and responsive, whether I am using a laptop, tablet or phone.
3. As a new visitor, when filling out forms or entering data I want reasonable feedback to tell me whether I was either successful, or unsuccessful, and what the error is. 
4. As a new visitor, when browsing the website  want it to have a professional feel and make me want to use this PT.
5. As a new visitor, when searching the site I want to know from other customers whether this PT is a good one or not.
6. As a new visitor, when browsing the products I want them to be presented to me in a tidy and easily readable/viewable manner.
7. As a new visitor, when viewing products, I want to get as much information from them as possible to see what the exercise plan may entail or incorporate.
8. As a new visitor, when browsing the products I want to be able to filter them by their types and sort them by features such as price or name.
9. As a new visitor, when browsing the site I want to be able to find out more information about the PT in an easy manner without having to go through a myriad of pages or open new browser sessions.
10. As a potential customer, when browsing the site I want to get a feel of the content that this PT offers, and the information that they offer so that I know the product will be the same.
11. As a potential customer, when purchasing the product I want to be able to change my mind in the cart if I want a different size or product.
12. As a potential customer, when purchasing a product I want the user experience to be slick and to flow in the correct, logical manner when putting in my details.
13. As a potential customer, when purchasing a product, I want my cart items to be viewable when I am filling out my checkout details.
14. As a returning customer, I want to be able to leave a testimonial or review for a product that I used, and rate it, whether it was good or bad.
15. As a returning customer, I want to be able to alter or delete my review if I change my mind on the product.
16. As a returning site user, i want to be able to edit my profile settings or details as I please.

## Wireframes



## Technologies

### Front End

- This project uses Html, JavaScript & CSS programming languages.
- [Bootstrap](https://getbootstrap.com/)
  - Used to make the website more responsive and streamline the grid layout.
- [jQuery](https://jquery.com/)
  - Used for the navbar, also the modal and to simplify DOM manipulation.
- [Popper.js](https://popper.js.org/)
  - A reference JS needed for the navbar & modal.
- [FontAwesome](https://fontawesome.com/)
  - The site used BootstrapCDN to provide icons from FontAwesome.
- [Autoprefixer](https://autoprefixer.github.io/)
  - Used to validate the CSS code for all browsers.
- [Jasmine](https://jasmine.github.io/)
  - To run automated tests for the JS code.
- More...

### Back End

- [Django](https://www.djangoproject.com/)
  - Django framework used to build the app.
- [PIP](https://pip.pypa.io/en/stable/installing/)
  - To install tools used in the project.
- [Travis](https://travis-ci.org/)
  - To verify build.
- [Stripe](https://stripe.com/ie)
  - Online payment platform for taking payments.
- [AWS S3 Bucket](https://aws.amazon.com/s3/)
  - To store static files and media content from the site on a server.
- [Gunicorn](https://gunicorn.org/)
  - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX, to deploy to Heroku.
- [Psycog2](https://pypi.org/project/psycopg2/)
  - PostgreSQL database adapter for Heroku.
- [PostgreSQL](https://www.postgresql.org/)
  - Open Source Relational Database for Heroku.
- [SQlite](https://www.sqlite.org/index.html)
  - In-process library used when developing the website.
- More..

## Features

#### *Elements common to all pages*

##### Navbar:

The navbar can be divided into two type, small screen sizes and screen sizes above small. The pages consist of; home, about, contact, shop, testimonials, cart and depending on whether the user is signed in or not, login, signup, log out or view profile. There is a search icon on both screens for easier interaction with the user, when hovered all pages will change colour to signify it is a clickable option. The nav header is the short name of the page and this is in bolder and larger font to notify the users of this fact, when clicked it will bring them back to the home page. It is positioned at the top of the page for better recipe viewing experience. The user can easily be returned to the navbar's location by clicking the up arrow which brings them to the top of the page.

*Small screen*:

The navbar is a burger icon with a vertical collapsible list of the pages when clicked to easily navigate the website. The pages pop down in a list form under the header as a collapsible list and the user can can click one of these and they are brought to said page. The shopping bag and search icons here are just words, so as to not disturb the uniformity of the collapsible content list. The shopping bag title has the number of items currently in the bag in brackets after the title.

*Larger screen:*

For bigger screens the navbar is displayed as a list of titles of the pages in a horizontal fashion. Again, the overlay for searching can be called by clicking the search icon. In larger screens this and the shopping bag icon are pushed to the right side of the nav, along with the user's profile name if signed in. If not signed in the the profile is replaced by register or login titles. The shopping bag icon attached a green badge to it when an item is added to the cart to signify how many items are currently in it.

##### Footer:



**Scroll Top button**

This button appears on all screen sizes but is mainly for use with the smaller screens as a handy means for the user to scroll to the top of the screen when clicked. It will appear after 80px of scrolling as an 'up' directional arrow which will allow the user to know its function. Once clicked it bring you back to the start of the page. It also changes colour on hover to notify the user that it is clickable and uses CSS to position itself at the bottom right of the screen, with a higher z-index to make sure it isn't covered by any html content.

**Search Icon**

The navbar uses a search icon in the shape of a magnifying glass which when clicked will call an overlay that covers the whole page. This overlay has less opacity to still show the user the page they were on, but in the 'background'. The overlay itself keeps to the pages colour scheme and consists of a search bar with a simple search button. This search bar searches the DB for products that match the sting searched.

**Color Scheme**

The site conforms to a very uniform colour scheme across the entire page, there are slight variations on buttons or icons hover but mainly just opacity changes. The scheme mainly stems from the following [Bootstrap theme](https://bootswatch.com/lux/), which gives the page the intended professional/cool design desired, convincing the customers to us this page. [Coolors](https://coolors.co/) website was used for the varying background colours, seen in the [about](https://xyfitness.herokuapp.com/page/about/) and [home](https://xyfitness.herokuapp.com/) pages, for example. This scheme is employed throughout the website and gives the user a more pleasant and immersive viewing experience. 

#### Home Page

##### Hero Image

The user is first presented when the y load the page by a hero image which consists of a darkened brick wall and some hero text as well. The image is taken from [Pexels](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/) and is fixed, it also ties in very well with the sub-text, telling the user to "build a better foundation". It serves a purpose as the user immediately knows what the purpose of this site is from their initial arrival. The button to learn more then scrolls the user down to the section on the page which tells them what this page offers, and how this PT works.

##### Info Section

The next section to scroll to then is what gives the user more of an insight in to how the PT works. This is achieved by stating the 3 pillars of how he operates to improve you on; physically, mentally and eating habits. Each pillar has a little paragraph describing what he means by them and how he plans on improving you in that category. The user is then encouraged to start their journey and click on the button which will then redirect them to the products page.

##### Testimonials slideshow

The user is then presented with a series of testimonials from previous clients in a slideshow fashion. Each of these slides will move on themselves after 6 seconds unless clicked by the user to do otherwise. The background image again enkeeps with the theme of the page and is a greyed picture of dumbbells, which is again fixed in order to keep that professional feel. These testimonials act as a means of shoring up any reservations the potential customer may have had about using this PT, and (providing the testimonials are good) will entice them to use this PT and purchases one of the products. In the event of there being no testimonials on the page an inspiration quote with the same background will be used instead.

##### Social Media

The three pillars of an aspiring fitness trainer's social media platform are then linked in the next section with a grey background. These icons send the user to their respective browsers in a new tab and will open up their platform there, where they can explore instructional videos etc. When the user hovers over any of these icons then they will slowly transition to their respective company colours, adding a bit of colour and also denoting to the user the icon is clickable and they are on it. 

##### Mission Statement

This gives the user a quick synopsis of the values and goals of our company. It is an honest statement of what you will get if you work with this PT and tries to give the user a more personal note. Again, this is trying to solidify the user;s trust in this PT and eventually going on to use his services. 

#### About page

The about page enkeeps with the previously mentioned home page with the dark background to begin with containing information about what XY is. This is because if the user is a new user to the site, the next logical step is to browse the about section to find out more about this PT and what they stand for. The user is given a quick synopsis of what the company is and how they operate. 

Next is a more personal section giving the user a little bit more background on what the PT's origins are and where they originate from. This would be accompanied by a picture of the actual person if it were put into production. This gives the user a little bit more knowledge the type of person they could potentially be working with.

The 3 means of operation section is next then which gives the user an insight in to how the plans work, and how this PT operates. It lets them know that changes won't be instant and it also ties in with the 3 pillars previously seen on the home page.

The next section then tells the user why our results last, as was previously explained in how the plans work, it is about giving them a fishing rod as opposed to a fish. If the user buys in to this mode of training or thinking then they will know that this is definitely the PT for them. Again, encouraging them to purchases the products.

#### All products page

The products page features a plane background and all the products in rows of three, the background is so that the customer can see the product easier. This allows for a better viewing experience. The products themselves are displayed as a picture showing it, with a title and rating, if it has one, underneath it, and the price. The picture has a slight shadow to stand out form the background which gradually but very slightly increases to denote to the user that they are hovering over the product. The picture and title themselves are clickable links which brings you to the <u>product page</u>.

The reviews are dependent on whether the product itself has been reviewed by customers on its page. The value returned is an average of all the reviews accumulated for this product. The stars themselves are gotten from [FA's](https://fontawesome.com/start) site, using a conditional statement to determine to number of full / half stars returned. The price is a set price for the respective and is not dependent on product size, only on the product being offered.

The items can then whittled down to their categories, showing them in a different view. These categories consist of "Apparel" or "Plan",  which are the two types of product being offered. The Apparel currently only consists of a training jumper, as the PT's brand expands this offering could turn into a plethora of different branded offerings. The items can then be sorted in these views using the 'sort' button. This button calls a view to sort the contents of the page either, alphabetically a-z and vice versa, or by prices, high to low / low to high.

#### Single product Page



#### Contact

The contact page is kept relatively simple as it only serves a purpose as a means for the user to get in contact with the PT if they have a query. This is because if they find themselves on this page in the first place then they do not want to be distracted by more text etc. They merely want to send the PT a message, so this page fits that purpose. Is the user is signed in then the form's initial data will have their email in the email field already.  

The message currently gets sent to the backend, being printed in the terminal window, and also gets added to the admin page. This could be set up in settings to send to my Gmail account but it means changing Gmail settings to less secure ones. If this website were to be fully deployed and used as a business then this would be altered and a work email utlised to take full advantage of this feature, and the Django settings altered. 

## Features to implement



## Information Architecture



## Credits

### Content

All text on XYfitness was written by me.

### Media

All images on this site were sourced from [Pexels](https://www.pexels.com/photo/burger-and-vegetables-placed-on-brown-wood-surface-1565982/)

### Code

The overlay for the search icon click was originally found [here](https://www.w3schools.com/howto/howto_js_fullscreen_overlay.asp) and heavily modified for my page.

### Acknowledgments

I would like to thank the CI tutors for all of their help throughout the course of this project, and my mentor, Simen.

### Disclaimer

This website and its content are for educational purposes only