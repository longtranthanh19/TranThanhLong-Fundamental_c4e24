from youtube_dl import YoutubeDL

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=O-Uw136cMi4&t=822s'])

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=Oi0sVRZ_49c&t=793s', 'https://www.youtube.com/watch?v=5soixb2U6xM'])

options = {
    'format': 'bestaudio/audio' 
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=zK9GTSm-SGk&t=819s'])

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(['Only Road Cosmix Gate'])

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Above and Beyond Acoustic II'])


