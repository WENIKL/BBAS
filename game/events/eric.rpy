
label Eric_talk_afterdinner:
    $ renpy.block_rollback()
    if day > 4:
        jump Eric_talk_afterdinner.second_talk
    $ spent_time = 20
    $ current_room = house[6]

    scene BG talk-terrace-00
    show Eric meet 01a
    show Max talk-terrace 01a
    Eric_00 "Макс, пока твоя мама переодевается, я бы хотел с тобой поговорить. С глазу на глаз, так сказать..."
    if eric.flags.crush > 1:
        Max_01 "Конечно..."
        $ eric.flags.crush = 7
        menu:
            Eric_05 "Я заметил, что ты настроен вполне дружелюбно. Для меня важно подружиться с твоей семьёй, чтобы твоя мама не испытывала дискомфорт на этой почве, если ты меня понимаешь..."
            "Понимаю, хорошо..." if True:
                jump Eric_talk_afterdinner.good
            "И зачем мне это?" if True:
                jump Eric_talk_afterdinner.bad
    elif eric.flags.crush > 0:
        Max_00 "Ну, давай..."
        $ eric.flags.crush = 5
        menu:
            Eric_09 "Я знаю, что мы начали знакомство не идеально, но мне показалось, что мы можем найти общий язык. Для меня важно, чтобы твоя мама не испытывала какой-либо дискомфорт из-за этого..."
            "Понимаю, хорошо..." if True:
                jump Eric_talk_afterdinner.good
            "И зачем мне это?" if True:
                jump Eric_talk_afterdinner.bad
    elif True:
        Max_09 "У меня есть выбор?"
        $ eric.flags.crush = 3
        menu:
            Eric_13 "Ты знаешь, мы начали знакомство как-то совсем неудачно. Предлагаю как-то уладить этот конфликт. Я бы очень не хотел, чтобы твоя мама испытывала дискомфорт по этому поводу..."
            "Понимаю, хорошо..." if True:
                jump Eric_talk_afterdinner.good
            "И зачем мне это?" if True:
                jump Eric_talk_afterdinner.bad

    label Eric_talk_afterdinner.good:
        $ eric.flags.crush += 1
        show Eric meet 01a
        show Max talk-terrace 01a
        menu:
            Eric_01 "Отлично. Если мы подружимся, ты не пожалеешь, Макс. Но, чтобы убедиться, давай вернёмся к этому разговору через неделю. Если мы найдём общий язык, то всё будет отлично. Ну а если нет..."
            "А если нет, то что?" if True:
                jump Eric_talk_afterdinner.what
            "Думаю, подружимся..." if True:
                $ eric.flags.crush += 2
                jump Eric_talk_afterdinner.friend

    label Eric_talk_afterdinner.bad:
        show Max talk-terrace 04a
        show Eric meet 01b
        $ eric.flags.crush -= 1
        menu:
            Eric_01 "Я бы на твоём месте не искал врага там, где его нет. Предлагаю вернуться к этому разговору через неделю. Если мы подружимся, ты не пожалеешь. А вот если решишь со мной воевать, то ты точно проиграешь..."
            "Это ещё почему?" if True:
                jump Eric_talk_afterdinner.what
            "Да я не собираюсь воевать..." if True:
                $ eric.flags.crush += 1
                jump Eric_talk_afterdinner.friend

    menu Eric_talk_afterdinner.what:
        Eric_05 "Если решишь испытать судьбу, то сам всё скоро узнаешь. У меня есть влияние, деньги, харизма. А главное - я умею убеждать и подчинять других людей. А что есть у тебя?"
        "Да верю, верю. Я просто спросил и не хочу ссориться..." if True:
            $ eric.flags.crush += 1
            jump Eric_talk_afterdinner.friend
        "Меня все любят и мне поверят, что ты мне угрожал!" if True:
            $ eric.flags.crush -= 2
            show Max talk-terrace 04a
            show Eric meet 01b
            menu:
                Eric_02 "Правда? А я вот уже слышал, что Алиса относится к тебе как к маленькому извращенцу, Лиза рядом с тобой просто потому, что других защитников в доме не было, а мать смотрит на тебя как на неудачника..."
                "Не верю! Всё не так!" if True:
                    jump Eric_talk_afterdinner.bullshit
                "Она так сказала?" if True:
                    jump Eric_talk_afterdinner.shesaid
        "У меня есть мозги и я что-нибудь придумаю!" if True:
            $ eric.flags.crush -= 2
            show Max talk-terrace 04a
            show Eric meet 01b
            menu:
                Eric_02 "Серьёзно? И как ты с этими мозгами довёл ситуацию до того, что Алиса в тебе видит маленького извращенца, подглядывающего из-за угла. Лиза рядом только потому, что других защитников не было, а мать... смотрит на тебя как на неудачника!"
                "Не верю! Всё не так!" if True:
                    jump Eric_talk_afterdinner.bullshit
                "Она так сказала?" if True:
                    jump Eric_talk_afterdinner.shesaid

    label Eric_talk_afterdinner.bullshit:
        menu:
            Eric_09 "Ну не знаю... Даже если что-то ещё и не так, то с моей помощью всё так и будет, поверь... Но повторюсь, я не хочу с тобой воевать и лучше бы ты был на моей стороне..."
            "Ладно, посмотрим..." if True:
                jump Eric_talk_afterdinner.ok
            "Никогда. Отвали!" if True:
                jump Eric_talk_afterdinner.no

    label Eric_talk_afterdinner.shesaid:
        Eric_09 "Ну не словами, но я же это вижу со стороны. Тебя выгнали из школы за отношения с учителем. Если ты не понял, то это такой зашквар, что вернуть себе репутацию будет непросто..."
        show Eric meet 01a
        menu:
            Eric_00 "Но повторюсь, я не хочу с тобой воевать. Наоборот, я бы хотел с тобой подружиться и если ты будешь на моей стороне, ты только выиграешь..."
            "Ладно, посмотрим... И что я выиграю?" if True:
                jump Eric_talk_afterdinner.ok
            "Никогда. Отвали!" if True:
                jump Eric_talk_afterdinner.no

    label Eric_talk_afterdinner.ok:
        show Max talk-terrace 01a
        show Eric meet 01a
        menu:
            Eric_05 "Смотря как пройдёт наше общение за следующую неделю. Если помиримся, то я буду помогать решать твои проблемы, ну а ты мои, если такие возникнут с твоей семьёй..."
            "Какие проблемы?" if True:
                menu:
                    Eric_00 "Ты слишком забегаешь вперёд, Макс. Давай сначала посмотрим на то, как всё пойдёт. Дай мне хотя бы шанс тебя убедить..."
                    "Ну, ладно, убедил." if True:
                        jump Eric_talk_afterdinner.friend
                    "Нет, без вариантов..." if True:
                        jump Eric_talk_afterdinner.no
            "Договорились..." if True:
                jump Eric_talk_afterdinner.friend

    label Eric_talk_afterdinner.no:
        show Max talk-terrace 04a
        show Eric meet 01b
        menu:
            Eric_00 "Ну, как хочешь. Надеюсь, в тебе сейчас говорят эмоции, а не здравый смысл. У тебя есть неделя, чтобы передумать. Тогда и поговорим снова и будет ясно, как быть."
            "{i}промолчать{/i}" if True:
                $ eric.flags.crush = 0
                $ poss['alpha'].open(0)
                jump Waiting

    label Eric_talk_afterdinner.friend:
        show Max talk-terrace 01a
        show Eric meet 01a
        Eric_05 "Я рад, правда. Ты не пожалеешь. Ладно, твоя мама уже идёт, мы поехали. Вернёмся к этому разговору через неделю..."
        Max_04 "Ага..."
        $ poss['alpha'].open(0)
        jump Waiting

    label Eric_talk_afterdinner.second_talk:
        $ spent_time = 20
        scene BG talk-terrace-00
        if eric.flags.crush > 5:
            show Eric meet 01a
            $ renpy.show('Max talk-terrace 01'+mgg.dress)
        elif True:
            show Eric meet 01b
            $ renpy.show('Max talk-terrace 04'+mgg.dress)
        Eric_00 "Ну что, Макс, готов пообщаться снова, пока твоя мама собирается?"
        if eric.flags.crush>7:
            Max_01 "Конечно!"
            menu:
                Eric_05 "Отлично! Ну что, вроде бы ты и правда настроен на дружбу. Я прав?"
                "Да, я только за." if True:
                    jump Eric_talk_afterdinner.goodgood
                "Тебе показалось. Я тебя ненавижу!" if True:
                    jump Eric_talk_afterdinner.badbad
        elif 3<eric.flags.crush<8:
            Max_00 "Ну, можно..."
            menu:
                Eric_01 "Правда, я не до конца понял твою позицию. Ты настроен на дружбу или хочешь попытаться повоевать?"
                "Думаю, воевать смысла нет..." if True:
                    jump Eric_talk_afterdinner.goodgood
                "Я тебя ненавижу!" if True:
                    jump Eric_talk_afterdinner.badbad
        elif True:
            Max_09 "Ты ещё здесь?"
            menu:
                Eric_09 "Значит, дружить ты не намерен. Я правильно понимаю?"
                "Почему? Я подумал как следует. Воевать точно не хочу..." if True:
                    jump Eric_talk_afterdinner.goodgood
                "Правильно. Я тебя ненавижу!" if True:
                    jump Eric_talk_afterdinner.badbad

    label Eric_talk_afterdinner.badbad:
        show Eric meet 01b
        $ renpy.show('Max talk-terrace 04'+mgg.dress)
        Eric_02 "Всё ясно с тобой. Ну, это твой выбор. У тебя была неделя, чтобы всё обдумать. Ты решил начать войну, ну что же, не вини меня за то, как я её закончу..."
        $ notify_list.append(_("{color=[orange]}{i}{b}Внимание:{/b} Ваши отношения значительно ухудшились!{/i}{/color}"))
        $ AttitudeChange('eric', -3)
        $ flags.voy_stage = -1
        $ poss['alpha'].open(3)
        jump Waiting

    label Eric_talk_afterdinner.goodgood:
        show Eric meet 01a
        $ renpy.show('Max talk-terrace 01'+mgg.dress)
        Eric_01 "Очень хорошо. Я рад. Ну, ты не пожалеешь, это правильный выбор..."
        Max_09 "Но ты так и не сказал, почему не пожалею..."
        Eric_03 "Ну давай начнём с самого простого. Чего ты хочешь?"
        Max_07 "В каком смысле?"
        menu:
            Eric_05 "Я не слепой и вижу как ты смотришь на своих сестёр и даже маму. Не отрицай, иногда даже твои штаны тебя выдают. Но я тебя не виню, ещё бы, такие цыпочки кругом!"
            "Что? Ты ошибаешься!" if True:
                pass
            "Они никакие не цыпочки!" if True:
                pass
            "Я вдруг понял... Да пошёл ты!" if True:
                jump Eric_talk_afterdinner.badbad
        menu:
            Eric_01 "Да ладно, здесь все свои! Любой мужик бы думал только о том, как поиметь их всех по очереди или даже разом. Это нормально! Я тебя понимаю!"
            "Думаешь?" if True:
                menu:
                    Eric_05 "Уверен в этом. И если честно, надеюсь, у меня всё получится. А ты мне в этом поможешь!"
                    "А если я расскажу про это всем?" if True:
                        jump Eric_talk_afterdinner.tell
                    "Только, если я что-то получу за это..." if True:
                        jump Eric_talk_afterdinner.get
                    "Ты подонок! Я передумал. Убирайся!" if True:
                        jump Eric_talk_afterdinner.badbad
            "Постой, и ты этого хочешь?" if True:
                menu:
                    Eric_05 "Конечно! Я же нормальный мужик... Кстати, ты же никому не расскажешь, верно? Мы же типа друзья?"
                    "А если я расскажу про это всем?" if True:
                        jump Eric_talk_afterdinner.tell
                    "Только, если я что-то получу за это..." if True:
                        jump Eric_talk_afterdinner.get
                    "Ты подонок! Я передумал. Убирайся!" if True:
                        jump Eric_talk_afterdinner.badbad
    menu Eric_talk_afterdinner.tell:
        Eric_03 "Всем? Это кому же? Сёстрам? Ну да, поверят они тебе... Расскажешь матери? Попытайся. Заодно, узнаешь на что способны мои, так сказать, \"чары\"..."
        "Да я не собираюсь рассказывать, просто спросил..." if True:
            pass
        "Вот и проверим..." if True:
            menu:
                Eric_09 "Не ожидал я от тебя такого... Ну ладно, дело твоё... Но учти, на этой войне у тебя нет ни единого шанса!"
                "Да я пошутил! Конечно, не расскажу никому..." if True:
                    pass
                "Вот и посмотрим..." if True:
                    jump Eric_talk_afterdinner.badbad
        "Ты - псих ненормальный. Убирайся!" if True:
            jump Eric_talk_afterdinner.badbad
    Eric_01 "Так ты меня разводишь? А я тебе почти поверил! Молодец..."
    Max_09 "Ладно, а что я с этого получу?"

    label Eric_talk_afterdinner.get:
        Eric_03 "Отличный вопрос, Макс! Пришло время выяснить, чего же именно ты хочешь?"
        Max_07 "Я хочу деньги, подглядывать и кое-что ещё..."
        Eric_05 "Ого. Вот это запросы! Ну, мы договоримся, Макс. Деньги для меня не проблема, но в разумных пределах, конечно..."
        Max_01 "Сколько?"
        Eric_04 "Посмотрим на твоё поведение. Ещё рано торговаться. Если будешь в своё время закрывать глаза, то денег будет больше. Ну а если будешь мешать, то..."
        Max_07 "Ладно. А что насчёт подглядывать? Это можно?"
        Eric_01 "Ну лично я не возражаю. Думаю, даже твою маму подготовлю, чтобы если заметила, то не наказывала. Если ты помнишь, со следующей недели шлёпать вас будут голыми, а это очень унизительно... Что ещё ты там просил?"
        Max_08 "Я бы тоже хотел кое-кого..."
        menu:
            Eric_02 "Если ты про свою семью, то хотя я тебя и понимаю, но торговаться на этот счёт не намерен. Я тебе буду платить за твоё невмешательство. Более того, даже разрешу подглядывать без последствий, а вот все женщины в семье - мои."
            "Договорились!" if True:
                pass
            "Нет, на это я не согласен." if True:
                menu:
                    Eric_09 "Ну, тогда мы с тобой перед диллемой. Ты знаешь слишком много о моих планах, я знаю, что ты тот ещё извращенец... Как быть?"
                    "Я не извращенец!" if True:
                        menu:
                            Eric_03 "Ну, это как посмотреть. Ты хотел потребовать \"доступа\" к женщинам в своей семье... Если бы твоя мать узнала, сомневаюсь, что это бы хорошо для тебя закончилось, правда?"
                            "А есть только два варианта?" if True:
                                pass
                            "Тогда... Остаётся только послать тебя куда подальше. Такая дружба мне не нужна!" if True:
                                jump Eric_talk_afterdinner.badbad
                    "А есть только два варианта?" if True:
                        pass
                    "Ты знаешь... Я тут подумал. Да пошёл ты! Не надо мне ничего от тебя. Я от тебя избавлюсь!" if True:
                        jump Eric_talk_afterdinner.badbad
                menu:
                    Eric_02 "Боюсь, что да. Либо ты со мной, либо против меня. Напомню - я тебе буду платить, ты сможешь смотреть, но нельзя трогать... Ну или война и ты точно проиграешь. Очень быстро..."
                    "Если так, то я согласен на твои условия, конечно!" if True:
                        pass
                    "Знаешь, что... Эрик? А иди-ка ты в жопу! Без тебя справимся!" if True:
                        jump Eric_talk_afterdinner.badbad
        Eric_05 "Вот это разговор! Ну, тогда мы точно поладим. Если я увижу, что ты держишь свои обещания, то даже дам тебе кое-что, от чего ни один мужик не откажется, поверь!"
        Max_03 "О чём речь?"
        Eric_06 "Любопытно? Ну я намекну... Сможешь не только подглядывать, но и принимать участие..."
        Max_06 "Да ладно?"
        Eric_03 "Ага. Так что, в твоих интересах мне не только не мешать, но и помогать, если возникнет такая необходимость. Ну там, слово замолвить или сделать что-то..."
        Max_05 "Договорились!"
        Eric_01 "Ну всё, Макс. Я рад, что мы разобрались и, так сказать, поделили территорию. Теперь всё в твоих руках. Ну и в моих тоже... О, твоя мама идёт. Ну всё, пока!"
        $ notify_list.append(_("{color=[lime]}{i}{b}Внимание:{/b} Ваши отношения значительно улучшились{/i}{/color}"))
        $ poss['alpha'].open(2)
        $ flags.voy_stage = 0
        $ flags.bonus_from_eric.append('money')
        $ AttitudeChange('eric', 4)
        jump Waiting


