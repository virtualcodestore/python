from collections import OrderedDict

favourite_languages = OrderedDict()
favourite_languages['Jen'] = 'python'
favourite_languages['Sarah'] = 'python'
favourite_languages['Edward'] = 'ruby'
favourite_languages['Paul'] = 'c#'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ",")
