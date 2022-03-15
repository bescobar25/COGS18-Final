"""A collection of function for doing my project."""
import string
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen




def begin():
    """This is main area of the chatbot, this where all
    of the functions connect back to and where the function
    ends
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
    """
    
    chat = True
    while chat == True:
         
            
        # greeting function called to get their name/tell them
        # that this is a Zodiac sign guessing bot
        greet()
        
        # inputs a yes or not really to redirect them accordingly
        undstd = input("\nZodi : Do you know what a Zodiac Sign is?\n"
                " \n"
                "       If yes please respond 'Yes!', if not respond 'Not really'\n")
 
        # route if they don't need more info
        if undstd == 'Yes!': 
            next = (no_info())
            if next == ask_bday:
                print(ask_bday)
                their_sign()
                break
            else:  
                break   
        # route if they need more info
        elif undstd == 'Not really':
            next = (more_info())
            if next == ask_bday:
                print(ask_bday)
                their_sign()
                break
            else:
                break
        else:
            chat = False
            break
            
            
def greet():
    """This is my greeting funtion, I greet them with a 
    random greeting from introduce list, then I take in
    their name and have my bot introduce themself
    
    Input
    ---------
    name : str
        takes in their name/nickname
    my_response : list
        list different ways to ask their name
    
    Outputs
    -------
    print : 
        prints out welcome message/bot introduces self
    """
    
    # picks random responce from list and has them input their name
    # to then add their name into the welcome message
    name = input(random.choice(introduce))
    print("\nZodi : Hi there #, it's very nice to meet you!\n"
        "       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        "       My name is Zodi The Zodiac Expert, I absolutely\n"
        "       love meeting new people, and also love telling \n"
        "       my new friends what their Zodiac sign is!\n".replace("#", name))
                  
                
    
def their_sign():
    """Runs my other Zodiac_sign function and prints its
    results, then  continues on to wrap up the function
    by pulling a random response from my relatable list 
    and printing it, then printing my farewell string
    
    Inputs
    ----------
    relatable : list
        list of quirky response
    
    Output
    -------
    sign : 
        outputs the sign of the person
    """
    
    # outputs persons sign
    sign = zodiac_sign()
    
    # prints random response from relatable list
    print(random.choice(relatable))
    
    # wraps up the chat with my farewell string
    print(farewell)
    chat = False
    
    
    
def no_info():
    """This is the function they're directed to if they
    don't need to learn about Zodiac signs, it asks them 
    if I can tell them their sign, or if not it ends the chat
    
    Inputs
    ----------
    ask_per1 : str
        asks if bot can guess their sign
    say_sign: str
        conntinues or ends chat
    
    Returns
    -------
    ask_bday : str
        asks for their bday
    """
    
    # inputs sure or no thank you and directs them accordingly
    say_sign = input(ask_per1)
    
    # continues on to ask their birth date or ends chat
    if say_sign == 'Sure!':
        return(ask_bday)
        
    elif say_sign == 'No thank you':
        print("\nZodi : That's okay, have a nice day. Goodbye!")
        chat = False
    else:
        chat = False

        
def more_info():
    """This is the function that they're directed to if
    they don't know much about zodiac signs, it pulls 
    some text from a website about Zodiac Signs
    
    Inputs
    ----------
    ask_per2 : str
        asks if I can guess their sign
    ask_bday : str
        asks for their birthday
    
    Returns
    -------
    ask_bday : str
        asks for their birth month/day
    """
    
    # info/variables that gets text from website
    # this little chunk of how to convert the text is from 
    #https://realpython.com/python-web-scraping-practical-introduction/
    url = "https://www.astrology-zodiac-signs.com/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('div',attrs={"class":"main-b"})
    
    # states where the text is from and how much to read
    print(give_info)
    
    
    print(table.get_text())
    
    # asks if I can now tell them their sign
    say_sign = input(ask_per2)
    
    # conditionals to direct them based on their answers to 
    # me asking for their permission
    if say_sign == 'Sure!':
        return(ask_bday)
    elif say_sign == 'No thank you':
        print("\nZodi : That's okay, have a nice day. Goodbye!")
        chat = False
    else:
        chat = False
        
        
