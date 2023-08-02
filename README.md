# Ninja Platformer
#### Video Demo:  https://www.youtube.com/watch?v=zIhs5xoZhfc
#### Description: 
Character assets - https://free-game-assets.itch.io/free-tiny-hero-sprites-pixel-art

Ninja Platformer is a tile-based, 2D platformer game where you play as a fully animated ninja character and try to make it to the end of the level. This game was developed entirely in Python using Pygame. All of the images for the game are stored in the assets folder and all of the code is stored in the code folder.

main.py initializes all of the necessary functions of the game which allows for it to display. 

settings.py contains an array called 'level map' which contains the map of the level, where different tiles are set as different characters (' ', 'X', 'D', 'Y', 'W'). This allows for the level file, discussed later, to generate a corresponding tile sprite for each of the characters where they belong. In this file, the tile size, screen height, and screen width are also set.

level.py contains all of the code necessary for the level including the generation of the tiles, horizontal scrolling, and collisions. The tiles are generated based on the array in the settings file and each of the tiles has different types of tiles have different implemented properties. A tile which sets with the character 'X' is a basic brick tile that the character can walk on. The tile 'P' is the character and the 'W' tile generates text to inform the player they have won when the tile is collided with. The 'D' and 'Y' tiles both kill the player. When the player gets to either end of the level, the scroll function will cause the player's speed to be negated, but each of the tiles will move in the opposite direction, creating the effect of the character moving forward. The different collisions have different properties depending on the tile the player is on. The horizontal and vertical collisions are for the normal brick tiles and ensure the player correctly collides with a brick. The win collision will display text informing the player they have won and the death collision will end the program as a result of either falling down a hole or touching a razor. 

player.py has all of the code for the character including animations, movement, and gravity. The animations are played by looping through each of the corresponding images from assets/character based on the character's current status. The character's statuses are either facing right, left, on the ground, and/or ceiling and these statuses determine the animation that is being played or what direction the ninja is facing. The player's speed is initialized as 8, the gravity is set as 0.8 and the jump is -16. The animations are loaded onto the program with the help of support.py. The character moves left and right with "A", "D" or "←", "→" and can jump with "Space", "W", or "↑". 

tiles.py, wintile.py, deathtiles1.py, and deathtiles2.py are all distinct objects for the different tiles which have different colors or images. The images are each generated onto the game using Pygame's Surface.fill for solid colors and Surface.blit for the images, specifically for the brick and razor textures.
