## Wang Tiles Visualizer 🎮

Welcome to the Wang Tiles Visualizer! This repository is a tribute to the brilliant work of mathematician, logician, and philosopher Hao Wang. His creation, the Wang tiles, introduced in 1961, is an intriguing system of multi-colored square tiles. It finds a sweet spot in the realm of computer graphics, most prominently in procedural texture generation and the creation of seamlessly tiled patterns for 2D game worlds. 

This repo hosts two intriguing Python implementations, based on Pygame, of Wang tileset generation and visualization.

## Wang Tiles - A Primer 🧩

Wang Tiles are a class of formal systems. They're square tiles with a color assigned to each edge. The challenge lies in arranging them on a grid such that the colors of the touching edges of any two tiles always match. Wang proposed that if a set of tiles can tile the plane, it can do so periodically. However, this claim, known as Wang's conjecture, was later disproved.

These tiles have found various applications in computer science, especially in computer graphics and procedural generation of images. For instance, in creating diverse, yet coherent, tile-based 2D world maps for games.

## Our Implementations 💻

### Block Pattern Wang Tiles 💠
The first implementation uses a custom set of rules to create large blocks of tiles. Each tile (represented by 'A', 'B', 'C', 'D') has a designated color. The placement rules ensure that each tile only connects with specific other tiles, maintaining the seamless nature of the grid. If we were using tillable textures for A, B, C and D, themselves, large blocks of the same texture would make sense since it would be like a patch of the same tile, but far better and diverse than using the same tile repeated for the entire map.

<img width="504" alt="Screenshot 2023-07-09 at 23 55 51" src="https://github.com/brunoarnuti/WangTilesAlgorithm/assets/61336603/a0c4ffb8-04f9-41b4-82d7-c868ebea553d">


### Stochastic Wang Tiles 🎲

While the first implementation yielded visually pleasing results, I observed the patterns became too predictable over time. Real-world patterns have a degree of randomness that was missing in the large blocks. 

<img width="505" alt="Screenshot 2023-07-09 at 23 55 15" src="https://github.com/brunoarnuti/WangTilesAlgorithm/assets/61336603/79920486-41e4-4dd8-a2e3-e19626e9a89a">


### Stochastic Wang Tiles - Adding a Dash of Randomness 🎲

It introduces an element of stochasticity to the Wang Tiles, making the output less predictable and more varied. We devised a modified set of Wang tile rules, but this time with a twist: there's a small chance of breaking these rules!

This chance factor results in occasional repeating tiles and 2x2 squares of the same tile type, adding more diversity to the grid patterns and a bit more life to the tile world.

This stochastic approach is highly beneficial in scenarios where a bit of randomness can lead to more natural-looking results, such as terrain generation in video games.

## Why?

Here's how the quest for seamless, diverse game backgrounds led me to the Wang Tiles Algorithm.

With four distinct, tileable textures (A, B, C, D) I had created using Midjourney in hand, I was determined to create an engaging environment for my RTS prototype game. However, connecting them seamlessly and avoiding unwanted patterns, like large squares or more than two consecutive same textures, required a smart, algorithmic solution.

Here are the four distinct textures that I needed to arrange in a grid, which led me to discover the algorithmic solution.

<div align="center">
    <img src="./images/image1.jpg" width="300" height="300">
    <img src="./images/image2.jpg" width="300" height="300">
</div>
<div align="center">
    <img src="./images/image3.jpg" width="300" height="300">
    <img src="./images/image4.jpg" width="300" height="300">
</div>


## Wrapping Up 🎁

These implementations exemplify how mathematical constructs like Wang Tiles can address real-world game development challenges. They offer a way to automate the generation of diverse yet coherent tile-based 2D world maps, saving countless hours of manual work and offering endless variation for your players.

This repository showcases the beauty and potential of Wang tiles in generating visually appealing and diverse 2D patterns. The implementations provided are both visually pleasing and a great introduction to the concept of Wang tiles.

Feel free to fork this repository, play around with the rules, tweak the stochasticity, or come up with your implementation.
