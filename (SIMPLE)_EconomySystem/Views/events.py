"""
YOU CAN ADD AS MUCH EVENTS AS YOU WANT
This are the text's that will be sent when you use the Commands!
"""


def workP(coins, eco):

    eventPositive = [
            f'You did great work and receive {eco} **{coins}** coins!',
            f'You baked a Cake and got {eco} **{coins}** coins!',
            f'You baked some cookies and someone bought them from you. He paid {eco} **{coins}** coins!',
            f'You were washing some cars and received {eco} **{coins}** coins!',
            f'You sold some Codes and got {eco} **{coins}** coins!',
            f'You work hard at the office today, but instead of gaining a promotion, you earn {eco} **{coins}** coins! Nice one.',
            f'Your boss were nice today and gave you {eco} **{coins}** coins!',
            f'You got a good grade so your mother decided to give you {eco} **{coins}** coins!',
            f'Someone donated {eco} **{coins}** coins in your Livestream! Good job.',
            f'You sold some Items and profited {eco} **{coins}** coins!',
            f'You work as the head of carrots and earn {eco} **{coins}** coins!',
            f'You catch a fish and gave it to your best friend. He pays you {eco} **{coins}** coins for a good job!',
            f'You work in a restaurant and got a Tip of {eco} **{coins}** coins for a good job!',
            f'You win a Burger eating contest. The prize is {eco} **{coins}** coins!',
            f'You work as a Police officer and earn {eco} **{coins}** coins!'
        ]

    return eventPositive


def workN(coins, eco):

    eventNegative = [
            f'You did bad work and loses {eco} **{coins}** coins!'
        ]

    return eventNegative


def slutP(coins, eco):

    eventPositive = [
            f'You did bad work and loses {eco} **{coins}** coins!'
        ]

    return eventPositive


def slutN(coins, eco):

    eventNegative = [
            f'You did bad work and loses {eco} **{coins}** coins!'
        ]

    return eventNegative



def crimeP(coins, eco):

    eventPositive = [
            f'You did bad work and loses {eco} **{coins}** coins!'
        ]

    return eventPositive


def crimeN(coins, eco):

    eventNegative = [
            f'You did bad work and loses {eco} **{coins}** coins!'
        ]

    return eventNegative


def RobP(coins, eco):

    eventPositive = [
            f"You stole an old man's wallet and took out {eco} **{coins}** coins!"
        ]

    return eventPositive


def RobN(coins, eco):

    eventNegative = [
            f'You got cought by a Police Officer! You needed to pay {eco} **{coins}** coins to get out of prison!',
            f'You tried to steal a phone by a old woman, but you didnt know that she was a Boxing pro! She punched you in the face and called the police. You paid {eco} **{coins}** coins to get out!'
        ]

    return eventNegative
