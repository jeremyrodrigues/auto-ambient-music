import pafy



def play(player, url='https://www.youtube.com/watch?v=6iFbuIpe68k', volume=75):
    try:
        instance = player.get_instance()
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        playurl = bestaudio.url
        Media = instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        player.audio_set_volume(volume)
        return True
    except Exception:
        return False

def stop(player):
    player.stop()



