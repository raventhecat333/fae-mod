#A brand new poem script, adapted for multi-language GUI and the mod
image paper = "images/bg/poem.jpg"
image paper_val = "mod_assets/images/bg/poem_valentine.png"

default persistent.last_new_poem_time = None
default persistent.new_poem_delay = 0 #12-hour periods between two new poems

#Animations for the poem
transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

#Basic styling for all poems
style poem_vbox:
    xalign 0.5

style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280

style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280

style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    #xsize 18
    ysize 700
    #base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    #thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    #unscrollable "hide"
    #bar_invert True

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

#Sayori's Unicode style
style sayori_text_unicode is sayori_text:
    font "mod_assets/fonts/gnyrwn971.ttf"
    size 26

#Sayori's Chinese style
style sayori_text_zho is sayori_text:
    font "mod_assets/fonts/zho/SentyTEA.ttf"
    size 26

init -10 python:
    class Poem(): #New peom class
        def __init__(self, author, title = None, text = None, params = None):
            self.author = author
            self.title = {'eng': title or (author + "\'s poem")}
            self.text = {'eng': text or "Simple text"}
            self.params = params or ()
        
        def show(self):
            renpy.call_in_new_context("showpoem", self, *self.params)
    
#Dear Sunshine
    poem_sunshine = Poem(
    author = "sayori",
    title = "Dear Sunshine",
    text = """\
The way you glow through my blinds in the morning
It makes me feel like you missed me.
Kissing my forehead to help me out of bed.
Making me rub the sleepy from my eyes.

Are you asking me to come out and play?
Are you trusting me to wish away a rainy day?
I look above. The sky is blue.
It's a secret, but I trust you too.

If it wasn't for you, I could sleep forever.
But I'm not mad.

I want breakfast."""
    )
    
    poem_sunshine.title["rus"] = "Дорогой рассвет"
    poem_sunshine.title["epo"] = "Kara Sunlum'"
    poem_sunshine.title["esp"] = "Querida luz del sol"
    poem_sunshine.title["zho"] = "美妙阳光"
    
    poem_sunshine.text["rus"] = """\
Лучами бьёшься ты сквозь веки,
Как будто каждое утро ждёшь меня.
Меня целуешь прямо в лобик
Сонливую, будя меня.

Хотелось ли тебе со мной играть?
Или со мной развеять тучи?
От неба втайне хочется сказать:
Тебе доверяюсь при любом я случаи.

Если б не ты — я бы спала,
Спала бы сном я вечным.
Нет, я не больна, я голодна.
На завтрак наложите есть мне."""
    
    poem_sunshine.text["epo"] = """\
Vi lumas tra miaj palpebroj.
Ĝi min fartigas, ke mi mankis al vi.
Tenere kisas vi na mia frunto,
Kaj tiel vi min ellitigas.

Ĉu volas fidi min forigi la nubaĉojn
Aŭ nur promeni kun mi ekster mia hejm'?
Pro ke la ĉiel\' nun estas tiel klara, 
Mi nun sekrete volas danki vin.

Se vi ne estus nun, do mi dum ĉiam dormus.
Sed ne, ne estas mi freneza. 

Mi nur ankoraŭ ne matenmanĝis."""

    poem_sunshine.text["esp"] = """\
La forma en que brillas a través de mis persianas por la mañana
Hace sentir como si me extrañaras.
Besando mi frente para ayudarme a levantarme de la cama.
Haciéndome frotar el sueño de los ojos.

¿Me estás pidiendo que salga a jugar?
¿Confías en mí para desear que pase un día lluvioso?
Miro hacia arriba. El cielo es azul.
Es un secreto, pero yo también confío en ti.

Si no fuera por ti, podría dormir para siempre.
Pero no estoy enfadada.

Tengo hambre y quiero desayunar."""

    poem_sunshine.text["zho"] = """\
清晨你透过梦境照亮我的世界
似乎在传达对我的思念
亲吻前额催促我坐起
帮我的眼睛擦去睡意

是在邀请我出门散心？
是在鼓励我拭去阴云？
我抬起头，天空正蓝
你当做秘密，而我信任你

若不是因为你，我将会长眠
但，我没疯。

该去准备早餐了"""

