# day 32_100 days  - Random Greeting

import random

greetings = ["Bonjour","Salut","Hola","¿Qué tal?","Zdravstvuyte","Privet","Nǐn hǎo","Nǐ hǎo","Salve","Ciao","Konnichiwa","Yā, Yō","Guten Tag","Hallo, Hi","Olá","Oi","Anyoung haseyo","Anyoung","Asalaam alaikum","Ahlan","Goddag","Hej, Halløj","Shikamoo","Habari, Hujambo","Goedendag","Hoi, Hallo","Yassas","Yassou","Dzień dobry","Cześć, Witaj","Selamat siang","Halo","Namaste, Namaskar","Hai, Helo","God dag","Hei","Merhaba","Selam","Shalom","Hey","God dag","Hej, Tjena"]

rnum = random.randint(0,len(greetings))
print(greetings[rnum])