Author: Max Krivonosov
Github ID: jbcorel
Description: This is a basic pong game. It allows us to choose between singleplayer with levels of difficulty and multiplayer (local). There is a small bug when the ball gets stuck, but it is a backdraw of using existing models instead of pygame-drawn.
Controls: W-S for singleplayer, W-S and arr_UP-arr_DOWN for multiplayer. NOTE: if a ball gets stuck in the singleplayer mode, press BACKSPACE to reset the position of the bot. 
Functions and classes: 
1) Class Player - contains movement () function that is responsible for player movement. update () method calls calls the movement () function and is inherited from pygame.sprite.Sprite
2) Class Ball - the ball itself. Contains a movement () function and update () method.
3) Button Class - buttons in the main menu and actual game. Contains draw () function that draws it into the screen based on the arguments passed upon object initiation. Contains check_click () that checks the mouse position and whether the button was clicked, returns True if yes. Update () function (not same as in previous classes, not inherited from pygame) calls the draw function and checks if the button was pressed by returning the check_click () function.
4) collision () - checks and implements collision mechanics of the ball and the pads.
5) ball_restart () - resets the ball after a goal.
6) display_score () - displays current score and changes it if someone scores; calls ball_restart ()
7) main_menu () - controls main menu, adds players to the player sprite group if multipler mode chosen. Returns difficulty_menu () if singleplayer chosen. Note: the speed of the default and the multiplayer pad can be changed in this function.
8) difficulty_menu - controls the difficulty menu. Based on what a user chooses, adds an AI player to the 'players' sprite group and specifies the speed of the AI. The speed is the only thing that defines difficulty. Note: yes, the function looks very sloppy, sorry for that.
9) gameover_screen () - controls the gameover screen. Nothing much.
10) main() - controls the flow of the program, draws sprites into the screen, calls collision (), display_score (), gameover_screen, ball_restart (), main_menu (). Note: can change how many goals need to be scored for each player to win. Note x2: gameover_screen () displays "{*player*} has won" line based on whose score is higher, so if, let's say, left pad needs to score 10 to win, and the right pad needs only 1, then in case the score is 9-1 the program will still display "Player1 has won". So mind it in case you decide to change it.

Global statements initiate buttons, score variables, sprite group "players", screen resolution, and other global things. Enjoy!