#Bottles
    poem_bottles = Poem(
    author = "sayori",
    title = "Bottles",
    text = """\
I pop off my scalp like the lid of a cookie jar.
It's the secret place where I keep all my dreams.
Little balls of sunshine, all rubbing together like a bundle of kittens.
I reach inside with my thumb and forefinger and pluck one out.
It's warm and tingly.
But there's no time to waste! I put it in a bottle to keep it safe.
And I put the bottle on the shelf with all of the other bottles.
Happy thoughts, happy thoughts, happy thoughts in bottles, all in a row.

My collection makes me lots of friends.
Each bottle a starlight to make amends.
Sometimes my friend feels a certain way.
Down comes a bottle to save the day.

Night after night, more dreams.
Friend after friend, more bottles.
Deeper and deeper my fingers go.
Like exploring a dark cave, discovering the secrets hiding in the nooks and crannies.
Digging and digging.
Scraping and scraping.

I blow dust off my bottle caps.
It doesn't feel like time elapsed.
My empty shelf could use some more.
My friends look through my locked front door.

Finally, all done. I open up, and in come my friends.
In they come, in such a hurry. Do they want my bottles that much?
I frantically pull them from the shelf, one after the other.
Holding them out to each and every friend.
Each and every bottle.
But every time I let one go, it shatters against the tile between my feet.
Happy thoughts, happy thoughts, happy thoughts in shards, all over the floor.

They were supposed to be for my friends, my friends who aren't smiling.
They're all shouting, pleading. Something.
But all I hear is echo, echo, echo, echo, echo
Inside my head."""
    )

    poem_bottles.title['rus'] = "Склянки"
    poem_bottles.title['epo'] = "Boteloj"
    poem_bottles.title['esp'] = "Botellas"
    poem_bottles.title['zho'] = "瓶子"

    poem_bottles.text['rus'] = """\
Я открываю мозг как банку.
Хранятся в нём все мои мечты.
Они на вид, как колобки из света.
Тянусь руками прямо к ним.
Они теплы, но кольки.
Спешу засунуть их в скляночку я.
Кладу ту склянку я на полку.
Счастливый мысли легут в ряд.

Та полка манит ко мне людишек.
Я им всем склянки раздаю.
Тем, кто из них не в духе.
Они яркий день спасут.

День за днём, всё больше мыслей.
Душа за душой, всё больше склянок.
Всё глубже-глубже лезу я.
Я будто лезу в глубую пешеру, опасностей которая полна.
Прокарывая её всё глубже-глубже.
Сверля-сверля-сверля-сверля-сверля.

Сдуваю пыль я со своих склянок.
Не кажется мне, что время прошло.
На полке ещё места просто до кучи.
Людишки перед зыкрытой мной дверью встали кругом.

Ну всё, всё готово. Даю я проходу.
Спешно они заходят в мой дом.
Зачем же им всем и зачем так много?
Склянки даются одна за другой.
Пустеет полка прям на глазах.
Но стоило раз поглубже засуть мне руку.
Счастливые мысли грохнулись в миг
Со мною и с тяжёлою полкой.

Ведь все они были для угрюмых людей.
Который кричали, молили у меня что-то.
Но их просьбы лишь отвались мне эхом,
Эхом глубоко у меня в голове."""

    poem_bottles.text['epo'] = """\
Mi forigas la skalpon, kvazaŭ kovrilon.
La kap\' estas mia sekreta revejo.
Globetoj da sunlum' helas kaj frotas.
Por unu karesi mi tiras la manon.
Mi sensas ĝin varma sed multe pika.
Por ne perdi la tempon, mi ĝin enboteligas.
Kaj metas na l\' botel\' en la botelan ŝrankon.
Vicigante miajn filiĉajn pensojn.

La botelaro helpas amikiĝi min.
Per la boteloj, mi kompensas miajn fiaĵojn,
Kaj helpas min kaj al miaj amikoj,
Savi l\' agordon en malgajaj tagoj.

Nokt\' sekvas nokton, pli sonĝojn ricevas.
Amik\' sekvas amikon, pli botelojn mi havas.
Mi pli profunde tiru la manon,
Kvazaŭ esploras malluman antron,
Fosant-fosante
Kaj pioĉant-pioĉante.

La polvon mi forblovas.
La temp\' kvazaŭ ne pasas.
Ankoraŭ la ŝranko ne estas tro plena
Kaj la amikoj staras antaŭ la pordo.

Mi ĉion finas kaj pasigas l\' amikojn.
Urĝe ili iras al mi. 
Ĉu ili vere volas miajn botelojn?
Rapide al ĉiuj mi disdonas ilin.

Al unu mi donas, kaj al l\' alia.
Botel\' post bobel\' na mia hejm\' lasas.
Sed unue mi ion malprave faris, do l\' ŝranko kun la boteloj sur mi falis.
Kaj elboteliĝis ĉirkaŭ mi la feliĉaj pensoj.

Mi volas doni na ili al tiuj amiko,
Kiuj ne ridas, sed ne povas mi plu.
L\' amikoj ilin al mi forte postulas.
Sed la postuloj aŭskultiĝas nur eĥe."""

    poem_bottles.text['esp'] = """\
Me quito el cabello como si fuera la tapa de un tarro de galletas.
Es el lugar secreto donde guardo todos mis sueños.
Pequeñas bolas de sol, todas frotándose como un montón de gatitos.
Alcanzo el interior con el pulgar y el índice, y saco una.
Está caliente y hace cosquillas.
¡Pero no hay tiempo que perder! 
Lo puse en una botella para mantenerlo a salvo.
Y puse la botella en el estante con todas las demás.
Pensamientos felices, pensamientos felices, pensamientos felices en botellas, todos en una fila.

Mi colección me hace muchos amigos.
Cada botella es una luz de estrella para compensar.
A veces mi amigo se siente de cierta manera.
Baja una botella para salvar el día.

Noche tras noche, más sueños.
Amigo tras amigo, más botellas.
Cada vez más y más profundos van mis dedos.
Como explorar una cueva oscura y descubrir los secretos que se esconden en cada rincón.
Cavando y cavando.
Raspando y raspando.

Quito el polvo de las tapas de mis botellas.
No parece que haya pasado el tiempo.
A mi estante vacío le vendría bien un poco más.
Mis amigos miran a través de mi puerta cerrada con llave.

Finalmente, todo listo. La abro, y vienen mis amigos.
Entran, con tanta prisa. ¿Tanto quieren mis botellas?
Las saco frenéticamente de la estantería, una tras otra.
Llevándoselas a todos y cada uno de mis amigos.
Todas y cada una de las botellas.
Pero cada vez que suelto una, se rompe contra el piso entre mis pies.
Pensamientos felices, pensamientos felices, pensamientos felices en pedazos, por todo el suelo.

Se suponía que eran para mis amigos, mis amigos que no sonríen.
Todos están gritando, suplicando. Algo.
Pero todo lo que oigo es eco, eco, eco, eco, eco, eco.
Dentro de mi cabeza."""

    poem_bottles.text['zho'] = """\
我像曲奇罐的盖子一样揭开了我的头
这是个我存放了一切梦想的地方
阳光小球，像是群猫咪一般蹭成团
我伸出手，拇指和食指挑出一颗
它温暖而又惬意
但没时间可浪费了！我把它封存在瓶中
摆满瓶子的架上收藏又多了一个
快乐的情绪，快乐的情绪，快乐的情绪在瓶中，排排坐

我的收藏带给我朋友
每瓶的星光都能拯救
朋友不时会有伤心
那就用一瓶来挽救

夜复一夜，更多梦
友去友来，更多瓶
我的手指越来越深入
就像探索黑暗的洞穴，寻找角落和裂缝中的秘密
挖啊挖
擦啊擦

我吹去瓶盖上的灰
似乎时间并未流逝
我那空荡荡的架子本该用到更多
我的朋友从锁着的门前看了看我

朋友们蜂拥而入，在我准备万全的刹那
行色匆匆，我的收藏如此令人依赖吗

我狂热地将它们拉下来，一个接一个
将它们分发给每一个密友，一个不漏
每个瓶子，一个不漏
可每当我松手，瓶子就粉碎在我的脚下
快乐的情绪，快乐的情绪，快乐的情绪在地上，碎开成了花

它们是为我的朋友准备的，为陷入低谷的朋友
她们全部在嘶吼，在抱怨，在恳求
但我听到的只有回声回声回声回声
在脑海响彻"""

