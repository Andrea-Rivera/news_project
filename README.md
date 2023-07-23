# Andrea Rivera- She Codes News Project

## About This Project
This project was done to practice python and Django concepts by building different features. This is a News Application where different users can post news. There is an authentication system (Create User, Log in and Log Out). A Profile View where users can see their information. The users can see other news created by other authors and can use a filter to see their post. The user can also update or delete news that they have created.

## How To Run This Code

1. Clone the repo to your local machine"
2. In the terminal, change directory into the repo you cloned using the command `cd news_project` .
3. Set up a virtual environment using the command `python -m venv venv`.
4. Activate the environment. if you use Windows with the command `venv/Scripts/activate`.  If you are in a Mac `source venv/bin/activate`
6. Open the folder in VS code.
7. Change directories so that you are in the same location as your manage.py file. Use the command `cd she_codes_news` 
8. Migrate the database using the command `python manage.py migrate`
9. Finally, run the server with the following command: `python manage.py runserver`

    
## Database Schema
![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )
    
## Project Features
- [x] Order stories by date
![Stories ordered by date in descending order.](./she_codes_news/news/static/news/images/order_by_date.png)

- [x] Styled "new story" form![ Adding styles to make the stories responsive ](./she_codes_news/news/static/news/images/news_style.png )

- [x] Story images![ Adding a field to the news stories for an image URL](./she_codes_news/news/static/news/images/news_image.png)

- [x] Log-in/log-out![ Adding Log In and Log out features ](./she_codes_news/news/static/news/images/login.png )

- [x] "Account view" page![View user's account information](./she_codes_news/news/static/news/images/account_view.png)

- [x] "Create Account" page![Create account](./she_codes_news/news/static/news/images/create_account.png)

- [x] "Create Account" page![users use dropdown menu to view stories by a particular author](./she_codes_news/news/static/news/images/create_account.png)

- [x] "View stories by author" Users can use dropdown menu to view stories by a particular author![{{users can use dropdown menu to view stories by a particular author}}](./she_codes_news/news/static/news/images/search_author.png)

- [x] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] "Create Story" functionality only available when user is logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

## Additional Features:

- [x] Add categories to the stories and allow the user to search for stories bycategory.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Add the ability to “favourite” stories and see a page with your favouritestories.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )