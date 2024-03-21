import random
import hangman_stages
while True:
    print('''WELCOME TO THE GAME "HANGMAN"''')
    category=input("\nWhich category words you want to guess(animals,fruits,countries)?:").lower()
    mode=input("\nWhich mode(easy,medium,difficult) do you want ?:").lower()
    if category=="fruits" and mode=="easy":
        words=["apple","kiwi","mango"]
    elif category=="fruits" and mode=="medium":
        words=["guava","lychee","papaya"]
    elif category=="fruits" and mode=="difficult":
        words=["pomegranate","dragonfruit"]
    elif category=="animals" and mode=="easy":
        words=["cat","fish","dog"]
    elif category=="animals" and mode=="medium":
        words=["elephant","giraffe","penguin"]
    elif category=="animals" and mode=="difficult":
        words=["chameleon","platypus","narwhal"]
    elif category=="countries" and mode=="easy":
        words=["india","china","egypt"]
    elif category=="countries" and mode=="medium":
        words=["france","germany","australia"]
    elif category=="countries" and mode=="difficult":
        words=["madagascar","Kyrgyzstan","Liechtenstein"]

    chosen=random.choice(words)
    if chosen=="apple":
        print('''\nHint:"Keeps the doctor away."\n''')
    elif chosen=="kiwi":
        print('''\nHint:"This fruit has brown, fuzzy skin and vibrant green flesh inside."\n''')
    elif chosen=="mango":
        print('''\nHint:"This juicy fruit is known as the "king of fruits."\n''')
    elif chosen=="guava":
        print('''\nHint:"This tropical fruit has a green or yellow skin and pink or white flesh, with a distinct fragrance."\n''')
    elif chosen=="lychee":
        print('''\nHint:" This small fruit has a rough, pinkish-red skin and sweet, translucent flesh surrounding a large seed."\n''')
    elif chosen=="papaya":
        print('''\nHint:"This tropical fruit has orange flesh and black seeds in the center, and it's often used in smoothies and salads."\n''')
    elif chosen=="pomegranate":
        print('''\nHint:"This fruit is known for its juicy seeds and is often associated with health benefits."\n''')
    elif chosen=="dragonfruit":
        print('''\nHint:"This exotic fruit has a bright pink or yellow skin with green scales, and its flesh is speckled with black seeds."\n''')
    elif chosen=="cat":
        print('''\nHint:"This common household pet is known for its independent and playful nature."\n''')
    elif chosen=="dog":
        print('''\nHint:"Often referred to as "man's best friend," this animal is loyal, friendly, and comes in various breeds."\n''')
    elif chosen=="fish":
        print('''\nHint:"This animal lives underwater, breathes through gills, and comes in various shapes, sizes, and colors."\n''')
    elif chosen=="elephant":
        print('''\nHint:"This large mammal is known for its long trunk, tusks, and large ears."\n''')
    elif chosen=="giraffe":
        print('''\nHint:"This tall animal has a long neck, spotted coat, and is known for being the tallest mammal on Earth."\n''')
    elif chosen=="penguin":
        print('''\nHint:"This flightless bird is often found in cold climates and is known for its black and white plumage."\n''')
    elif chosen=="chameleon":
        print('''\nHint:"This reptile is famous for its ability to change color to blend in with its surroundings."\n''')
    elif chosen=="platypus":
        print('''\nHint:"This unique mammal, native to Australia, has a duck-like bill, webbed feet, and lays eggs."\n''')
    elif chosen=="narwhal":
        print('''\nHint:" Often referred to as the "unicorn of the sea," this whale species is known for its long spiral tusk."\n''')
    elif chosen=="india":
        print('''\nHint:" This country is known for its diverse culture, spicy cuisine, iconic landmarks such as the Taj Mahal, and Bollywood movies."\n''')
    elif chosen=="egypt":
        print('''\nHint:"This African country is known for its ancient pyramids, Sphinx, and the Nile River."\n''')
    elif chosen=="china":
        print('''\nHint:"This Asian country is known for its rich history, including the Great Wall, as well as its delicious cuisine and vibrant culture."\n''')
    elif chosen=="france":
        print('''\nHint:"This European country is known for its romantic capital city, Paris, and its iconic landmark, the Eiffel Tower."\n''')
    elif chosen=="germany":
        print('''\nHint:"This country is known for its rich history, delicious cuisine (including sausages and beer), and famous car brands like BMW and Volkswagen."\n''')
    elif chosen=="australia":
        print('''\nHint:" This country is known for its unique wildlife (including kangaroos and koalas), stunning natural landscapes, and famous landmarks like the Sydney Opera House."\n''')
    elif chosen=="Kyrgyzstan":
        print('''\nHint:"This Central Asian country is known for its stunning mountain landscapes and nomadic traditions."\n''')
    elif chosen=="Liechtenstein":
        print('''\nHint:"This small European country is known for its beautiful alpine scenery and as a tax haven."\n''')
    elif chosen=="madagascar":
        print('''\nHint:"This island country off the southeastern coast of Africa is known for its unique biodiversity, including lemurs and baobab trees."\n''')

    display=[]
    for i in  range(len(chosen)):
        display.append("_")
    end=False
    lives=6
    a=[]

    while not end:
        guessed_letter=input("Guess a letter:").lower()
        if guessed_letter in a:
            print("You are repeating the incorrect letter again\n")
        elif guessed_letter in display:
            print("You have already guesed that letter\n")
        else:
            for j in range(len(chosen)):
                letter=chosen[j]
                if guessed_letter==letter:
                    display[j]=guessed_letter
            display2=" ".join(display)
            if guessed_letter in chosen:
                print(display2)
            if guessed_letter not in chosen:
                a.append(guessed_letter)
                a2=" ".join(a)
                print(display2)
                lives =lives-1
                if lives==1:
                    print("\nYour Guessed letters which were incorrect:"+str(a2)+"\n")
                    print("\nYou are now left with just "+str( lives)+" live\n")
                elif lives>0:
                    print("\nYour Guessed letters which were incorrect:"+str(a2)+"\n")
                    print("\nYou are now left with "+str( lives)+" lives\n")
                elif lives==0:
                    end=True
                    print("\nYou are left with no lives You lose!!\n")         
                print(hangman_stages.Hangman_stages[lives])
            if '_' not in display:
                end=True
                print("\nYou win!!")
                print("\nYou guessed the right word which was "+str(chosen))
    again=input("Do you want to play the game again?(yes or no):\n")
    if again!="yes":
        break       
     

        








