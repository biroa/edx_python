sec = int(input('give a number: '))

days       = int((sec//86400))
hours      = int((sec%86400)/3600)
minutes    = int(((sec%86400)%3600)/60)
seconds = int(round(((sec % 86400) % 3600) % 60,2));
print(days , " days " , hours , " hours " , minutes , " minutes " , seconds , " seconds");
