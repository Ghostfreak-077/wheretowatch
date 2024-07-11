import requests

url = 'http://localhost:5002/'

def getTitle(title):
    x = requests.get(url+'search?title='+title)
    return x


if __name__ == '__main__':
    
    query = input("Enter the title of the movie: ")
    # query = 'spider'

    datas = getTitle(query).json()
    # datas = getTitle(query).raise_for_status()
    
    print('\n')
    print('\n')
    
    for ind, data in enumerate(datas):
        print(ind+1, data['title'])
        
    movie = int((input("\nSelect your movie: ")))
    
    print("\nTitle: "+datas[movie-1]['originalTitle'] or datas[movie-1]['title'])
    print("\nPlot: "+datas[movie-1]['overview'])
    print("\nYear of Release: "+str(datas[movie-1]['releaseYear']))
    print("\nGenres: ")
    
    for genre in datas[movie-1]['genres']:
        print('\t\t'+genre['name'])
        
    print('\nRating: '+str(datas[movie-1]['rating']))
    print('\nCast: ')
    for cast in datas[movie-1]['cast']:
        print('\t\t'+cast)
        
    print('\nStreaming Options: ')
    for stream in datas[movie-1]['streamingOptions']['in']:
        print('\t\t'+stream['service']['name'] + ' - ' + stream['link'])
    
    
    # choice = int(input("What you wanna see?:\n1. Overview\n2. Genres\n3. Cast\n4. Ratings\n5. Streaming Options"))              
                       
    
    
    
    