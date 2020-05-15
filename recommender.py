#import pandas
#import numpy
import random
#artist, and genre

def recommend():
    popularSongsArtist = ["Intentions", "Blinding Lights", "No Time To Die", "Don't Start Now", 
    "The Box", "Falling", "Life is Good", "My Oh My", "Say So", "To Die For"]
    popularSongsGenre = ["Uptown Funk", "Shake of You", "Perfect", "Thank you next", "Despacito",
    "Havana", "Happier", "Better Now", "Sugar", "ABC"]
    #flippedList = dict([(value, key) for key, value in playList.items()])
    #userMostPlayed = flippedList[max(flippedList.keys())]
    overlapSong = list(set(popularSongsArtist) & set(popularSongsGenre))
    #print(overlapSong)
    if(len(overlapSong)!=0):
        return overlapSong[random.randint(0, len(overlapSong)-1)]
    else:
        combinedList = popularSongsArtist + popularSongsGenre
        #print(combinedList)
        return combinedList[random.randint(0,len(combinedList)-1)]
    
#s = recommend()
#print(s)
    #find artist from the api
    #find hotest song from the same artist
