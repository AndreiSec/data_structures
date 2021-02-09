"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Andrei Secara
ID:      190232560
Email:   seca2560@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""
from BST_linked import BST
# In order by letters.
data1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..--'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))

# In order by splitting.
data2 = (('M', '--'), ('F', '..-.'), ('T', '-'),
         ('C', '-.-.'), ('J', '.---'), ('P', '.--.'),
         ('W', '.--'), ('A', '.-'), ('D', '-..'),
         ('H', '....'), ('K', '-.-'), ('N', '-.'),
         ('R', '.-.'), ('U', '..--'), ('Y', '-.--'),
         ('B', '-...'), ('E', '.'), ('I', '..'),
         ('G', '--.'), ('L', '.-..'), ('O', '---'),
         ('Q', '--.-'), ('S', '...'), ('V', '...-'),
         ('X', '-..-'), ('Z', '--..'))

# In order by popularity.
data3 = (('E', '.'), ('T', '-'), ('A', '.-'),
         ('O', '---'), ('I', '..'), ('N', '-.'),
         ('S', '...'), ('H', '....'), ('R', '.-.'),
         ('D', '-..'), ('L', '.-..'), ('U', '..--'),
         ('C', '-.-.'), ('M', '--'), ('P', '.--.'),
         ('F', '..-.'), ('Y', '-.--'), ('W', '.--'),
         ('G', '--.'), ('B', '-...'), ('V', '...-'),
         ('K', '-.-'), ('J', '.---'), ('X', '-..-'),
         ('Z', '--..'), ('Q', '--.-'))


