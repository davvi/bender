from errbot import BotPlugin, botcmd
import random

class Bender(BotPlugin):
    """Quick little bunch of commands to give the bot some sass"""

    @botcmd
    def sass_me(self, msg, args):
        """Request bender to do something silly, he'll respond with some sass"""
        bender_quips = ("This is the worst kind of discrimination there is: the kind against me!",
                        "I guess if you want children beaten, you have to do it yourself.",
                        "Hahahahaha. Oh wait you're serious. Let me laugh even harder.",
                        "There. Now no one can say I don't own John Larroquettes spine.",
                        "Ill build by own theme park. With black jack, and hookers. In fact, forget the park!",
                        "The games over. I have all the money. Compare your lives to mine and then kill yourselves!",
                        "That's closest thing to Bender is great that anyone other me has ever said.",
                        "I'm Bender, baby! Oh god, please insert liquor!",
                        "Hey sexy mama, wanna kill all humans?",
                        "You know what cheers me up? Other people's misfortune.",
                        "Anything less than immortality is a complete waste of time.",
                        "Blackmail is such an ugly word. I prefer extortion. The x makes it sound cool.",
                        "Have you tried turning off the TV, sitting down with your children, and hitting them?",
                        "Fry cracked corn and I don't care. Leela cracked corn I still don't care. Bender cracked corn and he is great. Take that you stupid corn!",
                        "You're a pimple on society's ass and you'll never amount to anything!",
                        "Shut up baby, I know it!",
                        "I'm so embarrassed. I wish everyone else was dead!",
                        "I got ants my butt, and I needs to strut!",
                        "Afterlife? If I thought I had to live another life, Id kill myself right now!",
                        "Bite my shiny metal ass!")
        return random.choice(bender_quips)

