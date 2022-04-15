from random import *

words = ['apple', 'banana', 'coffee', 'dog', 'electric', 'father', 'general', 'histroy',\
     'iron', 'jump', 'kingdom', 'love', 'monster', 'native', 'orca', 'potato', 'qeen'\
         'random', 'secret', 'trip', 'union', 'victory', 'warrior', 'xylophone', 'zoo']

answer = choice(words)
guess = str()

chances = 10

while chances > 0:
    print()

    succeed = True

    for a in answer:
        if a in guess:
            print(a, end=' ')
        else:
            print('_', end=' ')
            succeed = False
            
    print()
    print()

    if succeed:
        print('クリアしました。\nおめでとうございます！')
        input('Press Enter to exit')
        break
    print(f'残りの機会：{chances}')
    latter = input('文字を入力してください。\n')

    if len(latter) > 1:
        try:
            raise ValueError
        except ValueError:
            print('一文字のみ入力してください')
            continue

    if latter not in guess:
        guess += latter
    else:
        print('既に入力した文字です。')
    
    if latter in answer:
        print('あり！')
    else:
        print('なし')
        chances -= 1

if chances == 0:
    print('GAME OVER!!')
    print(f'The answer is \"{answer}\"')
    input('Press Enter to exit')