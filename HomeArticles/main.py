"""
First File:
1
The first file seems to be the main entry point for the project.
It imports the Controller class from a module named controller and runs the Controller class's run method when executed.
Second File (Controller):
2
This file defines the Controller class, which is responsible for controlling the project's logic.
It imports the ArticlesList class from a module named model and the UserInterface class from a module named views.
The Controller class has methods to handle user input and manage articles.
 It interacts with the user through the UserInterface and stores articles in the ArticlesList.
Third File (UserInterface):
3
This file defines the UserInterface class, which handles user interactions.
It includes methods for user choices, creating articles, and displaying articles.
Additionally, it defines a decorator function add_text, which adds decorative lines around text when applied to a function.
Fourth File (Article and ArticlesList):
4
This file defines two classes, Article and ArticlesList.
The Article class represents an article and has attributes like title, author, pages, and description.
The ArticlesList class manages a collection of articles and has methods to add articles and retrieve all articles.
Overall, this project appears to be a basic implementation of an article management system with a command-line interface.
 Users can create, view, and manage articles using the provided classes and functions.
"""

from controller import Controller


def main():
    Controller().run()


if __name__ == "__main__":
    main()
