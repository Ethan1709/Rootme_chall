import irc.bot
import irc.strings
import math
import string

class MyBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.privmsg('candy', '!ep3')

    def on_privmsg(self, c, e):
        args = e.arguments
        arg  = args[0]
        print(arg)

        new = ""
        for v in arg:
            if v in string.ascii_lowercase:
                i = string.ascii_lowercase.index(v)
                new += string.ascii_lowercase[(i + 13) % 26]
            elif v in string.ascii_uppercase:
                i = string.ascii_uppercase.index(v)
                new += string.ascii_uppercase[(i + 13) % 26]
            else:
                new += v
        
        print(new)

        c.privmsg('candy', '!ep3 -rep ' + new)

def main():
    bot = MyBot("#root-me_challenge", "darthvader2", "irc.root-me.org", 6667)
    bot.start()

if __name__ == "__main__":
    main()