label eric_resting:
    scene BG char Ann relax-evening-01
    $ renpy.show('Eric relax '+pose3_1+eric.dress)
    $ persone_button1 = 'Eric relax '+pose3_1+eric.dress+'b'
    return


label eric_ann_tv:
    $ renpy.block_rollback()
    scene BG tv-watch-01
    $ film = ae_tv_order[0]

    if tv_scene == '' or not eric.daily.tv_sex:

        $ renpy.show('porn_'+film+' 01_02', at_list=[tv_screen,])
        $ renpy.show('Eric tv-watch 01'+eric.dress)
    elif eric.daily.tv_sex == 2:
        $ renpy.show('tv serial 0'+str(renpy.random.randint(1, 7))+'-0'+str(renpy.random.randint(1, 3)), at_list=[tv_screen,])
        $ renpy.show('Eric tv-watch 01'+eric.dress)
    elif True:

        if pose2_3 == '01':
            $ renpy.show('porn_'+film+' 05_06', at_list=[tv_screen,])
        elif True:
            $ renpy.show('porn_'+film+' 07_08', at_list=[tv_screen,])
        $ renpy.show('Eric tv-watch '+tv_scene+pose2_3+eric.dress)

    if eric.daily.tv_sex:
        return


    $ eric.daily.tv_sex = 1
    if eric.stat.handjob:
        $ txt = _("Кажется, мама с Эриком смотрят какой-то фильм. Наверняка, снова порно...")
        $ txt2 = _("Макс, мы тут с Эриком фильм смотрим. Я бы тебя пригласила, но он не для детей. Ты не мог бы погулять где-то? И, пожалуйста, не подглядывай. Хорошо?")
    elif True:
        $ txt = _("Кажется, мама с Эриком смотрят какой-то фильм. Интересно, какой...")
        $ txt2 = _("Ой, Макс... Мы тут с Эриком фильм смотрим. Я бы тебя пригласила, но он не для детей. Ты не мог бы погулять где-то? И, пожалуйста, не подглядывай. Хорошо?")
    menu:
        Max_07 "[txt!t]"
        "{i}наблюдать за ними{/i}" if True:
            pass
        "{i}подойти к ним{/i}" if True:
            scene BG lounge-tv-00
            $ renpy.show('Eric tv '+renpy.random.choice(['01', '02', '03'])+eric.dress)
            menu:
                Ann_12 "[txt2!t]"
                "Конечно, мам! {i}(уйти){/i}" if True:
                    jump eric_ann_tv.end
                "Конечно, мам! {i}(спрятаться){/i}" if True:
                    scene BG tv-watch-01
        "{i}уйти{/i}" if True:
            $ current_room = house[0]
            jump Waiting

    $ tv_scene = renpy.random.choice(['bj', 'hj']) if eric.stat.handjob > 0 else 'hj'

    $ spent_time += 10
    $ pose2_3 = '01'
    $ renpy.show('porn_'+film+' 03_04', at_list=[tv_screen,])
    $ renpy.show('Eric tv-watch '+tv_scene+pose2_3+eric.dress)
    $ _alt = False

    if tv_scene == 'bj':

        if eric.stat.blowjob:
            $ txt = _("Ого! На экране стало интереснее! А мама, видимо, снова потянулась отсасывать Эрику...")
            $ txt2 = _("На экране уже во всю идёт самое интересное и мама скинула полотенце! Вот бы посмотреть на эту голую попку с другого ракурса... Может быть, подойти ближе?")
        elif True:
            $ txt = _("Ого! На экране стало интереснее! А куда это мама так наклонилась?")
            $ txt2 = _("Ничего себе! Эрик стянул с мамы полотенце и я вижу её голую попку! Может быть, подойти ближе?")
        menu:
            Max_08 "[txt!t]"
            "{i}продолжать смотреть{/i}" if True:

                $ spent_time += 10
                $ pose2_3 = '02'
                $ ann.dress_inf = '00'
                $ renpy.show('porn_'+film+' 05_06', at_list=[tv_screen,])
                $ renpy.show('Eric tv-watch '+tv_scene+pose2_3+eric.dress)
                menu:
                    Max_07 "[txt2!t]"
                    "{i}Что за вопрос? Конечно!{/i}" if True:
                        jump eric_ann_tv.closer1
                    "{i}взглянуть со стороны{/i}" if eric.stat.handjob and mgg.stealth >= 11.0:
                        $ _alt = True
                        jump eric_ann_tv.closer1
                    "{i}продолжать смотреть{/i}" if True:
                        $ spent_time += 10
            "{i}подойти ближе{/i}" if True:

                jump eric_ann_tv.closer1
            "{i}взглянуть со стороны{/i}" if eric.stat.handjob != 0 and mgg.stealth >= 11.0:
                $ _alt = True
                jump eric_ann_tv.closer1
            "{i}тихо уйти{/i}" if True:
                jump eric_ann_tv.end
    elif True:

        if eric.stat.blowjob:
            $ txt = _("Ого! На экране стало интереснее! А мама, вроде, снова начала дрочить Эрику...")
            $ txt2 = _("На экране уже во всю идёт самое интересное и мама скинула полотенце! Жаль, что её грудь не очень хорошо видно... Может быть, подойти ближе?")
        elif True:
            $ txt = _("Ого! На экране стало интереснее! А что это мама там делает?")
            $ txt2 = _("Ничего себе! Эрик стянул с мамы полотенце и я вижу её голую грудь! Может быть, подойти ближе?")
        menu:
            Max_08 "[txt!t]"
            "{i}продолжать смотреть{/i}" if True:

                $ spent_time += 10
                $ pose2_3 = '02'
                $ ann.dress_inf = '00'
                $ renpy.show('porn_'+film+' 05_06', at_list=[tv_screen,])
                $ renpy.show('Eric tv-watch '+tv_scene+pose2_3+eric.dress)
                menu:
                    Max_07 "[txt2!t]"
                    "{i}Что за вопрос? Конечно!{/i}" if True:
                        jump eric_ann_tv.closer1
                    "{i}взглянуть со стороны{/i}" if eric.stat.handjob and mgg.stealth >= 11.0:
                        $ _alt = True
                        jump eric_ann_tv.closer1
                    "{i}продолжать смотреть{/i}" if True:
                        $ spent_time += 10
            "{i}подойти ближе{/i}" if True:

                jump eric_ann_tv.closer1
            "{i}взглянуть со стороны{/i}" if eric.stat.handjob != 0:
                $ _alt = True
                jump eric_ann_tv.closer1
            "{i}тихо уйти{/i}" if True:
                jump eric_ann_tv.end


    $ renpy.show('porn_'+film+' 07_08', at_list=[tv_screen,])
    if eric.stat.handjob:
        menu:
            Max_10 "Если меня заметят, пока я смотрю порно на большом экране и подглядываю за тем, что происходит здесь же, наяву, меня точно накажут"
            "{i}продолжать смотреть{/i}" if True:
                $ renpy.show('porn_'+film+' 09_10', at_list=[tv_screen,])
                Max_09 "Похоже, порно подходит к концу, а вот Эрик не кончает! Наверно, они просто решили {i}разогреться{/i} перед тем, что будет в маминой спальне... А это значит, мне пора уходить."
                $ spent_time = 50 - int(tm[-2:])
                jump eric_ann_tv.end
            "{i}тихо сматываться{/i}" if True:
                jump eric_ann_tv.end
    elif True:
        menu:
            Max_10 "Ого! Если меня заметят, пока я подглядываю за ТАКИМ, меня точно накажут. Нужно срочно уходить!"
            "{i}подойти ближе{/i}" if True:
                jump eric_ann_tv.closer1
            "{i}взглянуть со стороны{/i}" if eric.stat.handjob != 0 and mgg.stealth >= 11.0:
                $ _alt = True
                jump eric_ann_tv.closer1
            "{i}тихо уйти{/i}" if True:
                jump eric_ann_tv.end

    label eric_ann_tv.closer1:

        $ spent_time += 10
        if _alt:
            scene BG tv-mass-05
            $ renpy.show('Max tv 02'+mgg.dress)
            $ renpy.show('Eric tv '+tv_scene+pose2_3+eric.dress+'-alt')
        elif True:
            scene BG lounge-tv-00
            $ renpy.show('Eric tv '+tv_scene+pose2_3+eric.dress)

        if not eric.stat.handjob:
            if pose2_3 == '01':
                Max_15 "Она что, дрочит ему?! Прямо здесь... Нужно это срочно прекратить! Только, как это лучше сделать?" nointeract
            elif True:
                Max_16 "Она что, совершенно голая дрочит ему?! Прямо здесь... Нужно это срочно прекратить! Только, как это лучше сделать?" nointeract

            $ _m1_eric__dial = [(_("Вы охренели!"), 2), (_("{i}тихо уйти{/i}"), 3)]
            if False:
                $ _m1_eric__dial.insert(0, (_("Ма-а-ам?"), 1))
            $ _m1_eric__r1 = renpy.display_menu(_m1_eric__dial)

            if _m1_eric__r1 == 1:
                Eric_09 "Макс! Чего хотел? Не видишь, мы заняты? Если хочешь смотреть, делай это тихо и нам не мешай. А ты, Ань, не останавливайся, продолжай..."
                Max_12 "Охренеть!"
                jump eric_ann_tv.end
            elif _m1_eric__r1 == 2:
                pass
            elif True:

                jump eric_ann_tv.end
        elif True:
            if tv_scene == 'hj':
                if pose2_3 == '01':
                    Max_11 "Да, она ему дрочит! Прямо здесь... Они настолько увлечены друг другом, что ничего вокруг не замечают! Ну, кроме того, что на экране происходит..." nointeract
                elif True:
                    Max_07 "Ох... мама такая голая и мокрая... У неё такое соблазнительное тело, а какая попка! Ммм... Хорошо, что они настолько увлечены друг другом, что ничего вокруг не замечают! Ну, кроме того, что на экране происходит..." nointeract
            elif eric.stat.blowjob:
                if pose2_3 == '01':
                    Max_11 "Да, она отсасывает ему! Прямо здесь... Они настолько увлечены друг другом, что ничего вокруг не замечают! Ну, кроме того, что на экране происходит..." nointeract
                elif True:
                    Max_07 "Ох... мама такая голая и мокрая... У неё такое соблазнительное тело, а какая попка! Ммм... Хорошо, что они настолько увлечены друг другом, что ничего вокруг не замечают! Ну, кроме того, что на экране происходит..." nointeract
            elif True:
                Max_15 "Она что, отсасывает ему?! Прямо здесь... Вот же развратница, а если кто-то зайдёт и увидит!" nointeract

            $ _m1_eric__r1 = renpy.display_menu([("{i}тихо уйти{/i}", 3),])
            if _m1_eric__r1:
                jump eric_ann_tv.end


    $ renpy.show('Eric tv hjbj'+pose2_3+eric.dress)
    $ eric.daily.tv_sex = 2
    menu:
        Ann_13 "Что? Кто здесь? Макс?! Выйди немедленно, не видишь..."
        "Как раз всё вижу. Не стыдно?" if True:
            pass
        "Хорошо. А вы тут продолжайте... Не стесняйтесь." if True:
            pass
        "Извини, мам. Я просто не ожидал ТАКОЕ увидеть..." if True:
            Ann_04 "Я рада, Макс, что ты всё понимаешь. Сделаем вид, что ничего не было и ты ничего не видел, хорошо?"
            Max_01 "Конечно, мам!"
            jump eric_ann_tv.end

    Ann_14 "Так, Макс, нам надо поговорить! Отойдем на кухню..."
    Max_08 "Ну ладно."

    scene lounge-tv-talk-00
    $ renpy.show('Ann tv-talk '+pose2_3+'a')
    menu:
        Ann_12 "Послушай, сынок... Понимаешь, взрослым иногда нужно уединяться. Мы думали, что все наверху и что мы тут, всем и так понятно... В общем..."
        "Хотите потрахаться - идите в свою комнату. Нечего этим на виду у всех заниматься!" if True:
            Ann_15 "Макс! Что за слова? И как ты со мной разговариваешь? А ну-ка марш в свою комнату. Чтобы не видела тебя тут, пока мы смотрим фильмы!"
            Max_11 "Ладно, ладно. Так бы сразу и сказала..."
        "Да всё в порядке. Это ты извини... Я просто от неожиданности крикнул." if True:
            Ann_04 "Макс! Ты у меня такой умница. Хорошо, что ты всё понимаешь. Ладно, иди в свою комнату, мы больше не будем... Тебя смущать..."
            Max_01 "Хорошо, мам..."
        "А вы не против, если я посмотрю?" if True:
            Ann_13 "Посмотришь? На что? На нас? Или фильм? В любом случае нет! Ты ещё маленький. И, вообще, почему я перед тобой отчитываюсь. Дай взрослым отдохнуть. А ты иди в свою комнату!"
            Max_10 "Ладно, уже ухожу..."

    label eric_ann_tv.end:
        if tv_scene == 'hj':
            $ eric.stat.handjob += 1
        elif tv_scene == 'bj':
            $ eric.stat.blowjob += 1
        $ spent_time += 10
        $ current_room = house[0]
        jump Waiting


