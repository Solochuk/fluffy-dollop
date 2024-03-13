import json

games = {
    'Red Dead Redemption 2': {
        'site_url': 'https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/',
        'photo': 'https://cdn.akamai.steamstatic.com/steam/apps/1174180/header.jpg?t=1695140956',
        'description': 'The story is set in a fictionalized representation of the United States in 1899 and follows the exploits of Arthur Morgan, an outlaw and member of the Van der Linde gang, who must deal with the decline of the Wild West while attempting to survive against government forces, rival gangs, and other adversaries.',
        'rating': '9/10'
    },
    'Black Mesa': {
        'site_url': 'https://store.steampowered.com/app/362890/Black_Mesa/',
        'photo': 'https://cdn.akamai.steamstatic.com/steam/apps/362890/header.jpg?t=1698563440',
        'description': 'Black Mesa is a first-person shooter that requires the player to perform combat tasks and solve various puzzles to advance through the game.',
        'rating': '10/10'
    },
    'Metro Exodus': {
        'site_url': 'https://store.steampowered.com/app/412020/Metro_Exodus/',
        'photo': 'https://cdn.akamai.steamstatic.com/steam/apps/412020/header.jpg?t=1706778291',
        'description': 'Metro Exodus is an epic, story-driven first person shooter from 4A Games that blends deadly combat and stealth with exploration and survival horror in one of the most immersive game worlds ever created.',
        'rating': '9/10'
    },
    'Scrap Mechanic': {
        'site_url': 'https://store.steampowered.com/app/387990/Scrap_Mechanic/',
        'photo': 'https://cdn.akamai.steamstatic.com/steam/apps/387990/header.jpg?t=1593703247',
        'description': 'Enter the creative paradise of Scrap Mechanic! Build fantastic machines, go on adventures with your friends and defend against waves of evil Farmbots in this imaginative multiplayer survival sandbox. With Scrap Mechanics powerful creation tools you can engineer your own adventures!',
        'rating': '9/10'
    },
    'STAR WARS Jedi: Fallen Order™': {
        'site_url': 'https://store.steampowered.com/app/1172380/STAR_WARS_Jedi_Fallen_Order/',
        'photo': 'https://cdn.akamai.steamstatic.com/steam/apps/1172380/header.jpg?t=1701206847',
        'description': 'A galaxy-spanning adventure awaits in Star Wars Jedi: Fallen Order, a 3rd person action-adventure title from Respawn. An abandoned Padawan must complete his training, develop new powerful Force abilities, and master the art of the lightsaber - all while staying one step ahead of the Empire.',
        'rating': '9/10'
    },
    'S.T.A.L.K.E.R.: Shadow of Chernobyl': {
        'site_url': 'https://store.steampowered.com/app/4500/STALKER_Shadow_of_Chernobyl/',
        'photo': 'https://cdn.akamai.steamstatic.com/steam/apps/4500/header.jpg?t=1686945417',
        'description': 'S.T.A.L.K.E.R.: Shadow of Chernobyl tells a story about survival in the Zone – a very dangerous place, where you fear not only the radiation, anomalies and deadly creatures, but other S.T.A.L.K.E.R.s, who have their own goals and wishes.',
        'rating': '9/10'
    },
    'Brick Rigs': {
        'site_url': 'https://store.steampowered.com/app/552100/Brick_Rigs/',
        'photo': 'https://cdn.akamai.steamstatic.com/steam/apps/552100/header.jpg?t=1689355203',
        'description': 'Brick Rigs is a physics sandbox game that allows you to build, drive and destroy almost any type of vehicle imaginable. Whether it`s a dragster, fire engine, forklift, helicopter, plane, train, ship or even a tank, you can probably build it in Brick Rigs.',
        'rating': '9/10'
    }
}

with open("games.json", "w", encoding="utf-8") as file:
    json.dump(games, file, indent=4, ensure_ascii=False)
