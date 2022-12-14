# OGS Buddy

OGS Buddy is a tool to help make flashcards of OGS positions:

1. Review a game using the OGS AI facility
1. When you see a move where the AI did something much better than your choice, click "Make Flashcard" and a flashcard is made for you in the [Anki flashcard program](https://apps.ankiweb.net/).
1. Review your flashcards regularly to improve your ability to do better in those same positions.

# Screenshot

![image](https://user-images.githubusercontent.com/21293/189312364-e71d732f-8523-44db-a0f5-aea2c3b1a58c.png)

Let's click on "Make Flashcard" so we dont make this same mistake again.

## Anki quizzes us on the position:

![Now we are presented with the position in a flashcard](https://i.imgur.com/iJWkKYD.png)

Now we are presented with the position in a flashcard

![After pressing "show answer" we see the answer and can feedback on how well we did](https://user-images.githubusercontent.com/21293/189311588-c62bd4b6-e3c5-46dd-bff8-e5eeddfcfd30.png)

After pressing "show answer" we see the answer and can feedback on how well we did

# Installation

## Download and install the Anki flashcard software

https://apps.ankiweb.net/

### Download and install Anki-connect

https://github.com/FooSoft/anki-connect#installation

## Clone this repo

## Install Python on your machine

# Usage

1. Open a shell
2. Set your `PYTHONPATH` to the ogs-buddy cloned repo
3. change directory to the ogs-buddy cloned repo
4. type `python bin\main.py` to start up OGS Buddy
5. Startup the Anki flashcard software
6. Play a game in the browser window after logging in. Or alternatively browse to any game and then let the AI review it.
7. When you see a position you want to remember, click "Make Flashcard". Remember: you click "make flashcard' when the screen is showing the analysis

# FAQ

## Why not make a chrome plugin for this?

1. I am a professional Python developer and found making a Chrome plugin an aggravating experience. For instance,
look at [all the dain bramage you have to go through to make sure the plugin does not load the code twice.](https://stackoverflow.com/q/73635057/149741)
1. Even if I did want to jump through hoops of fire and make a Chrome plugin, there is something very mysterious
about the way the score markers are placed on the OGS goban. After much teeth-gnashing, I managed to get screenshots of the whole web browser (because a screenshot of the div was impossible because the goban is actually 5 layered canvases on top of each other) but those screenshots did not include the score markers for some reason
and [no one knew why](https://forums.online-go.com/t/why-does-taking-a-screenshot-of-the-html-body-using-javascript-not-show-the-analysis-feedback/44694).

# References

https://www.juliensobczak.com/write/2020/12/26/anki-scripting-for-non-programmers.html

https://ankiweb.net/shared/info/2055492159

https://forums.online-go.com/t/how-can-i-call-the-javascript-that-shows-hides-the-ai-analysis/44683?u=thequietcenter


