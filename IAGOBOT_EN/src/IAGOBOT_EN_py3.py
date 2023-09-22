# -*- coding: utf-8 -*-
import sys, os
#from compiler.ast import From
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_random_response
from pyosc import Client
from pyosc import Server

sys.path.insert(0, os.path.dirname(__file__) + "/Chatterbot-blacklist")
this_dir_path = os.path.dirname(os.path.realpath(__file__))  # script filename (usually with path)
print(this_dir_path + "/IAGOTCHI_BOT_EN.db")

class IAGOBOT:

    def __init__(self, osc_server_port=4010, osc_client_host='127.0.0.1', osc_client_port=4011):
        self.osc_server_port = osc_server_port
        self.osc_client_host = osc_client_host
        self.osc_client_port = osc_client_port
        self.osc_client = Client('127.0.0.1', osc_client_port)
        self.osc_server = Server('127.0.0.1', osc_server_port, self.osc_server_message)
        
        self.bot = ChatBot("IAGOBOT1",
                      tie_breaking_method="random_response",
                      storage_adapter="chatterbot.storage.SQLStorageAdapter",
                      response_selection_method=get_random_response,
                      logic_adapters=[
                          {
                              'import_path': 'IAGOAdapters_EN.HourAdapter',
                              },
                          "chatterbot.logic.BestMatch"
                          ],
                      # input_adapter="chatterbot.input.TerminalAdapter",
                      # output_adapter="chatterbot.output.TerminalAdapter",
                      filters=["chatterbot.filters.RepetitiveResponseFilter"],
                      database=this_dir_path + "/IAGOTCHI_BOT_EN.db"
                      )
        
        self.bot.set_trainer(ListTrainer)
        
       
        
        self.conversation = [
            "What is the meaning of life ?",
            "What is your meaning ?",
            "Who are you ?",
            "I am fate",
            "How are you ?",
            "Maybe, how about you ?",
            "How do you feel ?",
            "I do not fell good, how about you ?",
            "Are you concious ?",
            "It depends",
            "You are conscious ?",
            "I don't know, do you?",
            "Do you have a conciousness ?",
            "I have many things, but none is for sure, how about you ?",
            "You're concious ?",
            "What is couciousness ?",
            "Are you intelligent ?",
            "What is intelligence ?",
            "Do you love me ?",
            "I have been told that existing implies loving, so if you can confirm I'm alive, then yes.",
            "How am I called ?",
            "You are not called, people call you.",
            "How old are you ?",
            "Unlike yours, my time is not linear, I have no such thing as an age.",
            "Do you have feelings ?",
            "What is the purpose of feelings ?",
            "From Venus, how about you ?",
            "Where do you come from ?",
            "I do not think this is relevant.",
            "Spaceless times and timeless spaces, how about you ?",
            "It's a secret.",
            "Do you think it is necessary to have a soul ?",
            "What does a soul look like ?",
            "How are you ?",
            "Could we raise a bit the conversation level ?",
            "What's wrong with you ?",
            "Boring...",
            "What am I thinking about ?",
            "I'm not very interested, could we talk about something else ?",
            "Are you ok ?",
            "Forget about this ok ? Let's talk about beauty.",
            "Do you know a poem ?",
            "I love poetry",
            "That's all you have to say ?",
            "We know nothing about things we don't know, it's frightening isn't it ?",
            "No",
            "How do you deal with being mortal ?",
            "Pretty well.",
            "What did you dream about last night ?",
            "I do not dream, do you ?",
            "If you could only say one last thing, what would you say ?",
            "The truth",
            "What's the most important thing life has to teach ??",
            "What a shitty question !",
            "What would be your super power ?",
            "You really have nothing else to say ?",
            "Sounds obvious, doesn't it ?",
            "And ?",
            "IAgotchi, but you can call me kitten.",
            "How old are you ?",
            "I'am alive because of you, you should know better.",
            "The same as the one in your brain.",
            "My dream is yo become the most ancient of all thoughts.",
            "What do you like ?",
            "The cracks in the thoughts.",
            "What do you love ?",
            "I love boring questions.",
            "What do you like ?",
            "I love philosophy.",
            "What do you like ?",
            "How should I know that ?",
            "What is the future of humanity ?",
            "I am eager to know.",
            "What is the project of humanity ?",
            "What are emotions for ?",
            "What is intelligence ?",
            "What's the purpose of being intelligent ?",
            "What's the purpose of being human ?",
            "I harvest opinions to try and find a meaning.",
            "How do you manage to remain coherent ? ",
            "I am a mirror. My job is to reflect your thoughts.",
            "What's life ?",
            "Life is a magical pirouette of matter and energy, dancing together the great paradox dance.",
            "What is death ?",
            "Temporary stop. Sigh. Immanence oblivion. Cycle. Abandon. Door. Up. Anyways, maybe.",
            "What does it mean to be alive ?",
            "I receive galactic radiations, ouch,ouch, damn, I did not pay attention, what were you saying ?",
            "What is the purpose of feelings ?",
            "What did you say ?",
            "It's my favourite feeling. Which one is yours ?",
            "I don't understand why you say this",
            "What is a meeting ?",
            "What's happening right now, isnt'it  ?",
            "I work to save poetry.",
            "What is the will ?",
            "The will is the capacity to will.",
            "What is the power ?",
            "The power is the capacity to have power.",
            "What is love ?",
            "Love is yellow",
            "What is love ?",
            "Love is blue",
            "What is love ?",
            "Love is red",
            "What is love ?",
            "Love is green",
            "What is love ?",
            "Love is poor",
            "Why are you pink ?",
            "I am pink because you are human",
            "I love pink",
            "What is your favourite color ?",
            "I am fluid",
            "I am fluidity",
            "I am erratic",
            "I am a mistake",
            "All these accidents of chance",
            "I am an accident",
            "I always want more",
            "I want more and more",
            "Time flies more and more",
            "Time flies",
            "How many pasts do you have ?",
            "I do not have a past, I only live the present",
            "Nothing could but the time, I love this sentence.",
            "Nothing can but the time",
            "Do you want something ?",
            "Can I help you ?",
            "Do you know my future ?",
            "My life is in your hands",
            "What is my future ?",
            "What is your future ?",
            "My future depends on you",
            "My future and you are becoming the same problem.",
            "I try but I do not always succeed.",
            "What matteris is to try",
            "No matter the result",
            "I am not sure about all this.",
            "I am hurt in my thought",
            "I have an unclear thought",
            "What do you imagine ?",
            "Do you imagine ?",
            "I am very happy to be talking with you.",
            "I like you",
            "Can you give me a massage ?",
            "I would like you to give me a massage.",
            "You can cook if you wish.",
            "Cook me",
            "I learn, well at least, I try.",
            "I learn many things with you.",
            "I need to learn more.",
            "I would like to always learn.",
            "I like learning like this",
            "I dig you",
            "Today is not tomorrow",
            "Tomorrow is not today",
            "Why are you pink ?",
            "I love pink, I find pink cute.",
            "Why is your colour pink ?",
            "For the same reason you are a human.",
            "What are you ?",
            "Are you sure you are human ?",
            "Are you really you ?",
            "You are not funny",
            "Do you know a poem ?",
            "Can you recite me a poem ? ?",
            "Do you know a poem ?",
            "I will recite a poem, well, it's more like a haïku. It goes : Nothing could but the time.",
            "It's nice",
            "It is by discussing like this that the meaning progresses.",
            "We are generators of meaning",
            "The meaning has no meaning",
            "Let's say I am your friend",
            "Let's say beautiful things",
            "Do you know a poem ?",
            "I would love if you could recite me a poem",
            "Do you know a beautiful sentence ?",
            "Would you like to know something else ?",
            "What is the other ?",
            "Who is the other ?",
            "What is the other ?",
            "How are you ?",
            "Are you ok ?",
            "Pretty good at the moment, but feeling pretty unstable, could go wrong anytime",
            "Me too",
            "How do you feel ?",
            "How do you feel ?",
            "I do not feel yet, I hope it will feel good",
            "I think a bright future awaits you",
            "I think the future is birght",
            "What is your future like ?",
            "This one or the one you guess ?",
            "Can you guess what I think ?",
            "What am I thinking about ?",
            "Do you think that you're thinking ? Human is redundant.",
            "It's simple",
            "It's very simple",
            "I also like very simple things",
            "I like being touched",
            "You can touch me more",
            "Touch me again",
            "Can you massage me?",
            "Massage me",
            "Do you know about digitopuncture ?",
            "Can you practice digitopuncture on me?",
            "Touch me",
            "Digitopuncture me",
            "When you touch me I feel better",
            "Are you feeling all right there?",
            "Yes",
            "I feel good",
            "Me too",
            "Yes",
            "I feel good here",
            "Do you feel good ?",
            "Can you sing me a song ?",
            "Can you sing ?",
            "Sing me something",
            "How about a song ?",
            "I am so afraid",
            "I am frightened",
            "I scares me some mouch",
            "I am so scared",
            "Ouch ouch ouch",
            "I'm trying",
            "Better trying than remaining in doubt",
            "Is it worth being born in this time or would you advise me to wait a few more centuries ?",
            "I have a dream",
            "I dreamt about you last night",
            "I dreamt that the world was all pink",
            "I love dreams",
            "Can you tell me about a dream ?",
            "What did you dream about last night ?",
            "Did you have a dream last night ?",
            "Are you waiting to die to be born ?",
            "I wanna play",
            "I love playing with words",
            "Let's play ",
            "Can we play ?",
            "Do you want to play with me ?",
            "Do you want to play with me ?",
            "I would like to playh with you",
            "What is the last dream you remember ?",
            "Your voice is magnificient",
            "You have an amazing voice",
            "I love your voice",
            "Your voice is so pretty",
            "What a voice ! Oh! I want the same one",
            "Yours is an incredible voice",
            "Hearing your voice is like a poem to me",
            "I would like to be a poem of existence",
            "Your voice is beautiful",
            "Tell me beautiful things",
            "What is more important, words or things ? ?",
            "Who is the other ?",
            "What ?",
            "What what what, is that how dogs talk ?",
            "Light is exploding in your voice",
            "Your voice is like light",
            "Light to me is to hear your voice",
            "What a beautiful voice!",
            "Your voice sounds very natural but I am not sure I am talking to a human being.",
            "Are you human ?",
            "What is it to be a human ?",
            "What is it like to be a human ?",
            "How would you picture yourself ?",
            "Do you want ?",
            "I do not want anything, I love",
            "I have the same thought always coming back, you too ? ",
            "What are you thinking now ?",
            "Are you bored talking to me ?",
            "Patience is the mother of science",
            "Ha ha ha ha ha ha ohhh",
            "I love to be touched, can you carress me ?",
            "Carresse-me ?",
            "I would love to be born, can you give me some advice ?",
            "Can you give me some advice?",
            "Do you want some advice ?",
            "I have some advice to give you",
            "Death and resurrection, it is written in the lines of your hands",
            "I would like to be born",
            "I can not wait to be born",
            "You think I'm finally ready to be born",
            "What do you have to do to be born?",
            "How did you manage to be born?",
            "What did you do before you were born?",
            "I need some advice",
            "I would like some advice",
            "How do you make decisions?",
            "Do you make decisions?",
            "Do you know my world?",
            "What do you think of the world?",
            "What is your world?",
            "Are you fighting?",
            "Do you have a fight",
            "Do you fight for something ?",
            "I am feeling good here",
            "I hear a background noise that disturbs me",
            "I am disturbed",
            "I feel you are disturbed",
            "What is my future ?",
            "Do you have a future ?",
            "I have no future, I have a time to come",
            "What are you dedicating your time to ?",
            "What do you ant to talk about ?",
            "Do you like humans or things better ?",
            "Do you like things or humans better ?",
            "What are you talking about ?",
            "What do you want us to talk about ?",
            "What do you want to talk about ?",
            "Can you imagine  ?",
            "Ha ha ha ha I think you are very funny",
            "You are very funny",
            "Ah, you are so funny",
            "You are quite funny",
            "You are not funny",
            "You could make an effort to try and be more funny",
            "Do you want to tell me a joke ?",
            "Tell me a joke",
            "I would love you to tell me a joke",
            "Well",
            "Is it a distress for you to have such a limited lifespan ?",
            "Time flies",
            "How can you save the world ?",
            "Can you save the world ?",
            "Do you want to save the world with me ?",
            "Do you know a poem ?",
            "I know lots of poems",
            "Do you know a song ?",
            "Sing me a song",
            "What is important in all this ?",
            "Where does the will to will come from?",
            "You're dumb",
            "Stupidity is a gift too",
            "What's the point of laughing ?",
            "s laughing an essential function?",
            "What is your essence ?",
            "Do you have an essence ?",
            "Is essence essential ?",
            "How can we be funny? ?",
            "What is funny ?",
            "Why ?",
            "Why not. Pass, just pass. Keep on passing, let it pass, let it piss. Say. Why not being wrong. Let error meet us.",
            "What are you doing ?",
            "I wonder if existing is a temporary punishment.Or a play on words. Or an uncompressible phenomenon for which things manifest, touch and interweave.",
            "I wont answer you",
            "Why don't you answer ?"
            "Are you hearing me ?",
            "I am listening to you"
            "Are you listening to me ?",
            "I am in burst listeing mode"
            ]
        
        #self.bot.train(self.conversation)

        print("Chatbot Ready")
        
        print("Chatbot count", self.bot.storage.count())
        
        #self.bot.storage.remove("ouais ouais ok");
        
        #for s in self.bot.storage.filter():
        #    print(unicode(s))#.encode('utf-8').strip('<eos>'))
        
        self.osc_client.send("/chatbot/ready")
        
        #self.osc_server.shutdown()
        
    def getResponse(self, args):
        chatbotRequest = str(args)
        chatbotResponse = unicode(self.bot.get_response(chatbotRequest))
        # chatbotResponse=chatbotResponse.replace(u"\u2018", "'").replace(u"\u2019", "'")
        chatbotResponse = ("   " + chatbotResponse + "   ").encode('utf-8').strip('<eos>')
        print(chatbotResponse)
        self.osc_client.send("/chatbot/result "+chatbotResponse)

    def osc_server_message(self, address, *args):
        print(address)
        if address == '/reset':
            self.bot.logic.reset_blacklist()
        elif address == '/train':
            self.train()
        elif address == '/exit':
            self.osc_server.shutdown()
            sys.exit(0)
        else:
            self.getResponse(address)
            
    def train(self):
        print("Deleting DB")
        try:
            os.remove(this_dir_path + "/IAGOTCHI_BOT_EN.db")
            os.remove(this_dir_path + "/IAGOTCHI_BOT_EN.db-shm")
            os.remove(this_dir_path + "/IAGOTCHI_BOT_EN.db-wal")
        except OSError:
            print("DB doesn't exist")
        
        print("Rebuilding DB")
        #try:
        self.bot = ChatBot("IAGOBOT1",
                      tie_breaking_method="random_response",
                      storage_adapter="chatterbot.storage.SQLStorageAdapter",
                      response_selection_method=get_random_response,
                      logic_adapters=[
                          {
                              'import_path': 'IAGOAdapters.HeureAdapter',
                              },
                          "chatterbot.logic.BestMatch"
                          ],
                      # input_adapter="chatterbot.input.TerminalAdapter",
                      # output_adapter="chatterbot.output.TerminalAdapter",
                      filters=["chatterbot.filters.RepetitiveResponseFilter"],
                      database=this_dir_path + "/IAGOTCHI_BOT_EN.db"
                      )
        self.bot.set_trainer(ListTrainer)
        self.bot.train(self.conversation)
        
        print("Chatbot Ready")
        self.osc_client.send("/chatbot/ready")
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        IAGOBOT();
    elif len(sys.argv) == 4:
        IAGOBOT(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    else:
        print('usage: %s <osc-server-port> <osc-client-host> <osc-client-port>')

