class song: 
    def __init__(self, name, artist, album, year, duration, genre,key) -> None: 
        self.key = key 
        self.name = name 
        self.artist = artist 
        self.album = album 
        self.year = year 
        self.duration = duration 
        self.genre = genre 
     
    def __str__(self) -> str: 
        return f'{self.key} {self.name} {self.artist} {self.album} {self.year} {self.duration} {self.genre}'
 
      
 
class Playlist: 
    def __init__(self, name) -> None: 
        self.List = [] 
        self.name = name 
         
 
    def addToList(self, songs): 
        self.List.append(songs) 

    def __str__(self) -> str:
         return f'{self.name} {[str(songs) for songs in self.List]}'
     
 
class Musiclibrary: 
    def __init__(self,) -> None: 
        self.List = [] 
        self.songs = {} 
         
        
    def addToDict(self, Songs): 
        self.songs[Songs.key] = Songs 
     
    def addToList(self, playlist): 
        self.List.append(playlist) 

    def __str__(self) -> str:
        return f'{[str(playlist) for playlist in self.List]}, {[str(Songs) for Songs in self.songs]}'
    

       
 
 
 
Song = song("Ми — хлопці з Бандерштату","Брати Гадюкіни","Плейлист Незалежності", 1991, 5.24, "Рок", 1 ) 
print(Song) 
 
play_list = Playlist("Плейлист Незалежності") 
print(play_list) 
 
play_list.addToList(Song) 
for i in range(len(play_list.List)): 
    print(play_list.List[i]) 
 
library = Musiclibrary() 
library.addToList(play_list) 
for i in range(len(library.List)): 
    print(library.List[i]) 
library.addToDict(Song)