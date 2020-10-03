game_running = True
while game_running:
    new_round = True
    print("*"*26)
    print("*"*26)
    print(" WELCOME TO THE QUIZ GAME!")

    print("*"*26)
    print("*"*26)
    print("DO YOU THINK YOU ARE ENOUGH INTELLIGENT TO PASS THIS GAME?")
    print("*"*26)
    print("*"*26)
    print("Type 1 if you want to quit and 2 to continue")
    player_choice = input("Enter Your Choice:")
    if player_choice == '1':
        game_running = False
        new_round = False
    elif player_choice == '2':
        print("BE READY TO FACE QUESTIONS")
    while new_round:

        print("1.When Micheal Jordan played for NBA for the chicago bulls,\nhow many NBA championship did he win?")
        print("a)8         b)7")
        print("c)6         d)9")
        quizer_choice = input("Enter Your Choice:")
        if quizer_choice == 'c':
            print("correct")
        elif quizer_choice != 'c':
            print("you are wrong try again next time")

        print("2.Who was the first indian to go in space?")
        print("a)Vikram Ambala         b)Ravish Malhotra")
        print("c)Rakesh Sharma         d)Nagapathi Bhat")
        choice1 = input("Enter your choice:")
        if choice1 == 'c':
            print('correct')
        elif choice1 != 'c':
            print("you are wrong try again next time")

        print("3.Who was the first man to climb Mount everest\nwithout oxygen?")
        print("a)Junko Tabei         b)Reinhold Messener")
        print("c)Peter Habeler       d)Phu Dorji")
        choice2 = input("Enter your choice:")
        if choice2 == 'd':
            print('correct')
        elif choice2 != 'd':
            print("you are wrong try again next time")

        print("4.Who built the Jama Masjid?")
        print("a)Jahangir           b)Akbar")
        print("c)Imam Bukhari       d)Shah Jahan")
        choice3 = input("Enter your choice:")
        if choice3 == 'd':
            print('correct')
        elif choice3 != 'd':
            print("you are wrong try again next time")

        print("5.Who wrote the Indian National Anthem?")
        print("a)Bakim Chandra Chatterji         b)Rabindranath Tagore")
        print("c)Swami Bibekanand                d)None of the above")
        choice4 = input("Enter your choice:")
        if choice4 == 'b':
            print('correct')
        elif choice4 != 'b':
            print("you are wrong try again next time")

        print("6.Who was the first indian scientist to win a nobel prize?")
        print("a)CV Raman            b)Amartya Sen")
        print("c)Hargobind Khurana   d)Subramaniam Chandrasekhar")
        choice5 = input("Enter your choice:")
        if choice5 == 'a':
            print('correct')
        elif choice5 != 'a':
            print("you are wrong try again next time")

        print("7.Who is first indian to win a nobel prize?")
        print("a)Rabindranath Tagore         b)CV Raman")
        print("c)Mother Teresa               d)Hargobind Khurana")
        choice6 = input("Enter your choice:")
        if choice6 == 'a':
            print('correct')
        elif choice6 != 'a':
            print("you are wrong try again next time")

        print("8.Who was the first indian woman to win\nthe Miss World title?")
        print("a)Aishwarya Rai         b)Sushmita Sen")
        print("c)Reita Faria           d)Diya Mirza")
        choice7 = input("Enter your choice:")
        if choice7 == 'c':
            print('correct')
        elif choice7 != 'c':
            print("you are wrong try again next time")

        print("9.Who was the first president of India?")
        print("a)Abdul Kalam                 b)Lal Bahadur Shastri")
        print("c)DR. Rajendra prasad         d)Zakir Hussain")
        choice8 = input("Enter your choice:")
        if choice8 == 'c':
            print('correct')
        elif choice8 != 'c':
            print("you are wrong try again next time")

        print("10.Who was the first Indian to win the Booker prize?")
        print("a)Dhan Gopal Mukerji      b)Nirad C.Chaudhuri")
        print("c)Arundhati Roy           d)Arvind Adiga")
        choice9 = input("Enter your choice:")
        if choice9 == 'c':
            print('correct')
        elif choice9 != 'c':
            print("you are wrong try again next time")
            game_running = False
            new_round = False