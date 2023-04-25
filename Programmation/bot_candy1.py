import irc.bot
import irc.strings
import math


class MyBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.privmsg('candy', '!ep1')

    def on_privmsg(self, c, e):
        args = e.arguments
        arg  = args[0]
        nums = [float(v)for v in arg.split(' / ')]

        c.privmsg('candy', '!ep1 -rep %s' % (round(math.sqrt(nums[0]) * nums[1], 2)))

def main():
    bot = MyBot("#root-me_challenge", "darthvader", "irc.root-me.org", 6667)
    bot.start()

if __name__ == "__main__":
    main()

