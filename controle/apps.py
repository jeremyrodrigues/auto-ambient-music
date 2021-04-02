from django.apps import AppConfig
from threading import Thread

class PlayerThread(Thread):

    def run(self):
        from controle.player import play, stop
        from controle.models import Time
        from controle.choices import VOLUMES
        from datetime import datetime
        import vlc
        import time
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        print(f'Thread Player is ON')
        playing = None
        while True:
            times = Time.objects.all()
            now = datetime.now()
            for t in times:
                if playing and player.is_playing():
                    if playing.id == t.id:
                        if now.time() >= playing.final_time:
                            v=VOLUMES[t.vol][1]
                            while v>0:
                                v -= 1
                                player.audio_set_volume(v)
                                time.sleep(0.5)
                            playing = None
                            stop(player)

                else:
                    if t.weekday == now.weekday():
                        if t.initial_time <= now.time() < t.final_time:
                            playing = t
                            play(player, url=t.music.url, volume=0)
                            v_max = VOLUMES[t.vol][1]
                            v = 0
                            while v_max > v:
                                v += 1
                                player.audio_set_volume(v)
                                time.sleep(0.3)
            times = None
            now = None
            time.sleep(15)
        

class ControleConfig(AppConfig):
    name = 'controle'

    def ready(self):
        PlayerThread().start()