label eric_ann_fucking:
    scene location house annroom door-night
    if eric.daily.sex > 0:
        return

    $ eric.daily.sex = 1

    $ _ch1 = GetChance(mgg.stealth, 3, 900)
    menu:
        Max_00 "Судя по звукам, мама с Эриком чем-то занимаются. Открывать дверь точно не стоит, влетит..."
        "{i}заглянуть в окно\n{color=[_ch1.col]}(Скрытность. Шанс: [_ch1.vis]){/color}{/i}" if flags.voy_stage<0 or GetRelMax('eric')[0]<0:
            pass
        "{i}заглянуть в окно{/i}" if 0<=flags.voy_stage<4 and GetRelMax('eric')[0]>3:
            pass
        "{i}зайти в спальню{/i}" if 3<flags.voy_stage<8 and GetRelMax('eric')[0]>3:
            jump lessons_from_Eric
        "{i}уйти{/i}" if True:

            window hide
            $ current_room = house[0]
            jump AfterWaiting

    label eric_ann_fucking.voyeur:
        $ spent_time += 10

    $ fuck_scene = renpy.random.choice([6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6])
    if fuck_scene in [3, 6]:
        scene BG char Eric bed-02
    elif True:
        scene BG char Eric bed-01
    if fuck_scene == 6:
        show AnimAnnEric1
    elif True:
        $ renpy.show('Eric fuck 0'+str(fuck_scene))
    if fuck_scene in [3, 6]:
        $ renpy.show('FG ann&eric-voyeur-02')
    elif True:
        $ renpy.show('FG ann&eric-voyeur-01')

    if flags.voy_stage in [0, 1, 2, 3] and GetRelMax('eric')[0]>3:
        if fuck_scene == 6:
            scene BG char Eric bed-02
            $ renpy.show('Eric fuck 06b')
            $ renpy.show('FG ann&eric-voyeur-02')
        elif True:
            $ renpy.show('Eric fuck 0'+str(fuck_scene)+'b')
        if flags.voy_stage in [0, 1]:
            Ann_15 "[spotted!t]Макс?! Какого чёрта? Ты за нами подглядываешь?! Завтра ты будешь наказан! Немедленно убирайся!"
            $ punreason[3] = 1

        elif flags.voy_stage == 2:
            Ann_19 "Макс? Ты опять подглядываешь? Утром накажу у всех на глазах за это!"
            Max_10 "Э... Не надо!"
            Eric_03 "Ань, не спеши. Макс подросток и ему всё интересно. Ты же знаешь, запретный плод сладок. Думаю, не стоит его наказывать за такие шалости. Хорошо?"
            Ann_14 "Ну, хорошо, Эрик. Если ты так считаешь... Но пусть он уйдёт, я не могу так..."
            Max_07 "Я уже ухожу, мам... Продолжайте!"
            $ flags.voy_stage = 3

        elif flags.voy_stage == 3:
            menu:
                Ann_18 "Макс? Опять подглядываешь?! Ну-ка бегом отсюда!"
                "Я никому не мешаю же..." if True:
                    menu:
                        Eric_02 "Ань, пусть лучше смотрит на нас, чем на непойми какие извращения в интернете, верно? Так, Макс, зайди сюда, поговорим..."
                        "{i}войти в комнату{/i}" if True:
                            scene BG annroom-watch-01
                            show Eric watch 00
                            $ renpy.show('Max annroom-watch 01'+mgg.dress)

                            Ann_14 "Эрик, но... он мой сын. Это неправильно, ты же понимаешь..."
                            Eric_03 "Я думаю, что мы должны разрешить ему смотреть, если не будет мешать. Может быть, чему-то научится. Где-то ему же нужно учиться, пусть это будет таким образом... И Ань, не спорь со мной!"
                            Ann_12 "Как скажешь, Эрик..."
                            Eric_01 "Ну всё, Макс. Мы тут ещё побеседуем. А для тебя на сегодня хватит, иди."
                            Max_00 "Хорошо..."
                            $ flags.voy_stage = 4
                            $ poss['control'].open(0)
                "Я уже ухожу, мам... Извини..." if True:

                    pass

        $ current_room = house[0]
        jump Waiting

    if RandomChance(_ch1.ch) or flags.voy_stage > 6:
        if flags.voy_stage<6:
            $ Skill('hide', 0.1)
        $ ann.dress_inf = '00'
        $ eric.daily.sex = 3
        if fuck_scene == 1:
            Max_10 "[undetect!t]Боже мой, что моя мама творит?! Неужели ей действительно нравится отсасывать этому придурку?!" nointeract
        elif fuck_scene == 2:
            Max_07 "[undetect!t]Вот это да! Прямо как в крутом порнофильме! Я даже представить себе не мог, что моя строгая мама способна на такое. Да и Эрик от неё не отстаёт... Кажется, ей это очень нравится!" nointeract
        elif fuck_scene == 3:
            Max_10 "[undetect!t]Что?! Моя мама сосёт этому уроду? Эрик, гад, он же... трахает её в рот, как какую-то дешёвую уличную шлюху! Почему она ему это позволяет?!" nointeract
        elif fuck_scene == 4 or fuck_scene == 6:
            Max_08 "[undetect!t]Ну вот, Эрик трахает маму сзади, да так активно... Кажется, у неё просто нет сил противиться этому, хотя, может быть, ей это даже нравится!" nointeract
        elif fuck_scene == 5:
            Max_07 "[undetect!t]Ничего себе! Вот это страсть! Моя мама скачет на Эрике как сумасшедшая! Я даже представить себе не мог, что она способна на такое! Кажется, они так увлечены друг другом, что не заметят, если я выйду из-за угла..." nointeract
    elif True:
        $ eric.daily.sex = 2

        if fuck_scene == 6:
            scene BG char Eric bed-02
            $ renpy.show('Eric fuck 06b')
            $ renpy.show('FG ann&eric-voyeur-02')
        elif True:
            $ renpy.show('Eric fuck 0'+str(fuck_scene)+'b')
        Ann_15 "[spotted!t]Макс?! Какого чёрта? Ты за нами подглядываешь?! Завтра ты будешь наказан! Немедленно убирайся!"
        $ Skill('hide', 0.05)
        $ punreason[3] = 1
        $ current_room = house[0]
        jump Waiting

    $ Skill('hide', 0.1)

    $ rez = renpy.display_menu([(_("{i}продолжить смотреть{/i}"), 0), (_("{i}уйти{/i}"), 1)])
    if rez > 0:
        $ current_room = house[0]
        jump Waiting

    if fuck_scene == 6:
        scene BG char Eric bed-02
        $ renpy.show('Eric fuck 06a')
        $ renpy.show('FG ann&eric-voyeur-02')
    elif True:
        $ renpy.show('Eric fuck 0'+str(fuck_scene)+'a')
    if fuck_scene == 1:
        Max_09 "Чёрт, этот удачливый ублюдок кончил ей прямо в рот, причём, судя по довольному лицу мамы, ей это понравилось! Ну почему таким уродам всегда везёт?! Ладно, надо уходить, а то они сейчас меня заметят..."
    elif fuck_scene == 2:
        Max_08 "Ого! Похоже, мама кончила и... Эрик тоже... Хорошо, что хоть не маме в рот... А она у нас та ещё проказница! Пора сматываться, пока меня не заметили!"
    elif fuck_scene == 3:
        Max_11 "Чёрт, эта сволочь кончила ей прямо в рот и... похоже мама не в восторге от всего этого. Бедная моя мама... это нельзя так просто оставлять! А пока лучше скорее уходить, не хватало ещё, чтобы меня увидели..."
    elif fuck_scene == 4 or fuck_scene == 6:
        Max_10 "Ох, чёрт... наконец-то Эрик кончил и... хорошо, что не в маму... Вот же счастливый сукин сын... залил ей своей спермой всю спину... Пожалуй, не стоит здесь задерживаться, они могут меня увидеть."
    elif fuck_scene == 5:
        Max_10 "Чёрт возьми... он не сдержался и уже кончил... Хотя, это не удивительно, после таких-то скачек! Вот же повезло этой сволочи Эрику! И надо уже уходить, пока меня не заметили!"

    $ eric.daily.sex = 4

    $ spent_time += 20
    if flags.voy_stage<6:
        $ Skill('hide', 0.1)
    $ current_room = house[0]
    jump Waiting


