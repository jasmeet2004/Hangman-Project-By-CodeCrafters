import random
import hangman_stages
import pyfiglet
score=0
text=pyfiglet.print_figlet(text="HANGMAN",colors="Cyan",font="Slant")

print("\nNOTE:You will get 5 points for every right guess and -2 for every wrong guess\n")
while True:
    
    print('''For choosing category-:
    Enter 1 for Fruits.
    Enter 2 for Animals.
    Enter 3 for Sports.
    Enter 4 for Countries.
    Enter 5 for Car companies.''')
    category=input("\nWhich category words you want to guess(Fruits,Animals,Sports,Countries,Car companies)?:")
    print('''\nFor choosing mode-:
    Enter 1 for easy.
    Enter 2 for medium.
    Enter 3 for difficult.''')
    mode=input("\nWhich mode(easy,medium,difficult) do you want ?:")
    words={ "1":{
             "1":{
                "apple":"Keeps the doctor away.",
                "kiwi":"This fruit has brown, fuzzy skin and vibrant green flesh inside",
                "mango":"This juicy fruit is known as the king of fruits."
               },
            "2":{
                "guava":"This tropical fruit has a green or yellow skin and pink or white flesh, with a distinct fragrance.",
                "lychee":"This small fruit has a rough, pinkish-red skin and sweet, translucent flesh surrounding a large seed.",
                "papaya":"This tropical fruit has orange flesh and black seeds in the center, and it's often used in smoothies and salads."
                    },
            "3":{
                "pomegranate":"This fruit is known for its juicy seeds and is often associated with health benefits.",
                "dragonfruit":"This exotic fruit has a bright pink or yellow skin with green scales, and its flesh is speckled with black seeds."

                        }
                    },
            "2": {   
              "1":{
                  "cat":"This common household pet is known for its independent and playful nature.",
                  "fish":"This animal lives underwater, breathes through gills, and comes in various shapes, sizes, and colors.",
                  "dog":'''Often referred to as "man's best friend," this animal is loyal, friendly, and comes in various breeds.'''

              },
              "2":{
                  "elephant":"This large mammal is known for its long trunk, tusks, and large ears.",
                  "giraffe":"This tall animal has a long neck, spotted coat, and is known for being the tallest mammal on Earth.",
                  "penguin":"This flightless bird is often found in cold climates and is known for its black and white plumage."},
              "3":{
                  "chameleon":"This reptile is famous for its ability to change color to blend in with its surroundings.",
                  "platypus":"This unique mammal, native to Australia, has a duck-like bill, webbed feet, and lays eggs.",
                  "narwhal":'''Often referred to as the "unicorn of the sea," this whale species is known for its long spiral tusk.'''
                
                  }             

                } ,
              
            "3":{
                "1":{
                    "soccer":"This sport is also known as football in many countries.",
                    "basketball":"Players aim to shoot a ball through a hoop to score points.",
                    "tennis":" Players use rackets to hit a ball over a net into the opponent's court."

                },
                "2":{
                    "polo":"Players ride horses and use mallets to hit a ball through the opposing team's goal.",
                    "squash":"This indoor racket sport involves hitting a small rubber ball against a wall.",
                    "hurdling":"Athletes sprint and jump over a series of obstacles known as hurdles."
                },
                "3":{
                    "bobsledding":"Teams of athletes race down an icy track in a sled at high speeds.",
                    "pentathlon":"Modern pentathlon consists of five events: fencing, swimming, equestrian show jumping, and a combined event of pistol shooting and cross-country running.",
                    "parkour":" Participants navigate obstacles in urban environments using movements such as jumping, climbing, and running."}

            },
            "4":{
                "1":{
                    "india":"This country is known for its diverse culture, spicy cuisine, iconic landmarks such as the Taj Mahal, and Bollywood movies.",
                    "china":"This Asian country is known for its rich history, including the Great Wall, as well as its delicious cuisine and vibrant culture.",
                    "egypt":"This African country is known for its ancient pyramids, Sphinx, and the Nile River."

                },
                "2":{
                    "france":"This European country is known for its romantic capital city, Paris, and its iconic landmark, the Eiffel Tower.",
                    "germany":"This country is known for its rich history, delicious cuisine (including sausages and beer), and famous car brands like BMW and Volkswagen.",
                    "australia":"This country is known for its unique wildlife (including kangaroos and koalas), stunning natural landscapes, and famous landmarks like the Sydney Opera House."
                },
                "3":{
                    "madagascar":"This island country off the southeastern coast of Africa is known for its unique biodiversity, including lemurs and baobab trees.",
                    "kyrgyzstan":"This Central Asian country is known for its stunning mountain landscapes and nomadic traditions.",
                    "liechtenstein":"This small European country is known for its beautiful alpine scenery and as a tax haven."}


             
              },
              "5":{
                "1":{
                    "toyota":"This Japanese automaker is known for its reliable and fuel-efficient vehicles.",
                    "honda":"Another Japanese automaker famous for its diverse lineup of cars, motorcycles, and power equipment.",
                    "ford":"This American automaker is known for its trucks, SUVs, and iconic sports cars like the Mustang."

                },
                "2":{
                    "lamborghini":"An Italian brand renowned for its high-performance sports cars and luxurious grand tourers.",
                    "maserati":"An Italian luxury vehicle manufacturer known for its exotic sports cars and luxury sedans.",
                    "bugatti":": A French luxury automobile brand known for producing some of the fastest and most exclusive cars in the world."
                },
                "3":{
                    "koenigsegg":"A Swedish manufacturer known for producing high-performance hypercars with innovative engineering.",
                    "wiesmann":"A German manufacturer of hand-built luxury sports cars known for their retro-inspired design and exclusivity.",
                    "donkervoort":"A Dutch manufacturer of ultra-lightweight, high-performance sports cars inspired by classic Lotus models."}   
              
              } 
              
              }
        
    words2={"1":"FRUITS","2":"ANIMALS","3":"SPORTS","4":"COUNTRIES","5":"CAR COMPANIES"}
    
    text5=pyfiglet.print_figlet(text=words2[category],colors="GREEN")
    
    chosen=random.choice(list(words[category][mode].keys()))
    for i in words[category][mode]:
        if i==chosen:
            print("Hint:"+str(words[category][mode][chosen]))
        
    display=[]
    for i in  range(len(chosen)):
        display.append("_")
    end=False
    lives=7
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
                score+=5
            if guessed_letter not in chosen:
                score-=2
                a.append(guessed_letter)
                a2=" ".join(a)
                
                lives =lives-1
                if lives==1:
                    print(display2)
                    print("\nYour Guessed letters which were incorrect:"+str(a2)+"\n")
                    print("\nYou are now left with just "+str( lives)+" live\n")
                elif lives>0:
                    print(display2)
                    print("\nYour Guessed letters which were incorrect:"+str(a2)+"\n")
                    print("\nYou are now left with "+str( lives)+" lives\n")
                elif lives==0:
                    end=True
                    print("\nThe right word was "+str(chosen))
                    text4=pyfiglet.print_figlet(text="YOU LOOSE !!",colors="RED")
                print(hangman_stages.Hangman_stages[lives])           
                
            if '_' not in display:
                end=True
                text2=pyfiglet.print_figlet(text="YOU WIN !!",colors="BLUE")
                print("\nYou guessed the right word which was "+str(chosen))
    again=input("\nDo you want to play the game again?(yes or no):\n")
    if again!="yes":
        break   
text3=pyfiglet.print_figlet(text="YOUR SCORE : "+str(score),colors="YELLOW")        


        










        








