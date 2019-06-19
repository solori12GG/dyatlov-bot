#!/usr/bin/python3
import praw
import re
import random
import os

# Quotes!!
dyatlov_quotes = \
[
"Not great, not terrible",
"Do you think the right question will get you the truth?",
"It's just feedwater radiation, I've seen worse",
"You stalled the Reactor!! HOW THE FUCK DID YOU GET THIS JOB!",
"EXPLAIN TO ME HOW DOES AN RBMK REACTOR EXPLODE!!!",
"No. Leave.",
"So everything's my fault then?",
"What the fuck are you talking about?",
"YOU DIDN'T SEE GRAPHITE ON THE GROUND BECAUSE IT WASN'T THERE!",
"SHUT THE FUCK UP AND DO YOUR JOB",
"I'll personally supervise the test and it will be completed",
"I wasn't there, I was on the toilet",
"Raise the power",
"How do I even know it exploded?",
"Well, the State must protect it's secrets Comrade",
"YOU'RE CHOKING MY REACTOR, GET IT BACK UP!!",
"I can't make things better for you, but I can certainly make them worse",
"I would like to be considered",
"Reduce power to 700",
"I SAID THAT'S ENOUGH! I know what I'm Doing",
"He's in shock, get him out of here",
"You're confused, RBMK cores don't explode",
"Turn that FUCKING THING OFF!",
"I NEED WATER IN MY REACTOR CORE!!",
"What does the dosimeter say?",
"WHAT DID YOU DO!?!?",
"Did you lower the control rods or not?",
"YOU'RE A LIAR!",
"Take him to the infirmary, HE'S DELUSIONAL",
]

# Create the reddit instance
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('ChernobylTV')

while 1:
        for comment in subreddit.stream.comments(skip_existing=True):
                print(comment.body)
                if re.search("comrade dyatlov", comment.body, re.IGNORECASE):
                        dyatlov_reply = random.choice(dyatlov_quotes)
                        comment.reply(dyatlov_reply)
                        print(dyatlov_reply)