label eric_ann_sleep:
    scene location house annroom door-night
    if ann.hourly.sleep != 0:
        return

    $ ann.hourly.sleep = 1
    menu:
        Max_00 "Кажется, все спят..."
        "{i}заглянуть в окно{/i}" if True:
            scene BG char Ann bed-night-01
            if flags.eric_jerk and '02:00'<=tm<'02:30':

                if not alice.sleepnaked:

                    $ alice.hourly.sleep = 1
                    jump jerk_balkon

                $ renpy.show('Ann sleep-night '+pose3_3+ann.dress)
                $ renpy.show('FG ann-voyeur-night-00'+mgg.dress)
                if not prenoted and not flags.eric_noticed:

                    menu:
                        Max_09 "О! Мама спит одна... Как она прекрасна, особенно голая... А Эрик где? Уж не у Алисы ли в комнате?!"
                        "{i}проверить{/i}" if True:
                            jump jerk_balkon
                        "{i}прокрасться в комнату{/i}" if True:
                            jump eric_ann_sleep.not_eric_closer
                        "{i}уйти{/i}" if True:
                            jump eric_ann_sleep.end
                elif True:

                    jump eric_ann_sleep.not_eric

            elif not check_is_room('eric', house[2]):

                $ renpy.show('Ann sleep-night '+pose3_3+ann.dress)
                $ renpy.show('FG ann-voyeur-night-00'+mgg.dress)
                jump eric_ann_sleep.not_eric
            elif True:

                $ renpy.show('Eric sleep-night '+pose3_1)
                $ renpy.show('FG ann-voyeur-night-00'+mgg.dress)
                if pose3_1 == '01':
                    Max_01 "Похоже, они крепко спят... Совершенно голые! Чёрт, жаль только мама лежит за Эриком и её почти не видно... Почему он такой здоровый?" nointeract
                elif pose3_1 == '02':
                    Max_07 "О, да! Этой ночью мама предстала во всей красе... Полностью голенькая... такая соблазнительная. Только вот обезьяна здесь лишняя повисла!" nointeract
                elif True:
                    Max_04 "Класс! У моей мамы лучшая попка в мире... а голая она просто сводит с ума! Ещё бы эта гора мышц около неё не лежала..." nointeract
                $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), 'sneak'), (_("{i}уйти{/i}"), 'exit')])
                if rez != 'exit':
                    $ spent_time += 10
                elif True:
                    jump eric_ann_sleep.end
                scene BG char Ann bed-night-02
                $ renpy.show('Eric sleep-night-closer '+pose3_1)
                if pose3_1 == '01':
                    Max_03 "Они действительно крепко спят... Может самого интересного и не видно, но мама так элегантно, по-женски, закинула на него свою ножку... Хорошо, что такая жара и дома нет кондиционеров... Так, пора уходить." nointeract
                elif pose3_1 == '02':
                    Max_02 "Просто с ума сойти можно! Она лежит всего в метре от меня... совсем голая... и мне видно её киску... такая красивая! А этот ублюдок, Эрик, так по-хозяйски облапал её... Врезать бы ему, гаду... Ладно, пора бы мне уже уходить, а то они ещё проснутся." nointeract
                elif True:
                    Max_05 "Мама такая красивая... а её кругленькая оттопыренная попка просто чудо! Так завораживает! Как бы мне хотелось потрогать её... Ох, мечты... Только бы они сейчас не проснулись..." nointeract
                $ rez = renpy.display_menu([(_("{i}уйти{/i}"), 'exit')])
                jump eric_ann_sleep.end
        "{i}уйти{/i}" if True:

            jump eric_ann_sleep.end

    label eric_ann_sleep.not_eric:

        if pose3_1 == '01':
            Max_01 "Класс! Мама спит голая... Даже не верится, что у этой конфетки трое детей... В жизни бы в такое не поверил!" nointeract
        elif pose3_1 == '02':
            Max_07 "О, да! Какая у мамы голая попка! Всё-таки хорошо, что здесь так жарко и все спят не укрываясь... Просто супер!" nointeract
        elif True:
            Max_04 "Обалденно! Как же повезло, что у меня такая горячая мама... Голой она выглядит потрясающе, аж глаза отрывать не хочется!" nointeract
        $ rez = renpy.display_menu([(_("{i}прокрасться в комнату{/i}"), 'sneak'), (_("{i}уйти{/i}"), 'exit')])
        if rez != 'exit':
            $ spent_time += 10
            jump eric_ann_sleep.not_eric_closer
        elif True:
            jump eric_ann_sleep.end

    label eric_ann_sleep.not_eric_closer:

        scene BG char Ann bed-night-02
        $ renpy.show('Ann sleep-night-closer '+pose3_3+ann.dress)
        $ prenoted = 2
        if pose3_1 == '01':
            Max_03 "Чёрт, у меня самая аппетитная мама на свете! Я бы с огромным удовольствием пораспускал с ней руки... Но лучше потихоньку уходить, пока она не проснулась." nointeract
        elif pose3_1 == '02':
            Max_02 "Ухх! Так и хочется прижаться к этой обворожительной голой попке и шалить всю ночь... Но пора уходить, а то она может проснуться." nointeract
        elif True:
            Max_05 "Вот это да! От вида этих раздвинутых ножек становится всё равно, что она моя мама... Слишком соблазнительная у неё киска! Только бы она сейчас не проснулась..." nointeract
        $ rez = renpy.display_menu([(_("{i}уйти{/i}"), 'exit')])
        if rez != 'exit':
            jump eric_ann_sleep.end

    label eric_ann_sleep.end:
        $ spent_time = 10
        jump Waiting


