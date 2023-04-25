import irc.bot
import irc.strings
import math
import base64
import zlib

# base64.b64decode()
# base64.b64encode()

class MyBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.privmsg('candy', '!ep4')

    def on_privmsg(self, c, e):
        args = e.arguments
        arg  = args[0]
        new = base64.b64decode(arg) # bytes

        try:   
            res = zlib.decompress(new)
            d = res.decode()
        except Exception as e:
            print(e)
            print(arg)
            return


        c.privmsg('candy', '!ep4 -rep ' + str(d))

def main():
    bot = MyBot("#root-me_challenge", "darthvader", "irc.root-me.org", 6667)
    bot.start()

if __name__ == "__main__":
    main()

