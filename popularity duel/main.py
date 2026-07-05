import game_data
import art
import random


def compare(person1,person2):
    print(f"Compare A: {person1['name']} , {person1['description']}, From {person1['country']}")
    print(art.vs)
    print(f"Against B: {person2['name']} , {person2['description']}, From {person2['country']}")



def play_game():

    score = 0
    random1 = random.randint(1, len(game_data.data))
    random2 = random.randint(1, len(game_data.data))
    if random1 == random2:
        random2 = random.randint(1, 50)
    person1 = game_data.data[random1]
    person2 = game_data.data[random2]
    while True:
        print(art.logo)

        compare(person1,person2)

        if person1['follower_count']> person2['follower_count']:
            correct = 'a'
        else:
            correct = 'b'

        choice = input("Who has more followers : A or B : ").lower()
        if choice==correct:

                score+=1
                print(f"You are right. Current Score {score}")
                if choice=='b':
                    person1 = person2
                    person2 = random.choice(game_data.data)
                    if person1 == person2:
                        person2 = random.choice(game_data.data)
        else:
                print("\n" * 10)
                print(art.logo)
                print(f"Sorry you are wrong. Final Score{score}")
                break





play_game()