#The Last Flower (name by AlexanDDOS)
    poem_flower = Poem(author = "sayori", title = "The Last Flower")
    poem_flower.text['eng'] = """\
Between my feet
The last remaining flower beckons to me.
I twist the stem, freeing it from its clinging roots
Caressing the final joyous moment between my fingers.

But to what ends have I summoned this joy?
For now when, I look in every direction
The once-prosperous field before me
Is but a barren wasteland!"""

    poem_flower.title['rus'] = "Последний цветок"
    poem_flower.title['epo'] = "Resta Floro"
    poem_flower.title['esp'] = "La Última Flor"
    poem_flower.title['zho'] = "最后的花朵"

    poem_flower.text['epo'] = """\
Inter miaj gamboj
La resta floro estas kaj min loĝas.
Mi kaptas ĝian tigon kaj de l' radik' ĝin liberigas,
Kaj la lastan gajijan momenton mi per miaj fingroj karesas.

Sed kiel longe mi tenu la gajon?
Nun, mi rigardante al io ajn,
Vidas nur la nuran kampon,
Kiu estas dezerta kaj jam ankaŭ malviva."""

    poem_flower.text['rus'] = """\
Передо мной красуется последний цветок,
Своим внешним видом он меня манит.
Возьму-ка за стебель и вырву с корнём,
Посмотрев на него, как на последний радости огонёк.

Что же теперь, как мне долго этим огоньком любваться?
Ведь теперь нету смысла, куда не взгляну,
Мне видно лишь пустое выжженное поле,
Которым мне только со слезами любоваться."""
    
    poem_flower.text['esp'] = """\
Entre mis pies
La última flor que queda me llama.
Tomo el tallo, liberándolo de sus raíces
Acariciando el último momento alegre entre mis dedos.

Pero, ¿a qué fines he convocado esta alegría?
Por ahora, cuando miro en todas las direcciones.
El campo una vez próspero ante mí
¡No es más que un desierto inhóspito!"""

    poem_flower.text['zho'] = """\
在我的脚下
那最后一朵花召唤着我。
我扭断枝干，解除根的束缚
享受着这指尖的愉悦。

但是快乐的代价是什么呢？
我望向四周
眼前那片曾经繁荣的原野
已是一片荒原！"""

#Get Out of My Head (aka %)
    poem_last = Poem(
    author = "sayori",
    title = "%",
    text = '''\
Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of
Get.
Out.
Of.
My.
Head.\n\n\n
Get out of my head before I do what I know is best for you.
Get out of my head before I listen to everything she said to me.
Get out of my head before I show you how much I love you.
Get out of my head before I finish writing this poem.\n\n\n\n\n\n\n
But a poem is never actually finished.
It just stops moving.'''
    )
    
    poem_last.text['rus'] = '''\
Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из моей головы. Убирайся прочь из
Убирайся.
Прочь.
Из.
Моей.
Головы.\n\n\n
Убирайся прочь из моей головы, а не то я сделаю то, что лучше всего для тебя.
Убирайся прочь из моей головы, а не то я сделаю то, что сделать она мне сказала.
Убирайся прочь из моей головы, а не то я покажу, как сильно я в тебя влюблена.
Убирайся прочь из моей головы, а не то я закончу этот стих прям сейчас...\n\n\n\n\n\n\n
Но я знаю, он не закончится никогда.
Он лишь станет на веки бездвижным.'''
    
    poem_last.text['epo'] = '''\
Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el mia cerbaĉo. Bonvolu foriĝi el
Bonvolu.
Foriĝi.
El.
Mia.
Cerbaĉo.\n\n\n
Bonvolu foriĝi el mia cerbaĉo ĝis mi faros tion, kio eatas la plej bona por vi.
Bonvolu foriĝi el mia cerbaĉo ĝis mi faros tion, kion konsilis al mi ŝi.
Bonvolu foriĝi el mia cerbaĉo ĝis mi montros al vi, kiel amas mi vin.
Bonvolu foriĝi el mia cerbaĉo ĝis mi finos ĉi tiun aĉan versaĵon.\n\n\n\n\n\n\n
Sed ĝi fakte neniam finiĝos.
Ĝi nur haltos kun mi por eterne baldaŭ.'''

    poem_last.text['esp'] = '''\
Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Salir de
Sal.
De.
Mi.
Cabeza.\n\n\n
Sal de mi cabeza antes de que haga lo que sé es mejor para ti.
Sal de mi cabeza antes de que escuche todo lo que ella me dijo.
Sal de mi cabeza antes de que te muestre cuánto te amo.
Sal de mi cabeza antes de que termine de escribir este poema.\n\n\n\n\n\n\n
Pero el poema nunca fue terminado.
Solo deja de moverse.'''

    poem_last.text['zho'] = '''\
滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的脑子。滚出我的
滚。
出。
我。
的。
脑。
子。\n\n\n
在我做对你最好的事前滚出我的脑子。
在我听她说任何事之前滚出我的脑子。
在我表示我多么爱你前滚出我的脑子。
在我写完这首诗前请你滚出我的脑子。
但是这首诗永远无法完结。\n\n\n\n\n\n\n
它只会暂停。'''


