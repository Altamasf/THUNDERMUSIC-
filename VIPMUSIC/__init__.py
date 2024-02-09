from THUNDERMUSIC.core.bot import THUNDER
from THUNDERMUSIC.core.dir import dirr
from THUNDERMUSIC.core.git import git
from THUNDERMUSIC.core.userbot import Userbot
from THUNDERMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = THUNDER()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
