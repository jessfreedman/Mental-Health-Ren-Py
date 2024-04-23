# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


default happy_points = 0

# The game starts here.

label start:

    scene bg roomlight

    play music "cool.ogg" fadeout 1

    "I wake up tired. Once again, I barely slept."
    
    "Night after night, I can only stare at the ceiling."

    "Regardless of my exhaustion, I must get out of bed."

    "I have to get up and contribute to society and live a normal life and be a normal person."

    "I have to fulfil my responsibilities. I have to."
    
    "But imagine."
    
    "What would happen if I just didn’t?"
    
    "There’s this crushing feeling of responsibility, but is it real? Isn’t it all just a social construct?"
    
    "What if I just stay here in bed forever?"

    "Should I get out of bed?"

    menu bed:

        "Yes":
            jump getup

        "No":
            jump ending1


label ending1:

    "Life is pointless. Let me just stay in bed forever."

    "What a dumb way to end things."

return

label getup:
scene bg badbed

"Standing, bleary-eyed and crusty, I wonder if I should take advantage of my dazed state to make my bed."

"I’ve been avoiding it for weeks."

"What’s the point of making your bed when you’re just gonna mess it up again? Sisyphean tasks like this drive me mad."

"Making the bed, mopping the floors, doing the dishes, what’s the point? You’ll just have to do it again."

"It’s pointless. It’s hopeless."

"But maybe that’s why I should do it before my consciousness fully catches up to me."

"Should I make my bed?"

menu shouldmakebed:

        "Yes":
            jump makebed

        "No":
            jump dontmakebed

label makebed:
$ happy_points += 1

scene bg bedmade

"Huh. That… didn’t suck as much as I thought it would."

"Actually, I feel kinda… good? Maybe? At least, I feel lighter."

"I should do this more often."

jump bathroom 


label dontmakebed:

"Fuck it. I don't feel like doing that."

jump bathroom

label bathroom:

scene bg sink

"Okay, what next? I trudge over to the bathroom and avoid looking at my face in the mirror."

"My mouth feels grimy with sleep. But, again, what’s the fucking point?"

"Yeah, maybe I’ll smell bad, but common social courtesy should keep people from making any comments."

"And I brushed my teeth last night! I think. I… actually can’t remember. But I’m pretty sure I did."

"Maybe."

"Whatever."

"It doesn’t matter."

"Should I brush my teeth?"

menu shouldbrushteeth:

        "Yes":
            jump brushteeth

        "No":
            jump dontbrushteeth

label brushteeth:

$ happy_points += 1

scene bg sinkinside

"That... also didn't totally suck."

"In fact, the toothpaste has a nice minty taste and now my mouth tastes good too."

"And now people won't think I stink!"

jump eating

label dontbrushteeth:

"Ugh, brushing my teeth is just so much effort."

"The back and forth motions make my head feel sick and my arm tired."

"Damn, I'm weak as fuck."

"But, anyway, I really really don't want to do this."

"Who cares anyway?"

jump eating

label eating:

scene bg kitchen

"Next, I guess would be to have breakfast."

"It's 10:30am though, so wouldn't this technically be brunch?"

"But if my normal waking up time is 10, wouldn't this still be breakfast?"

"Ugh, I'm thinking about pointless things again."

"Making and eating breakfast just seems like so much work."

"Food doesn't even taste good these days."

"But I know, I know I need energy or nutrients or whatever to get through the day and not feel like I'm literally dying."

"But I don't wannaaaaaaaaaaaaaaaaaaaa!!!"

"Should I eat?"

menu shouldeat:

        "Yes":
            jump eat

        "No":
            jump donteat

label eat:
$ happy_points += 1

scene bg fruit

"Ugh, fine. I guess I don't want to feel like I'm literally dying."

"What should I make? Something easy, something easy..."

"Whatever, I'll just have a fruit. Better than nothing. Plus, I'm pretty sure it contains some sort of nutrients."

"It's tastier than I expected. The skin is slightly tart, but sweet juice makes up for it."

"My hands are sticky. Better wash them."

jump work


label donteat:

"Eating makes me nauseous. Being nauseous is not fun. Therefore, eating is not fun."

"And you shouldn't do things that are not fun."

"Yep yep. That's my motto right there. Don't do things that aren't fun."

"Because things are soooooooo fun for me."

"Heh."

"Anyway. Not eating today."

jump work

label work:

scene bg work

"Fuck, it's already 11! I haven't done any work! I'm a failure!"

"Okay, but I can fix this. If I just start getting some work done now, then maybe I'll feel better?"

"Or not. Maybe everything I try will be a failure and then my peers will hate me and I'll be a huge disappointment to everyone I care about!"

"Orrrrrr, maybe I should just like. Answer an email and see where I go from there?"

"Should I do some work?"

menu shouldwork:

        "Yes":
            jump working

        "No":
            jump dontwork

label working:

$ happy_points += 1

scene bg goodwork

"Let's just take this in baby steps."

"I'll sit down in front of my computer. I'll open my emails. I will answer an email."

"Okay, I've done that. It wasn't so hard."

"Great. Let's just do more of that!"

"Oh hell yes, I'm working! I'm being productive! I'm a contributing member of society!"

"I have value because I can send emails!!!!"

jump endings


label dontwork:

"I think today I will refuse to be a pawn of the evil capitalist system."

"Who am I kidding? That's just an excuse. Work is scary and boring and I hate it."

"I have accepted my fate as a disappointment and burden to the world."

"Thus, I will spend my day doing absolutely nothing."

jump endings

label endings:
if happy_points >= 2:
    jump goodending
else:
    jump badending

label goodending:

    scene bg goodend

    "All in all, I actually had a pretty good day."

    "I guess doing small things like making your bed and brushing your teeth can make life better."

    "Even if doing them totally fucking sucks."

    return

label badending:

    scene bg badend

    "Well, today was fucking awful."

    "I can't help but wonder..."

    "If I'd done something different, would today have been better?"
    

return
