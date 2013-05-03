PlyDraw2
========

PlyDraw is a game similar to Apples to Apples or Cards Against Humanity, but with drawing. The server randomly assigns a topic and a judge. The other, non-judge players draw the topic. After the drawings have been sumbmitted, the judge picks his/her favorite, and the artist of it becomes the next judge.

Tech:
* Python
* Flask
* Websockets
* Canvas
* Javscript
* Redis

Redis layout:

    game_ids = [ int ] # a game id is :game:<id>
    lobby_ids = [ int ] # a lobby id is :lobby:<id>
    player_ids = [ int ] # :player:<id>
    game_names = { game_id : name<string> }
    game_judge = { game_id : player_id }
    game_<id>_players = [ player_id ]
    game_submitted_images = { player_id : image_blob<string> }