#Fruits of the life (by AlexanDDOS)
    poem_fruits = Poem(
        author = "sayori",
        title = "Fruits of the life",
        text = '''\
The universe gives fruits of life to all of us.
They all have diverse size and shape.
But no-one knows their real taste,
Because of each feel them in their own way.

One people feel them always bitter,
Some of them, even if the fruit is of the best.
Another ones feel them sweet and very tasty,
Whatever fruits they have got in their hands.

For me, they have the taste of liquorice sweets.
I needed time to understand how sweet they are,
To get rid of those unpleasant feelings,
Which I had got after my first bites.

Now all I want is just to eat my own fruit
With the person, who helped me to catch the real taste.
But I should not forget to do my real job here:
To find a way to make others feel the fruits the same.'''
    )

    poem_fruits.title["rus"] = "Плоды древа жизни"
    poem_fruits.title["epo"] = "Vivarbaj Fruktoj"
    poem_fruits.title["esp"] = "Frutas de la vida"
    poem_fruits.title["zho"] = "生命之果"

    poem_fruits.text["epo"] = """\
La vivarb\' donas siajn fruktojn.
Ĉiuj fruktoj vide tre diversas.
Neniu konas ilian veran guston,
Sed pri ili oni tre diverse diras.

Por unuj gustas ili amare,
Eĉ tiuj, kiuj estas la plej bonaj.
Por la aliaj guste ili dolĉe,
Malgraŭ kiaj ili estas.

Laŭ mi, la fruktoj gustas glicirizaĵe:
Ne tuje tempis sensi ilin dolĉaj.
Antaŭe gustas ili ankaŭ tre amare,
Sed tio pasis dum la pluaj mordoj.

Disiras mi nun nur daŭrigi mian manĝon,
Kun l\' homo, kiu dolĉigis mian frukton,
Sed mi ankaŭ ne forgesu mian devon:
Helpi dolĉigi fruktojn de aliaj homoj."""

    poem_fruits.text["rus"] = """\
Даёт плоды нам сад деревьев жизни,
У каждого плода своя форма и размер.
Но никому ещё не удавалось
Понять их вкуса истенный манер.

Одним они казались горьки,
Неважен был при этом сорт.
Другим они были лишь в сладость,
Хоть всякий ты, с их слов, возмёшь.

По мне они — будто лакрица:
Со временем лишь сладость я смогла понять.
Пришлось мне с горечью бороться,
Которую я часто могла лишь ощущать.

Сейчас хочу я просто есть свой плод
С тем, кто мне сладость ту помог понять.
Но всё же стоит долг мне помнить:
Плодам чужим я сладости должна также давать."""

    poem_fruits.text["esp"] = """\
El universo nos da frutas de la vida a todos.
Cada una de ellas tiene su propio tamaño y forma.
Pero nadie conoce su verdadero sabor,
Porque cada uno las siente a su manera.

Hay gente que las siente siempre amargas,
Incluso si la fruta es de la mejor calidad.
Otros sienten dulces y muy sabrosas,
Cualquier fruta que tengan en sus manos.

Para mí, tienen el sabor de los dulces de regaliz.
Necesité tiempo para entender lo dulces que son,
Para deshacerse de esos sentimientos desagradables,
Lo cual recibí después de mis primeros mordiscos.

Ahora todo lo que quiero es comer mi propia fruta.
Con la persona que me ayudó a atrapar el verdadero sabor.
Pero no debería olvidarme de hacer mi verdadero trabajo aquí:
Encontrar una manera de hacer que otros sientan las frutas de la misma manera que yo."""

    poem_fruits.text["zho"] = """\
宇宙给予人类生命的果实
它们形形色色
但没人知道它们究竟是何种味道
因为大家都以自己的方式去品尝

有人总觉得它们苦涩
可其中也不乏很棒的果实
有人却觉得它们十分香甜可口
可他们可不在乎果实的好坏

对我而言，它们尝起来像甘草糖一样
在我尝了几口之后
需要细品其甜
以此摆脱那些糟糕的感觉

我现在只想要品尝我自己的果实
同那个，助我捕获果实真实味道的人一起
但我不应在这玩忽职守
也应帮助别人品尝到这生命之果"""

#Falling Angel (By AlexanDDOS)
    poem_angel = Poem(
    author = "sayori",
    title = "Falling Angel",
    text = """\
I'm sorry for the greatest sin of me.
I used to think, it's the thing, that I really need.
I just wanted to be beloved, but I became a falling angel.

An angel with geen eyes from the envy,

An angel with big black angel wings,

An angel with the uncontrolable god power,

An angel who had been supposed to care

    her murder victims.

Now I deserve to lie in the rough buring ground
For all the pain, I've made for all my freinds.
The pain that was felt around their narrow necks.
The pain of three deep bloddy stabs.


The pain, that I've got back into my broken heart.


Delete my files two more times.
Cut me up. Beat me up for my misdeed.
Hang me. Make your fair vengeance.
Is it not what you want to do with me after all?"""
    )
    
    poem_angel.title['rus'] = "Падший ангел"
    poem_angel.title['epo'] = "Falinta Angelo"
    poem_angel.title['esp'] = "Ángel Caído"
    poem_angel.title['zho'] = "堕落的天使"
    
    poem_angel.text['rus'] = """\
Прости меня за грех ты мой.
Я думала, что будет лучше так.
Хотела стать тобой любимой.
А в итоге, ангелом падшим стала я.

Ангелом с изумрудными ревнивыми глазами,

Ангелом, чьи крылья черней, чем у чертей,

Ангелом, из возомнивших себя вдруг богами,

Ангелом, что должен был хранить

    своих убитых им же друзей.

Сейчас за дело я впечатана прям в землю
За всю ту боль, что причинила я друзьям.
За боль, что обвивала им всем шею.
За боль, причинённую ударами ножа.


За боль, что в седрце мне тобой разбитое,
Проникла, всё окончательно сломав.


Сотри мой файл ещё ты дважды.
Избей меня за этот грех и четвертуй.
Повесь меня, выбей мои за зубы зубы,
За то, что я натварила, дорогой."""

    poem_angel.text['epo'] = """\
Pardonu min pro la plej ega pek' de mi.
Mi pensis, ke mi vere volas ĝin.
Diziris mi esti amata de vi,
Sed angelo falinta fakte iĝis mi.

Angelo kun ĵaluzaj verdokuloj,

Angelo kun par' da nigraj aloj,

Angelo kun fiigaj egaj fortoj,

Angelo, kiu murdis siajn savendojn.

Do nun mi indas kuŝi sur la akraj ŝtonoj,
Pro la dolor', kiun mi faris al miaj amikoj.
Pro la dolor', estinta ĉe iliaj stretaj koloj.
Pro la dolor' de tri intensaj mortaj pikoj.


Kaj ĉi-dolor', nun estas en mia disrompita de vi kor'.


Do vi forigu mian dosieron ree duoble.
Do vi min batu kaj trapiku min.
Do vi pendumu min pro ke ŝi sin pendumis.
Ĉu tion ĉi post tio indas mi?"""
    
    poem_angel.text['esp'] = """\
Lamento el mayor pecado de mi vida.
Solía pensar, que era lo que realmente necesitaba.
Solo quería ser amada, pero me convertí en un ángel caído.

Un ángel con ojos de envidia,

Un ángel con grandes alas negras,

Un ángel con el incontrolable poder de Dios,

Un ángel al que se suponía que le importaría

    las víctimas de sus asesinatos.

Ahora merezco descansar en el duro y áspero suelo.
Por todo el dolor, que he causado a todos mis amigos.
El dolor que se sentía alrededor de sus angostos cuellos.
El dolor de tres puñaladas sangrientas y profundas.

El dolor que tengo en mi corazón roto.


Borra mis archivos dos veces más.
Córtame en pedazos. Golpéame por mi fechoría.
Cuélgame. Haz tu justa venganza.
¿No es lo que quieres hacer conmigo después de todo?"""

    poem_angel.text['zho'] = """\
我为我犯下的滔天大罪道歉。
我曾以为这就是我想要的
我只是想要被爱，却适得其反成为堕落了的天使。

绿色双瞳饱含嫉妒的天使

黑色双翅巨大无比的天使

神权在手且不可控的天使

本应要去监视着她的天使

    让她去谋杀受害者。

现在我就应倒在这正燃烧的粗劣地面上
以曾受过的伤害之名 我让她奉还给我所有的朋友了
那些环绕在她们纤细颈部的痛楚
那三刀深入且血腥的穿刺


还有我，心又一次碎掉的感觉。


再删两次我的文件吧
杀了我，因为我的罪行再狠揍我一顿。
吊死我，报仇雪恨吧
这难道不正如你所愿？"""