class ByLetter:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by letter attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByLetter object.
        Use: var = ByLetter(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByLetter object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their letters match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if letters match, False otherwise (boolean)
        -------------------------------------------------------
        """

        # Your code here

        return self.letter == target.letter


    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        # Your code here

        return (self.letter < target.letter)

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        # Your code here

        return (self.letter <= target.letter)

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByLetter data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByLetter (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.letter, self.code)


class ByCode:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by code attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByCode object.
        Use: var = ByCode(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByCode object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their codes match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if codes match, False otherwise (boolean)
        -------------------------------------------------------
        """

        # Your code here

        return target.code == self.code

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        

        return self.code < target.code

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """

        # Your code here

        return self.code <= target.code

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByCode data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByCode (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.code, self.letter)


def fill_letter_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByLetter Morse code letter/code pairs
    (Function must convert contents of values to ByLetter objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """

    for value in values:
        var = ByLetter(value[0], value[1])
        bst.insert(var)

    return


def fill_code_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByCode Morse code letter/code pairs.
    (Function must convert contents of values to ByCode objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """

    for value in values:
        var = ByCode(value[0], value[1])
        bst.insert(var)

    return


def encode_morse(bst, text):
    """
    -------------------------------------------------------
    Converts English text to Morse code
    Use: code = encode_morse(bst, text)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by letter (BST)
        text - English text to convert (str)
    Returns:
        result - Morse code version of text (str)
    -------------------------------------------------------
    """
    
    fill_letter_bst(bst, data1)
    result = ""
    text = text.split(" ")
    for i in text:
        for char in i:
            if char.isalpha():
                answer = bst.retrieve(ByLetter(char, None))
                if answer is None:
                    result += ""
                else:
                    result += answer.code
                result += " "
        result += "\n"
    

    return result


def decode_morse(bst, code):
    """
    -------------------------------------------------------
    Converts Morse code to English text
    Use: text = decode_morse(bst, code)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by code (BST)
        code - Morse code to convert (str)
    Returns:
        result - English version of code (str)
    -------------------------------------------------------
    """

    fill_code_bst(bst, data1)
    result = ""
    text = code.split(" ")
    for i in text:
        print(i)
        answer = bst.retrieve(ByCode(None, i))
        if answer is None:
            result += ""
        else:
            result += answer.letter
    result += "\n"
    
    return result











import timeit

start = timeit.default_timer()


# print(code)

code = "... --- ..."
# text = """Hey, I'm once again: back. I don't suppose you fell for that little thing about the refresh button. After all, you're a responsible, intelligent person who apparently has a lot of time on your hands. Well, you can't possibly have more time than I do. I mean, after all, I made this site. You're only browsing it. And most people don't even come here. Not even my friends...*sniffle* The just ignore this poor, pathetic little page. All they do is fill out the TAB form and leave. I think. Maybe they're here right now! HI! HOW ARE YOU DOING? I'M FINE! THANKS FOR COMING! YES, I'M YELLING! Who am I kidding. This page won't get a single hit, unless I bribe people...now that has possibilities. Okay, fill out the TAB form, so I have proof that you bothered to come here and...uh...I'll...uh...send you a sandwich? Please allow 6-8 weeks for delivery. I'm bored. I'm gonna go hug a moose. MOOSE! I love-d you moose! Hey, I'm back again! Yea...*waits for applause* okay! Now I want all you loyal fans...*cricket chirps* to go to the link to see what I'm like. I took a whole bunch of personality quizzes and posted them there. I'm an evil villain, kitty and a freakazoid so far. And I only took the quiz once, too. Spooky how accurate they are...anyway, I command you to go! I'm going. I'm back. I'm gonna start counting how many times I say back. Let's see: 1...2...3...4...5! Wow. I must really be desperate for something to do. I now officially have proof that someone has been here! It was one of my friends. Apparently this page really is getting long, because my friend said something to that effect. Maybe. Anyway, moving on! I'm just basically typing nothing. Just like all those reports people have to do. You know? With a specific number of words. They start out with half that number, and then just fill in words until they have the right amount. I salute those people. You're great tradition is being carried out here, on the second most pointless site ever! Well. Maybe eventually some weird, bored person will wander onto my site on accident and be mildly entertained be my site until they wander onto a live video feed of a coffee maker. Or maybe not. I only know that I'm entertaining me, which was my original goal. So. I've done what I've set out to accomplish. Yea, me! I'm so special. You see, most people, they don't like reading or writing. So if you're not most people, you've made it down this far without skipping, skimming or getting the spark notes version. (Which I think does not exist) My point is, if you've bothered to read this, then, (like me) you probley have also read the ketchup bottle so many times that you have it down verbatim. Look verbatim up. It's a word. But, you should know that, since you like reading. Or maybe you're just skimming. Anyway, there's nothing wrong with reading food labels. You might be asked a question about them on a quiz show. And now, for the million-dollar question: How many calories are there in a single serving of Mustard? I can just see it now...It could be called Know-Your-Food. Or You are What you Eat. It'd probley be as popular as those game shows that no one's ever heard of. Speaking of food, what's up with pie? There's strawberry pie, apple, pumpkin and so many others, but there is no grape pie! I know. I'm just as upset about this unfortunate lack of development in the pie division. Think about it. Grapes are used to make jelly, jam, juice and raisins. What makes them undesirable for pie? Would they dry into raisins? Couldn't you just stick some jelly in a piecrust and bake it? It just doesn't make any sense. Another thing that bothers me is organ grinders. You know, the foreign guys with the bellhop hats and the little music thingy and the cute little monkey with the bellhop hat who collects the money? Okay. They're basically begging on the street. How did they ever afford an organ-thingy? Wouldn't it make more sense to get a kazoo, if you're broke? And if they're so poor, what possessed them to buy a monkey? I mean, I don't think I could afford a monkey, and I'm not exactly on the streets. Obviously I at least have a computer...so, back to the organ grinders. I would have sold the monkey and the organ and been able to eat for at least a year. Or, if I was weirder than I am, I could at least kill the monkey with the organ and eat it. Why on earth did they keep the monkey? It must have cost a fortune to feed...not to mention the mess. That's just one of those many facts of life that are better left mysteries. Especially since no one but me would ask the question. I better go. I think I hear a monkey...Okay...now I'm back. That's the sixth time I've said back! I realize that this longest text ever must be very boring and not worth anyone's time. But I'd like to take this time to thank the 2 and 1/2 people in the entire universe who have bothered to read this entire thing. I'm not exactly sure who they are, but: thanks! Right now, my spacebar is malfunctioning...that's not good...I have to press it two or three times just to insert a freaking space. Maybe the evil little faeries with the sharp little teeth have put their evil faerie dust on my computer. Or maybe not. This is too frustrating. Goodbye for now...Now I'm back. And still frustrated. But for a different reason. Today I had the misfortune of playing a Treasure Planet game on neopets.com It was terrible. Apparently the point of the game was to get your character to shout "Whoo-Hoo!" as many times as possible before you splattered your brains on the rocks, all the while listening to a soundtrack that is similar to a dying ceiling fan. Of course, when I started out I accidentally hit the rocks approximately three million times. Halfway though I used my four remaining brain-cells to decide that the game was dumb. So my goal changed from surviving to laughing evilly while my character died. So the game naturally did everything it could to preserve my life. The stupid game is still going on and I refuse to quit because I want my points. My character is actually dodging the stupid rocks better now then when I controlled him. I hate irony. Seeya. Okay. Now I'm back again. Today I added an update page, which is basically a less chaotic, outlined version of this without all the ranting. It's more like techno talk about arrays and how much I suck and whether or not the Braves will win this year. Okay, the whole braves thing is made up. But everything else I've said so far is true. I think. Maybe I should start on a boring disclaimer...Eh-hem. All contents of this site were designed for entertainment purposes only. Any use thereof that is not stated in the above mentioned statement would make the author, hereby referred to as Patron Saint of Paper Clips, very angry. Should you violate the purpose of this site: i.e. become not entertained, the Patron Saint of Paper Clips will be forced to take drastic measures. This is specified in Code: 343 of the Flaming Chicken Handbook. Ooooo…that’s a great idea! I’m gonna start quoting from the Flaming Chicken Handbook! Code: 343 of the Flaming Chicken Handbook states that the Patron Saint of Paper Clips (that’s me) is allowed to cause vague, pain like sensations while the offending person (or alien life form, dog, etc.) isn’t paying attention. Now I have a purpose in life! To make up quotes from the non-existent Flaming Chicken Handbook, which I’m sure you have a copy of. No? Too bad. It’s in the mail, I promise! Now I must take my leave…and remember. Cheese is watching. Okay...I'm back...I think that eventually half of this thing will consist of the word back over and over again...that's just weird. Which fits the motif of the rest of the site. There's even a money back guarantee. Isn’t' that nice? See? Now no one can ever say that I don't take care of my viewers. Especially since I don't have viewers. I have readers. Wait...I really don't even know if anyone bothers to read this. Even if I put it in a less chaotic, more user-friendly format people would still ignore this because it involves: reading. Yes. Sad to admit, but the majority of people would rather read the summary at the back of a book rather than the whole book itself. What has the world come to? It's pathetic. Especially since I'm bothering to write all this. It's not fair! Why can't I have more readers?! All the other internet writers have nothing on me, except they're better at advertising, having a central theme/plot and basically more talented. Whereas I'm more into the whole ranting and raving stage right now. Plus, I am horrible at spelling. Which is bad. Thank the powers that be for spell-check. The single greatest invention of the computer gods. I'm getting bored, so I think I'm done for the day. May your day be shiney! I'm back again! And I feel weird! I found at that yet another one of my friends is reading this. Creepy. Just how much time do they have on their hands. Perhaps their just trying to be nice. I can just see it now...an organization devoted not to feeding the hungry, or peace, or love or whatever, but to giving recognition to all those poor, pathetic, unpopular websites. I wonder what it's name would be. Don't Ignore Sites? Would it be called DIS? Isn't that like a slang term for an insult? Would that be considered poetic justice, or just a nice coincidence? And why do I even care? I'll tell you why. Because I have nothing else to do right now. I could be playing neopets, but ever since my bad experience with Treasure Planet, I don't feel like it. Oh, by the way, I noticed that whenever I use spell-check, my stupid computer turns the word probley into to word problem. To prevent this, I did nothing. So, it is now up to you, the imaginary reader, to decide whether I mean probley or problem...it's almost like a game! But without the bad sound track. And I promise not to force you to live when you would rather die. Moving on, I have nothing else to say, but don't feel like quitting just yet. I'm like the little engine that could. Or maybe the Energizer Bunny. I just keep going, and going and going. Or I could be like that annoying guy on T.V. who keeps asking if you can hear him. If my site manages to last a decade, my readers *snicker* will probley wonder what I'm talking about. My answer is simple. It doesn't matter. I'm just rambling. Which means that it doesn't matter if you understand anything I say. Doesn't that make you feel better? I bet it does. Wow. Look how long this has gotten. I even impress myself. Who would have thought I have this much free time? And I congratulate any reader who has gotten this far. Ooooooo! You must check out the fortunes section of the random stuff page! I've just gotten an idea for some more, original, fortunes...I gotta go!(may the moose be with you) And now I am back. I swear. If iI fill out the fake tab form I'm gonna have to put back as my favorite word...I already have filled it out, though. Would it be cheating to fill it out again? Only if I had multiple personalities. Or would it be cheating if I didn't have multiple personalities? The world may never know. Just like how many licks it takes to get to the bottom of a tootsie pop. Would it vary? The number of licks, I mean. Someone could have super-disolving spit, or watery-spit. Or what if you took big ol' slobbery licks? Does the commercial take that into account? No. It doesn't. And let me tell you, it's an outrage. It deludes all of American's sweet, innocent, candy-loving children into thinking that a cartoon owl is smarter than they are! "Mr. Owl, can you tell us how many licks does it take to get to the bottom of a tootsie pop?" Or whatever. And "Mr. Owl" replies "One...Twoo...Three! Chomp" And he bites it. That teaches our youth that it's okay to agree to help someone, and then ruin their experiment. Well...it's not. I am going to start a protest group. Teens Against Cartoon Owls. We could call ourselves TACO! I love the little tacos, I love them good! That is a direct quote from GIR, co-star and comic-relief on INVADER ZIM. Hmmmm...intersting. I put hyphens in both of his titles...it must be a conspiracy! I gotta go. Those TACO buttons don't make themselves, you know. I'm back again. And not so cheesed off about the whole tootsie roll pop thing. Right now, I have another twenty minutes on the Internet before I'm gonna watch T.V. And I can't think of anything else to do. So, predictably, here I am. It's not like I have anything better to do. Obviously, you know this. After all, look how long this text is. I wonder if I've made the world record? If I did, would I stop this? Why bother asking? I'll will most likely still be adding to this on my death bed. Hmmmmm...has any old, senile person ever written anything? Was it coherent? Did it make more sense that this text? Is it possible to make less sense? Am I enjoying asking retorical questions? Yes. Yes, I am. But I seriously wonder what something written by a senile person would be like. I've heard of poems and stuff written by people who were high, insane or paranoid. But never senile. Can a senile person write? Aren't they regressed to a child-like state? Does it even matter? Is anyone even reading this? Did I resume asking retorical questions? Do you care? Is this eating up time? I feel like I'm playing questions only on whose line is it anway. I probley should have capitalized something, or underlined but I'm feeling lazy...hey, you try to keep your two and a half readers happy! It's really stressfull. Someday, I'm gonna snap and just delete this entire thing. Gee, I hope not! I worked sorta hard on this. It's great for making random topics weave together to form an overall infrastructure of chaos. That made little sense. That's why it's here, and not some critically acclaimed site. Ooooooooooooo! I'm gonna quote from the FLAMING CHICKENS HANDBOOK again! Yep! I bet you were just breathless in anticipation. Okay. Here goes. Code: 472 of the Flaming Chickens Handbook states that this site in no way aknowledges the existance of other, better sites (hereon reffered to as the Losers) The Losers are a myth. The Patron Saint of Paper Clips (me again!) claims no knowledge as to where that particullary nasty rumor started, but confirms that this is the best site ever. It would be a sin against humanity for a better site to exist. Should you refuse to aknowledge the Patron Saint of Paper Clips as the ruler of the Internet, you will be subjected to punishment as stated in Code 343 of the Flaming Chicken Handbook (i.e. Experience vague, pain-like sensations when you're not paying attention) This has been a public service announcement. This is a test, I repeat only a test. Had this been an actual emergency, we would have bought up all the can openers and charged 3 cows and a pig for each one. I repeat, lock all you doors and windows, this is it. I repeat, there is nothing to worry about. Everything is fine. The end is not here. I'm going, you're on you're own! Ahhhhhhhhhh!!!!!!!!!!!!!!!! I'm back!*smiles brightly* And apparantly delusional! Anyway, I just finished rereading my longest text ever. And I became inspired to talk about nothing. You see, I periodically read the longest text ever to check the constant downward spiral of my sanity. Hmmm...I seem to be entertaining myself though, even while reading what I wrote. Which is why I still go to the Really Really Big Button That Doesn't Do Anything website. Because I am easily amused and have lots and lots of time on my hands. Maybe, some day far in the future (like next Thursday) I'll print a copy of this insane text. And then go door to door distributing it. Eventually, this would become a monthly tradition. Whole families would gather around their front door, in breathless anticipation while they attempted to barracade me out. I can just see the whole community rising to thwart my attempts to spread love, joy and insane chaos. I probley wouldn't actually print this out (think how much paper it would take!) but if I do, only friends and enemies will receive copies. Hmmmm...maybe my condition is worsening. Or not. I'm still peeved about the cartoon owl from the Tootsie Roll Pop commercials. He is pure evil. TACO will eventually destroy him. Unless he has already been destroyed by an even more radical Anti-Cartoon-Owl group. I hope not. Or, would that be good? I suppose I could let someone else have the glory. After all, I'm not in this line of buisness for the fame, fortune and power. What line of buisness, do you ask? Why, the assasinating annoying cartoon characters buisness. (Actually I just question them untill they spontaneously combust, I ask lots of questions) So, in conclusion, ladies and gentleman of the jury(that's you) I could not have possibly tortured "Mr. Owl" to death. I love owls. Hmm...I seem to be jumping from one subject to another more frequently. Either I am growing more comfortable with my on-line writing, or I am progressivly getting more insane and chaotic. I also am psyco-analyzing myself a lot today...hmmmm...I'm even saying "hmmmmm..." a lot. Just like a real psychologist. Hmmmmmmm. Time for another boring disclaimer!!!!!!! Code: 742 of the Flaming Chickens Handbook states that in no part does the Patron Saint of Paper Clips (That's still me!) actually claim to be mentally ill. That's either a) a publicity stunt b) An attempt at humor c) a cry for help or d) none of the above You can e-mail your responses by conducting a scavenger hunt of this site. Some of the pages of this site contain a link encouging the two and a half people to e-mail the Patron Saint of Paper Clips. There may also be evil little links that are designed to confuse you. These links send stuff to someone named johnjones333@hotmail.com The Patron Saint of Paper Clips does not know who this individual is, but sincerly wishes that you send all your hate mail to him. Not that the aformentioned individual claims to have received hate mail (or mail of any kind) via a website link. Thank-you for your time. Remember to send your answers to my sanity quiz to the e-mail account,"""
# bst2 = BST()
# code = encode_morse(bst2, text)
# print(code)


stop = timeit.default_timer()

print('Time: ', stop - start)  



"""

                                   (root)               
                                     |                   
                         -------------------------       
                       /                            \       
                     /                                \    
                   /                                    \    
                 E                                       T         
                 |                                       |        
             ---------                               --------      
          /             \                         /           \    
        /                 \                     /               \      
       I                   A                   N                 M  
   /       \           /      \            /       \           /   \
  S         U         R        W          D         K         G     O
 / \       /         /        / \        / \       / \       / \   
H   V     F         L         P   J     B   X     C   Y     Z   Q


Most inefficient Tree is data1 (by letter) because it must do more comparisons
when building the tree (as letters are not in the order in which they 
will be inserted. Most efficient is by splitting as it is in the order
in which they will appear in the tree and very little comparison 
is needed to input them.

You could theoretically figure it out by running timed trials of gigantic 
morse code conversions.


"""