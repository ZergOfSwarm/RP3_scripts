import subprocess
myplaylist = "/home/pi/music/PlayList"
#subprocess.call(['mplayer', '-vo', 'null', '-ao', 'alsa', '-playlist', myplaylist, '-shuffle'])
player = subprocess.call(['mplayer', '-vo', 'null', '-ao', 'alsa', '-playlist', myplaylist, '-shuffle'])
