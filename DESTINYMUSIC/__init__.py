from DESTINYMUSIC.core.bot import JARVIS
from DESTINYMUSIC.core.dir import dirr
from DESTINYMUSIC.core.git import git
from DESTINYMUSIC.core.userbot import Userbot
from DESTINYMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = JARVIS()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