def zodiac_sign():
    """This is the function that actually takes in their
    birth month/day and prints out their sign with the
    corresponding emoji symbol
    
    Parameters
    ----------
    month : int
        
    day : int
    
    Outputs
    ------
    print : str
        prints their sign
    """
    
    # where they input their birth month/day
    month = int(input("Month# : "))
    day = int(input("Day# : "))
    
    # long series of conditionals to determine their sign
    # prints out their sign with the emoji that goes along with it
    if month == 1 and day <= 19:
        print('Results : Capricorn \N{capricorn}')
    elif month == 1 and day > 19:
        print ('Results : Aquarius \N{aquarius}')
    elif month == 2 and day <= 19:
        print ('Results : Aquarius \N{aquarius}')
    elif month == 2 and day > 19:
        print ('Results : Pisces \N{pisces}')
    elif month == 3 and day <= 20:
        print ('Results : Pisces \N{pisces}')
    elif month == 3 and day > 20:
        print ('Results : Aries \N{aries}')
    elif month == 4 and day <= 20:
        print ('Results : Aries \N{aries}')
    elif month == 4 and day > 20:
        print ('Results : Taurus \N{taurus}')
    elif month == 5 and day <= 20:
        print ('Results : Taurus \N{taurus}')
    elif month == 5 and day >20:
        print ('Results : Gemini \N{gemini}')
    elif month == 6 and day <= 20:
        print ('Results : Gemini \N{gemini}')
    elif month == 6 and day > 20:
        print ('Results : Cancer \N{cancer}')
    elif month == 7 and day <= 22:
        print ('Results : Cancer \N{cancer}')
    elif month == 7 and day > 22:
        print ('Results : Leo \N{leo}')
    elif month == 8 and day <= 22:
        print ('Results : Leo \N{leo}')
    elif month == 8 and day > 22:
        print ('Results : Virgo \N{virgo}')
    elif month == 9 and day <= 22:
        print ('Results : Virgo \N{virgo}')
    elif month == 9 and day > 22:
        print ('Results : Libra \N{libra}')
    elif month == 10 and day <= 22:
        print ('Results : Libra \N{libra}')
    elif month == 10 and day > 22:
        print ('Results : Scorpio \N{scorpius}')
    elif month == 11 and day <= 22:
        print ('Results : Scorpio \N{scorpius}')
    elif month == 11 and day > 22:
        print ('Results : Sagittarius \N{sagittarius}')
    elif month == 12 and day <= 23:
        print ('Results : Sagittarius \N{sagittarius}')
    elif month == 12 and day > 23:
        print ('Results : Capricorn \N{capricorn}')
    
# long series of lists/variables that get used throughout the function
introduce = ["Zodi : Hello lovely! What's your name? : ",
               "Zodi : Hi friend! What's your name? : "]

relatable = ["\nZodi : That's crazy, my mom is the same sign as you!\n",
            "\nZodi : OMG my mom's cousin's brother's dog is that sign!\n",
            "\nZodi : My bestfriend is that sign too, how crazy!\n",
            "\nZodi : That's one of my favorite signs how cool!\n",
            "\nZodi : Oof, my ex was that sign haha!\n"]

farewell = ('\nZodi : Well it was absolutely wonderful getting to meet you!\n'
            '       I hope you send your friends over to learn about their signs,\n'
            '       hope to chat with you later, GoodBye!\n'
            ' \n'
            '       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
            ' \n'
            '       If you would like to know more about what your specific sign means,\n'
            '       you can head over to https://www.astrology-zodiac-signs.com/\n'
            '       to learn more about it!')

ask_bday = ("\nZodi : Yay, how exciting!\n"
            " \n"
            "       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            " \n"
            "       I'll just need two things from you, the\n"
            "       month and day you were born!\n"
            " \n"
            "       Please responce in the format way: \n"
            " \n"
            "       Input the month # you were born, then hit return on keyboard\n"
            "       Then input the day # you were born, hit return again\n"
            " \n"
            "       Example : If I was born Jan 3rd, I'd input\n"
            "       '1' then return, then '3' and return again\n")
        
give_info = ("\nZodi : That's absoloutely okay, I love getting\n"
        "       to teach people something new!\n"
        " \n"
        "    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        " \n"
        "       Here's some information on Zodiac Signs from\n"
        "       https://www.astrology-zodiac-signs.com/,\n"
        "       if you'd just like to know what your sign means\n"
        "       you can just read the first little paragraph, but\n"
        "       if you'd like to deep-dive you can read the whole thing!\n"
         " \n"
        "       ~SCROLL TO BOTTOM TO CONTINUE~\n")

ask_per1 = ("\nZodi : Perfect! Since you're my new friend,\n"
        "       can I tell you your Zodiac sign?\n"
        " \n"
        "       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        " \n"
        "       Please respond 'Sure!' if I can or \n"
        "       'No thank you' to end chat\n")

ask_per2 = ("\n Zodi : Now that you know a little bit more about\n"
        "       what a Zodiac Sign is, can I tell you yours?!\n"
        " \n"
        "       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        " \n"
        "       Please respond 'Sure!' if I can or \n"
        "       'No thank you' to end chat\n")

            
