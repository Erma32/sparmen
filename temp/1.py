import re, os, sys

url = '/home/markus/sparmen/songTXT/Kluedo_(HT_2019)/'
for file in os.listdir(url):
    pass

txt2 = re.split(r'\d+[.]', txt)

i=0
for song in txt2:
    i+=1
    f = open(url+str(i)+'.txt', 'w')
    f.write(song)
    f.close()
# %%
txt = '''
1. Färgernas entrékuplett
Plinge-linge-plinge-ling-ling-ling
Här haltar Senap in
Plinge-linge-plinge-ling-ling-ling
Här haltar Senap in
Fienderna flyr
När Senaps vrede gryr
Plinge-linge-plinge-ling-ling-ling
Här haltar Senap in

Hallå!
Jag är Fru Påfågel.
Och jag fick en invit att komma hit,
Just denna kväll.
Hallå!?
Än är jag inte klar.
Visst blir här mat på stora fat?
Och självklart öppen bar?

Här kommer Plommon,
Professor det är jag!
Jag är så bra!
Hipp hipp hurra!
För att det finns empiri och garanti
Att jag ett geni!

Jag gör entré
En fräck fröken av hög kvalité
Här för soaré
Denna kvällen kommer bli succé

Nu kan allting ske
Nu är Scharlakan, ja Sharlakan här
Jag vet jag ger dig habegär
För att Scharlakan ja Scharlakan är här

Hon har öppnat ytterporten
Så att jag fick komma in
(Komma in det vill han)
Pastor Grön, en lustfylld prälle,
Kan förlåta synden din!

Doktor Vit, Vit,
Fick också en invit
Doktor Vit, Doktor Vit,
Här är jag!
(Där är hon)

Och nu så ska vi festa
Här hos Mono Paul
För vi är ju dom bästa

2. Tisseltassel-Tango
Blev ensam kvar, vad händer här?
En plötsligt kuslig atmosfär...
Har alla gäster hämndbegär?
Vad sker, i mörkrets foajé? Olé.

Se Grön, han smyger runt med kniv?
Och Vit, går runt, med ljusstativ?
Stämningen känns suggestiv
Vad sker, i mörkrets foajé? Ole.

Är det ingen mer än jag som vill ha mer champagne?
Nä, jag är faktiskt här för att äta lasagne.

Men jag har en känsla att det är nånting på gång!
(Vad) är det som sker? När ingen ser?
I min tangosång!

Professor Plommon ter sig slug...
Scharlakan är så full av ljug!
(Det heter lögn!)
Och Översten är aggressiv…
Vad sker, i mörkrets foajé?!
Ole.

Vad som, vi trodde var en fest.
Blev kaos, och Paul, svek varje gäst.
Vi smyger runt, i ren protest.
Vad sker? Ska nån i huset dö? Adjö!
Vad är deras mål? Ska dom ta kål? På Mono Paul?
I mörkrets foajé. Ole!

3.  Kåtplett
Åh Gu-ud, förlåt för mina synder,
Synder som kan va tabu
Är du ren och andligt trogen
Håll för dina öron nu

Herre hör nu på min bön
En bikt ifrån din Pastor Grön
Snälla Gud, förlåt
För att jag är så himla kåt

När jag var en liten gosse,
Plugga’ jag teologi,
Men på bibblan fanns en tidning
(Med) nakna män och kvinnor i

Sen kunde jag ej rå på
Lusterna som locka så
Det stärkte mig i tron,
Att Gud skapa masturbation
(Oh onanera)

Dock fanns det ett fel med min nya passion

Ty jag hade ju en celibatvision
Om man ska tjäna vår Gud
Bör man ha sexförbud
Så herre hör min bön, om att undvika mitt kön
Sen i himmelriket får jag min lön

Tänk att tjäna våran herre
Skulle va så himla svårt
Kan ni tänka er nått värre
Än att vara ständigt kåt

Så, nu har ni hört min bikt
Om mitt underlivs konflikt
Snälla Gud förlåt
Herre, för att jag är så himla kåt.

4. Kuplettsk studie av forskningens relevans
Allting är timing (och) att finna en koppling
(För) att fängsla en brottsling, ja då krävs det vett
(Va?)
Vid vinkling av sanning, jag höjer en varning
Om du går på feeling blir det aldrig rätt
(Vafalls...?!)

Spring ej omkring
I ring, du blir ding
Och nu blir det swing!
Hej och hoppsan sa!

Morsning och korsning, att finna en brottsling
Ja det kräver forskning och är inte lätt

Vid vinkling av sanning, jag höjer en varning

Om du går feeling, blir det aldrig rätt!
Forskning! (För-står ing-en-ting och jag känn-er mig ding-ding)
Satsning! (Allting rörs omkring, jag förstår ingenting)
Sanning! (Är sanning en tolkning som sen blir till forskning?)
Nej forskning är sanning - allt annat är skit

En fuling gör tolkning - försöker en luring
Förfalskning, förnedring, ger ingen tillit
Nej forskning är satsning som ger försäkring
Du når endast sanningen genom flit!

Forskning? (Ironi är snobberi, gör energi av komedi)
Satsning? (Symfoni gör harmoni av en melodi)
Sanning? (Terapi är trolleri och garanti till utopi)
Empiri är poesi - och finfinfin magi!

En fuling gör tolkning - försöker en luring
Förfalskning, förnedring, ger ingen tillit
Nej forskning är satsning som ger en försäkring
Du når endast sanningen genom flit!

Forskning! (Jag tror jag fattar allt nu!)
Satsning! (Kan du bara repetera det du sa i början?)
Sanning! (Eller ge en kort sammanfattning)

Skapar utveckling - och det ger profit!

5. Butlerns svanesång
Ska jag nu dö, tid för adjö?
Får ej drabbas av panik

Jag drack ett glas och allt blev knas
Kan det varit arsenik?

Giftet når min kropp, till mitt blodomlopp
Hjärtat i full galopp

Min kropp känns kall som permafrost
Snart blir jag jord i din kompost
Kan göda ekologisk kost...
Hör nu på min svanesång
En sån svanemärkt sång

Jag ruttnar och blir jordavfall…
Så bränn min kropp om du är kall
Då gör jag gott iallafall…

Ja, den enes död, blir den andres bröd
Hör mig rimma - i nöd

Nu får jag aldrig gå på bal
I AFs nya Stora Sal
Jag håller nu mitt avskedstal
Synd att det har en sån trist sensmoral

Har alltid varit för lojal
Och saknar kollektivavtal
Tynar bort i denna aktfinal
Giftet sprider sig i… hela min kropp…
och jag… får andningsstopp…
Vem släckte ljuset? Gick det en propp?

6. Dödskul kuplett
Min nyfunna vän dags att ge sig av
Från livets strapatser till livad grav
Få samhällsstöd för plötslig död
Nu slipper du alla inkassokrav
Det komma en dam i en svart lång rock
Men det är bara jag, så få ingen chock
Här får du nu en biljett i hand
Sen blir det partaj i dom dödas land

Måste döden helt genomgå vara grå
När du istället kan prima må
En efterfest med sköna lik
Där döingar jammar till jazzmusik

Samba eller tango, OH, jättefest
Salsa utav mango, OH, efterfest
Efter din död vänta lattjo pris
Som givetvis är ett paradis
Samba eller tango, OH, jättefest (Sambaaaa eller tango)
Salsa utav mango, OH, efterfest (Salsaaaa utav mango)
Efter min död vänta lattjo pris
Som givetvis är ett paradis

Så ta å beställ dig en cocktailmix
Och glöm inte att ge en massa dricks
För Dödens bar är underbar
Vi servera drinkar med fix och trix
En Pina Colada att döda för
En Cocktail Nevada så god du dör
Men bäst av allt är vår VIP
Där kan man få öl som är glutenfri

Måste Döden helt genomgå vara grå
När du istället kan prima må
En efterfest med sköna lik
Där döingar jammar till jazzmusik

Samba eller tango, OH, jättefest (Sambaaaa eller tango)
Salsa utav mango, OH, alkotest (Salsaaaa - utav mango)

En destination med ett glatt humör
Vår död är ju det som vi lever för

Så snart ska jag få ett lattjo pris?
Ja, du är död och få lattjo pris
Som givetvis (blir ett paradis)

Exempelvis (bättre än Paris)
Och vanligtvis (ingen syfilis)
Ja lyckligtvis (finns ett paradis)
De dödas land är ett paradis

7. Spökplett
Det är rysligt kul, att gå igen
Spöket Paul, OH!
Ni får aldrig ro!

Jag spökar, dom krökar
Och smörjer sina krås
Nu ska dom få, jag ska dom klå
Min plan den går i lås

Jag gastar och dom hastar,
Dom försöker vinna tid
Men spelet är snart över
Min hämnd - den blir morbid

Buu-uu!
(Ooo-ooo!)
Buu-uu!
(Åh hjälp!)
Haha!
(Ooo-ooo!)
Jag är spöket Mono Paul!

Ja tärningen är kastad
Och spelet är igång
Ska spela mina kort så väl
I denna spelomgång
Jag spelar fult, okej då
Men inget får gå fel
Jag skiter väl i kärleken
om jag får tur i spel

Buu-uu!
(Ooo-ooo!)
Buu-uu!
(Åh hjälp!)
Haha!
(Ooo-ooo!)
Jag är spöket Mono Paul!

Snart är spelet över
Och ni får stå ert kast
Jag går igen och ger igen
Fast jag är en gast

Ni tror ni dansar på min grav,
(Men) min rock är fylld av ess
Finess, javisst, det är ett krav
Vill ej dö av tristess

Och kanske du tycker (att)
Mitt spratt känns överdrivet
Då vill jag bara säga att
Ett skratt förlänger livet

Mohahahahahaaaa!

8. Humörsvängig tablettkuplett
Jag blir riktigt jädra ilsken, ja nu ser jag bara rött
Känns som alla här vill göra mig förnär
Hon den hyndan ville mörda mig, jag kunde ju ha dött
Va-ar fasen har jag gjort av mitt gevär?!

Blir så satans arg,
När ni andra ställer till en massa tjafs och larv och stök
Satans arg (Han är arg)
Ja så arg att arga snickarn framstår som en muntergök

Så förbaskat arg
Ja, som troll på internet som skriver hett på instagram
Riktigt arg (som en varg)
(Och) som en varg så blev jag plötsligt väldigt sugen på att lämlästa små lamm

Nej men hejsan Senap, säg mig varför löper du amok?
Har du slutat med ditt utskrivna recept? (“Allt är slut!”)
Jaså det förklarar varför du beter dig som en tok
Abstinensen i ditt sinne gör dig knäpp!

Sluta va’ så arg!
Kära doktorn får jag be dig att du SNÄLLA HÅLLER TRUT?
Oj så arg!? (Superarg!)
Ja jag går ju snart i taket, för tabletterna är slut

Och då blir jag sur!
En man med kort stubin är inte alls nåt attraktivt…
Åh så sur (pH 2)
Så här, ta ett extra litet piller med ett litet extra...här ta två. (tack!)

Min ordinering kanske inte alltid är helt enligt FASS
Nä, jag styrs av självbeprövad empiri.
Alla piller väljs baserat på dess narkotikaklass.
Nöjda kunder - ja det är min garanti!

När jag tar en pilleluring blir jag genast jätteglad.
Till och med när jag ska prata politik!
Och helt plötsligt kan jag tolerera Alexander Bard.
Ja mitt sinne blir sig inte längre likt!

Är så himlans glad!
Det finns  mycket i min/din rock här som kan göra livet gött
I extaaas (Oh kalas!)
Du är nog den mesta bästa männskan som jag nånsin mött

Ta en ritalin!
Vilken fest, ja vi är bäst och vreden den kan hälsa hem
Är i frid! (Opioid!)
Är du kanske lite extra arg så ta en extra extra… nej TA FEM!

Ta en ritalin!
Vilken fest, ja vi är bäst - vreden den kan hälsa hem
Är i frid! (Opioid!)
Är du kanske extra lite lite arg så ta en extra extra...nä TA FEM!

9. Mamma åt upp min pappa-kuplett
Mamma åt upp min pappa...
Är detta något skämt som jag ej fatta?
(Att) äta upp sin livskamrat
Är ju ganska ofattbart
Vet ej om jag ska gråta eller skratta…

(Ja,) mamma åt upp din pappa
Männ’skokött på kroken fick mig nappa
Det finns massa protein, och är gott till rosmarin
Rätt svårsmält...så jag avsluta’ med Grappa!

Han var god, full av blod
Läckra vader
Du är knäpp, har inget grepp
Du åt min fader

Sån skandal
(En) kannibal!
Lilla mamma

Grillad man,
Som han brann,
Min mannaflamma
Mamma, åt upp din pappa
Du vet ju att resurserna är knappa
Ät upp det som finns på fat
Så väl spenat som livskamrat
Jag stekte hela ryggfilén med kappa.

Mamma åt upp min pappa
Man blir rätt sugen på att bara sjappa
Fast hon är ju ändå snäll, kanske något speciell
Vår relation går nog trots allt att lappa!
Mamma åt upp din/min pappa!

10. Døgøttig trødeløtt
Jag sjöng min svanesång… för jag var döö’
Mitt lidande var långt…
jag borde va’ dööö’
Men ännu har jag ej sagt adjöööö

Jag är inte död
Trots jag är död
Om jag nu är dööööd?
Dödidö, dö, dö, dö, död

Vilket grymt kalas - med massa död
Folk har gått i kras - i överflöd.
Av blod blir scenparketten snart helt rööööd!
Alla ska dö,
ja, alla ska dö,
ja, alla ska dööööö.

Non é una favola, sono mortooooooo
Una pizza diavola, sono mortoooooo.
E ora il diavolo mi porta via
Perche sono morto,
perche sono morto
perche sono mortooo

O jag är bara här, för han är död.
En anledning så prekär -  att hon är död.
Jag lämnade helvetet i nööööd.

Yeah hey!
För han är död
Och hon är död
Och han är döööööd
För han är död
Och hon är död
Och han är döööööd
För han är död
Och hon är död
Alla ska dööööö

11.  Slutkuplett
Tänk vilken kväll det varit
Paul åkte på en smäll
Döden har fått mer jobb än vanligt
Vilken kväll, ja, vilken kväll

Vi skulle hitta vem som mördat
(Med) vilket vapen, i rätt rum
Men alla tycks förlorat
För Paul var ej död, bara’ dum

Vi har fått svar på våran gåta
O’ kan andas ut
En del har dött, men varför gråta?
För nu är spexet slut

(Lever) butlern efter denna sång?
Om det kan vi slå vad!
Du lev(er) bara en gång
Så Var Glad!

 Vår Pastor är en syndare
(Och) Scharlakan är tjuv minsann
(Men) professorn han är dummare
Och Påfågel åt upp sin man

Vår Senap var en arg filur
Men Doktorn hade bot
Hennes piller var en fin kur
(Nu) är det slut på mord och hot

Vi har fått svar på våran gåta
O’ kan andas ut
En del har dött, men varför gråta?
För nu är spexet slut

(Lever) butlern efter denna sång?
Om det kan vi slå vad!
Du lev(er) bara en gång
Så Var Glad!

Du lever bara en gång
Du lever bara en gång
Du lever bara en gång
Så Var Glad!
'''
