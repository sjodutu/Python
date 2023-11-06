import random
when = ['One day', 'There was Once', 'Once upon a time', 'A long time ago', 'IT was lovely summer weather in the country', 'Far out in the ocean']
who = ['the golden corn', 'an old woman', 'the cook', 'a queen ', 'an old mother', 'a dear little girl', 'a poor widow and her son Jack']
what = ['piled up in the meadows looked beautiful', 'sitting in her rocking chair', 'went into the kitchen to make some gingerbread', 'had no children', 'had three little pigs', 'loved by every one who looked at her']
subject = ['thinking how happy she would be if she had a child', "One winter's afternoon she was sitting by the window sewing when she pricked her finger", 'So when they were old enough, she sent them out into the world to seek their fortunes.']
'''
story1 = random.choice(when)
story2 = random.choice(who)
story3 = random.choice(what)
story4 = random.choice(subject)
print(f'{story1} {story2} {story3} {story4}')
'''
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(what) + ', went to the ' + random.choice(subject))