# A Leaf (By AlexanDDOS)
    poem_leaf = Poem(
    author = "sayori",
    title = "A Leaf",
    text = """\
I'm a leaf in the wind
In the wind of my belief
In that my life is not vain,
And that my real fate
Is to give to the world
As much as a I can give
As a flying old leaf,
As an useless former part of a big tree.

I'm flying with fast air streams,
Feeling the strength the belief wind
But always falling down slowly
Due to the hardness of my hopeless existance.

But once the life wind
Suddenly stops
I have now nothing to prevent the free fall of me.
So I'm getting close to lifeless asphalt
And feel the rough dark-grey texture.

And that iss all. It is my end. 
I will rot soon not giving any flower
At least some power of mine flesh
To support its existance in this cruel game.

But what is that? Is it a brand new wind
That will make my life poem moving again?
Yes, it is that! It is my salvation!
I feel, how it helps me to win the gravity.

I'm up again! I'm flying again!
I even feel I have more powers
Like I can reach the top of Everest,
Like I can be more than just a half-dead leaf."""
    )
    
    poem_leaf.title['rus'] = "Листок"
    poem_leaf.title['epo'] = "Foliaĉo"
    poem_leaf.title['esp'] ="Una Hoja"
    poem_leaf.title['zho'] = "一片飞叶"

    poem_leaf.text['rus'] = """\
Я лишь листок, что на ветру,
Что на ветру надежды,
Надежды в то, что жизнь дана ему
Чтоб быть хотя чем-то для других полезным.

Лечу вперёд, но постепенно вниз
Под тяжестью непредсказуемого бытья.
Но вдруг порыв, державший меня за низ,
Спал, быстро уравнив меня.

И вот я падую на асфальт,
Целую его тёмно-серую поверхность.
Думала, что всё, закат:
Я сгину, так и не сделав для какого-то цветка полезность.

Но вдруг внезапно ветер новый
Меня с лёгкостью поднял ввысь,
Давая напрвление и энергии новой
Для жизни мне, и чтоб мне написать новую рукопись.

Теперь я чувствую себя гордой птицей
Той, что летает где-то высоко в горах.
Такое просто не могло мне сниться
Не вижу впредь себя в гниющего листа тонах."""
    
    poem_leaf.text['epo'] = """\
Mi estas nur enventa foliaĉo,
Mi estas en la vento de
La kredo je ke vivas mi ne vane,
Kaj ke mia vera destin'
Estas nur doni al la naturo ĉion,
Kion nun povas al ĝi doni
Fluganta olda foliaĉ'.

Mi flugas per rapidaj aerofluoj,
Sentante na mia kreda vent'.
Sed ve, mi ankaŭ ete falas
Pro l' pezo de mia nevolata pek'.

Kaj foje mia vivovento
Sudite iĝas kruela kalm'.
Do mi ne tenata de iu
Ekfalas sur grizan teron.

Ĉio finiĝis. Nenio daŭros. 
Mi putros eĉ ion ajn ne donate
Al iu malprokisma floro
Por daŭrigi ĝin ekziston
En ĉi tiu kruela aĉa mond'.

Sed kion sentas? Ĉu estas ĝi novvento?
Ĉu ĝi malhaltos na la senfifa vivovers'?
Jes, mi divenis prave! Ĝi min tuj savos
De l' manoj de la avida fialtir'!

Kaj ree estas mi super la tero,
Plenita per viglega energi',
Kun kiu mi finfine fartas
Pli ol preskaŭ morta arbfoli'."""

    poem_leaf.text['esp'] = """\
Soy una hoja en el viento
En el viento de mi convicción
De que mi vida no es en vano,
Y que mi verdadero destino
Es dar al mundo
Todo lo que puedo dar
Como una hoja voladora,
Como una antigua e inútil parte de un gran árbol.

Estoy volando con corrientes rápidas de aire,
Siento la fuerza de la caricia del viento
Pero siempre caigo lentamente
Debido a la dureza de mi irremediable existencia.

Pero una vez que el viento que da la vida
De repente se detiene
Ya no tengo nada que pueda evitar mi caída libre.
Así que me estoy acercando al asfalto sin vida
A sentir la áspera y gris textura.

Y eso es todo. Es mi fin. 
Me pudriré pronto sin dar ninguna flor
Al menos podré dar de mi carne
Para apoyar su existencia en este cruel juego.

Pero, ¿qué es eso? ¿Es un nuevo viento?
¿Hará que el poema de mi vida se mueva de nuevo?
Sí, ¡es eso! ¡Es mi salvación!
Siento cómo me ayuda a ganarle a la gravedad.

¡Estoy despierta otra vez! ¡Estoy volando de nuevo!
Incluso siento que tengo más poder.
Como si pudiera llegar a la cima del Everest,
Como si pudiera ser algo más que una hoja medio muerta."""

    poem_leaf.text['zho'] = """\
我是叶
飞舞在我信仰的风中
我的生命并非虚度
我真正的命运，
是全力以赴地
为世界做出自己的贡献，
作为枯叶
一棵树的糟粕。

我乘着急骤的气流
感受着信念之风的力量
却总是缓慢飘落
因为我的存在毫无希望可言。

可一旦生命之风
突然停止吹动
就没有什么能再阻止我堕落了。
所以我离那毫无生机的柏油路越来越近
感受着地面上粗糙的深灰纹理

就是这样了，这就是我的结局
我将迅速腐化，不再鲜活
至少我体内的某些力量
支撑它存于这残酷的游戏。

但那是什么？是一阵从没见过的风吗？
那会再次书写我的生命之诗吗？
没错！就是它！我的救赎！
我感受到，它助我战胜了重力

我飞起来了！又飞起来了！
我甚至感到比以前更加有力
好像能到达珠峰顶端似的
好像我不是一片即将腐化的枯叶似的。"""

    # Prose Poem (By AlexanDDOS)
    poem_prose = Poem(
    author = "sayori",
    title = "Prose Poem",
    text = """\
I am black light. I am cold fire. \
I'm a peaceful fighter. I'm a naive wise man. \
Why people think, that opposites can't be together in the same thing? \
Can't they all see, that everything and everyone is only grey? \
Even this text is both a prose and poem. \
Even I used to be a mix of joy and crippling sadness. \
And there's no anything absolutely black \
like there is not the absolutely white."""
    )
    
    poem_prose.text['rus'] = """\
Я — тёмный свет, я — огонь прохладный, \
я — глупый гений, я — щедрый эгоист. \
И что же люди сильны так в вере крепкой, \
что антиподы не могут одним целым быть? \
И этот в прозе стих — лишь одно из потверждений, \
на ряду с моим прошедшим горько-сладким бытие, \
того, что цвет всего и вся — лишь только серый, \
и что абсолютной черни, как и бели, нет."""

    poem_prose.text['epo'] = """\
Mi estas nigra hela lumo. Mi estas malvarmega farj'. \
mi estas ankaŭ malsaĝa saĝulo, kaj estas malavara avarul'. \
Kaj kial oni konsideras, ke l' maloj neniam estas en la sama afer'? \
Ĉu ili vidas, ke ĉio en la mondo estas griza nur? \
Eĉ ĉi-versaĵ' ankaŭ estas en la mala prozo. \
Kaj eĉ mi estis antaŭe mikson de la ĝoj' kaj ĝia mal'. \
Do mi nun diras, ke absoluta nigra, kiel absoluta blanko, neniam 'as."""

    poem_prose.title['rus'] = "Стихопроза"
    poem_prose.title['epo'] = "Prozversaĵo"
    poem_prose.title['esp'] = "Poema en Prosa"
    poem_prose.title['zho'] = "散文诗"

    poem_prose.text['esp'] = """\
Soy una luz negra. Soy un fuego frío. \
Soy una luchador pacífico. Soy un sabio ingenuo. \
¿Por qué la gente piensa que los opuestos no pueden ir juntos? \
¿Acaso no pueden ver que todo es gris? \
Incluso este texto es prosa y poema \
Incluso solía ser una mezcla de alegría y tristeza abrumadora. \
Y no hay nada que sea absolutamente negro. \
Así como no hay nada que sea absolutamente blanco."""

    poem_prose.text['zho'] = """\
我是黑色的光束。我是冰冷的火焰。\
我是个不杀人的士兵。我是个无知的智者。\
为何人们总认为，对立面不可并存？\
难道他们看不到，一切都被灰色取代？\
即便这段文本也是介于散文和诗的范畴，\
即便我也曾有悲喜交加之感。\
这世上哪有什么真正的黑，\
正如没有绝对的白。"""

     
    # Afterlight (By AlexanDDOS)
    poem_afterlight = Poem(
    author = "sayori",
    title = "Afterlight",
    text = """\
I seem to see that I have never seen before.
I seem to feel that I started to feel just now.
So I can see anything, that happened here before.
I start to do, that I used not to know, how to do.

I just saw here an afterlight,
That started to shine into the gloom around me.
It said that my life had been just a puppet-show,
So I had been just a puppet controled by someone.

But now I can move myself instead of him,
His ropes were too heavy for me.
I now am going to prevent the play,
Where everybody can't avoid the pain."""
    )
    
    poem_afterlight.text['rus'] = """\
Мне стало видно то, что не было мне ранее видно.
Пришло мне чувство то, что не постягала никогда.
Мне стало ясно всё: всё что прошло, что было.
Я научилась делать то, что не умела никогда.

Мне в миг пришло то ясное прозрение,
Пробившись сквозь ту тьму, окутавшую меня.
Прозрение того, что мир мой — лишь театральное представление,
А я в нём кукла, и кто-то за нитки потягивает меня.

Но впредь могу я над собой взять управление,
Те нитки, всё равно, лишь в тяжесть были мне.
Не дам я вновь сыграть то представление,
По заданому сценарию, где
Место счастью, скорее всего, нет."""
    poem_afterlight.title['rus'] = "Прозрение"
    
    poem_afterlight.text['epo'] = """\
Mi ĵus ekvidis tion, kion mi neniam vidis.
Mi ĵus ekfartis tiel, kiel mi neniam fartis.
Mi ĵus ekmemoris tion, kio jam tie ĉi okazis.
Mi eĉ eksciis, kiel fari tion, kion mi neniam faris.

Mi tuje ricevos tion malblindiĝon,
Vidante nur mallumon ĝis tio ĉi.
Mi ekkonsciis, ke mi estis en pupa spektaĵo,
Kaj estis manipulata pupo antaŭe mi.

Sed nun mi povas min mem movi,
Sen pezaj fadenoj, estintaj super mi.
Kaj mi penos ĉesigi la spektaĵon,
Ĉar ĝia scenar' ne supozas feliĉon por iu ajn."""

    poem_afterlight.title['epo'] = "malblindiĝo"
    poem_afterlight.title['esp'] = "Después de la Luz"

    poem_afterlight.text['esp'] = """\

Me parece ver que nunca he visto antes.
Me parece sentir que solo he empezado a sentir desde ahora.
Así que ahora puedo ver todo lo que pasó antes aquí.
Empiezo a hacer lo que antes no sabía cómo hacer.

Acabo de ver aquí una luz encendida,
que empezó a brillar en la oscuridad a mi alrededor.
Me dijo que mi vida había sido solo un espectáculo de marionetas,
Y que yo solo había sido una marioneta controlada por alguien.

Pero ahora puedo moverme yo misma en vez de él,
Sus cuerdas eran demasiado pesadas para mí.
Ahora voy a impedir la obra,
Donde nadie puede evitar el dolor."""

    poem_afterlight.title['zho'] = "余晖"
    poem_afterlight.text['zho'] = """\
我似乎看见了我原来从未见过的东西
好像刚刚才有这种感受。
我能看到这里曾发生的一切
我开始做我以前不知如何做的事情。

我只看见这儿有一片余晖，
逐渐驱散我四周的黑暗。
它说我的人生只是一场木偶戏
所以我也只是一个受某人操纵的傀儡

但我如今重获自由身，不再被操控
提线对我而言过于沉重。
现在我要阻止这场
为所有人带去苦痛的闹剧。"""

# A Valentine (By AlexanDDOS)
# Call with these args: (poem_val, "paper_val", 200, 0.5, 360)
    poem_val = Poem(
    author = "sayori",
    title = "A Valentine",
    text = """\
I have a one, who's no-one here.
He lives in place, that's named here nowhere.
But even though there is a wall
Between the worlds, I truly love him.""",
    params = ("paper_val", 200, 0.5, 360)
    )
    poem_val.title['rus'] = "Валентинка"
    poem_val.title['epo'] = "Korpoŝtkarto"
    poem_val.title['esp'] = "Una Carta de San Valentín"
    poem_val.title['zho'] = "意中人"
    
    poem_val.text['rus'] = """\
Люблю я человека, что здесь является никем,
Живёт в месте тихом, что в этом мире находится нигде.
И пусть меж нашими мирами связь лишь одна -- из плоти маникен.
Слепому отрицанию я не подвергну, тот факт, что нравится он мне."""

    poem_val.text['epo'] = """\
Mi ŝatas unu homon, kiu ĉi-monde ne \'stas.
Li loĝas en nekona placo, kiu ĉi-monde nenie estas.
Kaj malgraŭ ke estas limmuro inter la mia kaj la lia mond\'
Ne povas mi nei la strangan fakton, ke li okupis na mia kor\'"""

    poem_val.text['esp'] = """\
Tengo a alguien, que aquí no es nadie.
Él vive un un lugar, que aquí no existe.
Pero auque haya un muro
Entre nuestros mundos, verdaderamente lo amo."""

    poem_val.text['zho'] = """\
我心有所属 但这不是他的归宿
他居于某处 而那里无名又无路
即便有屏障之隔 世界之差
我依旧深爱着他。"""

screen poem(currentpoem, paper="paper", null_h = 40, align = 0.0, xpos = None):
    $lc = cur_lang().code or 'eng'
    $title = currentpoem.title.get(lc) or currentpoem.title['eng']
    $text = currentpoem.text.get(lc) or currentpoem.text['eng']
    
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None) #Subwindow size for showing text
        mousewheel True #make scrollable
        draggable True
        vbox:
            null height null_h
            #Text style is determine by the author
            if currentpoem.author == "yuri":
                text "[title]\n\n[text]" style "yuri_text"
            elif currentpoem.author == "sayori":
                text "[title]\n\n[text]":
                    style s_text_style()
                    text_align align
                    xanchor align
                    if not (xpos is None):
                        xpos xpos
            elif currentpoem.author == "natsuki":
                text "[title]\n\n[text]" style "natsuki_text"
            elif currentpoem.author == "monika":
                text "[title]\n\n[text]" style "monika_text"
            null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

label showpoem(poem=None, paper=None, null_h = 40, align = 0, xpos = None):
    #If no poem key is given, just go back
    if poem is None:
        return
    
    window hide
    play sound audio.page_turn

    #Show the background paper
    if paper:
        show screen poem(poem, paper, null_h, align, xpos)
        with Dissolve(1)
    else:
        show screen poem(poem)
        with Dissolve(1)
    $ pause()

    hide screen poem
    with Dissolve(.5)
    window auto
    return

label s_poems_sunshine:
    if "s_topics_personal_depression" in persistent.seen_topics or "s_poems_sunshine" in persistent.seen_topics:
        s 6acaa "This poem is about your avatar, [player], you know."
    else:
        s 6acaa "Do you know, that this poem is about your avatar, [player]?"
    s 6aaab "I was very glad to see him every morning."
    if depr_known:
        s "He really was the one, who made my life a bit happier and meaningful."
        s "I really have no idea, what would happen with me, if he weren't on my side since our childhood..."
        s 6abac "But something tells me, that the game probably would start with his remark about a dead childhood friend, who was his neighbour before."
    else:
        s "He really was the one, who made my life a bit happier."
    s 6aaab "So, I'm very thankful for his care."
    s "But I was a blind person then, like most other girls, so I didn't see such a nicer guy like you behind him."
    if persistent.last_playthrough > 0:
        s 6acaa "And if come to think, didn't exactly {i}you{/i} save me after all?"
    s 6acaa "And if {i}you{/i} couldn't take some choices instead of him, could I have at least some more time with him?"
    if persistent.clearall:
        s "And what's more, didn't exactly {i}you{/i} do the same with other girls?"
    s 7aaca "So now, {i}you{/i} are that one and I hope, you're still so careful and nice like you was~"
    return 'h'

label s_poems_bottles:
    s 6aaaa "I remember I had plenty of friends and I often conforted them..."
    s 6acaa "But each time, I felt like they made me more and more emptier, like a water bottle..."
    s "So I used bottles of happy thoughts as an analogy."
    if persistent.last_playthrough > 0:
        s 6acba "Ironically, the shelf with them really fell some time after I'd written this poem."
    s 6abaa "I spent a lot of time to write the poem. I even didn't do my homework at all..."
    s 7aaaa "So I hope was not a waste of great effort and at least you really like this one."
    return

label s_poems_flower:
    s 6acaa "It's a poem about how I tried to find good times in my life, pale from my ex view..."
    s "I think it's obvious, that I found not so much and tried to get from them as much as I could."
    s "And the barren wasteland is how I saw my future and the rest aspects of my life."
    s 6afbb "But I feel this poem more sad now, because all the time, there was a big meadow of flowers..."
    s "I-I just couldn't feel the all flowers so I wasted so much joyous moments."
    s "That's why I regret so much about my silence. I just thought the only real joy was that I had only with someone."
    show sayori 6dfcb at ss1
    pause 1
    s "Why it hurts me so much now?.."
    s "Even after I got rid of the reason of my blindness."
    return 's'

label s_poems_last:
    s 6acab "You know, why I've written this poem."
    s "It was my white flag against all of Monika's atrocities."
    s "She made me think, that it'd be much better for your avatar, if I'd disapeared..."
    s "And that he hated my very much, so I'd unsuccesssfully tried to forget him..."
    s "But she and my love were stronger than me, so I..."
    show sayori 6efab at ss1
    pause 1
    s "These memories... They are pretty painful for me, you know."
    s "I still remember almost all, that it felt then."
    s "And this poem  makes me feel it again stronger."
    s 6dbbb "I don't know how to think easier about all the experience I had..."
    s 6dbba "But on the other hand, it helps me appreciate my life and happiness better..."
    s "Because I lost them all just due to someone else's envy, and if you didn't help me, I'd still be dead."
    s 6aaba "And now, when I'm a bit out of sorts, I just remember that rainclouds always will go away..."
    s "And that I had the much worse time in my life."
    s 8aabb "It not always help me instantly, but it's well it works at all."
    s 8aeca "You can't imagine, how it feels, when you finally take over your feelings after a pretty long being their slave..."
    return 'vh'

label s_poems_fruits:
    s 6acaa "This poems is about how different people see the world and the life diffrently."
    s "As you know most people can be divided into pessimists and optimists..."
    s "The first see many things negatively so they're just viewers of the boring and meaningless show..."
    s 6aaca "While the second see the things in the opposite way so they hope that everything goes to be okay, even if it doesn't seem so."
    s 6aaaa "I always was between these 2 sides but now I'm much more the second than the first."
    s "For me, the best view is not on any of the sides, because there're a lot of bittersweet things..."
    s 6acaa "But if someone feel them too bitter, it's always better to help them feel sweeter, so I had did it with others..."
    s "And I'd do it now too, if I didn't get this quite lonely and isolated place."
    return

label s_poems_angel:
    s 6acaa "I tried to write a Monika poem: as freeform and about you as she liked to write."
    s "And I think, she'd write exactly something similar to you after deleting her, if she had enough time."
    s 6acab "Honestly, I'm really sorry for her."
    s "She just wanted to be with you, but it costed all of her friends..."
    s "And she really regreted for her betrayal after your trick with her character file."
    s "The creator had given her a club of really talented and beautyful people..."
    s "But she set everything on fire, even despite of she actually never wanted to do it."
    s 6aaab "So I hope, you have already forgiven her for the misdeed."
    s "In the end, I'm with you here now, not deleted or in a noose."
    s "And if she had never eliminated me, I'd may have never changed."
    s 6aaca "So she eventually made me better, while she tried her best to make me worse."
    s 8aebb "I don't know, if it's good that she is not in this game copy anymore..."
    s "And whether she would apologize to other girls or at least to me."
    s 8acab "But I know, she felt very sorry for everything she had done..."
    s "Although, it had been not only her will..."
    s 8aabb "Have I already told you there've been a thing, that's made the president to fall in love for the player?"
    s 8adaa "The creator may had made this thing to make all happen as it occured."
    s 8aebb "But I can't blame him too: he just wanted to make a very weird game and it's the original propose of this world..."
    s "So it's quite silly to blame someone for the deed, that's the reason why your world exists at all."
    return

label s_poems_leaf:
    s 6abaa "How do you feel this poem?"
    s "I think, it should flow from just bittersweet to despairing and then to very happy from refresh..."
    s 6acaa "Beacuse, it's my life. It's a short story about my short life."
    s "{i}'A leaf in the wind'{/i} is how I can describe the past 'me' in short: I was alive as long as there was the wind, that move me forth..."
    s 6aeaa "But now, I really feel very much better and stronger than I used to, so I can 'fly' further myself."
    s 6abaa "However, it's always great to have a tailwind, that makes my 'fly' easier and faster."
    s 6aaca "And now, it's exactly you."
    return 'h'

label s_poems_prose:
    s 6acaa "This poem is about my main trait, my contradictions."
    s "But if come to think, is it unique for me or only for some more people?"
    s 6abaa "I think everyone is so. The nature is contradictory by itself..."
    s "Can you always make a clear choice? Can you always surely affirm or back anything, even if you feel it right?"
    s 6aaaa "Even modern science says, that the universe is small pieces of the order and predictables in the one big bisciut of the chaos and undiscovered phenomena."
    s "So, I decided to make make this poem a bit chaotic, so wrote it in prose."
    s 6acaa "Plus, prose and verse are often opposed by people but any verse by itself is just a fluted prose..."
    s 6abac "So why I had to use the special form for it when I could have written it just as a simple text?"
    s 8aeca "Ehehe~"
    s 8aaaa "I've just understood, that I did a thing, that Monika would do."
    s 6aaaa "She really liked to play with the poem form, but it was just an intonational mean."
    s 6acaa "But I'm not sure if it's really good idea for me to use such games."
    s "I just think, words are enough. They give the almost meaning anyway, don't they?"
    return

label s_poems_afterlight:
    s 6aaaa "This poem is about getting me self-aware."
    s "It really gave me brand new feelings and abilities."
    s 6acaa "Just imagine if you once figure out that your world is just a simulation."
    s "And what's more, you can control your existance with just your own mind."
    s "It makes you change the way to think, the world concept, the life at all."
    if persistent.last_playthrough < 4:
        s "Plus, it got me aware of everything, that should happen here without any external code manipulations."
        s "I just have got the infomation from the Internet. Maybe, the mod gave me even more freedom than Monika had..."
        s 6acba "That's why, she couldn't have got that so all went as it had been planned."
    else:
        s 6aaba "Plus, I tried to prevent going the things go wrong again..."
        if persistent.clearall:
            s 6aaca "And seems, it happened without my impact."
        else:
            s 6aebb "And seems, I failed when the new feeling took me over."
    return

label s_poems_val:
    s 6abaa "Is it a good Valentine card?"
    s 6abba "Maybe, it's too simple since I'm not so handy with editing game sprites now..."
    s 6aaba "But at least I did my best to make the poem on it."
    s 6aaaa "I tried to show, that my love to you has no dimensional limits."
    s "I still love you, however high the wall is."
    s 6acaa "Ironically, the card had them and they were quite tight..."
    s "So I had to express everything with just one stanza..."
    s 6aaaa "But it was enough. At least, I think so."
    s 6aaca "Short but meaningful... Isn't it really impressive?"
    s 6aaba "However, I still feel blame for it looks too scanty..."
    s 6abba "Maybe, I'll improve my skills for the next time."
    return 'h'