label eric_ann_shower:
    scene location house bathroom door-morning
    if ann.daily.shower != 0:
        return

    $ ann.daily.shower = 1
    $ spent_time += 10
    menu:
        Max_00 "Похоже, мама вместе с Эриком принимают душ... Или что они там ещё могут делать?"
        "{i}заглянуть со двора{/i}" if True:
            jump eric_ann_shower.start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump eric_ann_shower.ladder
        "{i}уйти{/i}" if True:
            return

    label eric_ann_shower.ladder:
        $ eric.flags.ladder += 1
        $ ann.flags.ladder += 1
        $ spent_time += 20
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        $ fuck_scene = renpy.random.choice([6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6])

        scene BG bathroom-morning-00
        if fuck_scene == 4:
            show Eric bath-window-morning 02a
        elif True:
            $ renpy.show('Eric bath-window-morning 0'+str(fuck_scene)+'a')
        show FG bathroom-morning-00
        $ Skill('hide', 0.05)
        $ spent_time += 30
        Max_07 "Охх... Боже мой, какие нежности. Похоже, сейчас что-то начнётся..."

        if fuck_scene == 1:
            show Eric bath-window-morning 01b
            Max_10 "Моя мама снова отсасывает этому... Эрику! Да с такой страстью! Ей что, действительно так нравится это делать или она его настолько любит? Хотя о втором мне даже думать не хочется..."
            show Eric bath-window-morning 01c
            Max_09 "Вот чёрт! Эрик кончает маме прямо на лицо, как в каком-то порно! Причём, ей это настолько нравится, что она улыбается и ловит его сперму своим ртом! Неужели она настолько развратна?!"
        elif fuck_scene == 2:
            show Eric bath-window-morning 02b
            Max_09 "Да уж, устроился Эрик хорошо... Мама отсасывает ему с таким наслаждением, аж оторваться не может! Неужели ей действительно нравится сосать этот его огрызок?!"
            show Eric bath-window-morning 02c
            jump eric_ann_shower.fin2
        elif fuck_scene == 3:
            show Eric bath-window-morning 03b
            Max_09 "Вау! С какой же страстью мама отсасывает Эрику... А ему, похоже, этого даже мало и он пытается засадить свой член поглубже ей в рот... Почему она ему это позволяет, ей что, нравится подчиняться?"
            show Eric bath-window-morning 03c
            jump eric_ann_shower.fin1
        elif fuck_scene == 4:
            show Eric bath-window-morning 04b
            Max_08 "О Боже! Как бы я мечтал оказаться на месте это счастливого ублюдка! И всё равно, что она - моя мама... Когда её мокрая попка так красиво скачет на члене, голова начинает идти кругом!"
            show Eric bath-window-morning 02c
            jump eric_ann_shower.fin2
        elif fuck_scene == 5:
            show Eric bath-window-morning 05b
            Max_10 "Ничего себе! Вот это они вытворяют! Эрик трахает маму, разложив её у зеркала как какую-то шлюшку, а она ещё при этом ласкает свою и без того влажную киску... Да уж, только бы со стремянки не упасть от такого зрелища!"
            show Eric bath-window-morning 03c
            jump eric_ann_shower.fin1
        elif True:
            scene BG bathroom-morning-00
            show AnimAnnEric2
            show FG bathroom-morning-00
            Max_10 "Ого! Эрик долбит маму сзади с такой силой, что через стекло даже слышны шлепки о её попку! Похоже, она еле сдерживается, чтобы не кричать слишком громко..."
            hide AnimAnnEric2
            show Eric bath-window-morning 03c
            jump eric_ann_shower.fin1
        jump eric_ann_shower.end

    label eric_ann_shower.fin1:
        Max_08 "Чёрт возьми! Она приняла всю его сперму себе в рот и на лицо, и теперь с такой жадностью и удовольствием слизывает её с его члена... Охх... мама, а ведь ты та ещё развратница!"
        jump eric_ann_shower.end

    label eric_ann_shower.fin2:
        Max_10 "А вот и финал не заставил себя ждать! Эрик обкончал маме всё лицо и грудь, и она, похоже, очень довольна... улыбается... Охх... какая же она горячая и развратная!"
        jump eric_ann_shower.end

    label eric_ann_shower.end:
        Max_00 "Хоть и не хочется, но пока меня не заметили, лучше уходить..."
        if eric.flags.ladder > 1 and house[3].cams and house[3].max_cam<2:
            $ house[3].max_cam = 2
            Max_09 "Кстати, они здесь во всю развлекаются и совершенно не попадают под ракурс моей камеры в ванной! Похоже, мне стоит установить ещё одну камеру, чтобы мои зрители видели всю происходящую здесь картину..."

        $ current_room = house[6]
        jump Waiting

    label eric_ann_shower.start_peeping:
        $ Skill('hide', 0.03)
        $ _m1_eric__r1 = renpy.random.choice(['01', '02', '03'])
        $ _ch1 = GetChance(mgg.stealth, 3, 900)
        $ _ch2 = GetChance(mgg.stealth, 2, 900)
        $ renpy.scene()
        $ renpy.show('Eric shower '+ _m1_eric__r1)
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Вот это да... Похоже намечается что-то большее, чем просто принять душ! Боюсь даже представить, что будет, если меня поймают, пока я подглядываю... за этим..."
            "{i}продолжить смотреть\n{color=[_ch1.col]}(Скрытность. Шанс: [_ch1.vis]){/color}{/i}" if True:
                jump eric_ann_shower.closer_peepeng
            "{i}взглянуть со стороны\n{color=[_ch2.col]}(Скрытность. Шанс: [_ch2.vis]){/color}{/i}" if True:
                jump eric_ann_shower.alt_peepeng
            "{i}уйти{/i}" if True:
                jump Waiting
    label eric_ann_shower.alt_peepeng:
        $ spent_time += 10
        if _m1_eric__r1 == '01':
            $ _m1_eric__r2 = renpy.random.choice(['01', '02', '03'])
        elif _m1_eric__r1 == '02':
            $ _m1_eric__r2 = renpy.random.choice(['05', '06'])
        elif True:
            $ _m1_eric__r2 = renpy.random.choice(['04', '07'])
        if not RandomChance(_ch2.ch) and flags.voy_stage<1:
            jump eric_ann_shower.not_luck
        $ Skill('hide', 0.2)
        $ ann.dress_inf = '00a'
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Eric shower-alt '+str(_m1_eric__r2))
        show FG shower-water
        if _m1_eric__r2 == '01':
            Max_10 "[undetect!t]Моя мама снова отсасывает этому... Эрику! Да с такой страстью! Ей что, действительно так нравится это делать или она его настолько любит? Хотя о втором мне даже думать не хочется..." nointeract
        elif _m1_eric__r2 == '02':
            Max_09 "[undetect!t]Да уж, устроился Эрик хорошо... Мама отсасывает ему с таким наслаждением, аж оторваться не может! Неужели ей действительно нравится сосать этот его огрызок?!" nointeract
        elif _m1_eric__r2 in ['03', '04']:
            Max_04 "[undetect!t]Охх... Вот же Эрику повезло... Ведь у мамы такие нежные и ласковые руки! Уже только от одного вида её совершенно голого и мокрого тела можно кончить..." nointeract
        elif _m1_eric__r2 == '05':
            Max_06 "[undetect!t]Охренеть! Вот это страсть! Кажется, они так увлечены друг другом, что им всё равно, увидит их кто-то или нет... И похоже, маме это очень нравится!" nointeract
        elif True:
            Max_05 "[undetect!t]Ого! Эрик трахает маму сзади, да так активно... И... кажется, ей это очень нравится, она даже двигается ему навстречу... и изнывает от страсти!" nointeract
        $ rez = renpy.display_menu([(_("{i}смотреть до конца{/i}"), 'sneak'), (_("{i}уйти{/i}"), 'exit')])
        if rez == 'exit':
            $ current_room = house[6]
            jump Waiting

        $ spent_time += 10
        $ renpy.show('Eric shower-alt '+str(_m1_eric__r2)+'a')
        if _m1_eric__r2 in ['01', '02']:
            Max_09 "Вот чёрт! Эрик кончает маме прямо на лицо, как в каком-то порно! Причём, ей это настолько нравится, что она улыбается и ловит его сперму своим ртом! Неужели она настолько развратна?!" nointeract
        elif _m1_eric__r2 in ['03', '04']:
            Max_01 "Ну да! Кто бы сомневался, что Эрик не продержится слишком долго. Мама своё дело знает! Ладно, надо сматываться, пока они меня не заметили!" nointeract
        elif _m1_eric__r2 == '05':
            Max_07 "Ох, чёрт... Эрик уже кончил... Хорошо, что не в маму... Счастливый сукин сын... И она ещё улыбается?! Пора бы мне уходить, а то ещё заметят..." nointeract
        elif True:
            Max_08 "Чёрт возьми... он уже кончил... Счастливый ублюдок... забрызгал маме всю спину с попкой своей спермой! Нужно уходить, а то они вот-вот меня заметят..." nointeract
        $ rez = renpy.display_menu([(_("{i}уйти{/i}"), 'exit')])
        $ current_room = house[6]
        jump Waiting

    label eric_ann_shower.closer_peepeng:
        $ spent_time += 10
        if _m1_eric__r1 == '01':
            $ _m1_eric__r2 = renpy.random.choice(['01', '02', '03'])
        elif _m1_eric__r1 == '02':
            $ _m1_eric__r2 = renpy.random.choice(['04', '05'])
        elif True:
            $ _m1_eric__r2 = renpy.random.choice(['06', '07'])
        if not RandomChance(_ch1.ch) and flags.voy_stage<1:
            jump eric_ann_shower.not_luck

        $ Skill('hide', 0.2)
        $ ann.dress_inf = '00a'
        scene BG shower-closer
        $ renpy.show('Eric shower-closer '+_m1_eric__r2)
        show FG shower-closer
        if _m1_eric__r1 == '01':
            Max_04 "[undetect!t]Охх... Вот же Эрику повезло... Ведь у мамы такие нежные и ласковые руки! Уже только от одного вида её совершенно голого и мокрого тела можно кончить..." nointeract
        elif _m1_eric__r1 == '02':
            Max_06 "[undetect!t]Охренеть! Вот это страсть! Кажется, они так увлечены друг другом, что им всё равно, увидит их кто-то или нет... И похоже, маме это очень нравится!" nointeract
        elif True:
            Max_05 "[undetect!t]Ого! Эрик трахает маму сзади, да так активно... И... кажется, ей это очень нравится, она даже двигается ему навстречу... и изнывает от страсти!" nointeract
        $ rez = renpy.display_menu([(_("{i}смотреть до конца{/i}"), 'sneak'), (_("{i}уйти{/i}"), 'exit')])
        if rez == 'exit':
            $ current_room = house[6]
            jump Waiting

        $ spent_time += 10
        $ renpy.show('Eric shower-closer '+_m1_eric__r2+'a')
        if _m1_eric__r1 == '01':
            Max_01 "Ну да! Кто бы сомневался, что Эрик не продержится слишком долго. Мама своё дело знает! Ладно, надо сматываться, пока они меня не заметили!" nointeract
        elif _m1_eric__r1 == '02':
            Max_07 "Ох, чёрт... Эрик уже кончил... Хорошо, что не в маму... Счастливый сукин сын... И она ещё улыбается?! Пора бы мне уходить, а то ещё заметят..." nointeract
        elif True:
            Max_08 "Чёрт возьми... он уже кончил... Счастливый ублюдок... забрызгал маме всю спину с попкой своей спермой! Нужно уходить, а то они вот-вот меня заметят..." nointeract
        $ rez = renpy.display_menu([(_("{i}уйти{/i}"), 'exit')])
        $ current_room = house[6]
        jump Waiting

    label eric_ann_shower.not_luck:
        scene BG shower-closer
        if _m1_eric__r1 == '01':
            show Eric shower-closer seen01
        elif True:
            show Eric shower-closer seen02
        show FG shower-closer
        $ Skill('hide', 0.01)
        Ann_15 "[spotted!t]Макс?! Ты какого чёрта здесь делаешь? Подглядывал за нами?! Сегодня будешь наказан! А ну быстро убирайся!"
        $ punreason[3] = 1
        $ current_room = house[6]
        jump Waiting


label sexed_lisa:
    scene location house annroom door-night
    if eric.daily.sex_ed > 0:
        return

    $ eric.daily.sex_ed = 1

    if flags.lisa_sexed < 0:
        if house[2].cams:
            menu:
                Max_09 "{i}( Интересно, зачем мама позвала Лизу в комнату? А там ведь ещё и Эрик. Может хоть через камеру посмотреть, что там происходит? ){/i}"
                "{i}посмотреть через камеру{/i}" if True:
                    $ create_cam_list()
                    $ current_room = house[0]
                    $ _m1_eric__cam = 1 if house[0].cams else 0
                    if house[1].cams:
                        $ _m1_eric__cam += 1
                    $ view_cam = (house[2], house[2].cams[0], 0, house, _m1_eric__cam)
                    $ at_comp = True
                    jump Waiting
                "{i}уйти{/i}" if True:

                    return
        elif True:
            menu:
                Max_09 "{i}( Интересно, зачем мама позвала Лизу в комнату? А там ведь ещё Эрик. Если бы я установил камеру в этой комнате, то сейчас смог бы всё увидеть, а так придётся ждать, пока Лиза вернётся, чтобы всё узнать. ){/i}"
                "{i}уйти{/i}" if True:
                    return
    elif True:

        if GetRelMax('eric')[0]>0:

            menu:
                Max_07 "{i}( Эрик сказал, что всё устроит так, чтобы меня не заметили, когда я буду подглядывать. Сейчас посмотрим... ){/i}"
                "{i}заглянуть в окно{/i}" if True:
                    if flags.lisa_sexed == 0:
                        jump sexed_lisa.lesson_0
                    elif flags.lisa_sexed == 1:
                        jump sexed_lisa.lesson_1
                    elif flags.lisa_sexed == 2:
                        jump sexed_lisa.lesson_2
                    elif flags.lisa_sexed == 3:
                        jump sexed_lisa.lesson_3
        elif True:

            if house[2].cams:
                menu:
                    Max_09 "{i}( Интересно, чем они там с Лизой занимаются?! Можно бы было попробовать подглядеть через окно, но не стоит давать Эрику шанс меня унизить или ещё чего хуже. Лучше посмотреть через камеру... ){/i}"
                    "{i}посмотреть через камеру{/i}" if True:
                        $ create_cam_list()
                        $ current_room = house[0]
                        $ _m1_eric__cam = 1 if house[0].cams else 0
                        if house[1].cams:
                            $ _m1_eric__cam += 1
                        $ view_cam = (house[2], house[2].cams[0], 0, house, _m1_eric__cam)
                        $ at_comp = True
                        jump Waiting
                    "{i}уйти{/i}" if True:

                        return
            elif True:

                menu:
                    Max_09 "{i}( Интересно, чем они там с Лизой занимаются?! Можно бы было попробовать подглядеть через окно, но не стоит давать Эрику шанс меня унизить или ещё чего хуже. Придётся ждать, пока Лиза вернётся и расскажет сама, хотя не лишним и будет камеру в мамину комнату поставить. ){/i}"
                    "{i}уйти{/i}" if True:
                        return

    label sexed_lisa.lesson_0:

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 01-01'+eric.dress)
        $ renpy.show('Lisa sexed 01'+lisa.dress)
        show Max Lisa-sexed 01

        Max_01 "{i}( Отлично! Мне как раз всё видно в зеркале. Посмотрим, чему мою сестрёнку будут учить эти извращенцы... ){/i}"
        Eric_01 "... Рано или поздно у тебя появится парень и тебе нужно знать, как доставить ему удовольствие руками. Но это если вы с ним настроены на серьёзные отношения!"
        Ann_12 "Да, Лиза, вы должны естественно к этому прийти, не нужно с этим торопиться и уж тем более, чтобы тебя к этому принуждали."

        scene BG char Eric sexed-talk
        $ renpy.show('Eric sexed talk-01'+eric.dress)
        $ renpy.show('Lisa sexed talk-01'+lisa.dress)

        Lisa_01 "Конечно, мам, на какие же ещё отношения я могу быть настроена... Итак, что и как надо делать руками?"
        Eric_02 "Давай я встану, Ань, чтобы Лизе было всё хорошо видно..."

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-01'+eric.dress)
        $ renpy.show('Lisa sexed 02'+lisa.dress)
        show Max Lisa-sexed 01

        Ann_02 "Конечно, дорогой. Вот, Лиза, смотри... Нужно взять член крепко, но нежно и делать вот так... Если почувствуешь, что не хватает смазки, можешь использовать слюну или масло..."
        Lisa_02 "Мам, а как понять, что всё происходит как надо?"
        Ann_05 "Ты поймёшь, дорогая. Сразу поймёшь... А может быть твой избранник даже будет подсказывать тебе, как ему больше нравится."
        Max_08 "{i}( Офигеть, что творят! Мама надрачивает Эрику прямо на глазах у Лизы, которую она так всё время оберегала. Да, хорошо Эрик над ней поработал... ){/i}"

        scene BG char Eric sexed-hj
        $ renpy.show('Eric sexed hj-01'+eric.dress)
        $ renpy.show('Lisa sexed hj-01'+lisa.dress)

        Lisa_03 "Со стороны всё выглядит довольно просто или это не так?"
        Ann_07 "Ну, Лиза, я уже делала это много раз, поэтому и выглядит это очень просто, но здесь нужно чувствовать своего партнёра. У тебя ещё это всё впереди, когда придёт время..."
        Lisa_09 "Надеюсь, я при этом ничего не испорчу..."
        Eric_03 "О, Лиза, это вряд ли! Уже просто лёгкое прикосновение женской руки к мужскому члену очень возбуждает. Всё можно испортить, если ты начнёшь это делать грубо и бесчувственно, но ты точно не такая. Всё у тебя получится, не сомневайся!"
        Lisa_10 "Ой, так я делать не буду!"
        Max_02 "{i}( Да, как же классно бы было, если бы моя младшая сестрёнка запустила свои нежные ручки в мои шорты и неспеша поласкала мой член... Ухх! ){/i}"

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 01-02'+eric.dress)
        $ renpy.show('Lisa sexed 01'+lisa.dress)
        show Max Lisa-sexed 01

        Ann_04 "Ты у меня умница, дочка. Ладно, ступай, на сегодня я думаю достаточно. Через неделю продолжим..."
        Lisa_02 "Мам, а что будет в следующий раз?"
        Ann_01 "Ну, нам с Эриком есть, что тебе ещё показать и рассказать. Но это в следующий раз..."
        Max_07 "{i}( О, пора мне валить к себе... ){/i}"

        jump sexed_lisa.end

    label sexed_lisa.lesson_1:

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 01-02'+eric.dress)
        $ renpy.show('Lisa sexed 01'+lisa.dress)
        show Max Lisa-sexed 01

        Max_01 "{i}( Посмотрим, чему мою сестрёнку будут сегодня учить... ){/i}"
        Ann_02 "... Как правильно стимулировать мужской член рукой я тебе показала. Теперь покажу тебе довольно безобидный и эффективный способ ещё больше возбудить мужчину..."
        Lisa_01 "Это будет какая-то хитрая техника?"

        scene BG char Eric sexed-talk
        $ renpy.show('Eric sexed talk-02'+eric.dress)
        $ renpy.show('Lisa sexed talk-01'+lisa.dress)

        Ann_04 "Ну, на технику это не тянет, скорее... очень приятное дополнение к ласкам."
        Eric_02 "Давай я встану, Ань, чтобы Лизе было всё хорошо видно... Да и мне тоже."

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-01'+eric.dress)
        $ renpy.show('Lisa sexed 02'+lisa.dress)
        show Max Lisa-sexed 01

        Ann_05 "Мужчин очень заводит, когда женщина раздевается, так что в дополнение к ласкам можно обнажить грудь, это точно понравится твоему избраннику."
        Max_03 "{i}( О да, мам! Мне бы очень понравилось, если бы ты подрочила мне обнажив свою сочную и упругую грудь... ){/i}"

        scene BG char Eric sexed-hj
        $ renpy.show('Eric sexed hj-01'+eric.dress)
        $ renpy.show('Lisa sexed hj-01'+lisa.dress)

        Lisa_02 "А, ну это я делать умею..."
        Ann_15 "В каком это смысле умеешь?! Ты что, уже кому-то показывала свою грудь? Признавайся!"
        Lisa_10 "Ой, нет, я имела ввиду, что одеваться-раздеваться я умею, каждый день это делаю."

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-02'+eric.dress)
        $ renpy.show('Lisa sexed 02'+lisa.dress)
        show Max Lisa-sexed 01

        Ann_08 "Смотри мне, Лиза! Вот... Такая мелочь, дочка, а мужчине приятно..."
        Lisa_09 "Мам, твоя грудь - уж точно не мелочь! У меня поменьше будет..."
        Ann_02 "Не переживай из-за этого, тебе ещё расти и расти."
        Max_04 "{i}( Как по мне, а грудь у Лизы весьма симпатичная. Не сравнится с маминой, но они все хороши, по-своему... ){/i}"

        scene BG char Eric sexed-hj
        $ renpy.show('Eric sexed hj-02'+eric.dress)
        $ renpy.show('Lisa sexed hj-01'+lisa.dress)

        Lisa_02 "Значит, достаточно просто обнажить грудь и всё?"
        Ann_05 "Ну... можно ещё немного подразнить своего партнёра и поводить его членом по своей груди. Он уж точно от этого не откажется..."
        Eric_05 "А если размеры груди позволяют, то некоторые могут стимулировать член и без рук, верно Ань?"
        Ann_01 "Я думаю, сегодня Лиза и без этого увидела и узнала достаточно. Так что продолжим мы через неделю."

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-01'+eric.dress)
        $ renpy.show('Lisa sexed 02'+lisa.dress)
        show Max Lisa-sexed 01

        Lisa_01 "Конечно, мам. С интересом буду ждать следующего урока..."
        Max_07 "{i}( С интересом... Да уж, а ещё меня называют в этом доме извращенцем! Хотя, если бы не Эрик... ){/i}"

        jump sexed_lisa.end

    label sexed_lisa.lesson_2:

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 01-02'+eric.dress)
        $ renpy.show('Lisa sexed 01'+lisa.dress)
        show Max Lisa-sexed 01

        Max_01 "{i}( Посмотрим, чему мою сестрёнку будут сегодня учить... ){/i}"
        Ann_02 "... В дополнение к тому, что ты уже видела, не стоит забывать и ещё кое о чём. Дорогой, встань. Так Лизе будет лучше видно..."
        Eric_01 "Конечно, Ань, сейчас."

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-02'+eric.dress)
        $ renpy.show('Lisa sexed 02'+lisa.dress)
        show Max Lisa-sexed 01

        Ann_04 "Так вот, Лиза, во время стимуляции члена можно ещё ласкать яички. Делать это нужно нежно и аккуратно."
        Lisa_10 "Как много всяких нюансов..."
        Ann_05 "Как и в любом процессе. Если знаешь как и к чему прикасаться, то принесёшь массу удовольствия мужчине. Вот, посмотри..."

        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-03'+eric.dress)
        $ renpy.show('Lisa sexed 02'+lisa.dress)
        show Max Lisa-sexed 01

        Lisa_02 "Значит, всё делать так же как и с членом?"
        Ann_07 "Да, разве что член нужно держать крепко, а вот яичкам достаточно лёгких прикосновений, чтобы мужчине стало невероятно хорошо. Так ведь, дорогой?"
        Eric_07 "О да! Невероятно хорошо - это твоя мама верно сказала... Кажется, она всего лишь легонько водит по ним своими пальчиками, но ощущения... непередаваемые..."

        scene BG char Eric sexed-hj
        $ renpy.show('Eric sexed hj-03'+eric.dress)
        $ renpy.show('Lisa sexed hj-01'+lisa.dress)

        Max_10 "{i}( Эй! Я тоже хочу, чтобы мне яички ласкали! Судя по млеющей физиономии Эрика - это как минимум очень блаженно. ){/i}"
        Lisa_03 "Круто! А как долго это всё надо делать?"
        Ann_08 "А об этом мы поговорим уже на следующем уроке, дочка. Заодно и пробежимся ещё раз по всем моментам, которые я тебе показывала. Не хочется, чтобы я тут напрасно распиналась."
        Lisa_10 "Ну хорошо. А я надеялась, что хоть здесь экзаменов не будет."
        Ann_04 "Тут ничего сложного нет. Так что не волнуйся."
        Max_07 "{i}( Экзамен... Тянет на какую-то ролевую игру. Хорошо хоть без костюмов! Хотя маму я бы не прочь увидеть в строгом, но сексуальном костюме... ){/i}"

        jump sexed_lisa.end

    label sexed_lisa.lesson_3:


        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 01-01'+eric.dress)
        $ renpy.show('Lisa sexed 01'+lisa.dress)
        show Max Lisa-sexed 01
        Max_01 "{i}( И чему же мою сестрёнку будут сегодня учить... ){/i}"
        Ann_02 "... Посмотрим, всё ли ты усвоила из наших уроков. Что и как мне нужно сделать, чтобы доставить мужчине удовольствие?"
        Lisa_10 "Ой, мам, сейчас... Так... Нужно взять его член крепко, но нежно и ласкать, да?"


        $ renpy.show('Eric sexed 01-02'+eric.dress)
        Ann_04 "Верно, дорогая. Я снова покажу всё ещё раз, чтобы мы этот этап стимулирования мужского члена руками закончили и могли двигаться дальше."
        Lisa_11 "А будет что-то ещё?! Ещё уроки?"
        Ann_05 "Да, дочка. Это не единственный способ доставить мужчине удовольствие."
        Lisa_02 "А как ещё?"


        $ renpy.show('Eric sexed 02-01'+eric.dress)
        Max_08 "{i}( Мама что, и отсасывать собирается Эрику при Лизе?! Да нет... Хотя, уже можно не удивляться чему-то такому... ){/i}"
        Ann_12 "Лиза, не сегодня. Сегодня у нас что?"
        Lisa_09 "Да, я поняла, закрепление пройденного материала."


        scene BG char Eric sexed-hj
        $ renpy.show('Eric sexed hj-01'+eric.dress)
        $ renpy.show('Lisa sexed hj-01'+lisa.dress)
        Ann_07 "Вот и славно. Как я могу ещё больше возбудить мужчину во время стимуляции руками?"
        Lisa_01 "Можно обнажить грудь! Я это помню..."


        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-02'+eric.dress)
        $ renpy.show('Lisa sexed 01'+lisa.dress)
        show Max Lisa-sexed 01
        Ann_08 "Верно. Поводить его членом по своей груди тоже будет не лишним."
        Lisa_10 "Ой, забыла. Точно, ты говорила о том, чтобы немного подразнить этим мужчину."


        scene BG char Eric sexed-hj
        $ renpy.show('Eric sexed hj-02'+eric.dress)
        $ renpy.show('Lisa sexed hj-01'+lisa.dress)
        Ann_02 "Что ещё мы можем делать?"
        Lisa_02 "Сейчас... Ах да, ласкать яички!"


        scene BG char Eric sexed-annroom-01
        $ renpy.show('Eric sexed 02-03'+eric.dress)
        $ renpy.show('Lisa sexed 01'+lisa.dress)
        show Max Lisa-sexed 01
        Ann_04 "И как надо это делать?"
        Lisa_10 "Эээ... Нежно и аккуратно. Легонько массировать... Верно, мам?"


        scene BG char Eric sexed-hj
        $ renpy.show('Eric sexed hj-03'+eric.dress)
        $ renpy.show('Lisa sexed hj-01'+lisa.dress)
        Ann_05 "Верно, моя дорогая. Ты спрашивала в прошлый раз, как долго это нужно делать. Так вот, этой стимуляцией мужчину нужно довести до оргазма, когда он кончает от наслаждения."
        Lisa_03 "О, это как?!"
        Ann_07 "Уже скоро увидишь. Довести мужчину до оргазма не сложно, не то что нас, женщин. Эрик, сегодня нужно показать Лизе как мужчины кончают, так что не сдерживайся..."
        Eric_04 "Да, я уже близок к этому... Давай, детка, поработай немного быстрее и жёстче. О да... То, что надо..."


        $ renpy.show('Eric sexed hj-04'+eric.dress)
        Max_10 "{i}( Эй, вы там на мою сестрёнку только не попадите! Ладно вы люди взрослые, но при Лизе то поаккуратнее будьте... ){/i}"
        Ann_06 "Вот так, Лиза, мужчины и кончают... Лучше при себе иметь влажные салфетки, чтобы привести всё в порядок после этого."
        Lisa_13 "Да уж, а никак нельзя избежать этого... беспорядка?"
        Ann_14 "Ну, куда бы мужчина не кончил, всё равно придётся прибраться за собой. Можно ещё конечно... Может ей ещё рано знать о таком, дорогой?"
        Eric_06 "О том, что можно принять всю сперму в рот и проглотить? Что ты, я думаю это самый подходящий момент!"


        scene BG char Eric sexed-talk
        $ renpy.show('Eric sexed talk-01'+eric.dress)
        $ renpy.show('Lisa sexed talk-01'+lisa.dress)
        Lisa_11 "В рот?! И проглотить! Ой, фу-фу-фу! Нет, уж лучше салфетки, потому что это даже звучит противно..."
        Ann_01 "Пожалуй, я с тобой соглашусь, дочка. По крайней мере, пока в твоей жизни не появится особенный мужчина."
        Lisa_13 "Всё равно, выглядит и звучит это всё ну так себе, если не сказать похуже!"
        Eric_02 "Зато, теперь ты знаешь, как оно всё есть без прикрас. И теперь ты готова к дальнейшим урокам..."
        Ann_13 "Эрик, давай не спешить, пусть у неё это хоть осядет в голове. И вообще, лучше всё ещё раз обсудить, прежде чем показывать ей такое."
        Lisa_02 "А о чём таком вы говорите?"
        Ann_12 "Давай не сейчас. Ступай к себе, на сегодня достаточно. Мы тебе скажем, если решим продолжить эти... уроки."
        Lisa_09 "Мам, ты сказала, что мальчикам сложнее сделать нам приятно там внизу, да? А почему?"
        Eric_09 "Хватит на сегодня вопросов. Давай беги к себе, Лиза. У взрослых ещё есть дела."
        Lisa_01 "Хорошо. Ну, я побежала..."

        jump sexed_lisa.end

    label sexed_lisa.end:
        $ renpy.end_replay()
        $ current_room = house[0]
        $ spent_time = 30
        jump Waiting


label first_jerk_balkon:
    scene Eric jerk off 01
    Max_09 "Опа, Эрик! Что это он там делает, дрочит что ли? Да... Ого! Эрик стоит посреди ночи и дрочит на спящую Алису! А я и не знал, что Эрик любитель такого..."
    menu:
        Max_03 "Может, мне стоит сфотографировать его по-тихому в следующий раз?! Так, на всякий случай..."
        "{i}уйти{/i}" if True:
            $ flags.eric_noticed = True
    $ eric.stat.mast += 1
    $ poss['discrediting'].open(0)
    $ spent_time += 10
    jump Waiting


label first_jerk_yard:

    scene Eric jerk off 00
    menu:
        Max_07 "Опа, Эрик! Что это он делает среди ночи у окна Алисы?!"
        "{i}Осторожно подсмотреть за ним с балкона{/i}" if True:
            pass

    scene Eric jerk off 01
    Max_09 "Вот и он! Что это он там делает, дрочит что ли? Да... Ого! Эрик стоит посреди ночи и дрочит на спящую Алису! А я и не знал, что Эрик любитель такого..."
    menu:
        Max_03 "Может, мне стоит сфотографировать его по-тихому в следующий раз?! Так, на всякий случай..."
        "{i}уйти{/i}" if True:
            $ flags.eric_noticed = True
    $ eric.stat.mast += 1
    $ poss['discrediting'].open(0)
    $ spent_time += 10
    jump Waiting


label jerk_balkon:


    $ _ch1 = Chance(500)
    if not eric.stat.mast:
        jump first_jerk_balkon

    $ eric.stat.mast += 1
    if not alice.sleepnaked:
        $ flags.eric_noticed = True
        scene Eric jerk off 01
        menu:
            Max_07 "Эрик всё дрочит на Алису! И не лень ему вставать среди ночи для этого?!"
            "{i}сбегать за фотоаппаратом и пойти на балкон {color=[_ch1.col]}(Удача. Шанс: [_ch1.vis]){/color}{/i}" if flags.eric_photo1 < 1:
                jump jerk_photohant1
            "{i}уйти{/i}" if True:
                jump Waiting
    elif True:

        $ poss['discrediting'].open(2)
        scene BG char Alice bed-night-01
        $ renpy.show('Alice sleep-night '+pose3_2)
        show Eric jerk off 02
        menu:
            Max_03 "Ага, Эрик здесь! Не устоял перед голой Алисой и дрочит прямо посреди её комнаты... Вот же грязное животное!"
            "{i}сбегать за фотоаппаратом и вернуться {color=[_ch1.col]}(Удача. Шанс: [_ch1.vis]){/color}{/i}" if flags.eric_photo2 < 1:
                jump jerk_photohant2
            "{i}уйти{/i}" if True:
                jump Waiting


















label jerk_yard:

    scene Eric jerk off 00
    if not eric.stat.mast:
        jump first_jerk_yard

    $ _ch1 = Chance(500)
    $ flags.eric_noticed = True
    $ eric.stat.mast += 1
    menu:
        Max_07 "Эрик всё дрочит на Алису! И не лень ему вставать среди ночи для этого?!"
        "{i}сбегать за фотоаппаратом и пойти на балкон {color=[_ch1.col]}(Удача. Шанс: [_ch1.vis]){/color}{/i}" if flags.eric_photo1 < 1:
            jump jerk_photohant1
        "{i}уйти{/i}" if True:

            jump Waiting


label jerk_photohant1:

    if RandomChance(500):


        scene Eric jerk off 01
        menu:
            Max_09 "Вот и он! Всё ещё дрочит... Да так жёско! Смотри, шышку не сотри... Хотя нет, лучше стирай!"
            "{i}сфотографировать его{/i}" if True:
                pass

        show FG photocamera
        play sound "<from 1>audio/PhotoshootSound.ogg"
        Max_02 "О да! Такой отвратительный снимок явно может стать полезным для меня. Конечно, если правильно его использовать..."
        hide FG
        menu:
            Max_09 "А если попробовать загнать Эрика в комнату Алисы?! Тогда бы у меня появился шанс сделать уже более определённый снимок, где видно на кого дрочит Эрик. Только вот как..."
            "{i}уйти{/i}" if True:
                $ poss['discrediting'].open(1)
                $ flags.eric_photo1 = 1
    elif True:


        scene BG char Alice bed-night-01
        $ renpy.show('Alice sleep-night '+pose3_2)
        if not alice.sleepnaked:
            $ renpy.show('other Alice sleep-night '+pose3_2+alice.dress)
        $ renpy.show('FG alice-voyeur-night-00'+mgg.dress)
        menu:
            Max_10 "Блин, пока я бегал, Эрик уже ушёл... Ну ничего, поймаю его в следующий раз..."
            "{i}уйти{/i}" if True:
                $ flags.eric_jerk = False

    $ spent_time += 20
    jump Waiting


label jerk_photohant2:

    if RandomChance(500) and prenoted < 2:


        scene BG char Alice bed-night-01
        $ renpy.show('Alice sleep-night '+pose3_2)
        show Eric jerk off 02
        show FG photocamera
        play sound "<from 1>audio/PhotoshootSound.ogg"
        menu:
            Max_05 "Вот ты и попался! С таким \"грязным\" снимком, в случае чего, уже всем всё будет понятно... Главное сейчас не попасться!"
            "{i}уйти{/i}" if True:
                $ flags.eric_photo2 = 1
                $ poss['discrediting'].open(3)
    elif True:


        scene BG char Alice bed-night-01
        $ renpy.show('Alice sleep-night '+pose3_2)
        $ renpy.show('FG alice-voyeur-night-00'+mgg.dress)
        menu:
            Max_10 "Блин, пока я бегал, Эрик уже ушёл... Ну ничего, поймаю его в следующий раз..."
            "{i}уйти{/i}" if True:
                $ flags.eric_jerk = False

    $ spent_time += 20
    jump Waiting
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
