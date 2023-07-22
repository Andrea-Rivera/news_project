# Andrea Rivera- She Codes News Project

## About This Project
Give a brief description of your project here. What is it for, how do you useit? 

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
- [ ] Order stories by date
![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Styled "new story" form![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Story images![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Log-in/log-out![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Account view" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Account" page![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] View stories by author![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Story" functionality only available when user is logged in![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

## Additional Features:

- [ ] Add categories to the stories and allow the user to search for stories bycategory.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )