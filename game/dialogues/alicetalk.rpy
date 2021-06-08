label AliceTalkStart:

    $ dial = TalkMenuItems()


    $ _m1_alicetalk__cur_plan = alice.get_plan()
    if _m1_alicetalk__cur_plan.talklabel is not None:
        call expression _m1_alicetalk__cur_plan.talklabel from _call_expression_1

    if len(dial) > 0:
        $ dial.append((_("{i}уйти{/i}"), "exit"))
    elif True:
        jump Waiting


    $ renpy.block_rollback()
    Alice_00 "Ну, Макс, чего надо?" nointeract

    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        $ _m1_alicetalk__mood = alice.GetMood()[0]
        if rez in gifts['alice']:
            if renpy.has_label(rez.label):
                call expression rez.label from _call_expression_2
        elif _m1_alicetalk__mood < talks[rez].mood:
            if _m1_alicetalk__mood < -2:
                jump Alice_badbadmood
            elif _m1_alicetalk__mood < 0:
                jump Alice_badmood
            elif True:
                jump Alice_normalmood
        elif talks[rez].kd_id != "" and talks[rez].kd_id in cooldown and not ItsTime(cooldown[talks[rez].kd_id]):
            jump Alice_cooldown
        elif renpy.has_label(talks[rez].label):
            call expression talks[rez].label from _call_expression_3
        jump AliceTalkStart

    jump Waiting


label Alice_badbadmood:
    menu:
        Alice_09 "Да пошёл ты! Не хочу тебя видеть даже!"
        "Ок..." if True:
            jump Waiting
        "Я хотел извиниться" if True:
            jump Alice_asksorry


label Alice_badmood:
    menu:
        Alice_09 "Макс, отвали! Я не хочу с тобой разговаривать."
        "Ок..." if True:
            jump Waiting
        "Я хотел извиниться" if True:
            jump Alice_asksorry


label Alice_asksorry:
    menu:
        Alice_13 "Хотел извиниться? Каким образом?"
        "Ты знаешь, я передумал..." if True:
            jump Waiting


label Alice_normalmood:
    menu:
        Alice_09 "Макс, давай не сейчас..."
        "Ок..." if True:
            jump Waiting


label Alice_cooldown:
    Alice_09 "Макс... Не сейчас."
    Max_00 "Ладно..."
    jump AfterWaiting


label wash_dishes_alice:
    $ alice.daily.dishes = 1
    menu:
        Alice_13 "Хочешь о посуде поговорить или пришёл помочь?"
        "Давай, я домою остальное" if True:
            menu:
                Alice_07 "Что это с тобой? Но я не откажусь. И... спасибо."
                "{i}мыть посуду{/i}" if True:
                    $ AddRelMood('alice', 10, 60, 2)
                    $ dishes_washed = True
                    $ spent_time = max((60 - int(tm[-2:])), 30)
                    scene BG crockery-morning-00
                    $ renpy.show("Max crockery-morning 01"+mgg.dress)
                    menu:
                        Max_11 "И почему здесь нет посудомоечной машины..."
                        "{i}закончить{/i}" if True:
                            $ cur_ratio = 2
                            jump Waiting
        "Нет, просто хотел поглазеть" if True:
            menu:
                Alice_09 "Знаешь что, вали отсюда, пока мокрой тряпкой по голове не получил!"
                "{i}уйти{/i}" if True:
                    $ spent_time = 10
                    jump Waiting


label talkblog1:
    if "blog" in cooldown:
        if ItsTime(cooldown['blog']):
            $ del cooldown['blog']
        elif True:
            jump Alice_cooldown

    menu:
        Alice_00 "А типа ты не знаешь? Позлорадствовать пришёл?"
        "Нет, хотел просто больше узнать" if True:
            menu:
                Alice_02 "Что, даже не начнёшь подкалывать? И что ты хотел узнать?"
                "Расскажи, что ты там делаешь" if True:
                    menu:
                        Alice_13 "Ну, пока наши вещи не пропали во время переезда, я показывала как наносить лак, как применять различные средства и делилась разными хитростями..."
                        "Хитростями? А откуда ты сама всё это узнала?" if True:
                            menu:
                                Alice_01 "Да у других таких же блогеров подсмотрела, конечно. Все так делают! Ну и сама в интернете разное читаю, изучаю..."
                                "Тема бьюти разве единственная?" if True:
                                    menu:
                                        Alice_00 "Нет, но мне это всё как-то по душе. Говорят, у человека лучше получается то, что нравится. А мне это нравится..."
                                        "Давай что-то придумаем вместе!" if True:
                                            jump talkblog1.together
                                        "Может быть, изменить твой блог?" if True:
                                            jump talkblog1.otherway
                                "Понятно. Ну, и что теперь?" if True:
                                    jump talkblog1.whatnow
                        "И что теперь без этих своих вещей делать будешь?" if True:
                            jump talkblog1.whatnow
                "Как планируешь развиваться?" if True:
                    menu:
                        Alice_00 "Развиваться? Шутишь? Все мои вещи, лаки, материалы и прочее было в том контейнере, который пропал. Теперь у меня нет ничего..."
                        "Что, совсем всё пропало?" if True:
                            menu:
                                Alice_13 "Совсем всё. У меня даже нет подходящей одежды, чтобы вести блог. Нельзя же постоянно быть в одной майке перед зрителями..."
                                "Может, это твоя фишка. Да и майка счастливая..." if True:
                                    menu:
                                        Alice_00 "Ага, потому что единственная, да? А ещё какая фишка? Нет материалов, нечего показывать?"
                                        "Да уж, грусть-печаль..." if True:
                                            jump talkblog1.sad
                                        "Тебе как-то можно помочь?" if True:
                                            jump talkblog1.help
                                "Разве это важно?" if True:
                                    menu:
                                        Alice_00 "Очень важно. Ну, ладно, чёрт с ней, с одеждой, а что мне в блоге показывать? Как себя правильно расчёсывать? У меня нет ничего..."
                                        "Да уж, грусть-печаль..." if True:
                                            jump talkblog1.sad
                                        "Тебе как-то можно помочь?" if True:
                                            jump talkblog1.help
                        "Постой, и что теперь будет?" if True:
                            jump talkblog1.whatnow
        "Много подписчиков уже?" if True:
            menu:
                Alice_13 "Да ты издеваешься, да?"
                "Нет. С чего ты взяла?" if True:
                    pass
                "Ты о чём, вообще?" if True:
                    pass
            menu talkblog1.no:
                Alice_00 "Типа ты не в курсе, что у нас пропала большая часть вещей во время переезда?"
                "Да ладно?" if True:
                    $ cooldown['blog'] = CooldownTime("03:00")
                    Alice_09 "Знаешь что, Макс, отвали!"
                    Max_00 "Ну и ладно..."
                    $ AddRelMood('alice', -5, -50)
                    jump talkblog1.end
                "В курсе, конечно" if True:
                    menu:
                        Alice_13 "Ну, вот среди тех вещей было всё, что я использовала для ведения своего блога. Одежда, различные лаки, кремы... вообще всё!"
                        "Мне очень жаль..." if True:
                            jump talkblog1.sad
                        "И как тебе помочь?" if True:
                            jump talkblog1.help
        "Заработала уже на нём что-то?" if True:
            menu:
                Alice_13 "Макс, тебе заняться нечем, кроме как меня доставать? Ты же знаешь, что у меня всё пропало!"
                "Что пропало? Ты о чём?" if True:
                    jump talkblog1.no
                "Ты о тех вещах во время переезда?" if True:
                    menu:
                        Alice_00 "Конечно! Там же было вообще всё, что мне нужно для ведения блога. Шмотки, мои любимые лаки, косметика... вообще всё!"
                        "Да, печально..." if True:
                            jump talkblog1.sad
                        "Тебе можно как-то помочь?" if True:
                            jump talkblog1.help
    menu talkblog1.sad:
        Alice_13 "Вот-вот... Надо было всё с собой брать, а не складывать в тот контейнер.."
        "Может быть, попробуем вместе найти решение?" if True:
            jump talkblog1.together
        "Я обязательно придумаю, что можно с этим сделать" if True:
            jump talkblog1.findout

    menu talkblog1.help:
        Alice_01 "Ты у нас внезапно стал миллионером? Или просто деньги появились? Самый простой способ - это купить недостающее. Ну, или найти то, что пропало"
        "Денег у меня нет..." if True:
            menu:
                Alice_13 "А без денег тут ничем не поможешь. Вообще, я в депрессии из-за всей этой истории. Вся жизнь перевернулась..."
                "Вся жизнь? Но это всё к лучшему же. Такой дом, бассейн, место отличное!" if True:
                    menu:
                        Alice_00 "Да, в этом плане ты прав, Макс. Но я хотела чего-то добиться. Стать известным блогером и заработать кучу денег. А теперь..."
                        "Давай что-то придумаем вместе!" if True:
                            jump talkblog1.together
                        "Ты всё ещё можешь. Может быть, просто смени формат блога" if True:
                            jump talkblog1.otherway
                "Не грусти. Могло быть и хуже" if True:
                    menu:
                        Alice_00 "Верно. Но всё равно, это всё очень грустно. Я даже не представляю, как теперь быть..."
                        "Давай что-то придумаем вместе!" if True:
                            jump talkblog1.together
                        "Ты всё ещё можешь. Может быть, просто смени формат блога" if True:
                            jump talkblog1.otherway
                "Может быть, зарабатывать на чём-то другом?" if True:
                    jump talkblog1.otherway
        "Я не детектив, чтобы искать вещи..." if True:
            menu:
                Alice_00 "А кто ты тогда? Чем же именно можешь помочь?"
                "Ну, у меня много разных идей" if True:
                    menu:
                        Alice_07 "Много разных идей? Например?"
                        "Давай что-то придумаем вместе!" if True:
                            jump talkblog1.together
                        "Может быть, изменить твой блог?" if True:
                            jump talkblog1.otherway
                "Советами!" if True:
                    menu:
                        Alice_06 "И кому уже помогли твои советы? Знаешь, советчиков много. Лучше бы что-то конкретное предложил..."
                        "Давай что-то придумаем вместе!" if True:
                            jump talkblog1.together
                        "Может быть, изменить твой блог?" if True:
                            jump talkblog1.otherway

    menu talkblog1.whatnow:
        Alice_00 "Не знаю, если честно. Мне даже показаться перед зрителями не в чем. Какой же я бьюти-блогер, если на мне всегда одна и та же одежда..."
        "Тебе как-то можно помочь?" if True:
            jump talkblog1.help
        "Может быть, заняться чем-то другим?" if True:
            jump talkblog1.otherway
        "Да уж, грусть-печаль..." if True:
            jump talkblog1.sad

    menu talkblog1.otherway:
        Alice_00 "Ты о чём? Есть какие-то мысли?"
        "Мы можем с тобой вместе что-то придумать" if True:
            jump talkblog1.together
        "Давай, я подумаю и, когда будут мысли, продолжим разговор" if True:
            jump talkblog1.findout
        "Пока нет, но я подумаю что можно сделать" if True:
            jump talkblog1.findout

    label talkblog1.together:
        $ alice.flags.crush = 2
        menu:
            Alice_14 "Вместе? Ещё ничего нет, а уже в партнёры набиваешься?"
            "Ну если придумаю что-то, то почему нет?" if True:
                Alice_01 "Ну, если придумаешь. Если. Да и смотря что... Сильно удаляться от этой темы не хочется. Но попробовать что-то новое можно... В общем, когда что-то придумаешь, тогда и поговорим..."
                Max_00 "Хорошо!"
            "Конечно! Будет у нас семейный бизнес!" if True:
                menu:
                    Alice_07 "Семейный бизнес? На моём блоге? Может ещё и сам вести будешь?"
                    "Ну да, многие так делают!" if True:
                        pass
                    "Нет, из меня ведущий так себе..." if True:
                        pass
                    "Попробовать то можем?" if True:
                        pass
                Alice_00 "Знаешь, мне кажется, что это всё пустые разговоры. Сначала что-то предложи, тогда и обсудим..."
                Max_00 "Хорошо, я подумаю"
            "Ну, можно попробовать же?" if True:
                Alice_00 "Попробовать можно, но сначала надо понять что. Ты пока ничего конкретного не предложил. Когда будут идеи, тогда и подходи..."
                Max_00 "Ладно, когда будут идеи, обсудим..."
        jump talkblog1.end

    label talkblog1.findout:
        $ alice.flags.crush = 2
        menu:
            Alice_07 "Ну, давай. Сомневаюсь, конечно, что это не пустая болтовня, но вдруг... Удиви меня!"
            "Постараюсь..." if True:
                Alice_00 "Постарайся. Я тоже буду думать. Но бросать блог не хочу. Может быть и правда стоит сменить формат, но на какой?"
                Max_00 "Договорились!"
            "Но ничего не обещаю" if True:
                Alice_00 "А я другого и не жду. Если бы у тебя были мысли, ты бы и сам мог на таком заработать... В общем, будем думать..."
                Max_00 "Ага..."
            "Обещаю, что-нибудь придумаю" if True:
                Alice_06 "Обещание, конечно, обнадёживает... Но я бы не стала на твоём месте что-то обещать. Конечно, если у тебя уже нет идей. Так или иначе, я тоже буду думать. Может быть, и правда не всё так плохо..."
                Max_00 "Да прорвёмся!"

    label talkblog1.end:
        $ spent_time = 10
        jump Waiting


label alice_talk_tv:
    if _in_replay:
        call alice_tv_closer from _call_alice_tv_closer
    elif True:
        if 'alice_talk_tv' not in persistent.memories:
            $ persistent.memories['alice_talk_tv'] = 0
    Alice_00 "Нет, садись. Тут места много..."
    $ alice.daily.tvwatch = 1
    $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
    Max_00 "Хорошо. Что смотришь?"
    $ SetCamsGrow(house[4], 110)
    menu:
        Alice_13 "Да так, всякую ерунду. Я просто отдыхаю, и мне без разницы, что смотреть. Поэтому смотрю всё подряд..."
        "Ну, давай смотреть всё подряд..." if not _in_replay:
            Max_11 "{i}( По телеку сегодня нет ничего интересного... Ни порнушки, ни даже эротики... А было бы забавно посмотреть такое с сестрёнкой... ){/i}"
            Max_00 "Ладно, пойду я..."
            jump alice_talk_tv.end
        "Тебе сделать массаж ног?" if _in_replay or all([not alice.daily.massage, learned_foot_massage()]):
            $ renpy.show("Max tv-closer 04"+mgg.dress)

    $ alice.daily.massage = 1
    $ _ch4 = GetChance(mgg.social, 4, 900)
    $ _drink = 0
    if alice.flags.m_foot == 0:
        Alice_02 "Что-то новенькое... А ты умеешь?"
        Max_01 "Само собой!"
        Alice_01 "Могу я спросить откуда? Раньше ты, вроде бы, не умел. Да и не представляю, где бы ты мог этому научиться..."
        Max_02 "Онлайн-курсы!"
        menu:
            Alice_02 "Очень смешно, Макс. Разве можно научиться массажу через ютуб?"
            "Почему ютуб? Это платные курсы..." if True:
                Alice_01 "А, ну если ты им ещё и заплатил, то это всё меняет!" nointeract
            "Конечно! Я же научился..." if True:
                Alice_01 "Что-то я очень сомневаюсь, Макс..." nointeract
        if renpy.display_menu([(_("Так тебе продемонстрировать или как? \n{color=[_ch4.col]}(Убеждение. Шанс: [_ch4.vis]){/color}"), 1)]) == 1:
            pass
        $ alice.flags.m_foot = 1
    elif alice.flags.m_foot in range(1, 6):
        menu:
            Alice_02 "Ну, не знаю, не знаю..."
            "Тебе понравится! \n{color=[_ch4.col]}(Убеждение. Шанс: [_ch4.vis]){/color}" if True:
                pass
    elif True:
        menu:
            Alice_07 "Дай-ка подумаю... Да! Я готова..."
            "Хорошо {i}(начать массаж){/i}" if not _in_replay:
                jump alice_talk_tv.massage
            "Может конфетку перед массажем?" if kol_choco or _in_replay:
                jump alice_talk_tv.choco

    if not RandomChance(_ch4.ch):
        $ Skill('social', 0.05)
        Alice_02 "[failed!t]Нет, Макс, в другой раз. Что-то я сомневаюсь. Вдруг, ты мне что-то сломаешь... Нет, спасибо."
        Max_08 "Ну, как хочешь... Не буду тебе мешать..."
        jump alice_talk_tv.end


    $ Skill('social', 0.1)
    menu:
        Alice_03 "[succes!t]Ну, давай. Только я очень привередлива в вопросах массажа. Если сделаешь что-то не так, сразу закончим."
        "Хорошо {i}(начать массаж){/i}" if True:
            jump alice_talk_tv.massage
        "Может конфетку перед массажем?" if kol_choco:
            jump alice_talk_tv.choco

    label alice_talk_tv.choco:
        if alice.flags.hip_mass > 4:
            menu:
                Alice_02 "Как же без неё. Но только одну... Вкусно... Теперь я готова, начинай массаж!"
                "Хорошо {i}(начать массаж){/i}" if True:
                    $ give_choco()
                    $ _drink = 1
                    jump alice_talk_tv.massage
        elif alice.dcv.seduce.done:
            menu:
                Alice_02 "У меня такое чувство, что ты чего-то от меня хочешь... Но не сознаешься ведь?"
                "Хочу тебя!" if not _in_replay:
                    menu:
                        Alice_15 "Макс! Вали нахрен отсюда со своими шуточками. Дай спокойно телевизор посмотреть!"
                        "{i}уйти{/i}" if True:
                            jump alice_talk_tv.end
                "Просто я такой хороший парень!" if True:
                    Alice_05 "Угу... Точно! Извини, а где мой брат Макс?"
                    Max_01 "Очень смешно. Так ты хочешь конфеты?"
                "Ты узнаешь... В своё время..." if True:
                    Alice_02 "Звучит очень зловеще... И что же я узнаю, интересно? Ах да. Это же секрет... Самому не смешно?"
                    Max_01 "Да, да, очень! Так ты хочешь конфеты?"

    $ _ch3 = GetChance(mgg.social, 3, 900)
    menu:
        Alice_13 "Честно говоря, не знаю. Конфеты я люблю, но не хочу портить фигуру..."
        "От конфетки не поправишься! {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}" if True:
            if RandomChance(_ch3.ch) or _in_replay:

                $ give_choco()
                $ alice.dcv.seduce.set_lost(3)
                $ _drink = 1
                $ Skill('social', 0.1)
                menu:
                    Alice_07 "[succes!t]Эх.. Уболтал, чертяка языкастый! Давай сюда конфетку. Но только одну... Вкусно... Теперь я готова, начинай массаж!"
                    "Ну, хорошо {i}(начать массаж){/i}" if True:
                        jump alice_talk_tv.massage
            elif True:
                $ alice.dcv.seduce.set_lost(2)
                $ Skill('social', 0.05)
                menu:
                    Alice_01 "[failed!t]Нет, Макс. Спасибо, конечно, но рисковать я не буду. Ну так что, массаж делать будешь или забыл, что собирался?"
                    "Ну, хорошо {i}(начать массаж){/i}" if True:
                        jump alice_talk_tv.massage

    label alice_talk_tv.massage:
        $ _pose = {'01':'01', '03':'02', '02':renpy.random.choice(['01','02'])}[pose3_2]
        $ _dress = mgg.dress+alice.dress
        $ _ch25 = GetChance(mgg.massage, 15)
        $ _ch20 = GetChance(mgg.massage, 10)
        $ _ch15 = GetChance(mgg.massage, 7)

        scene BG tv-mass-01
        $ renpy.show('Alice tv-mass ' + _pose + _dress)
        menu:
            Max_03 "{i}( Какая у Алисы нежная кожа... Интересно, о чём она сейчас думает? ){/i}"
            "{i}продолжить{/i} \n{color=[_ch20.col]}(Массаж. Шанс: [_ch20.vis]){/color}" if True:
                pass
        if RandomChance(_ch20.ch) or _in_replay:
            $ Skill('massage', 0.1)
            $ _ch2 = GetChance(mgg.social, 2)
            $ alice.flags.m_foot += 1
            $ _can_double_choko = _drink>0 and kol_choco>0 and (alice.flags.hip_mass or alice.dress=='a')
            $ _pose = {'01':'03', '02':'04'}[_pose]
            scene BG tv-mass-03
            $ renpy.show('Alice tv-mass ' + _pose + _dress)
            Alice_04 "[alice_good_mass!t]А ты неплох сегодня в этом деле... Хорошо, что ты никакой не работяга. Руки у тебя нежные. Приятно очень..." nointeract
            jump alice_talk_tv.choice_mass
        elif True:
            $ Skill('massage', 0.05)
            menu:
                Alice_12 "[alice_bad_mass!t]Ой, Макс, больно! Не надо так. Ты чуть лодыжку не вывихнул мне... Иди ещё потренируйся там на кошках или в ютубе поучись!"
                "{i}закончить{/i}" if True:
                    if alice.flags.m_foot in range(2, 6):
                        $ alice.flags.m_foot -= 1
                    jump alice_talk_tv.end

    label alice_talk_tv.choice_mass:
        $ dial = []
        if _can_double_choko and alice.flags.hip_mass < 5:
            $ dial.append((_("Может, ещё конфетку? \n{color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}"), 'double_drink'))
        if alice.dress=='a':
            if alice.flags.hip_mass < 5:
                $ dial.append((_("Тебе джинсы не мешают? \n{color=[_ch2.col]}(Убеждение. Шанс: [_ch2.vis]){/color}"), 'jeans'))
            elif alice.flags.hip_mass > 4:
                if not _drink:
                    $ dial.append((_("Тебе джинсы не мешают?"), 'jeans'))
                elif True:
                    $ dial.append((_("Тебе джинсы не мешают? Может, снять..."), 'jeans_off'))
        elif True:
            if _drink:
                $ dial.append((_("{i}продолжить{/i} \n{color=[_ch20.col]}(Массаж. Шанс: [_ch20.vis]){/color}"), 'mass'))
            elif True:
                $ dial.append((_("{i}продолжить{/i} \n{color=[_ch15.col]}(Массаж. Шанс: [_ch15.vis]){/color}"), 'mass'))
                if 5 > alice.flags.hip_mass > 1 and alice.flags.touched:
                    $ dial.append((_("{i}высунуть член{/i}"), 'sober'))
                elif alice.flags.hip_mass > 4:
                    $ dial.append((_("{i}высунуть член{/i}"), 'sober_r'))

        if not _in_replay:
            $ dial.append((_("{i}закончить массаж{/i}"), 'end_mass'))
        $ _can_double_choko = False
        $ rez =  renpy.display_menu(dial)

        if rez == 'jeans_off':
            jump alice_talk_tv.jeans_off
        elif rez == 'double_drink':
            if RandomChance(_ch3.ch) or _in_replay:
                $ _drink = 2
                $ give_choco()
                $ Skill('social', 0.1)
                Alice_02 "[succes!t]Макс, ну какой же ты... А, ладно, давай ещё одну... Но это последняя, больше не предлагай, а то пну сам знаешь куда! А эта конфета, кажется, ещё вкуснее той! От них стало так жарко..."
                if alice.dress != 'a':
                    jump alice_talk_tv.massage_next
                Max_01 "Может, тогда тебе стоит снять джинсы? Не будет так жарко..."
                jump alice_talk_tv.jeans_off
            elif True:
                Alice_03 "[failed!t]Нет, мне хватит одной... А то я мигом фигуру испорчу. Лучше продолжай массировать мои ножки..." nointeract
                jump alice_talk_tv.choice_mass

        elif rez == 'jeans':
            if RandomChance(_ch2.ch) or _in_replay:
                jump alice_talk_tv.jeans
            elif True:
                $ Skill('social', 0.05)
                menu:
                    Alice_05 "[failed!t]Это так ты к девушкам подкатываешь, сразу предлагаешь снять штаны?"
                    "Э... Я к тебе не подкатываю. Просто, жарко же..." if True:
                        pass
                    "Ну у тебя и фантазии, Алиса... Я не подкатываю!" if True:
                        pass
                Alice_01 "Да шучу я. Но джинсы снимать не стану. Даже не надейся. Кстати, ты закончил с массажем? Спасибо большое, можешь идти..."
                Max_00 "Вот так вот..."
                jump alice_talk_tv.end

        elif rez == 'mass':
            jump alice_talk_tv.massage_next
        elif rez == 'sober':
            jump alice_talk_tv.sober_mass
        elif rez == 'sober_r':
            jump alice_talk_tv.sober_mass_r
        elif True:
            Alice_07 "Как, всё? А мне понравилось... Спасибо, Макс. Вот ты и сделал девушке приятно!"
            Max_07 "Я и не так могу..."
            Alice_05 "Ах ты и не так можешь? Боюсь даже представить, как... Но не буду. И тебе не советую. Так что давай, дуй отсюда!"
            Max_00 "Угу..."
            jump alice_talk_tv.end

    label alice_talk_tv.jeans_off:
        Alice_04 "Только давай ты снимешь их с меня сам, а то я уже так расслабилась, что двигаться не хочется."
        Max_03 "О, это я с радостью сделаю!"
        Alice_07 "Я немного приподнимусь, чтобы тебе было проще их стянуть..."
        if alice.req.result == 'nopants':
            $ renpy.show('Alice tv-mass ' + _pose + _dress+'-2')
            Max_06 "О да, это ты классно придумала!"
        elif True:
            $ renpy.show('Alice tv-mass ' + _pose + _dress+'-1')
            Max_05 "О да, так гораздо лучше..."
        Alice_05 "Ты только там сильно не заглядывайся, куда не нужно! Лучше скорее продолжай массаж, пока я не расхотела..."
        if alice.req.result == 'nopants':
            Max_07 "Ну да... точно... я же... это... массаж делал."
            Alice_03 "Ты чего там так тормозишь? Как будто в трусиках меня никогда не видел..."

            $ renpy.show('Alice tv-mass '+_pose+'-3a')
            $ renpy.show('Max tv-mass '+_pose+'-3'+mgg.dress)
            Alice_15 "Ой, Макс, я же сегодня без них! Вот чёрт! Чего глазеешь, иди отсюда, ты и так увидел больше положенного..."
            Max_05 "Ладно, но это было так сногсшибательно, что я аж забыл, как ходить!"
            Alice_18 "Макс!!!"
            Max_04 "Всё, ушёл."
            if not _in_replay:
                $ current_room = house[0]
            jump alice_talk_tv.end
        elif True:
            Max_02 "Ага, сейчас продолжим..."

            $ _dress = mgg.dress+'c'
            $ renpy.show('Alice tv-mass ' + _pose + _dress)
            jump alice_talk_tv.not_jeans

    label alice_talk_tv.jeans:
        if alice.flags.hip_mass > 4:

            if alice.req.result == 'nopants':
                Alice_02 "Да, что-то тесновато в них и так жарко... Хотя... Не-е-ет, нет, нет! Не буду снимать я сейчас джинсы. Не дождёшься!" nointeract
            elif True:
                Alice_04 "Ты знаешь, мешают. И очень жарко. Пожалуй, порадую тебя немного, раз ты так хорошо массаж делаешь..." nointeract
        elif True:
            $ Skill('social', 0.1)
            if alice.req.result == 'nopants':
                Alice_02 "[succes!t]Да, что-то тесновато в них и так жарко... Хотя... Не-е-ет, нет, нет! Не буду снимать я сейчас джинсы. Не дождёшься!" nointeract
            elif True:
                Alice_04 "[succes!t]Ты знаешь, мешают. И очень жарко. Пожалуй, порадую тебя немного, раз ты так хорошо массаж делаешь..." nointeract

        if alice.req.result == 'nopants':
            menu:
                "Почему?" if True:
                    Alice_01 "Сам догадайся, глупый. Но я намекну: возможно, под джинсами ничего нет. Понял? Всё, а теперь иди отсюда, фантазируй..."
                    Max_01 "Ух, пойду тогда... Пофантазирую где-нибудь..."
                    jump alice_talk_tv.end
                "Потому-что ты без трусиков?" if True:
                    Alice_03 "Сам догадался, или кто подсказал? Ну всё, теперь ты всё обо мне знаешь, иди и фантазируй о чём хочешь..."
                    Max_01 "Ладно, пойду пофантазирую где-нибудь..."
                    jump alice_talk_tv.end
        elif True:
            Max_07 "{i}( Ого... ){/i}"

            $ _dress = mgg.dress+'c'
            $ renpy.show('Alice tv-mass ' + _pose + _dress)
            menu alice_talk_tv.not_jeans:
                Alice_05 "Да, так гораздо лучше. Только ты не пялься, куда не надо. Вижу, краем глаза пытаешься что-то разглядеть. Вот не надо. Лучше, продолжай массаж..."
                "А почему на тебе трусики?" if alice.req.result == 'not_nopants':
                    Alice_07 "А с чего бы мне быть без них!"
                    Alice_14 "Ой..."
                    Max_09 "Вот ты и попалась! Я значит тут со всей любезностью массаж сестрёнке делаю, конфетами угощаю, а она..."
                    Alice_12 "Просто забыла..."
                    Max_07 "Тогда, если хочешь продолжения массажа, то снимай их!"
                    Alice_06 "Макс! Какой же ты... Ладно, только не смотри. И когда продолжишь массаж, не пялься на меня!"
                    Max_03 "Да, да, конечно."
                    $ renpy.show('Alice tv-mass '+_pose+'-3a')
                    $ renpy.show('Max tv-mass '+_pose+'-3'+mgg.dress)
                    Alice_13 "Хотя, нет, не пойдёт! У меня так всё видно будет... И хватит уже пялиться! Лучше иди уже по своим делам."
                    Max_05 "Как скажешь. Трусы не потеряй."
                    if not _in_replay:
                        $ added_mem_var('alice_not_nopants')
                        $ current_room = house[0]
                        $ alice.dcv.prudence.set_lost(renpy.random.randint(2, 5))
                        $ punalice[2][0]=10
                    jump alice_talk_tv.end
                "{i}продолжить{/i} \n{color=[_ch25.col]}(Массаж. Шанс: [_ch25.vis]){/color}" if _drink==2:
                    $ alice.dress = 'c'
                    jump alice_talk_tv.massage_next
                "{i}продолжить{/i} \n{color=[_ch20.col]}(Массаж. Шанс: [_ch20.vis]){/color}" if _drink==1:
                    $ alice.dress = 'c'
                    jump alice_talk_tv.massage_next
                "{i}продолжить{/i} \n{color=[_ch15.col]}(Массаж. Шанс: [_ch15.vis]){/color}" if not _drink:
                    $ alice.dress = 'c'
                    jump alice_talk_tv.massage_next
                "{i}высунуть член{/i}" if all([not _drink, 5 > alice.flags.hip_mass > 1, alice.flags.touched]):
                    $ alice.dress = 'c'
                    jump alice_talk_tv.sober_mass
                "{i}высунуть член{/i}" if all([not _drink, alice.flags.hip_mass > 4]):
                    $ alice.dress = 'c'
                    jump alice_talk_tv.sober_mass_r
    label alice_talk_tv.massage_next:
        if (RandomChance(_ch20.ch) and _drink==1) or (RandomChance(_ch25.ch) and _drink==2) or _in_replay:
            $ Skill('massage', 0.1)
            $ _pose = {'03':'05', '04':'06'}[_pose]
            scene BG tv-mass-05
            $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
            $ renpy.show('Max tv-mass ' + _pose + mgg.dress)
            menu:
                Alice_07 "Макс... Сегодня твои ручки творят чудеса... А во что это моя нога упёрлась? Это часть программы или как?"
                "Да, это будет на десерт..." if True:
                    menu:
                        Alice_08 "Ты так в себе уверен, Макс... Забыл, что я твоя сестра? Не говори глупости... Просто продолжай массировать мои ножки. Если ты ещё не в курсе, они у меня целиком - эрогенная зона..."
                        "{i}попытаться приставать{/i}" if _drink < 2 and not _in_replay and not alice.flags.hip_mass:
                            jump alice_talk_tv.fail
                        "{i}массировать её ноги выше{/i}" if _drink > 1 and alice.flags.hip_mass:
                            jump advanced_massage1
                        "{i}массировать её ноги выше{/i}" if _drink == 1 and alice.flags.hip_mass > 4:
                            jump advanced_massage1
                        "{i}продолжать массаж{/i}" if not _in_replay or (_in_replay and (not alice.flags.hip_mass or (alice.flags.hip_mass > 4 and not _drink))):
                            pass
                "{i}продолжать молча{/i}" if True:
                    menu:
                        Alice_04 "Эх, Макс... А я бы захотела продолжения, если бы ты был моим парнем... Жаль, что ты только мой брат..."
                        "Ну я могу стать твоим парнем... Хотя бы на час... или насколько захочешь..." if not _in_replay:
                            menu:
                                Alice_05 "На сколько захочу? На секунду! Ой. Она прошла... Всё, Макс, твоё время вышло... Ладно, засовывай свою штуку обратно. Что-то голова кружится... Макс, уйди по хорошему, а..."
                                "{i}уйти{/i}" if True:
                                    jump alice_talk_tv.end
                        "{i}попытаться приставать{/i}" if _drink < 2 and not _in_replay and not alice.flags.hip_mass:
                            jump alice_talk_tv.fail
                        "{i}массировать её ноги выше{/i}" if all([_drink > 1, alice.flags.hip_mass, 'kira' in chars]):
                            jump advanced_massage1
                        "{i}массировать её ноги выше{/i}" if _drink == 1 and alice.flags.hip_mass > 4:
                            jump advanced_massage1
                        "{i}продолжать массаж{/i}" if not _in_replay or (_in_replay and (not alice.flags.hip_mass or (alice.flags.hip_mass > 4 and not _drink))):
                            pass

        elif RandomChance(_ch15.ch) and not _drink:
            $ Skill('massage', 0.1)
            $ infl[alice].add_m(12)
            Alice_03 "Ух, как хорошо... Макс, а ты молодец сегодня! Не ожидала такой чувственности и в то же время силы... Ну всё спасибо, иди..."
            Max_04 "Не за что..."
            jump alice_talk_tv.end
        elif True:

            $ Skill('massage', 0.05)
            Alice_13 "[alice_bad_mass!t]Ой, нет, что-то не то. Ты же так хорошо начал, и что-то неприятно стало... Иди, ещё поучись этому своему массажу на ютубе. Так не пойдёт..."
            Max_00 "Ладно..."
            jump alice_talk_tv.end

    $ _pose = {'05':'07', '06':'08'}[_pose]
    scene BG tv-mass-07
    $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
    $ renpy.show('Max tv-mass ' + _pose + mgg.dress)
    Alice_04 "Ну всё, кажется хватит. Во всяком случае, тебе. А то мне ногу испачкаешь... Но ручки у тебя - что надо. Даже не ожидала такого от тебя..."
    Max_05 "Я тоже не ожидал... такого..."
    Alice_08 "Значит, мы оба полны сюрпризов. Ну всё, хорошего помаленьку. Давай, засовывай свой член обратно, а то до добра это всё дело не дойдёт... Да, и спасибо за массаж..."
    Max_03 "Тебе спасибо..."
    $ persistent.memories['alice_talk_tv'] = 1
    $ alice.stat.footjob += 1
    $ alice.daily.massage = 3
    jump alice_talk_tv.end

    menu alice_talk_tv.fail:
        Alice_12 "Макс! Ещё одно лишнее движение, и я дам тебе по шарам вот это самой ногой. Ты меня понял? Всё, массаж окончен, вали отсюда!"
        "{i}уйти{/i}" if True:
            jump alice_talk_tv.end

    label alice_talk_tv.sober_mass:

        $ _pose = {'03':'05', '04':'06'}[_pose]
        scene BG tv-mass-05
        $ renpy.show('Max tv-mass ' + _pose + mgg.dress)
        $ renpy.show('Alice tv-mass ' + _pose + alice.dress)

        if alice.flags.hip_mass < 3:

            $ alice.flags.hip_mass = 3
            Alice_07 "Макс... Сегодня твои ручки творят чудеса... Но мне немного щекотно. Раньше ты массировал мне ножки без этого..."
            Max_02 "Ты права. Без этого... Не нравится?"
            Alice_04 "Нет, мне очень нравится! Просто, я пока не поняла, что изменилось и как ты это делаешь... А хотя... Подожди-ка..."
            Max_07 "Знай, я не специально."

            scene BG tv-mass-03
            $ renpy.show('Max tv-mass 04-3' + mgg.dress)
            $ renpy.show('Alice tv-mass 04-3' + alice.dress)
            Alice_15 "Так я об член твой тёрлась?! Ну, Макс! Ты зачем так сделал, совсем что ли извращенец? Хотя, зачем я спрашиваю..."
            Max_04 "У тебя такая нежная кожа, вот у меня и встал. И несмотря на это, я хотел закончить массаж... для своей дорогой сестрёнки."
            Alice_16 "Да ты что! А если бы я так и не поняла, что ты мне ножки членом своим щекочешь?!"
            Max_03 "Ты же сама сказала, что тебе очень нравится! А для меня это главное."
            Alice_17 "Ещё бы! Должно быть, это очень приятно, делать массаж ног, когда тебе в ответ дрочат. Пнуть бы тебя за это сам знаешь куда!"
            Max_07 "Алиса, зачем этого стыдиться? Тебе же понравилось..."
            Alice_06 "Макс, это ведь грязно! Я твоя сестра!"
            Max_09 "И что теперь, мне нельзя что-то приятное сделать для тебя? Это не круто."
            Alice_12 "Можно, но не так же..."
            Max_08 "Смотри... Тогда буду массировать руками."
            Alice_00 "Вот именно! Но уже в следующий раз. На сегодня хватит. Я так уж и быть, представлю, что ничего не было, потому что твой массаж мне нравится."
            Max_00 "Хорошо."

        elif alice.flags.hip_mass < 4:

            $ alice.flags.hip_mass = 4
            Alice_07 "Макс... Сегодня твои ручки творят чудеса... Мне снова щекотно... Это что, снова твой член! Ты же сказал, что будешь массировать руками!"
            Max_02 "Так и есть."
            Alice_06 "Я ведь и пнуть могу, если не уберёшь свою штуку!"
            Max_04 "Я бы убрал, если бы ты перестала тереться об него своими ножками."

            scene BG tv-mass-03
            $ renpy.show('Max tv-mass 04-3' + mgg.dress)
            $ renpy.show('Alice tv-mass 04-3' + alice.dress)
            Alice_14 "Ничего я не тёрлась! Просто по инерции... немного... Это всё массаж твой. Мне становится так хорошо, что я не осознаю, что делаю."
            Max_03 "Ну и делай себе дальше, если тебе нравится. Будет у нас маленький секретик."
            Alice_06 "Да мне просто стыдно, что я тут делаю со своим братом на диване!"
            Max_07 "Подумаешь! Я просто хочу сделать приятно своей сестрёнке, а уж как - не важно."
            Alice_13 "Мило, Макс. Хочешь сказать, мне стоило бы просто дать тебе закончить вот такой массаж и ни о чём не думать?"
            Max_02 "Попробовала бы разок. Уверен, ты останешься весьма довольной."
            Alice_05 "Ты так в себе уверен?! Что ж, в следующий раз я попробую. И если мне хоть что-то, хоть немного не понравится... тебе будет плохо."
            Max_01 "Не будет."
        elif True:


            $ alice.flags.hip_mass = 5
            Alice_07 "Макс... Сегодня твои ручки творят чудеса... Но будь осторожен, высовывая свой член... Мне не должно быть слишком щекотно..."
            Max_02 "Не будет."

            $ _pose = {'05':'07', '06':'08'}[_pose]
            scene BG tv-mass-07
            $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
            $ renpy.show('Max tv-mass ' + _pose + mgg.dress)
            menu:
                Alice_08 "Ты так в себе уверен, Макс... Ну посмотрим... Просто продолжай массировать мои ножки. Если ты ещё не в курсе, они у меня целиком - эрогенная зона..."
                "{i}продолжать массаж{/i}" if True:
                    Alice_04 "Эх, Макс... Хоть мне и хорошо, но нам пора закругляться. Мне кажется, ты уже близок к тому, чтобы испачкать меня или диван."
                    Max_09 "Как бы не так!"

            scene BG tv-mass-03
            $ renpy.show('Max tv-mass 04-3' + mgg.dress)
            $ renpy.show('Alice tv-mass 04-3' + alice.dress)
            Alice_12 "Да ты что! Хочешь сказать, для тебя это было не так уж и приятно?!"
            Max_03 "Шутишь? Было супер! Но этого мало, чтобы я тебя испачкал."
            Alice_05 "Даже так... Ну, проверять мы это, пожалуй, не будем. Спасибо за массаж, Макс. Мне понравилось. Но это будет только нашей вечерней шалостью, так что не думай, что к тебе будет особенное отношение во всё остальное время."
            Max_01 "Хотя бы так."

        $ Skill('massage', 0.1)
        $ alice.stat.footjob += 1
        $ alice.daily.massage = 3
        $ alice.free += 1
        $ infl[alice].add_m(16)
        jump alice_talk_tv.end

    label alice_talk_tv.sober_mass_r:

        $ _pose = {'03':'05', '04':'06'}[_pose]
        scene BG tv-mass-05
        $ renpy.show('Max tv-mass ' + _pose + mgg.dress)
        $ renpy.show('Alice tv-mass ' + _pose + alice.dress)

        Alice_07 "Макс... Обожаю то, какие чудеса творят твои руки... Но будь осторожен, высовывая свой член... Мне не должно быть слишком щекотно..."
        Max_02 "Не будет."

        $ _pose = {'05':'07', '06':'08'}[_pose]
        scene BG tv-mass-07
        $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
        $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

        $ renpy.dynamic('ch')
        $ ch = GetChance(mgg.massage, 3)

        menu:
            Alice_08 "Ты так в себе уверен, Макс... Ну посмотрим... Просто продолжай массировать мои ножки. Они у меня любят твой твёрдый... настрой."
            "{i}продолжать массаж{/i}" if True:

                scene BG tv-mass-03
                $ renpy.show('Max tv-mass 04-3' + mgg.dress)
                $ renpy.show('Alice tv-mass 04-3' + alice.dress)
                Alice_03 "Ух, как хорошо... Но пора закругляться. Ты молодец, Макс! Мне нравится эта чувственность и в то же время сила... Спасибо тебе."
                Max_04 "Не за что..."
                $ Skill('massage', 0.05)
            "{i}массировать её ноги выше{/i} \n{color=[ch.col]}(Массаж. Шанс: [ch.vis]){/color}" if True:
                if RandomChance(ch.ch):


                    scene BG tv-mass-03
                    $ _pose = {'07':'09', '08':'10'}[_pose]
                    $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
                    $ renpy.show('Max tv-mass ' + _pose + mgg.dress)
                    Alice_07 "[like!t]Да, моим ножкам становится так легко от твоих прикосновений... И они очень тебе благодарны. Чувствуешь, насколько?"
                    Max_03 "А как же... Они у тебя шаловливые..."
                    menu:
                        Alice_04 "Они у меня такие... Любят помассировать кое-что большое и твёрдое... Главное, не перестараться и чувствовать, когда нужно заканчивать..."
                        "{i}закончить массаж{/i}" if True:

                            scene BG tv-mass-03
                            $ renpy.show('Max tv-mass 04-3' + mgg.dress)
                            $ renpy.show('Alice tv-mass 04-3' + alice.dress)
                            Alice_03 "Ух, как хорошо... Макс, а ты молодец! Мне нравится эта чувственность и в то же время сила... Спасибо тебе."
                            Max_04 "Не за что..."


                    $ alice.stat.footjob += 1
                    $ add_lim('alice.free', 0.1, 5)
                    $ infl[alice].add_m(16)
                    $ Skill('massage', 0.1)
                elif True:


                    scene BG tv-mass-03
                    $ renpy.show('Max tv-mass 04-3' + mgg.dress)
                    $ renpy.show('Alice tv-mass 04-3' + alice.dress)
                    Alice_03 "[dont_like!t]Было хорошо, Макс! Но ты немного поспешил двигаться выше... Но ручки у тебя - что надо. До следующего раза... и спасибо..."
                    Max_04 "Не за что..."
                    $ Skill('massage', 0.05)

        $ alice.daily.massage = 3
        jump alice_talk_tv.end

    label alice_talk_tv.end:
        $ renpy.end_replay()
        $ spent_time = max((60 - int(tm[-2:])), 40)
        $ AddRelMood('alice', 0, 50, 3)
        $ cur_ratio = 0.5
        jump Waiting

label advanced_massage1:
    $ added_mem_var('advanced_massage1')
    scene BG tv-mass-03
    $ _pose = {'05':'09', '06':'10'}[_pose]
    $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
    $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

    if alice.flags.hip_mass < 2:
        Max_08 "{i}( Я раньше и внимания не обращал, а ведь Алиса всегда намекала на то, что мне можно массировать не только её ступни! Вот я олух... ){/i}"
        $ alice.flags.hip_mass = 2
    $ added_mem_var('double_mass_alice')
    if alice.flags.hip_mass > 4:
        Alice_07 "Да, моим ножкам становится так легко от твоих прикосновений... И они очень тебе благодарны. Чувствуешь, насколько?"
        Max_03 "А как же... Они у тебя шаловливые..."
    elif True:
        Alice_07 "Да, моим ножкам становится так легко от твоих прикосновений... У меня ведь красивые ноги, правда?"
        Max_03 "Очень красивые, сестрёнка! Такие мягкие, но упругие... Массировать их - одно удовольствие! А ещё они у тебя шаловливые..."
    menu:
        Alice_04 "Они у меня такие... Любят помассировать кое-что большое и твёрдое..."
        "{i}массировать ещё выше{/i}" if True:
            pass
    scene BG char Alice tv-mass-11
    $ _pose = {'09':'11', '10':'12'}[_pose]
    $ renpy.show('Alice tv-mass ' + _pose + _dress)

    menu:
        Max_04 "{i}( Похоже, Алиса не на шутку завелась! Она всё активнее дрочит мне своими ножками... Почему бы и мне не поласкать её киску, она ведь так близко... ){/i}"
        "{i}ласкать её киску через одежду{/i}" if True:
            pass
    scene BG tv-mass-07
    $ _pose = {'11':'13', '12':'14'}[_pose]
    $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
    $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

    Alice_09 "Ммм, Макс... Да... Какой же у меня похотливый брат! Как приятно!"
    Max_02 "{i}( Ухх... Алиса начала сама тереться об мои пальцы! Конфеты сделали своё дело и теперь она уже не хочет останавливаться... ){/i}"
    menu:
        Alice_11 "Мне так тепло... там внизу... Кажется, я уже близко... Как хорошо... да..."
        "{i}ласкать её киску быстрее{/i}" if True:
            jump advanced_massage1.faster
        "{i}не торопиться{/i}" if alice.dcv.intrusion.stage in [5, 7]:
            jump advanced_massage1.no_rush

    label advanced_massage1.faster:
        scene BG char Alice tv-mass-15
        $ _pose = {'13':'15', '14':'16'}[_pose]
        $ renpy.show('Alice tv-mass ' + _pose + _dress)

        Max_05 "{i}( Алиса так жарко и классно трётся об мои пальцы своей киской! Хоть на ней и есть одежда, но я чувствую через неё всё... ){/i}"
        Alice_10 "Ох, чёрт... Макс... я больше не могу! Только не убирай свою руку оттуда... Я уже кончаю... Ахх!"
        Max_06 "{i}( Моя старшая сестрёнка совсем сошла с ума... Её ноги дрожат от того, как сладко она кончила! ){/i}"
        scene BG tv-mass-03
        $ _pose = {'15':'09', '16':'10'}[_pose]
        $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
        $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

        Alice_07 "Да... такой массаж мне нравится... Вот бы всё время так!"
        Max_01 "Это запросто, Алиса! Наверно, хочешь теперь побыть одна и отдохнуть?"
        Alice_05 "Ага. Давай, засовывай свой член обратно, а то все ноги мне испачкаешь... Массаж классный, Макс... Спасибо!"
        Max_03 "Тебе спасибо..."
        jump advanced_massage1.end

    label advanced_massage1.no_rush:
        $ _pose = {'13':'17', '14':'18'}[_pose]
        if _pose == '17':
            scene BG tv-cun-01
        elif True:
            scene BG tv-mass-07
        $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
        $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

        Alice_06 "Макс, ты почему замедлился? Я хочу ещё, не останавливайся!"
        Max_03 "Хочешь узнать, что я умею делать языком?"
        menu:
            Alice_08 "Ммм... Макс... Я же твоя сестра, а ты... ведёшь себя со мной... как будто я твоя девушка... Но я могу это представить, ненадолго... Так что успевай."
            "{i}снять с Алисы трусики{/i}" if alice.dress == 'c':
                pass
            "{i}снять с Алисы шортики{/i}" if alice.dress != 'c':
                pass
        $ _pose = {'17':'19', '18':'20'}[_pose]
        if _pose == '19':
            scene BG tv-mass-01
        $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
        $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

        $ renpy.dynamic('ch')
        $ ch = GetChance(mgg.sex, 5, 900)
        Alice_07 "Мне любопытно узнать, сможешь ли ты что-то противопоставить тем, кто это делал до тебя... А это, между прочим, были девушки, которые куда больше твоего знают, как это надо делать."
        Max_07 "Сомневаешься во мне?"
        menu:
            Alice_05 "А ты болтай поменьше... Может и перестану."
            "{i}ласкать её киску языком{/i} {color=[ch.col]}(Сексуальный опыт. Шанс: [ch.vis]){/color}" if True:
                if RandomChance(ch.ch):

                    $ Skill('sex', 0.2)
                    $ _pose = {'19':'21', '20':'22'}[_pose]
                    if _pose == '21':
                        scene BG tv-sex03-01
                    elif True:
                        scene BG tv-mass-01
                    $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
                    $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

                    Alice_09 "[like!t]Да, Макс, да! Я уже так близко... Не останавливайся... У тебя такой быстрый и ловкий язычок, Макс... Ммм... Как хорошо!"
                    menu:
                        Max_04 "{i}( Я сейчас устрою твоей сладкой киске такое, чего ты точно не забудешь! Хотя... нет, ты забудешь... Да и ладно. ){/i}"
                        "{i}ещё быстрее работать языком{/i}" if True:
                            pass
                    $ _pose = {'21':'23', '22':'24'}[_pose]
                    if _pose == '23':
                        scene BG tv-mass-01
                    elif True:
                        scene BG tv-sex03-01
                    $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
                    $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

                    Alice_11 "Ах! Я больше не могу, Макс... Кончаю! Да... Как же это было классно! Ох... Это было потрясающе..."
                    Max_02 "Будешь ещё сомневаться в моих навыках?"
                    $ _pose = {'23':'19', '24':'20'}[_pose]
                    if _pose == '20':
                        scene BG tv-mass-07
                    $ renpy.show('Alice tv-mass ' + _pose + alice.dress)
                    $ renpy.show('Max tv-mass ' + _pose + mgg.dress)

                    Alice_07 "Ах, Макс! И где ты такому научился?! Неужто, просмотр порнушки может такому научить?"
                    Max_05 "Просто сделал всё так, как хотел бы, чтобы сделали мне..."
                    Alice_05 "Да... такой массаж мне нравится... Вот бы всё время так! А сейчас, давай-ка засовывай свой член обратно, а то все ноги мне испачкаешь... Массаж класcный, Макс... Спасибо!"
                    Max_03 "Тебе спасибо..."
                    if alice.flags.hip_mass < 3:
                        Max_09 "{i}( С Алисой нужно как-то сближаться без конфет. Только как?! Она стала более адекватно воспринимать мои стояки, после случая с пауком во дворе... Так может, и при массаже ног у ТВ без конфет у меня что-то выгорит? ){/i}"
                elif True:

                    scene BG tv-mass-03
                    $ renpy.show('Max tv-mass 03-3' + mgg.dress)
                    $ renpy.show('Alice tv-mass 03-3' + alice.dress)

                    $ Skill('sex', 0.1)
                    Alice_03 "[dont_like!t]Всё, Макс! Я передумала! Массаж был неплохой, но на этом мы закончим..."
                    Max_08 "Да ладно, Алиса! Я же ещё ничего не успел сделать!"
                    Alice_05 "Слишком много болтал. Вот и передумала. Но за массаж, спасибо! Давай, засовывай свой член обратно и гуляй..."
                    Max_10 "Ладно..."
        jump advanced_massage1.end

    label advanced_massage1.end:
        $ renpy.end_replay()
        $ current_room = house[0]
        $ alice.daily.massage = 4
        jump alice_talk_tv.end


label alice_aboutbooks:
    menu:
        Alice_13 "Книжку, очевидно..."
        "Спасибо, кэп!" if True:
            Alice_01 "Так чего хотел, Макс?"
            Max_00 "Хотел узнать что именно читаешь..."
        "Очень смешно..." if True:
            Alice_01 "Так чего хотел, Макс?"
            Max_00 "Хотел узнать что именно читаешь..."
        "Это понятно, а какую? Только не говори, что бумажную..." if True:
            Alice_01 "Ну вот... Хотела пошутить, и ты так меня обломал... А если серьёзно, то чего хотел?"
            Max_00 "Да вот и хотел узнать, что именно читаешь..."
    menu:
        Alice_02 "Забавно. А тебе не всё равно? Или делать нечего?"
        "Не всё равно, раз спрашиваю" if True:
            pass
        "Так ты скажешь или нет?" if True:
            pass
    menu:
        Alice_00 "Не скажу. Сиди теперь и гадай! \n\n{i}Алиса прикрыла обложку рукой{/i}"
        "Какой-то дамский роман?" if True:
            pass
        "Какие-то сопли с сахаром?" if True:
            pass
        "Неужели справочник по квантовой механике?" if True:
            pass
    $ poss['secretbook'].open(0)
    menu:
        Alice_01 "Думай, что хочешь, а я всё равно не скажу."
        "Ну и ладно!" if True:
            pass
        "{i}узнать подробнее о \"Возможностях\"{/i}" if sum([1 if sum(poss[ps].stages) else 0 for ps in poss_dict]) < 2:
            call about_poss from _call_about_poss_1
    $ spent_time += 10
    $ AvailableActions['searchbook'].enabled = True
    jump Waiting


label first_talk_smoke:
    $ _m1_alicetalk__mood = 0
    Alice_13 "Упс. Макс, ты ничего не видел!"
    $ poss['smoke'].open(0)
    Max_08 "Алиса, ты куришь?!"
    $ alice.dcv.special.stage = 1
    menu:
        Alice_12 "Нет, блин, просто зажгла сигарету, посмотреть как горит... Давай так, ты уйдёшь и сделаешь вид, что ничего не было, хорошо?"
        "А если уйду, что мне за это будет?" if True:
            Alice_16 "Вот если не уйдёшь, то узнаешь, что тебе за это будет! Бегом отсюда!"
            Max_09 "Может быть я и уйду, но..."
        "Ну ок, только я ничего не обещаю..." if True:
            pass
    menu:
        Alice_14 "Что это значит? Шантажировать меня вздумал?!"
        "Ну да. Мама что с тобой сделает, если узнает?" if True:
            menu:
                Alice_13 "Макс, я тебя по-человечески прошу. Сделай вид, что ничего не было. Я не хочу расстраивать маму..."
                "Не хочешь расстраивать маму или получить по заднице?" if True:
                    menu:
                        Alice_12 "Может быть, и то и другое. Ну так как, Макс?"
                        "Мы всё ещё можем договориться..." if True:
                            jump first_talk_smoke.talk
                        "Посмотрим..." if True:
                            jump first_talk_smoke.maybe
                        "Ну ладно, ладно..." if True:
                            $ _m1_alicetalk__mood += 75
                            jump first_talk_smoke.goodend
                "Мы всё ещё можем договориться..." if True:
                    jump first_talk_smoke.talk
                "Посмотрим..." if True:
                    jump first_talk_smoke.maybe
                "Ну ладно, ладно..." if True:
                    $ _m1_alicetalk__mood += 100
                    jump first_talk_smoke.goodend
        "Ну, мы можем договориться" if True:
            jump first_talk_smoke.talk
        "Как знать, может быть..." if True:
            jump first_talk_smoke.maybe
        "Нет, конечно. Мне жизнь дорога!" if True:
            $ _m1_alicetalk__mood += 50
            jump first_talk_smoke.goodend

    menu first_talk_smoke.talk:
        Alice_13 "Договориться? Ну ладно. Чего ты хочешь?"
        "Если заплатишь, буду молчать" if True:
            menu:
                Alice_12 "Макс, ты же знаешь, что я на мели. У меня нет денег. Ну, точнее есть, но баксов 10. Тебя устроит?"
                "Ну, давай" if True:
                    $ _m1_alicetalk__mood -= 50
                    $ spent_time += 10
                    $ mgg.ask(0)
                    $ alice.req.req = 'money'
                    menu:
                        Alice_13 "Сейчас сбегаю за деньгами...\nВот, держи $10, и теперь-то уж точно ты ничего не видел. Так?"
                        "Так!" if True:
                            jump first_talk_smoke.end
                        "Как знать..." if True:
                            menu:
                                Alice_16 "И как это понимать, Макс? Мы же договорились! Ну ты и гад... Всё, вали отсюда!"
                                "Ну, как скажешь..." if True:
                                    jump first_talk_smoke.end
                "Нет, этого мало..." if True:

                    $ _m1_alicetalk__mood -= 100
                    menu:
                        Alice_12 "Ну... больше у меня нет. Может, просто забудем обо всём?"
                        "Покажи сиськи!" if True:
                            jump first_talk_smoke.bad
                        "Сними трусы!" if True:
                            jump first_talk_smoke.bad
                        "Отсоси мне!" if True:
                            jump first_talk_smoke.suck
                        "Ты будешь мне должна услугу" if True:
                            jump first_talk_smoke.owe
        "Покажи сиськи!" if True:
            jump first_talk_smoke.bad
        "Сними трусы!" if True:
            jump first_talk_smoke.bad
        "Отсоси мне!" if True:
            jump first_talk_smoke.suck
        "Ты будешь мне должна услугу" if True:
            jump first_talk_smoke.owe

    menu first_talk_smoke.bad:
        Alice_15 "Что?! Ну ты хам! Всё, быстро свалил!"
        "Ну, как скажешь..." if True:
            $ _m1_alicetalk__mood -= 100
            jump first_talk_smoke.end

    menu first_talk_smoke.suck:
        Alice_14 "Что?! Отсоси себе сам! Пошёл вон отсюда!"
        "Ну, как скажешь..." if True:
            $ _m1_alicetalk__mood -= 150
            jump first_talk_smoke.end

    menu first_talk_smoke.owe:
        Alice_06 "И какую услугу я тебе буду должна? Например?"
        "Покажешь сиськи, когда попрошу..." if True:
            pass
        "Разденешься, когда скажу..." if True:
            pass
        "Отсосёшь, когда нужно будет..." if True:
            jump first_talk_smoke.suck
        "Я ещё не решил..." if True:
            menu:
                Alice_03 "Ну, вот когда решишь, тогда и поговорим. А теперь иди отсюда, пока ещё можешь!"
                "Ну, как скажешь..." if True:
                    jump first_talk_smoke.end

    menu:
        Alice_15 "Да ты что?! А не охренел ли ты, мальчик? Это всего лишь сигарета, а запросы у тебя... Всё, свалил отсюда!"
        "Ну, как скажешь..." if True:
            $ _m1_alicetalk__mood -= 100
            jump first_talk_smoke.end

    menu first_talk_smoke.maybe:
        Alice_12 "Сам смотри... Воевать со мной - себе дороже. И, вообще, иди отсюда. Я уже взрослая и могу делать что хочу..."
        "Ну, как скажешь..." if True:
            pass

    menu first_talk_smoke.goodend:
        Alice_05 "Вот это другое дело. Ладно, разговор окончен..."
        "Хорошо..." if True:
            pass

    label first_talk_smoke.end:
        $ spent_time += 10
        $ AddRelMood('alice', 0, _m1_alicetalk__mood)
        jump Waiting


label second_talk_smoke:
    $ _m1_alicetalk__mood = 0
    menu:
        Alice_12 "А, Макс... Чего хотел?"
        "Да хотел узнать, что ты куришь?" if True:
            menu:
                Alice_03 "Это так важно для тебя? Почему спрашиваешь?"
                "Просто любопытно" if True:
                    Alice_00 "Любопытный он... Это сигареты Lucky Strike..."
                "Для поддержания разговора" if True:
                    Alice_00 "Да уж, поддержание разговора... А курю я сигареты Lucky Strike..."
                "А, не важно..." if True:
                    Alice_00 "Ну, раз не важно, то и не скажу..."
                    Max_01 "Конечно, если это секрет..."
                    Alice_01 "Вот ты зануда, Макс! Обычные сигареты Lucky Strike..."
        "Нет, ничего..." if True:
            jump Waiting
    Max_07 "Они же не женские?!"
    menu:
        Alice_13 "Ну да... Просто нравится именно эти. Их наш отец курил, сначала запах нравился. Когда выросла, попробовала и теперь вот втянулась..."
        "Скучаешь о нём?" if True:
            Alice_00 "Ну так, не очень, если честно. Уже слишком много времени прошло... А сигареты - это так, привычка..."
            Max_00 "Может, и мне попробовать?"
        "Может, и мне попробовать?" if True:
            pass
    menu:
        Alice_06 "Нет уж, самой мало. Знаешь, как сложно их достать? Особенно, чтобы мама не узнала..."
        "Может быть, тебе помочь?" if True:
            $ _m1_alicetalk__mood += 100
            menu:
                Alice_02 "С чем? Можешь доставать такие сигареты?"
                "Ну, я попробую через интернет" if True:
                    pass
                "Может быть..." if True:
                    pass
            Alice_03 "Давай! Было бы чудненько. Только маме не пали меня, а то я на тебя обижусь и больше никогда разговаривать не буду..."
            Max_05 "Договорились!"
        "Ну и ладно..." if True:

            $ _m1_alicetalk__mood += 50
            Alice_12 "Я закончила. Если мама спросит, скажешь, от соседей надуло, хорошо?"
            Max_01 "Конечно!"

    $ AddRelMood('alice', 5, _m1_alicetalk__mood)
    $ items['cigarettes'].unblock()
    $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    $ alice.dcv.special.stage = 2
    $ alice.dcv.special.set_lost(1)
    $ AvailableActions['searchciga'].enabled = True
    $ spent_time = 30 - int(tm[-2:])
    jump Waiting


label gift_cigarettes:
    $ _m1_alicetalk__mood = 0
    menu:
        Alice_03 "Это то, что я думаю? Давай сюда!"
        "А что взамен?" if True:
            Alice_13 "Макс! Не будь придурком. Давай сюда!"
            Max_01 "Ну, держи..."
        "Только давай условимся, что ты не скажешь маме о том, как я за тобой подглядывал в душе..." if alice.daily.shower == 3:
            Alice_12 "Хоть ты и тот ещё извращенец, Макс, но мне было сложно достать эти сигареты самой... Так и быть, мама ничего не узнает, по крайней мере в этот раз."
            Max_05 "Спасибо, Алиса! И я не извращенец. Просто проходил мимо, а там такая красотища..."
            Alice_05 "Ну да, ну да... Мимо он проходил..."
            $ punreason[1] = 0
            $ alice.daily.shower = 0
        "Держи!" if True:
            if alice.GetMood()[0] < -1:
                Alice_05 "Хотя ты и полный придурок, но, похоже, начинаешь исправляться!"
                Max_08 "Я не полный придурок!"
                $ _m1_alicetalk__mood += 50
            elif True:
                Alice_07 "Спасибо, Макс. Вот теперь я понимаю, ты настоящий брат!"
                Max_05 "Да не за что..."
    Alice_03 "Спасибо. И маме ни слова! У неё рука очень тяжёлая, особенно когда речь о сигаретах..."
    Max_01 "Конечно!"
    $ items['cigarettes'].use()
    $ _m1_alicetalk__mood += 100
    $ spent_time += 10
    $ alice.dcv.special.set_lost(0)
    $ AddRelMood('alice', 10, _m1_alicetalk__mood, 3)
    return


label smoke_nofear:
    Alice_00 "Макс, поглазеть пришёл?"
    Max_09 "Не боишься, что мама накажет, если узнает?"
    menu:
        Alice_03 "И как она узнает? Ты расскажешь?"
        "Может быть..." if True:
            Alice_12 "Ты хорошо подумал, Макс? Жизнь-то у тебя одна... И что ты хочешь за... молчание?"
            Max_01 "Вот это разговор!"
            menu:
                Alice_13 "Сначала скажи, что у тебя на уме..."
                "Дай $20, и я буду молчать" if True:
                    pass
                "Если днем ты будешь ходить без трусов, буду молчать" if True:
                    pass
                "Если будешь курить без верха, буду молчать" if True:
                    pass
                "Если разрешишь тебя отшлёпать, ничего не скажу" if True:
                    pass
                "Ничего. Не переживай!" if True:
                    jump smoke_nofear.no
            Alice_16 "А больше ты ничего не хочешь? Свали отсюда, пока не наваляла!!"
            $ AddRelMood('alice', 0, -100)
            $ poss['smoke'].open(2)
            $ alice.dcv.set_up.enabled = True
            $ punalice.append([2, 0, 0, 0, 0,])
            $ spent_time = 10
            jump Waiting
        "Нет, конечно!" if True:
            jump smoke_nofear.no
    menu smoke_nofear.no:
        Alice_03 "Ну вот и пугать не надо. Не узнает. А если ты проболтаешься, я тебя во сне придушу, понял? Теперь иди, не мешай мне..."
        "Угу..." if True:
            $ AddRelMood('alice', 0, 30)
            $ spent_time = 10
            jump Waiting


label smoke_fear:
    Alice_00 "Макс, поглазеть пришёл?"
    Max_09 "Не боишься, что мама накажет если узнает?"
    Alice_12 "Ты же ей не скажешь? Она так больно меня отшлёпала в прошлый раз, что до сих пор сидеть неприятно..."
    Max_01 "Ну, это зависит от тебя..."
    $ _ch8 = GetChanceConvince(punalice, 8)
    $ _ch4 = GetChanceConvince(punalice, 4)
    $ _ch3 = GetChanceConvince(punalice, 3)
    $ _ch2 = GetChanceConvince(punalice, 2)
    $ _ch1 = GetChanceConvince(punalice)
    $ _m1_alicetalk__can_nojeans = all(['kira' in chars, alice.clothes.casual.cur==0, 'pajamas' in alice.gifts])
    menu:
        Alice_13 "Говори, что ты хочешь за молчание?"
        "Дай $20, и я ничего не скажу {color=[_ch8.col]}(Убеждение. Шанс: [_ch8.vis]){/color}" if True:
            jump smoke_fear.money
        "Если днем ты будешь ходить без трусов, буду молчать {color=[_ch4.col]}(Убеждение. Шанс: [_ch4.vis]){/color}" if alice.clothes.casual.cur==0:

            jump smoke_fear.nopants
        "Если больше не будешь носить лифчик, буду молчать {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}" if True:
            jump smoke_fear.sleep_toples
        "Если будешь курить без верха купальника, буду молчать {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}" if True:
            jump smoke_fear.smoke_toples
        "Если хочешь, чтобы мама ничего не знала, ты будешь ходить без джинсов." if _m1_alicetalk__can_nojeans:
            Alice_12 "Ходить без джинсов? А ты не обнаглел, Макс?!"
            Max_01 "Нет, нисколько. Согласна?"
            Alice_05 "И как ты себе это представляешь? Или в твоей извращённой фантазии мама просто не заметит, что я расхаживаю по дому в трусах?!"
            Max_02 "А ты снимай джинсы когда её нет дома и всё будет в порядке."
            Alice_13 "Ладно, тётя Кира ещё может на это и не обратит внимание, а если Лиза спросит, почему я без штанов?"
            Max_08 "Ой, Алиса, хватит уже искать отговорки... Как будто тебе бы и в голову не пришло сказать ей, что дома просто жарко."
            menu:
                Alice_06 "Лучше попроси что-то другое..."
                "Нет. Или получаешь вечером по заднице или не одеваешь джинсы. {color=[_ch2.col]}(Убеждение. Шанс: [_ch2.vis]){/color}" if True:
                    if RandomChance(_ch2.ch):
                        $ Skill('social', 0.2)
                        $ poss['smoke'].open(4)
                        menu:
                            Alice_03 "[succes!t]Хорошо. Не буду я одевать джинсы, только дай уже покурить спокойно!"
                            "Конечно!" if True:
                                $ punalice[0][0] = 7
                                $ alice.req.req = "nojeans"
                                $ alice.req.result = "nojeans"
                                $ added_mem_var('nojeans')
                                jump smoke_fear.end
                    elif True:
                        jump smoke_fear.fail2
                "Дай $20, и я ничего не скажу {color=[_ch8.col]}(Убеждение. Шанс: [_ch8.vis]){/color}" if True:
                    jump smoke_fear.money
                "Если днем ты будешь ходить без трусов, буду молчать {color=[_ch4.col]}(Убеждение. Шанс: [_ch4.vis]){/color}" if alice.clothes.casual.cur==0:

                    jump smoke_fear.nopants
                "Если больше не будешь носить лифчик, буду молчать {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}" if True:
                    jump smoke_fear.sleep_toples
                "Если будешь курить без верха купальника, буду молчать {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}" if True:
                    jump smoke_fear.smoke_toples
        "Если разрешишь тебя отшлёпать, то я ничего не скажу!" if alice.dcv.private.stage > 4 and not alice.spanked:

            if not alice.dcv.private.done:

                jump alice_private_punish_r.smoke
            elif True:
                if not (punalice[1][2] or punalice[1][3]):

                    Alice_12 "Это ещё с чего, Макс?! Меня же не наказывали! А мы договаривались, если ты меня спас от мамы, то и отшлёпать можешь..." nointeract
                elif True:

                    Alice_12 "Это ещё с чего, Макс?! Ты же мою попку от мамы не спас! А мы договаривались, если ты меня выручаешь, то и отшлёпать можешь..." nointeract
                menu:
                    "Но сейчас тебя есть за что отшлёпать! {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)

                            Alice_05 "[succes!t]Ну... Только если легонько! Понял?! Только докурю сперва в тишине и покое..."
                            menu:
                                Max_03 "Хорошо. Я подожду..."
                                "{i}подождать Алису{/i}" if True:
                                    jump alice_private_punish_r.smoke_pun
                        elif True:
                            menu:
                                Alice_16 "[failed!t]Нет уж! Что-то другое ещё можешь попробовать выпросить, но к своей попке я тебя сегодня не подпущу."
                                "Дай $20, и я ничего не скажу {color=[_ch8.col]}(Убеждение. Шанс: [_ch8.vis]){/color}" if True:
                                    jump smoke_fear.money
                                "Если днем ты будешь ходить без трусов, буду молчать {color=[_ch4.col]}(Убеждение. Шанс: [_ch4.vis]){/color}" if alice.clothes.casual.cur==0:

                                    jump smoke_fear.nopants
                                "Если больше не будешь носить лифчик, буду молчать {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}" if True:
                                    jump smoke_fear.sleep_toples
                                "Если будешь курить без верха купальника, буду молчать {color=[_ch3.col]}(Убеждение. Шанс: [_ch3.vis]){/color}" if True:
                                    jump smoke_fear.smoke_toples
        "Хочу, чтобы ты спала голой! {color=[_ch2.col]}(Убеждение. Шанс: [_ch2.vis]){/color}" if all([eric.stat.mast, alice.flags.nakedpunish, flags.eric_photo1>0]):

            if RandomChance(_ch2.ch):
                $ Skill('social', 0.2)
                Alice_14 "Голой? Прямо совсем-совсем голой?! Что, фантазия закончилась, скатился до самого простейшего?"
                Max_07 "То же голое наказание, только без шлёпающей по твоей чудесной попке руки мамы. Просто подумал, ты бы и сама этого хотела."
                Alice_12 "Я то совсем не против спать голой, только вот ты же неспроста этого хочешь... Задумал что-то, Макс?! Ну-ка признавайся!"
                Max_03 "Всё ты какого-то подвоха от меня ждёшь! Спи себе голенькой в удовольствие, а мне уже от одной этой мысли на душе приятно."
                Alice_05 "Не знаю, зачем тебе, извращенцу, это нужно, но лучше я соглашусь на этот пустяк... Пока ты что-нибудь ещё не попросил."
                Max_04 "Вот и отлично!"
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                $ punalice[0][0] = 8
                $ alice.req.req = "naked"
                $ alice.req.result = "naked"
                $ alice.sleepnaked = True
                $ added_mem_var('alice_sleepnaked')
                jump smoke_fear.end
            elif True:
                jump smoke_fear.fail
        "Ты знаешь, я сегодня добрый..." if True:
            $ punalice[0][0] = 1
            menu:
                Alice_06 "Сегодня? Значит, попросишь в следующий раз?"
                "Как знать, может быть..." if True:
                    pass
                "Что ты! Нет, конечно..." if True:
                    pass
            menu:
                Alice_13 "Ну вот тогда иди чем-нибудь займись, а меня не отвлекай..."
                "{i}уйти{/i}" if True:
                    $ alice.req.reset()
                    jump smoke_fear.end

    label smoke_fear.smoke_toples:
        if RandomChance(_ch3.ch):
            $ Skill('social', 0.2)
            $ poss['smoke'].open(4)
            Alice_12 "[succes!t]Маленький извращенец... Ладно, но при условии, что маме не будешь ничего говорить. И разденусь только с завтрашнего дня. Договорились?"
            Max_03 "Само собой!"
            $ punalice[0][0] = 4
            $ alice.req.req = "toples"
            menu:
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                "{i}уйти{/i}" if True:
                    jump smoke_fear.end
        elif True:
            jump smoke_fear.fail

    label smoke_fear.sleep_toples:
        if RandomChance(_ch3.ch):
            $ Skill('social', 0.2)
            $ poss['smoke'].open(4)
            Alice_03 "[succes!t]Да я вообще-то и так без лифчика все время хожу, только когда сплю одеваю..."
            Max_01 "Значит, тогда просто спи без него."
            Alice_05 "Не знаю, зачем тебе, извращенцу, это нужно, но лучше я соглашусь на этот пустяк... Пока ты что-нибудь ещё не попросил."
            Max_04 "Вот и отлично!"
            $ punalice[0][0] = 5
            $ alice.req.req = "sleep"
            $ alice.req.result = 'sleep'
            $ alice.sleeptoples = True
            $ added_mem_var('alice_sleeptoples')
            menu:
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                "{i}уйти{/i}" if True:
                    jump smoke_fear.end
        elif True:
            jump smoke_fear.fail

    label smoke_fear.nopants:
        if RandomChance(_ch4.ch):
            $ Skill('social', 0.2)
            $ poss['smoke'].open(4)
            Alice_13 "[succes!t]Тебя так заботят мои трусы? Ну, хорошо. Всё равно я почти всё время в джинсах, так что не страшно. Значит, договорились?"
            Max_02 "Конечно!"
            $ punalice[0][0] = 6
            $ alice.req.req = "nopants"
            $ alice.req.result = 'nopants'
            $ alice.nopants = True
            $ added_mem_var('alice_nopants')
            menu:
                Alice_01 "А теперь вали отсюда. Дай спокойно покурить!"
                "{i}уйти{/i}" if True:
                    jump smoke_fear.end
        elif True:
            jump smoke_fear.fail

    label smoke_fear.money:
        if RandomChance(_ch8.ch):
            $ poss['smoke'].open(4)
            $ punalice[0][0] = 3
            $ spent_time += 10
            $ Skill('social', 0.2)
            $ _ch2 = GetChanceConvince(punalice, 2)
            $ alice.req.req = 'money'
            menu:
                Alice_12 "[succes!t]Ладно, Макс, я дам тебе денег, но только $10, ок?"
                "Нет, давай $20 {color=[_ch2.col]}(Убеждение. Шанс: [_ch2.vis]){/color}" if True:
                    if RandomChance(_ch2.ch):
                        $ Skill('social', 0.2)
                        Alice_13 "[succes!t]Чёрт с тобой, Макс. Совсем без денег оставить хочешь... Сейчас принесу..."
                        Max_03 "Я жду..."
                        $ mgg.ask(1)
                        $ AddRelMood('alice', 0, -50)
                    elif True:
                        Alice_16 "[failed!t]Макс, не наглей! Сейчас принесу $10. Жди..."
                        Max_04 "Ну ладно, я жду..."
                        $ mgg.ask(0)
                        $ Skill('social', 0.1)
                        $ AddRelMood('alice', 0, -75)
                "Хорошо, устроит и $10" if True:
                    $ mgg.ask(0)
                    $ AddRelMood('alice', 0, -25)
            menu:
                Alice_12 "Держи свои деньги... И больше меня не шантажируй. Я очень это не люблю... А теперь вали отсюда!"
                "Удачи!" if True:
                    jump smoke_fear.end
        elif True:
            jump smoke_fear.fail

    menu smoke_fear.fail:
        Alice_16 "[failed!t]Ага, сейчас! Ну ты и хам, Макс... Всё, отвали, дай покурить спокойно..."
        "{i}уйти{/i}" if True:
            $ Skill('social', 0.1)
            $ alice.req.reset()
            $ punalice[0][0] = 2
            $ AddRelMood('alice', 0, -50)
            jump smoke_fear.end

    menu smoke_fear.fail2:
        Alice_12 "[failed!t]Вот так значит? А я вот выбираю вариант, в котором ты, может быть, останешься сегодня цел, если очень быстро свалишь отсюда и не будешь мне надоедать... Пока я ещё более-менее добрая."
        "{i}Ну, как скажешь...{/i}" if True:
            $ Skill('social', 0.1)
            $ alice.req.reset()
            $ punalice[0][0] = 2
            $ AddRelMood('alice', 0, -50)
            jump smoke_fear.end

    label smoke_fear.end:
        $ spent_time += 10
        jump Waiting


label smoke_toples:
    menu:
        Alice_02 "Ну что, извращенец, доволен видом?"
        "Доволен, конечно!" if True:
            menu:
                Alice_05 "Надеюсь, маме ничего не расскажешь? А то это опасно для твоей жизни..."
                "Не переживай, не скажу" if True:
                    Alice_04 "Вот и молодец. А теперь иди, займись чем-нибудь..."
                    Max_01 "Хорошо..."
                "Ну... это зависит от тебя!" if True:
                    Alice_09 "Макс, не играй с огнём! Мы договоривались. А теперь сгинь с глаз моих!"
                    Max_07 "Уже ухожу..."
                    $ AddRelMood('alice', 0, -50)
        "А чего ты прикрываешься?" if True:
            Alice_04 "А про руки мы не договаривались. Хочу - прикрываюсь. Хочу - нет. А тебя так радовать я точно не хочу... Так что вали уже..."
            Max_09 "Ну и ладно..."
        "Я передумал. Можешь одеться." if True:
            menu:
                Alice_12 "Спасибо, ваше величество! А чего это ты так расщедрился? Я больше не в твоём вкусе?"
                "Ну, я перегнул палку..." if True:
                    menu:
                        Alice_04 "Спасибо, Макс! Это мудрый поступок... Но ты можешь в последний раз поглазеть..."
                        "{i}уйти{/i}" if True:
                            $ AddRelMood('alice', 0, 100)
                "Это мой шаг к дружбе" if True:
                    menu:
                        Alice_03 "Даже так?! Ну, дружбу я не обещаю, но могу пытаться с тобой как-то уживаться. А если серьёзно, то спасибо, Макс. Я это оценила..."
                        "{i}уйти{/i}" if True:
                            $ AddRelMood('alice', 0, 120)
                "Да надоела!" if True:
                    menu:
                        Alice_15 "Что?! А ну-ка вали отсюда, пока цел! И оденусь теперь, будь уверен!"
                        "{i}свалить{/i}" if True:
                            pass
                "Ты знаешь, пусть всё остаётся как есть..." if True:
                    menu:
                        Alice_12 "Ах вот как? Опять передумал? Всё, ты мне надоел, свали отсюда!"
                        "{i}свалить{/i}" if True:
                            $ AddRelMood('alice', 0, -50)
                            $ spent_time += 10
                            jump Waiting
            $ alice.req.reset()
            $ alice.dcv.prudence.set_lost(0)

    label smoke_toples.end:
        $ spent_time += 10
        jump Waiting


label smoke_not_toples:
    Alice_02 "Ты чего-то хотел, Макс?"
    Max_07 "Да, хотел... Мы ведь договорились, что ты будешь курить без верха купальника!"
    Alice_13 "Знаешь, Макс, мне это надоело... Сколько можно? Я хочу спокойно курить и не волноваться, что ты за мной подглядываешь!"
    Max_09 "Ну хорошо, Алиса, как скажешь, можешь курить одетой. Только вот, если ты решила нарушить условия нашей договорённости, то почему бы тогда и мне не поступить так же?"
    Alice_06 "Только не надо маме рассказывать о об этом..."
    Max_00 "Всё зависит от тебя, сестрёнка... Если сейчас снимешь верх и в качестве извинения покажешь грудь, то я представлю, будто ты ничего не нарушала."
    Alice_15 "Ах ещё и грудь показать! Может сразу и полапать её дать?!"
    Max_03 "Очень заманчивое предложение... Но просто показать - я считаю справедливо! Сама накосячила..."

    $ renpy.show("Alice smoke "+renpy.random.choice(["01", "02", "03"])+"c")

    Alice_06 "Ладно, один разок и быстро... Но не вздумай маме рассказывать! Ни про это, ни про сигареты."
    Max_05 "Конечно, я ведь своё слово держу. Симпатичные сосочки!"
    menu:
        Alice_13 "Ну всё, полюбовался и хватит. Вали отсюда, дай спокойно покурить..."
        "Ага..." if True:
            pass
    $ renpy.show("Alice smoke "+pose3_3+alice.dress)
    $ alice.req.reset()
    $ alice.dcv.prudence.set_lost(0)
    $ spent_time += 10
    $ current_room = house[5]
    jump Waiting


label smoke_nopants:
    menu:
        Alice_02 "Макс, чего хотел?"
        "Ничего, просто любуюсь..." if True:
            Alice_13 "Налюбовался? А вот теперь постой в сторонке, пока я покурю! Давай, вали уже..."
            Max_01 "Хорошо, хорошо..."
        "А ты чего в трусах?" if True:
            menu:
                Alice_12 "В каком смысле?!"
                "Мы же договорились - без трусов!" if True:
                    Alice_01 "Ты совсем идиот, Макс? Я в купальнике. Это не трусы. А трусы я и так не ношу под джинсами. Можешь себе фантазировать теперь сколько хочешь... Всё, уйди с глаз моих долой!"
                    Max_01 "Ухожу, ухожу..."
                "Да шучу я..." if True:
                    Alice_02 "Ты наверное думаешь, что у тебя забавные шутки, да? Так вот нет. Абсолютно несмешные, дебильные шутки, как и ты сам. Всё, свалил отсюда. Я занята..."
                    Max_01 "Как скажешь..."
        "Я передумал. Можешь носить трусы..." if True:
            menu:
                Alice_03 "А чего передумал? А, хотя не важно. Я рада, а то мне всё натирает в джинсах... Хотя, тебе такие подробности знать не нужно. Спасибо за разрешение, ваше величество. Теперь дай покурю..."
                "{i}уйти{/i}" if True:
                    $ alice.req.reset()
                    $ alice.dcv.prudence.set_lost(0)
                    $ alice.nopants = False
                    $ AddRelMood('alice', 0, 100)

    $ spent_time += 10
    jump Waiting


label smoke_not_nopants:
    Alice_02 "Ты чего-то хотел, Макс?"
    Max_09 "Алиса, ну что за дела?! Я думал у нас уговор!"
    Alice_06 "Это ты сейчас о чём, Макс?"
    Max_08 "Мы ведь договорились, что ты не будешь одевать трусы днём. А я их на тебе видел!"
    Alice_14 "А мне вот интересно, когда это ты их мог увидеть?! Подглядывал, как я одеваюсь?"
    Max_07 "Да здесь и подглядывать не нужно, они у тебя иногда прямо из-под джинс слегка торчат... Так что важно не то, как и где я это увидел, а то, что они на тебе были!"
    Alice_00 "Ладно, ладно, признаю, я их снова ношу, потому что без них мне все натирает. Да и мама, если видит, что я без трусов во время наказания, шлепает гораздо сильней."
    Max_00 "Ну хорошо, я тебя освобождаю от уговора. Но только, если в качестве компенсации ты прямо сейчас покажешь мне сиськи!"
    Alice_16 "А не многого ли ты, мелкий извращенец, хочешь?!"
    Max_01 "Посмотреть на красивые сиськи - не извращение! И мне кажется, проще один раз показать, чем всё натирать будет..."

    $ renpy.show("Alice smoke "+renpy.random.choice(["01", "02", "03"])+"c")

    Alice_06 "Ну на, любуйся, раз уж и дня не можешь прожить без извращений."
    Max_03 "Классные сиськи!"
    Alice_13 "Спасибо. А теперь иди уже, погуляй где-нибудь. Дай докурить спокойно."
    Max_01 "Хорошо. Я ушёл..."

    $ added_mem_var('alice_not_nopants')
    $ renpy.show("Alice smoke "+pose3_3+alice.dress)
    $ alice.req.reset()
    $ alice.dcv.prudence.set_lost(0)
    $ spent_time += 10
    $ current_room = house[5]
    jump Waiting


label smoke_sleep:
    menu:
        Alice_02 "Макс, чего хотел?"
        "Ничего, просто любуюсь..." if True:
            Alice_13 "Налюбовался? А вот теперь постой в сторонке, пока я покурю! Давай, вали уже..."
            Max_01 "Хорошо, хорошо..."
            $ spent_time += 10
            jump Waiting

        "Я передумал. Ты можешь спать в лифчике, если хочешь." if alice.req.req=='sleep':
            pass
        "Я передумал. Ты можешь спать в нижнем белье..." if alice.req.req=='naked':
            pass
    menu:
        Alice_04 "А чего это ты передумал? А, хотя не важно. Я рада, а то мне неудобно ночью, если выйти куда-то нужно, да и мама заметить может. Спасибо за разрешение, ваше величество. Теперь дай покурю..."
        "{i}уйти{/i}" if True:
            pass

    $ alice.req.reset()
    $ alice.dcv.prudence.set_lost(0)
    $ AddRelMood('alice', 0, 100)

    $ spent_time += 10
    jump Waiting

label smoke_nojeans:
    menu:
        Alice_02 "Макс, чего хотел?"
        "Ничего, просто любуюсь..." if True:
            Alice_13 "Налюбовался? А вот теперь постой в сторонке, пока я покурю! Давай, иди уже..."
            Max_01 "Ладно, ладно, как скажешь..."
        "Я передумал. Ты можешь носить свои джинсы, если захочешь." if True:
            menu:
                Alice_04 "Чего это ты вдруг передумал? Надоело глазеть на мою попку? А, не важно. Спасибо за разрешение, ваше величество. Теперь дай покурю..."
                "{i}уйти{/i}" if True:
                    $ alice.req.reset()
                    $ alice.dcv.prudence.set_lost(0)
                    $ AddRelMood('alice', 0, 100)
    $ spent_time += 10
    jump Waiting


label Alice_sorry:
    if len(alice.sorry.give) == 0:
        Alice_15 "Ух ты, у тебя, извращенца мелкого, совесть проснулась?! Неожиданно..."
        Max_10 "Нет, я думаю, ты вряд ли правильно поняла то, что случилось. Я за тобой не подглядывал..."
        Alice_16 "Макс, я по-твоему полная дура что ли?! Ты стоял за стеной, и нагло смотрел, как я принимала душ!"
        Max_14 "Но на деле же, так получилось не специально... Я просто шёл мимо..."
        Alice_05 "Да, да, конечно... Я очень хочу посмотреть, что с тобой сделает мама, когда об этом узнает..."
        Max_10 "Да, знаю, в такое очень трудно поверить, но я просто шёл мимо, а ты душ как раз принимала... Ну я и отскочил к стене... где ты меня и заметила... Вот и всё, я даже и не видел ничего такого!"
        Alice_03 "Ну вот никак мне в это не верится, Макс! Никаких твоих оправданий не хватит, чтобы я в это поверила."
        Max_07 "В таком случае, предлагаю представить, что ничего такого утром не было. Ты ничего не говоришь маме, а я в свою очередь куплю тебе чего-нибудь вкусненького?"
        if GetWeekday(day) == 6:
            Alice_08 "Ах ты... паршивец... Это подлый ход, потому что от вкусняшки я бы не отказалась... Хорошо, но обещать ничего не буду, сперва посмотрю, что это будет за вкусность... Если ты конечно успеешь до вечера понедельника!"
            Max_01 "Обязательно успею! В понедельник всё будет..."
        elif True:
            Alice_08 "Ах ты... паршивец... Это подлый ход, потому что от вкусняшки я бы не отказалась... Хорошо, но обещать ничего не буду, сперва посмотрю, что это будет за вкусность... Если ты конечно успеешь до завтрашего вечера!"
            Max_01 "Обязательно успею! Завтра всё будет..."
        Alice_07 "И смотри, чтобы мне понравилось..."
        Max_04 "Хорошо."
        $ alice.sorry.valid = {'ritter-m', 'raffaello-m', 'ferrero-m'}
        if not all([items['ritter-m'].InShop, items['raffaello-m'].InShop, items['ferrero-m'].InShop]):
            $ notify_list.append(_("В интернет-магазине доступен новый товар."))
        $ items['ritter-m'].unblock()
        $ items['raffaello-m'].unblock()
        $ items['ferrero-m'].unblock()
        $ poss['risk'].open(0)
    elif len(alice.sorry.give) == 1:
        Alice_03 "Ой, Макс, конечно же я тебя прощаю! Не переживай ты так... Всё прекрасно!"
        Max_09 "Э-э-э... Правда?!"
        Alice_16 "Конечно нет, дубина! Стоял снова и глазел на меня голую! Мама обязательно об этом узнает..."
        Max_08 "А вдруг это была случайность и ты напрасно меня сдашь?"
        Alice_12 "Макс, какая это случайность, стоять за углом и глазеть на меня?!"
        Max_07 "Понимаю, верится с большим трудом. Тогда давай это разрешим без мамы?"
        Alice_05 "Снова хочешь попробовать купить моё молчание сладостью? Серьёзно?!"
        Max_10 "Да, серьёзно! Попытка - не пытка..."
        Alice_02 "Ты, конечно, можешь попробовать, от чего-нибудь сладенького я не откажусь, но ты же понимаешь, что мне должно это очень понравиться."
        if GetWeekday(day) == 6:
            Max_01 "Значит, до ужина понедельника?"
        elif True:
            Max_01 "Значит, до следующего ужина?"
        Alice_05 "Ничего не обещаю, но не опаздывай, Макс!"
        Max_04 "Постараюсь."
    elif len(alice.sorry.give) == 2:
        Alice_05 "Макс, а давай всё упростим до того, что ты сейчас уходишь покупать мне конфеты, а я их жду до следующего ужина? Как тебе, а?!"
        Max_08 "Можно и так... Только мне как-то немного не по себе от того, что это предлагаешь ты, а не я!"
        Alice_03 "Просто экономлю время, которое тебе лучше потратить на то, чтобы я в итоге осталась очень довольна этим."
        Max_07 "Тогда я пойду, да?"
        Alice_01 "Бегом! Извращенец тормозной..."
        Max_01 "Ага..."
    elif len(alice.sorry.give) == 3 and 'pajamas' not in alice.gifts:
        Alice_05 "Но ведь не только это! Ясно же, что снова пообещаешь вкусняшку за моё молчание."
        Max_07 "Ну а что мне ещё остаётся?"
        Alice_03 "Только вот на этот раз Я буду ставить условия! Сладости - это хорошо, но я хочу большего..."
        Max_09 "И чего такого ты хочешь?"
        Alice_07 "Хочу себе новую одежду, а то надоело в одном и том же дома сидеть. А именно - пижаму!"
        Max_05 "Пижаму?! А при чём тут пижама, в ней же спать положено? А если надоела одежда, просто сними её и сиди в нижнем белье. Или голая!"
        Alice_05 "Конечно, тебе бы это понравилось! Но я не хочу спать в пижаме. Я почти всё время провожу дома и хочу одевать что-то лёгкое."
        Max_07 "Тогда это должна быть какая-нибудь коротенькая пижама!"
        Alice_02 "Именно! Хочу лёгкие топик и шортики для дома. И ты мне их купишь, если не хочешь получить по заднице от мамы."
        Max_08 "Хорошо, но мне нужно больше времени..."
        Alice_01 "Согласна подождать три дня. А ты не тормози..."
        Max_00 "Хорошо."
        $ alice.sorry.valid.clear()
        $ punreason[1] = 0
        $ alice.daily.shower = 0
        $ items['pajamas'].unblock()
        $ alice.sorry.start(3)
        $ spent_time += 10
        $ poss['risk'].open(7)
        jump Waiting

    $ punreason[1] = 0
    $ alice.daily.shower = 0
    $ alice.sorry.start()
    $ spent_time += 10
    jump Waiting


label gift_dress:
    Alice_15 "Макс? Это платье для клуба? Правда?!"
    Max_01 "Ага..."
    menu:
        Alice_07 "Спасибо, Макс! Ты такой... Не знаю даже, я просто в шоке!"
        "Держи..." if True:
            jump gift_dress.gift
        "Не так быстро..." if True:
            menu:
                Alice_02 "Так и знала, что есть какой-то подвох... И что ты хочешь за него?"
                "Да ничего, просто держи..." if True:
                    jump gift_dress.gift
                "Устрой мне показ в нём..." if True:
                    Alice_05 "Ты хочешь, чтобы я его примерила прямо при тебе?"
                    Max_03 "Конечно! Я это и хочу!"
                    Alice_03 "Макс... А жить... хочешь?"
                    Max_07 "Эй, что за угрозы?"
                    jump gift_dress.newdress_show

    label gift_dress.gift:
        Alice_02 "Вот так вот сразу и без подвоха? Обалдеть... Не ожидала от тебя, Макс... Спасибо!"
        Max_04 "Не за что!"
        $ AddRelMood('alice', 0, 300)
        $ AttitudeChange('alice', 0.9)
        jump gift_dress.end

    label gift_dress.newdress_show:
        if '09:00' <= tm < '20:00':
            $ _m1_alicetalk__suf = ""
        elif True:
            $ _m1_alicetalk__suf = "a"

        if "06:00" <= tm < "11:00":
            scene location house aliceroom door-morning
        elif "11:00" <= tm < "18:00":
            scene location house aliceroom door-day
        elif "18:00" <= tm < "22:00":
            scene location house aliceroom door-evening
        elif True:
            scene location house aliceroom door-night

        menu:
            Alice_03 "Жди за дверью. Я сейчас надену платье и тебе покажу, так уж и быть..."
            "Э... Хорошо..." if True:
                pass
        if _m1_alicetalk__suf == "":
            scene BG char Alice newdress
        elif True:
            scene BG char Alice spider-night-05
        $ renpy.show("Alice newdress 01"+_m1_alicetalk__suf)
        Alice_05 "Ну как, Макс? Мне идёт?"
        Max_05 "Выглядишь... шикарно!"
        $ renpy.show("Alice newdress 02"+_m1_alicetalk__suf)
        Alice_07 "Спасибо, Макс! Честно говоря, я не ожидала от тебя такого подарка. Спасибо! И..."
        Max_07 "И?"
        $ renpy.show("Alice newdress 03"+_m1_alicetalk__suf)
        menu:
            Alice_05 "...И небольшой бонус. Я знаю, что ты ждал чего-то подобного..."
            "Очень... очень хорошо..." if True:
                pass
            "А можешь наклониться?" if True:
                pass
        $ renpy.show("Alice newdress 04"+_m1_alicetalk__suf)
        Alice_02 "Хорошего в меру... Правда, ты меня очень сильно выручил. Спасибо ещё раз!"
        Max_01 "Не за что!"
        $ AddRelMood('alice', 0, 200)
        $ AttitudeChange('alice', 0.9)
        $ spent_time += max((50 - int(tm[-2:])), 30)
        $ current_room = house[5]

    label gift_dress.end:
        $ items['dress'].give()
        $ poss['nightclub'].open(4)
        $ alice.gifts.append('dress')
        $ alice.dcv.feature.set_lost(1)
        $ infl[alice].add_m(40, True)
        $ spent_time += 10
        jump Waiting


label gift_book:
    if items['erobook_1'].have:
        Alice_02 "У тебя для меня подарок? У ТЕБЯ... для МЕНЯ? Какая прелесть. Давай, показывай, что за книжка?"
        Max_01 "Держи..."
        menu:
            Alice_01 "Прикольно... Давно хотела её почитать. А ты как узнал, что мне такие нравятся?"
            "Порылся в твоих вещах и нашёл, что читаешь!" if True:
                Alice_14 "Что?! Да как ты посмел?!"
                Max_02 "Да я пошутил. Просто угадал!"
                Alice_13 "Шуточки у тебя, как и прежде, дурацкие! А книжку я возьму. Молодец, что угадал... Спасибо."
                Max_04 "Не за что"
            "Ну, я догадался! Я же умный!" if True:
                Alice_07 "Умный он... Ну, молодец, что догадался. Спасибо, Макс! Если ещё попадутся из этой серии, буду рада принять их от тебя. Безвозмездно!"
                Max_04 "Хорошо..."
            "Я и не знал. Просто угадал видимо..." if True:
                Alice_05 "Поздравляю, попал в десятку! Если найдёшь ещё что-то подобное, буду рада такому подарку. Даже от тебя..."
                Max_04 "Ну, если даже от меня, то ладно..."
        $ poss['secretbook'].open(3)
        $ AddRelMood('alice', 0, 100)
        $ AttitudeChange('alice', 0.25)
        $ items['erobook_1'].give()
        $ alice.gifts.append('erobook_1')
        $ alice.dcv.gifts.set_lost(7)
        $ alice.dcv.gifts.stage = 2
    elif items['erobook_2'].have:
        Alice_04 "Да? И какая на этот раз? Давай сюда..."
        Max_01 "Держи..."
        Alice_07 "Супер! Ты меня удивляешь, Макс! Если ещё что будет почитать, приноси. Я люблю подобную... литературу."
        Max_04 "Конечно!"
        $ AddRelMood('alice', 0, 120)
        $ AttitudeChange('alice', 0.3)
        $ items['erobook_2'].give()
        $ alice.gifts.append('erobook_2')
        $ alice.dcv.gifts.set_lost(9)
        $ alice.dcv.gifts.stage = 3
    elif items['erobook_3'].have or items['erobook_4'].have:
        Alice_04 "Супер! Давай, показывай, что тут у нас..."
        Max_01 "Держи..."
        Alice_05 "То, что нужно! Если ещё что будет почитать, приноси. Ты же знаешь, как я люблю такие книги..."
        Max_04 "Конечно!"
        $ AddRelMood('alice', 0, 100)
        $ AttitudeChange('alice', 0.25)
        if items['erobook_4'].have:
            $ items['erobook_4'].give()
            $ alice.gifts.append('erobook_4')
            $ alice.dcv.gifts.set_lost(13)
            $ alice.dcv.gifts.stage = 5
        elif True:
            $ items['erobook_3'].give()
            $ alice.gifts.append('erobook_3')
            $ alice.dcv.gifts.set_lost(11)
            $ alice.dcv.gifts.stage = 4
    elif items['erobook_5'].have:
        Alice_04 "Да? И какая на этот раз? Давай сюда..."
        Max_01 "Держи..."
        Alice_07 "Забавная книжка. Давно хотела почитать... Спасибо, Макс. Ты меня балуешь!"
        Max_04 "Конечно!"
        $ AddRelMood('alice', 0, 160)
        $ AttitudeChange('alice', 0.4)
        $ items['erobook_5'].give()
        $ alice.dcv.gifts.stage = 6
        $ alice.gifts.append('erobook_5')

    $ spent_time += 10
    return


label gift_pajamas:
    if not _in_replay:
        $ _ch1 = GetChance(mgg.social, 3, 900)
        if 'gift_pajamas' not in persistent.memories:
            $ persistent.memories['gift_pajamas'] = -1
    elif True:

        if alice.plan_name == 'sun':
            call alice_sun from _call_alice_sun
        elif True:
            if tm > '20:00':
                call alice_evening_closer from _call_alice_evening_closer
            elif True:
                call alice_morning_closer from _call_alice_morning_closer
    Alice_06 "Только скажи, что это пижамка, а не сладости! Ты же купил то, что я просила?!"
    Max_04 "Конечно! Топик и шортики, как ты хотела. Вот, держи..."
    Alice_07 "О да! Какие симпатичные! Ты такой молодец, Макс! Спасибо тебе большое..."
    Max_03 "Ну что, примеришь при мне?"
    if not alice.sorry.owe:
        Alice_04 "А жирно тебе не будет?! В душе не нагляделся на меня и теперь хочешь подсмотреть, как я переодеваюсь, да?"
        Max_01 "Нет, просто хотел увидеть, как на тебе будет смотреться пижама..."
        Alice_05 "Ладно, поверю... Ого, а что это у тебя здесь..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."

    elif alice.flags.hugs_type > 3:
        if not _in_replay:
            $ persistent.memories['gift_pajamas'] = 1
            $ poss['risk'].open(8)
        Alice_03 "Примерю при тебе? Об этом мы не договаривались. Я покажусь в ней, но... Хотя, ладно. Примерю при тебе, но ты не подглядывай! Увижу, что смотришь, получишь и пойдёшь в бассейн. Вниз головой."
        Max_02 "Как страшно... Давай уже, примеряй."
        scene BG char Alice newpajamas
        $ _m1_alicetalk__suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
        if not ('09:00' <= tm < '20:00'):
            $ _m1_alicetalk__suf += 'e'
        $ renpy.show('Alice newpajamas 01'+_m1_alicetalk__suf)
        if not _in_replay:
            $ SetCamsGrow(house[1], 150)
        menu:
            Alice_05 "Макс, у тебя же есть инстинкт самосохранения, верно? Не вздумай подглядывать!"
            "Ага, я и не подглядываю..." if True:
                if renpy.random.randint(0, 1):
                    $ renpy.show('Alice newpajamas 02'+_m1_alicetalk__suf)
                    Alice_01 "Макс! Ты что, пялишься на мою грудь? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"
                    Max_03 "Я не пялюсь..."
                    $ renpy.show('Alice newpajamas 04'+_m1_alicetalk__suf)
                    Alice_02 "Похоже, размер мне подходит... и удобно. Очень лёгонький топик. Ну, как тебе?"
                    Max_04 "Тебе идёт! Мне нравится..."
                    if alice.req.result != 'nopants':
                        Alice_03 "Отлично! А теперь отвернись, не подглядывай! Нужно ещё шортики примерить."
                        if not _in_replay:
                            $ SetCamsGrow(house[1], 180)
                    elif True:
                        Alice_05 "Класс! А теперь быстро отвернись, а то на мне трусиков нет, благодаря твоим уговорам! Нужно ещё шортики примерить."
                    $ _m1_alicetalk__suf = 'an' if any([alice.plan_name in ['sun', 'swim'], alice.dress=='d', alice.req.result == 'nopants']) else 'a'
                    if not ('09:00' <= tm < '20:00'):
                        $ _m1_alicetalk__suf += 'e'
                    $ renpy.show('Alice newpajamas 06'+_m1_alicetalk__suf)
                    if any([alice.req.result != 'not_nopants', alice.plan_name in ['sun', 'swim'], alice.dress=='d']):
                        Max_02 "Конечно, я не смотрю..."
                    elif True:
                        Max_08 "Конечно, я не смотрю... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"
                        Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                        Max_01 "Ладно, считай, я ничего не видел."
                    if '09:00' <= tm < '20:00':
                        show Alice newpajamas 08
                    elif True:
                        show Alice newpajamas 08e
                    Alice_07 "Размер в самый раз... Удобненько и легко. Как тебе, Макс? Хорошо сидит?"
                    Max_05 "Не то слово, всё выглядит шикарно!"
                elif True:
                    $ _m1_alicetalk__suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
                    if _m1_alicetalk__suf=='a' and alice.req.result == 'nopants':
                        $ _m1_alicetalk__suf += 'n'
                    if not ('09:00' <= tm < '20:00'):
                        $ _m1_alicetalk__suf += 'e'
                    $ renpy.show('Alice newpajamas 03'+_m1_alicetalk__suf)
                    if alice.req.result != 'nopants':
                        Alice_03 "Макс! Ты что, пялишься на мой зад? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"
                    elif True:
                        if not _in_replay:
                            $ SetCamsGrow(house[1], 180)
                        Alice_05 "Макс! Ты что, пялишься на мой зад? Быстро отвернись, на мне же нет трусиков, благодаря твоим уговорам!"
                    if alice.req.result != 'not_nopants' or alice.plan_name in ['sun', 'swim']:
                        Max_02 "Я не пялюсь..."
                    elif True:
                        Max_08 "Я не пялюсь... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"
                        Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                        Max_01 "Ладно, считай, я ничего не видел."
                    $ _m1_alicetalk__suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
                    if not ('09:00' <= tm < '20:00'):
                        $ _m1_alicetalk__suf += 'e'
                    $ renpy.show('Alice newpajamas 05'+_m1_alicetalk__suf)
                    Alice_02 "Размер в самый раз... Удобненько и легко. Как тебе, Макс? Хорошо сидят?"
                    Max_04 "Не то слово, сидят прекрасно!"
                    Alice_01 "Здорово! А теперь отвернись, не подглядывай! Нужно ещё топик примерить."
                    if '09:00' <= tm < '20:00':
                        show Alice newpajamas 07
                    elif True:
                        show Alice newpajamas 07e
                    Max_03 "Конечно, я не смотрю..."
                    if '09:00' <= tm < '20:00':
                        show Alice newpajamas 08
                    elif True:
                        show Alice newpajamas 08e
                    Alice_07 "Похоже, размер мне подходит... и удобно. Очень лёгонький топик. Ну, как тебе всё в целом?"
                    Max_05 "Тебе идёт, всё выглядит шикарно!"
        Alice_03 "Спасибо тебе ещё раз! Иди ко мне, я тебя приобниму... немного."
        Max_04 "О, это я с радостью!"
        scene BG char Alice newdress
        if '09:00' <= tm < '20:00':
            $ renpy.show("Alice hugging aliceroom 02b"+mgg.dress)
        elif True:
            $ renpy.show("Alice hugging aliceroom 02b"+mgg.dress+'e')
        Alice_05 "Но ты не зазнавайся, Макс. В следующий раз тебе может так не повезти, как сегодня."
        Max_02 "Буду иметь ввиду, сестрёнка."
        Alice_02 "Всё, давай шуруй по своим делам, не надоедай мне."
        Max_01 "Ага..."
        if not _in_replay:
            $ spent_time += 20
    elif alice.flags.hugs_type > 2:
        Alice_04 "А жирно тебе не будет?! В душе на меня глазел, а теперь и здесь хочешь подглядеть... Нет уж! Но за пижамку я тебя всё же обниму! Ну так... совсем немного..."
        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs
        Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
        Alice_07 "Не смотря на твои замашки, ты всё-таки купил мне пижамку, которую я просила. Вот я и не вредничаю..."
        Max_05 "Да, надо бы почаще так делать."
        Alice_02 "Подглядывать или что-нибудь мне дарить?!"
        Max_02 "Второе, конечно!"
        Alice_05 "Ну да, конечно... Иди давай."

    elif alice.flags.hugs_type > 1:
        menu:
            Alice_04 "А жирно тебе не будет?! В душе не нагляделся на меня и теперь хочешь подсмотреть, как я переодеваюсь, да?"
            "Нет, просто хотел увидеть, как на тебе будет смотреться пижама... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                if RandomChance(_ch1.ch):
                    $ Skill('social', 0.2)
                    Alice_03 "[succes!t]Ладно, поверю, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                    Max_07 "Что, вот так вот просто?!"
                    Alice_05 "Ну, ты обещал купить мне пижаму и сдержал слово. А я сейчас более-менее добрая... Так что не искушай судьбу!"
                    Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                elif True:
                    $ Skill('social', 0.1)
                    Alice_05 "[failed!t]Ладно, поверю, считай твои извинения приняты... Ого, а что это у тебя здесь..."
                    call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_1
                    Max_12 "А-а-ай! Мне же больно, Алиса!"
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    Max_10 "Да я же случайно оказался около душа..."
                    Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                    Max_14 "Ой! Я понял... Больше не буду!"
                    Alice_02 "Вот и молодец! Гуляй..."
    elif True:

        Alice_04 "А жирно тебе не будет?! В душе не нагляделся на меня и теперь хочешь подсмотреть, как я переодеваюсь, да?"
        Max_01 "Нет, просто хотел увидеть, как на тебе будет смотреться пижама..."
        Alice_05 "Ладно, поверю, считай твои извинения приняты... Ого, а что это у тебя здесь..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_2
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."

    $ renpy.end_replay()
    $ AddRelMood('alice', 0, 200)
    $ AttitudeChange('alice', 0.9)
    $ items['pajamas'].give()
    $ alice.gifts.append('pajamas')
    $ added_mem_var('pajamas')
    $ setting_clothes_by_conditions()
    $ infl[alice].add_m(40, True)

    $ alice.sorry.valid = {'ferrero-b', 'ferrero-m'}

    $ alice.sorry.give.append(4)
    $ spent_time += 10
    $ alice.sorry.owe = False
    jump Waiting


label Alice_solar:
    $ alice.hourly.sun_cream = 1

    menu:
        Alice_02 "Как ты догадался, Шерлок?"
        "Может быть, тебя намазать кремом для загара?" if alice.daily.oiled == 3:
            Alice_04 "Достаточно на сегодня, Макс..."
            Max_00 "Ясно. Ну, тогда, может, завтра..."
            $ alice.daily.oiled = 4
            jump AfterWaiting
        "Может быть, тебя намазать кремом для загара?" if not items['solar'].have:
            Alice_13 "Может быть. Вот только у меня его нет..."
            Max_00 "Ясно. Ну, в другой раз значит..."
            if not any([items['max-a'].InShop, items['max-a'].have]):
                Max_09 "Такой крем наверняка можно найти в интернет-магазине. Да и прежде чем пытаться поприставать к сестрёнке таким образом, стоит обзавестись одеждой полегче."
                $ items['solar'].unblock()
                $ items['max-a'].unblock()
                $ notify_list.append(_("В интернет-магазине доступен новый товар."))
            jump AfterWaiting
        "{i}Предложить Алисе намазать её кремом{/i}" if items['solar'].have and any([mgg.dress == 'a', kol_cream < 3]):
            if mgg.dress == 'a':
                if items['max-a'].have:
                    $ mgg.dress = 'b'
                elif True:
                    Max_07 "{i}( Прежде чем пытаться поприставать к сестрёнке таким образом, стоит обзавестись одеждой полегче. ){/i}"
                    $ items['max-a'].unblock()
                    jump AfterWaiting

            if kol_cream < 3:
                Max_07 "{i}( Крем почти закончился. Нужно купить ещё. ){/i}"
                $ items['solar'].unblock()
                jump AfterWaiting

        "Может быть, тебя намазать кремом для загара?" if all([alice.daily.oiled==0, kol_cream>=3, mgg.dress!='a']):
            Alice_03 "Если у тебя есть крем, то давай, раз тебе делать нечего."
            Max_01 "Ложись на живот тогда..."
            $ alice.daily.oiled = 1
        "Ладно, загорай..." if True:
            jump AfterWaiting

    scene BG char Alice sun-alone 01f
    show Alice sun-alone 01-01
    $ renpy.show('Max sun-alone 01'+mgg.dress)
    menu Alice_solar.type_choice:
        Alice_07 "Эти шезлонги всем хороши, но на животе загорать не получается. Приходится коврик для йоги использовать..."
        "{i}нанести крем{/i}" if (kol_cream >= 3 and not learned_foot_massage()) or 3<=kol_cream<7:
            $ SetCamsGrow(house[6], 140)
            $ _suf = 'a'
            $ spent_time += 20
            $ kol_cream -= 3
            scene BG char Alice sun-alone 05
            $ renpy.show('Alice sun-alone 05'+_suf+mgg.dress)
            Max_01 "{i}( Так, хорошенько намажем эти стройные ножки... ){/i}"
            scene BG char Alice sun-alone 04
            $ renpy.show('Alice sun-alone 04'+_suf+mgg.dress)
            Max_01 "{i}( Теперь плечи и совсем немного шею... ){/i}" nointeract
            $ _m1_alicetalk__res = renpy.display_menu([(_("{i}наносить крем молча{/i}"), 0), (_("А тебе нравится, что следы от лямок остаются?"), 1)])
            if _m1_alicetalk__res > 0:
                $ _talk_top = True
                call massage_sunscreen.talk_topless from _call_massage_sunscreen_talk_topless
            $ _m1_alicetalk__r1 = renpy.random.choice(['02','03'])
            $ renpy.scene()
            $ renpy.show('BG char Alice sun-alone '+_m1_alicetalk__r1)
            $ renpy.show('Alice sun-alone '+_m1_alicetalk__r1+_suf+mgg.dress)
            Max_03 "{i}( И закончим, хорошенько намазав всю её спину... ){/i}"
            $ Skill('massage', 0.005)
            if mgg.massage >= 0.01 and len(online_cources) == 1:
                Alice_04 "Спасибо, Макс! На сегодня достаточно. У тебя очень неплохо получается, а если поучишься, может стать ещё лучше!"
                Max_04 "Да не за что, обращайся!"
                scene BG char Alice sun-alone 01
                if alice.daily.oiled == 2:
                    show Alice sun-alone 01a
                elif True:
                    show Alice sun-alone 01
                Max_07 "{i}( В чём-то Алиса права, поучиться этому, пожалуй, стоит. ){/i}"
                $ online_cources.append(
                    OnLineCources(_("Массаж"), "massage", "bm", [
                        OnLineCource(_("Массаж ступней"), _("Это уникальная методика массажа с целью оказания оздоравливающего воздействия на организм. Она эффективна и в тоже время несложна в исполнении."), 3, 100, 2),
                        OnLineCource(_("Массаж кистей рук"), _("Это уникальная методика массажа с целью оказания оздоравливающего воздействия на организм. Она эффективна и в тоже время несложна в исполнении."), 3, 200, 2),
                        ]),
                    )
            elif True:
                Alice_03 "Спасибо, Макс. Так намного лучше..."
                Max_04 "Обращайся, если что..."
            scene BG char Alice sun-alone 01
            if alice.daily.oiled == 2:
                show Alice sun-alone 01a
            elif True:
                show Alice sun-alone 01
            if kol_cream < 2:
                Max_10 "{i}( Ну вот, крем закончился. Надо ещё купить. ){/i}"
                if kol_cream == 0:
                    $ items['solar'].use()
                    $ items['solar'].unblock()
            elif kol_cream < 7:
                Max_08 "{i}( Осталось мало крема, в следующий раз может не хватить, лучше купить заранее. ){/i}"
                $ items['solar'].unblock()
            $ AddRelMood('alice', 5, 50, 2)
        "{i}сделать массаж с кремом{/i}" if all([kol_cream >= 7, learned_foot_massage()]):
            $ _massaged = []
            $ _talk_top = False
            $ SetCamsGrow(house[6], 160)
            jump massage_sunscreen
        "{i}{color=[gray]}сделать массаж с кремом{/color}{color=[red]}\nкрема недостаточно{/color}{/i}" if kol_cream < 7:
            jump Alice_solar.type_choice
        "{i}Блин, крем практически закончился... Давай в другой раз тогда...{/i}" if kol_cream < 3:
            Alice_00 "Ну что же ты, Макс... Эх, только настроилась..."
            $ alice.daily.oiled = 4
            jump AfterWaiting

    jump Waiting


label massage_sunscreen:
    scene BG char Alice sun-alone 01f
    if alice.daily.oiled == 2:
        show Alice sun-alone 01-01a
        $ _suf = 'b'
    elif True:
        show Alice sun-alone 01-01
        $ _suf = 'a'
    $ renpy.show('Max sun-alone 01'+mgg.dress)
    if learned_hand_massage():
        if len(_massaged) == (5 if alice.dcv.intrusion.stage in [5, 7] else 4):
            Alice_07 "Макс, ты делаешь успехи! Ещё немного попрактикуешься, и к тебе будет сложно записаться на приём!"
            Max_03 "Да пустяки, обращайся!"
            Alice_04 "Ладно, хватит на сегодня, Макс. И... спасибо!"
            Max_05 "Не за что! Всегда рад..."
            $ AddRelMood('alice', 15, 150, 3)
            jump massage_sunscreen.end

    elif len(_massaged) == 4:
        Alice_04 "Спасибо, Макс! На сегодня достаточно. У тебя очень неплохо получается, а если поучишься, может стать ещё лучше!"
        Max_04 "Да не за что, обращайся!"
        $ AddRelMood('alice', 10, 100, 3)
        jump massage_sunscreen.end

    elif len(_massaged) == 2 and _massaged[0] != 'foot':
        Alice_03 "Спасибо, Макс! На сегодня достаточно."
        Max_01 "Да не за что, обращайся!"
        $ AddRelMood('alice', 5, 50, 2)
        jump massage_sunscreen.end


    if not _in_replay:
        $ kol_cream -= 1
    call screen choice_zone_sunscreen

    label massage_sunscreen.left_foot:
        scene BG char Alice sun-alone 06
        $ renpy.show('Alice sun-alone 06'+_suf+mgg.dress)
        Max_01 "{i}( Начнём сегодня с левой пяточки... Вот так. И, пока я хорошенько её массирую, можно заодно поглазеть на аппетитную Алисину попку! ){/i}"
        scene BG char Alice sun-alone 07
        $ renpy.show('Alice sun-alone 07'+_suf+mgg.dress)
        Max_03 "{i}( А теперь правую... Вот так. Да уж, глаз не оторвать, попка - что надо! ){/i}"
        jump massage_sunscreen.foot

    label massage_sunscreen.right_foot:
        scene BG char Alice sun-alone 07
        $ renpy.show('Alice sun-alone 07'+_suf+mgg.dress)
        Max_01 "{i}( Начнём сегодня с правой пяточки... Вот так. И, пока я хорошенько её массирую, можно заодно поглазеть на аппетитную Алисину попку! ){/i}"
        scene BG char Alice sun-alone 06
        $ renpy.show('Alice sun-alone 06'+_suf+mgg.dress)
        Max_03 "{i}( А теперь левую... Вот так. Да уж, глаз не оторвать, попка - что надо! ){/i}"
        jump massage_sunscreen.foot

    label massage_sunscreen.shin:
        scene BG char Alice sun-alone 05
        $ renpy.show('Alice sun-alone 05'+_suf+mgg.dress)
        Max_02 "{i}( Помассируем эти стройные ножки, вот так... ){/i}"
        if 'shin' in _massaged:

            jump massage_sunscreen.double
        elif True:
            $ _multipler = 10 - len(_massaged)
            if len(_massaged)>0 and _massaged[0]=='foot':
                $ _multipler *= 2

            if RandomChance(GetChance(mgg.massage, _multipler, 950).ch) or _in_replay:

                $ Skill('massage', 0.05)
                Alice_07 "Ух, как приятно... Ты молодец, Макс! Моим ножкам это понравилось... Не останавливайся, продолжай..."
                $ infl[alice].add_m(4)
            elif True:
                $ Skill('massage', 0.02)
                jump massage_sunscreen.fail
        $ _massaged.append('shin')
        jump massage_sunscreen

    label massage_sunscreen.shoulders:
        scene BG char Alice sun-alone 04
        $ renpy.show('Alice sun-alone 04'+_suf+mgg.dress)
        Max_04 "{i}( Хорошенько разомнём плечи и немного шею... ){/i}" nointeract
        if not _talk_top:
            $ _m1_alicetalk__res = renpy.display_menu([(_("{i}массировать молча{/i}"), 0), (_("А тебе нравится, что следы от лямок остаются?"), 1)])
            if _m1_alicetalk__res > 0:
                $ _talk_top = True
                call massage_sunscreen.talk_topless from _call_massage_sunscreen_talk_topless_1
                $ renpy.show('Alice sun-alone 04'+_suf+mgg.dress)
                Max_01 "И ещё немного..."

        if 'shoulders' in _massaged:

            jump massage_sunscreen.double
        elif True:
            $ _multipler = 10 - len(_massaged)
            if len(_massaged)>0 and _massaged[0]=='foot':
                $ _multipler *= 2

            $ _massaged.append('shoulders')
            if RandomChance(GetChance(mgg.massage, _multipler, 950).ch) or _in_replay:

                $ Skill('massage', 0.05)
                $ infl[alice].add_m(4)
                menu:
                    Alice_07 "Это так классно расслабляет... У тебя очень хорошо получается, Макс!"
                    "{i}продолжить{/i}" if True:
                        pass
                    "{i}выпустить рядом паука{/i}" if items['spider'].have and poss['spider'].used(4) and not _in_replay:
                        show FG sun-alone-04
                        jump massage_sunscreen.spider
            elif True:
                $ Skill('massage', 0.02)
                jump massage_sunscreen.fail
        jump massage_sunscreen

    label massage_sunscreen.spine:
        $ _m1_alicetalk__r1 = renpy.random.choice(['02','03'])
        $ renpy.scene()
        $ renpy.show('BG char Alice sun-alone '+_m1_alicetalk__r1)
        $ renpy.show('Alice sun-alone '+_m1_alicetalk__r1+_suf+mgg.dress)
        Max_05 "{i}( Вот так, нужно хорошенько растереть крем... А теперь тщательно помнём спинку... Нежно, но сильно. ){/i}" nointeract
        if not _talk_top:
            $ _m1_alicetalk__res = renpy.display_menu([(_("{i}массировать молча{/i}"), 0), (_("А тебе нравится, что следы от лямок остаются?"), 1)])
            if _m1_alicetalk__res > 0:
                $ _talk_top = True
                call massage_sunscreen.talk_topless from _call_massage_sunscreen_talk_topless_2
                $ renpy.show('Alice sun-alone '+_m1_alicetalk__r1+_suf+mgg.dress)
                Max_01 "Ещё немного крема..."

        if 'spine' in _massaged:

            jump massage_sunscreen.double
        elif True:
            $ _multipler = 10 - len(_massaged)
            if len(_massaged)>0 and _massaged[0]=='foot':
                $ _multipler *= 2

            $ _massaged.append('spine')
            if RandomChance(GetChance(mgg.massage, _multipler, 950).ch) or _in_replay:

                $ Skill('massage', 0.05)
                $ infl[alice].add_m(4)
                menu:
                    Alice_07 "Как приятно... Макс, ты делаешь успехи! Мне это нравится..."
                    "{i}продолжить{/i}" if True:
                        pass
                    "{i}выпустить рядом паука{/i}" if items['spider'].have and poss['spider'].used(4) and not _in_replay:
                        $ renpy.show("FG sun-alone-"+_m1_alicetalk__r1)
                        jump massage_sunscreen.spider
            elif True:
                $ Skill('massage', 0.02)
                jump massage_sunscreen.fail
        jump massage_sunscreen

    label massage_sunscreen.ass:
        "попка"
        jump massage_sunscreen

    label massage_sunscreen.hips:


        if renpy.random.randint(1, 2)<2:

            scene BG char Alice sun-alone 07
            $ renpy.show('Alice sun-alone 08'+_suf+mgg.dress)
        elif True:

            scene BG char Alice sun-alone 01f
            $ renpy.show('Alice sun-alone 09'+_suf+mgg.dress)

        if 'hips' in _massaged:

            jump massage_sunscreen.double

        if not len(_massaged):

            Alice_06 "Макс, а ты куда это там полез так неожиданно?! Лучше сосредоточься на всём остальном, а туда не лезь..."

        elif all([len(_massaged)==1, _massaged[0] in ['foot', 'shin']]) or _massaged==['shin', 'foot']:

            Alice_13 "Макс, ты слишком высоко забрался! Лучше сосредоточься на всём остальном..."

        elif (all([len(_massaged)==2, _massaged==['foot', 'shin']]) or
                any([_massaged==['shoulders', 'spine', 'foot', 'shin'], _massaged==['spine', 'shoulders', 'foot', 'shin']])):

            Alice_04 "Хоть это и приятно, но ощущение, будто ты не знаешь, как правильно массировать там... Лучше сосредоточься на том, что ты умеешь..."
            $ infl[alice].add_m(4)

        elif any([_massaged==['shoulders'], _massaged==['spine'], set(_massaged)==set(['shoulders', 'spine']), set(_massaged)==set(['shoulders', 'spine', 'shin'])]):

            Alice_13 "Макс, а ты куда это там полез так неожиданно?! Если уж решил перейти на ноги, то массируй с самого низа..."
        elif True:

            Alice_06 "Макс, ты уже определись, что ты массируешь! Ноги или спину... Похоже, на твоих онлайн-курсах не учили тому, что прыгать туда-сюда не здорово..."

        $ _massaged.append('hips')
        jump massage_sunscreen

    label massage_sunscreen.foot:
        if 'foot' in _massaged:

            jump massage_sunscreen.double
        elif True:
            $ _multipler = 10 - len(_massaged) if len(_massaged) else 20
            if RandomChance(GetChance(mgg.massage, _multipler, 950).ch) or _in_replay:

                $ Skill('massage', 0.05)
                $ infl[alice].add_m(4)
                Alice_07 "Ух, как же моим пяточкам приятно... Не останавливайся, продолжай..."
            elif True:
                $ Skill('massage', 0.02)
                jump massage_sunscreen.fail
        $ _massaged.append('foot')
        jump massage_sunscreen

    label massage_sunscreen.double:
        Alice_13 "Взялся делать массаж, а сам не знаешь что делать! Хватит, иди отсюда, дай позагорать спокойно."
        Max_11 "Эх... Ладно..."
        jump massage_sunscreen.end

    label massage_sunscreen.fail:
        if len(_massaged) > 0:
            Alice_06 "Хватит, Макс... Что-то у тебя не так пошло... А ведь так хорошо начал..."
        elif True:
            Alice_13 "Макс, хватит... Что-то не похоже, что ты знаешь, что делаешь... Давай на этом закончим..."
        Max_10 "Хорошо, извини..."
        jump massage_sunscreen.end

    label massage_sunscreen.talk_topless:
        $ _ch1 = GetChance(mgg.social, 3, 900)
        menu:
            Alice_06 "Нет, конечно. Но тебя я так радовать не собираюсь!"
            "Что, стесняешься? {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                if RandomChance(_ch1.ch) or _in_replay:
                    $ Skill('social', 0.1)
                    Alice_07 "[succes!t]Нет, но... Ладно, всё равно тебе ничего не видно..."
                    Max_02 "Так держать, сестрёнка!"
                    $ alice.daily.oiled = 2
                    $ alice.dress = 'b'
                    $ _suf = 'b'
                    $ SetCamsGrow(house[6], 200)
                elif True:
                    $ Skill('social', 0.05)
                    Alice_04 "[failed!t]Вот только на \"слабо\" меня брать не надо!"
                    Max_01 "Ладно, как скажешь..."
            "Ну, как хочешь..." if True:
                pass
        return

    label massage_sunscreen.spider:
        if _in_replay:
            $ _suf = 'b' if alice.daily.oiled == 2 else 'a'
            $ _m1_alicetalk__r1 = renpy.random.choice(['02','03'])
            $ renpy.scene()
            $ renpy.show('BG char Alice sun-alone '+_m1_alicetalk__r1)
            $ renpy.show('Alice sun-alone '+_m1_alicetalk__r1+_suf+mgg.dress)
            $ renpy.show("FG sun-alone-"+_m1_alicetalk__r1)
        elif True:
            $ poss['spider'].open(5)
            $ items['spider'].use()
            $ SpiderKill = 0
            $ SpiderResp = 1
            if 'massage_sunscreen.spider' not in persistent.memories:
                $ persistent.memories['massage_sunscreen.spider'] = 0
        Max_07 "Э-э-э... Алиса, ты только не пугайся, просто лежи, как лежала..."
        Alice_13 "А чего мне пугаться, Макс? Сейчас что, будешь больно массировать?"
        Max_00 "Нет, просто у нас тут одна проблемка подкралась..."
        scene BG char Alice sun-alone 03
        $ renpy.show('Alice sun-alone 03'+_suf+mgg.dress)
        show FG sun-alone-03
        Alice_12 "Что?! Подкралась?! Ты же говоришь не о том, о чём я подумала?"
        Max_08 "Ну... Ты только не дёргайся!"

        scene BG char Alice spider-sun-01
        $ renpy.show('Alice spider-sun 01'+_suf+mgg.dress)
        show FG spider-sun-01
        Alice_15 "А-а-а! Макс! Вот чёрт! Какой он здоровенный!"
        Max_02 "И не говори!"
        Alice_14 "Макс, чего сидишь?! Убери его отсюда! А ещё лучше убей!"
        Max_04 "Да мне как-то не хочется."

        scene BG char Alice spider-sun-02
        $ renpy.show('Alice spider-sun 02-01'+_suf+mgg.dress)
        Alice_06 "В смысле, не хочется?! Охренеть, он страшный!"
        Max_05 "Так хорошо же сидим. Да и он в нашу сторону не ползёт. По-моему, он в сторону травы сменил курс..."
        if alice.daily.oiled != 2:
            Alice_16 "Да плевать мне, куда он ползёт! Я хочу, чтобы его не было!"

            Max_01 "Ладно, тогда слезай, я с ним разберусь."
            Alice_06 "Не-е-ет, он тогда сразу ко мне поползёт! Что я их, не знаю что ли..."
            Max_03 "Ты определись уже, Алиса, чего хочешь. Я бы просто немного подождал, вон он, уползает..."
            Alice_12 "Точно?!"
            Max_04 "Ага. В траву убежал."

            scene BG char Alice hugging sun-01
            $ renpy.show('Alice hugging sun 02a'+mgg.dress)
            Alice_07 "Фух... Ладно. Только ты посматривай, временами, чтобы в мою сторону никто не полз."
            Max_02 "Хорошо. Но, если что, зови. Ещё посидим."
            Alice_05 "Тебе хватит. Не обольщайся..."
            Max_01 "Ага."
            $ renpy.end_replay()
            $ infl[alice].add_m(4)
            jump massage_sunscreen.end
        elif True:

            menu:
                Alice_16 "Да плевать мне, куда он ползёт! Я хочу, чтобы его не было!"
                "Давай лучше ещё так посидим, подождём. Вон он, уползает..." if True:
                    Alice_12 "Макс, а что это в меня такое упёрлось там внизу?!"
                    Max_02 "Ну... это я, так сказать."
                    Alice_14 "Ой, блин, это член твой что ли?!"
                    Max_01 "Ага. Он самый."
                    jump massage_sunscreen.sit_and_wait

                "Спрячься за меня, хотя бы..." if all([alice.dcv.intrusion.stage in [5, 7], alice.flags.privpunish, mgg.dress=='c']):

                    jump massage_sunscreen.hide_behind

                "{i}потискать Алису за грудь{/i}" if alice.dcv.intrusion.stage in [5, 7]:
                    jump massage_sunscreen.squeeze_chest

    label massage_sunscreen.sit_and_wait:
        if mgg.dress == 'b':

            if alice.flags.touched:


                scene BG char Alice spider-sun-02
                show Alice spider-sun 02-01bb
                Alice_13 "Ну, Макс... Может хватит уже так на меня реагировать?! Я же твоя сестра всё-таки!"
                Max_02 "А ты ещё сильнее прижмись ко мне своими сиськами... Эффект будет ещё ощутимее!"
                Alice_06 "Паука бы лучше отогнал!"
                Max_03 "Незачем, он и так уползает..."
                Alice_12 "Точно?!"
                Max_04 "Ага. В траву убежал."

                scene BG char Alice hugging sun-01
                show Alice hugging sun 02bb
                Alice_07 "Фух... Ладно. Только ты посматривай, временами, чтобы в мою сторону никто не полз."
                Max_02 "Хорошо. Но, если что, зови. Ещё посидим."
                Alice_05 "Тебе хватит. Не обольщайся..."
                Max_01 "Ага."
            elif True:
                scene BG char Alice hugging sun-01
                show Alice hugging sun 01bb
                Alice_15 "Ты совсем что ли извращенец? На родную сестру у него стоит!"
                Max_10 "Ай, Алиса, больно! Сама же своими голыми сиськами в моё лицо упёрлась! А они красивые... Чего ты ещё ожидала?!"
                Alice_16 "Всё, не хочу об этом говорить... Давай, шуруй отсюда. Бегом! А то я живо тебе по заднице напинаю!"
                Max_09 "Да ухожу я, уши только мои в покое оставь!"
            jump massage_sunscreen.end
        elif True:

            if alice.flags.touched:

                scene BG char Alice spider-sun-02
                show Alice spider-sun 02-01bc
                Alice_13 "Ну, Макс... Может хватит уже так на меня реагировать?! Я же твоя сестра всё-таки!"
                Max_02 "А ты ещё сильнее прижмись ко мне своими сиськами... Эффект будет ещё ощутимее!"
                Alice_06 "Куда уж ещё ощутимее! Я и так почти что на твоём члене сижу..."
                Max_03 "Зато, паук в совершенно противоположную сторону от нас уползает!"
                Alice_12 "Точно?!"
                Max_04 "Ага. В траву убежал."

                scene BG char Alice hugging sun-01
                show Alice hugging sun 02bc
                Alice_05 "Ой... Ты извини, что я тебя тут, посовращала немного... Я же не специально."
                Max_03 "Не слишком-то ты раскаиваешься, а?"
                Alice_02 "Будем считать, что твой стояк меня сегодня спас! Паук сразу убежал... И я теперь чувствую себя, какой-то защищённой, что ли... Кажется, уже и я какой-то извращенкой становлюсь!"
                Max_04 "Это у нас семейное, по-видимому."
                Alice_07 "Только ты давай прибери свою штуку, а то мы со стороны очень странно сейчас выглядим."
                Max_02 "Да не так-то это просто сделать..."
                Alice_05 "А ты постарайся."
                Max_01 "Ага."
            elif True:
                $ persistent.memories['massage_sunscreen.spider'] = 1
                show Alice spider-sun 02-02bc
                Alice_12 "Какого чёрта, Макс?! Совсем что ли извращенец? Я же твоя сестра! Блин... Прикройся хоть..."
                Max_01 "Да не так-то это просто, прикрыть его."
                Alice_06 "Не ожидала я от тебя такого, Макс. И что у тебя в голове творится?!"
                Max_07 "А чего ты ожидала?! Сама же на меня запрыгнула и сиськами своими голыми мне в лицо упёрлась... Кстати, не могу не отметить, они у тебя красивые и упругие!"
                Alice_13 "Нет, ну ты точно больной... Ладно, представим, что ничего не было. Убирай эту свою штуку и не появляйся в таком виде рядом со мной!"
                Max_02 "Хорошо. Не скучай."
                $ renpy.end_replay()
                $ infl[alice].add_m(10)
            jump massage_sunscreen.end

    label massage_sunscreen.hide_behind:
        $ added_mem_var('hide_behind')
        Alice_06 "Нет, я боюсь..."
        Max_09 "А вдруг он на нас побежит, прямо к твоей попке!"

        scene BG char Alice spider-sun-03
        show Alice spider-sun 03bc
        Alice_13 "Ой, нет! Не надо к моей попке! Что ему вообще надо тут?! Почему ему в траве не сидится или где он там живёт..."
        Max_07 "Ну... Не то, чтобы меня что-то не устраивало сейчас, но ты держишься за меня!"

        scene BG char Alice spider-sun-04
        show Alice spider-sun 04-01bc
        Alice_12 "Конечно держусь! Мне же страшно, Макс! Ты ведь знаешь, как я их боюсь..."
        Max_03 "Нет, я в смысле, ты держишься за мой член! Это, конечно, весьма приятно... Но ты же на меня, как всегда, разорёшься потом!"

        show Alice spider-sun 04-02bc
        Alice_15 "Ой! Я это не специально! Видишь, насколько я этих пауков не переношу? Даже не поняла, за что схватилась..."
        Max_02 "Да ладно, схватилась и схватилась. Уж это точно не страшно!"
        Alice_12 "Он уползает, кстати..."
        Max_05 "Точно! Наверно, испугался моей торчащей мощи!"
        Alice_07 "У тебя что, стоит до сих пор?!"
        Max_04 "Ну... Ты так классно ко мне прижимаешься... Мне приятно!"

        scene BG char Alice hugging sun-01
        show Alice hugging sun 02bc
        Alice_05 "Ой... Ты извини, что я тебя тут, посовращала немного... Я же не специально."
        Max_03 "Не слишком-то ты раскаиваешься, а?"
        Alice_02 "Будем считать, что твой стояк меня сегодня спас! Паук сразу убежал... И я теперь чувствую себя, какой-то защищённой, что ли... Кажется, уже и я какой-то извращенкой становлюсь!"
        Max_04 "Это у нас семейное, по-видимому."
        Alice_07 "Только ты давай прибери свою штуку, а то мы со стороны очень странно сейчас выглядим."
        Max_02 "Да не так-то это просто сделать..."
        Alice_05 "А ты постарайся."
        Max_01 "Ага."
        $ poss['spider'].open(6)
        $ alice.flags.touched = True
        jump massage_sunscreen.end

    label massage_sunscreen.squeeze_chest:
        $ added_mem_var('squeeze_chest')

        scene BG char Alice spider-sun-02
        $ renpy.show('Alice spider-sun 02-03b'+mgg.dress)
        Alice_14 "Ты офигел что ли, Макс! Ну-ка руки быстро убери, пока не получил..."
        Max_07 "Шуму-то сколько... У тебя сиськи голые, вот я их и прикрыл! А то мало ли кто увидит..."
        $ ctd = Countdown(3, 'massage_sunscreen.hands_off')
        $ renpy.block_rollback()
        Alice_15 "Кто??? Пауки что ли?! Если через пять секунд не уберёшь руки, тебе будет плохо...{p=5}{nw}"
        show screen countdown       
        $ renpy.dynamic('dial')
        $ dial = [(_("{i}убрать руки{/i}"), 1), (_("{i}тискать дальше...{/i}"), 0)]
        $ renpy.random.shuffle(dial)
        extend "" nointeract
        $ rez =  renpy.display_menu(dial)
        $ renpy.block_rollback()
        if rez:

            hide screen countdown

            scene BG char Alice spider-sun-02
            $ renpy.show('Alice spider-sun 02-01b'+mgg.dress)
            Max_02 "Всё, убрал. Правда, если ты продолжишь так крепко прижиматься ими к моему лицу, то есть риск..."
            Alice_06 "Макс... Я что, практически на твоём члене сейчас сижу?!"
            Max_03 "А сама как думаешь?"
            jump massage_sunscreen.sit_and_wait
        elif True:
            hide screen countdown
            jump massage_sunscreen.hands_off

    label massage_sunscreen.hands_off:
        $ renpy.block_rollback()

        if mgg.dress == 'b':


            scene BG char Alice hugging sun-01
            show Alice hugging sun 01bb
            Max_12 "А-а-ай! Мне же больно, Алиса! Перестань!"
            Alice_16 "А я ведь тебя предупреждала! Наверно, раз до тебя не дошло, нужно крутануть ещё сильнее..."
            Max_14 "Ой! Я понял... Больше не буду! Отпусти уже..."
            Alice_17 "Всё, давай, шуруй отсюда. Бегом! А то я живо тебе по заднице напинаю!"
        elif True:


            scene BG char Alice hugging sun-01
            show Alice hugging sun 01bc
            Max_12 "А-а-ай! Мне же больно, Алиса! Перестань!"
            Alice_00 "Ах, у тебя ещё и стоит на это всё! Совсем что ли извращенец? Я же твоя сестра!"
            Max_07 "А чего ты ожидала?! Сама же на меня запрыгнула и сиськами своими голыми мне в лицо упёрлась... Кстати, не могу не отметить, они у тебя красивые и упругие!"
            Alice_13 "Нет, ну ты точно больной... Ладно, представим, что ничего не было. Убирай эту свою штуку и не появляйся в таком виде рядом со мной!"
        Max_09 "Да ухожу я, уши только мои в покое оставь!"
        jump massage_sunscreen.end

    label massage_sunscreen.end:
        $ renpy.end_replay()
        scene BG char Alice sun-alone 01
        if alice.daily.oiled == 2:
            show Alice sun-alone 01a
        elif True:
            show Alice sun-alone 01
        $ spent_time += 10 + clip(int(round(5*len(_massaged), -1)), 0, 30)
        if kol_cream < 3 and mgg.massage < 2.0:
            Max_10 "{i}( Ну вот, крем закончился. Надо ещё купить. ){/i}"
            if kol_cream == 0:
                $ items['solar'].use()
                $ items['solar'].unblock()
        elif kol_cream < 7:
            Max_08 "{i}( Осталось мало крема, в следующий раз может не хватить, лучше купить заранее. ){/i}"
            $ items['solar'].unblock()

        jump Waiting


label alice_sorry_gifts:
    if alice.sorry.days[0] == day:
        Max_09 "Думаю, не стоит дарить вкусняшку сегодня. Это может вызвать ненужные подозрения... Лучше это сделать завтра."
        return

    $ _ch1 = GetChance(mgg.social, 3, 900)
    $ txt = {
        0 : _("Да ладно! Это мне нравится... И что там у тебя?"),
        1 : _("Ого! И правда хочешь рискнуть... И что там у тебя на этот раз?"),
        2 : _("Наконец-то! Ну давай, показывай, что у тебя на этот раз?!"),
        }[len(alice.sorry.give)]
    $ alice.sorry.owe = False
    menu:
        Alice_02 "[txt!t]"
        "Конфеты \"Raffaello\" (16 штук)" if items['raffaello-m'].have:
            $ _m1_alicetalk__give = 'raffaello-m'
            jump alice_sorry_gifts.bad
        "Конфеты \"Raffaello\" (24 штуки)" if items['raffaello-b'].have:
            $ _m1_alicetalk__give = 'raffaello-b'
            jump alice_sorry_gifts.bad
        "Конфеты \"Ferrero Rocher\" (16 штук)" if items['ferrero-m'].have:
            $ _m1_alicetalk__give = 'ferrero-m'
            jump alice_sorry_gifts.good
        "Конфеты \"Ferrero Rocher\" (24 штуки)" if items['ferrero-b'].have:
            $ _m1_alicetalk__give = 'ferrero-b'
            jump alice_sorry_gifts.good
        "Шоколад \"Ritter Sport\" mini (9 штук)" if items['ritter-m'].have:
            $ _m1_alicetalk__give = 'ritter-m'
            jump alice_sorry_gifts.middle
        "Шоколад \"Ritter Sport\" (4 штуки)" if items['ritter-b'].have:
            $ _m1_alicetalk__give = 'ritter-b'
            jump alice_sorry_gifts.middle

    label alice_sorry_gifts.kick_ears:
        $ poss['risk'].open(5)
        if current_room == house[1]:
            scene BG char Alice newdress
            if '09:00' <= tm < '20:00':
                $ renpy.show("Alice hugging aliceroom 01"+alice.dress+mgg.dress)
            elif True:
                $ renpy.show("Alice hugging aliceroom 01"+alice.dress+mgg.dress+'e')
        elif current_room == house[5]:
            scene BG char Alice hugging terrace-01
            $ renpy.show("Alice hugging terrace 01"+alice.dress+mgg.dress)
        elif current_room == house[6]:
            scene BG char Alice hugging sun-01
            $ renpy.show("Alice hugging sun 01"+alice.dress+mgg.dress)
        return

    label alice_sorry_gifts.kindred_hugs:
        $ poss['risk'].open(6)
        if current_room == house[1]:
            scene BG char Alice newdress
            if '09:00' <= tm < '20:00':
                $ renpy.show("Alice hugging aliceroom 02"+alice.dress+mgg.dress)
            elif True:
                $ renpy.show("Alice hugging aliceroom 02"+alice.dress+mgg.dress+'e')
        elif current_room == house[5]:
            scene BG char Alice hugging terrace-01
            $ renpy.show("Alice hugging terrace 02"+alice.dress+mgg.dress)
        elif current_room == house[6]:
            scene BG char Alice hugging sun-01
            $ renpy.show("Alice hugging sun 02"+alice.dress+mgg.dress)
        return

    label alice_sorry_gifts.middle_again:
        Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
        Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
        Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_3
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        menu:
            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
            "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                if RandomChance(_ch1.ch):
                    $ Skill('social', 0.2)
                    Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                    Max_14 "Ой! Я понял... Больше не буду!"
                    Alice_02 "Вот и молодец! Гуляй..."
                    $ alice.flags.hugs_type = 2
                elif True:
                    $ Skill('social', 0.1)
                    Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                    Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                    Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                    Max_14 "Ой! Я понял... Больше не буду!"
                    Alice_02 "Вот и молодец! Гуляй..."
                    $ alice.flags.hugs_type = 1
                    $ punreason[1] = 1
        return

    label alice_sorry_gifts.bad_again:
        Alice_17 "Макс, ты что, тупой?! Я тебе уже говорила, что не люблю эти конфеты! Ты меня, что, совсем не слушаешь, или у тебя помяти нет?!"
        Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
        Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_4
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
        Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
        Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."
        $ punreason[1] = 1
        $ alice.flags.hugs_type = 1
        return

    label alice_sorry_gifts.apology_accepted:
        Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_5
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        Alice_02 "Вот и молодец! Гуляй..."
        $ alice.flags.hugs_type = 2
        return

    label alice_sorry_gifts.you_deserve:
        $ Skill('social', 0.2)
        Alice_04 "[succes!t]Ладно, Макс, пожалуй ты заслужил это своими подарками..."
        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_1
        Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
        Alice_07 "Я вижу, что ты не просто хочешь избежать наказания, а ещё и мне приятно сделать стремишься. Вот я и не вредничаю..."
        Max_05 "Да, надо бы почаще так делать."
        Alice_02 "Подглядывать за мной или дарить мне сладости?!"
        Max_02 "Второе, конечно!"
        Alice_05 "Ну да, конечно... Иди давай."
        $ alice.flags.hugs_type = 4
        return

    label alice_sorry_gifts.what_bummer:
        $ Skill('social', 0.1)
        Alice_05 "[failed!t]Ах, а так хотелось! Какой облом..."
        Max_09 "Обнять меня или придушить?"
        Alice_07 "Зачем останавливаться на чём-то одном, Макс? Хи-хи..."
        Max_01 "Я тогда лучше пойду... погуляю."
        Alice_02 "Ну как хочешь..."
        $ alice.flags.hugs_type = 3
        return

    label alice_sorry_gifts.im_in_pain:
        Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_6
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
        Max_14 "Ой! Я понял... Больше не буду!"
        $ alice.flags.hugs_type = 2
        return

    label alice_sorry_gifts.what_disgusting:
        Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
        Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
        Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."
        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_7
        Max_12 "А-а-ай! Мне же больно, Алиса!"
        Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
        Max_10 "Да я же случайно оказался около душа..."
        $ alice.flags.hugs_type = 2
        return

    label alice_sorry_gifts.bad:
        $ items[_m1_alicetalk__give].use()
        $ poss['risk'].open(4)
        if len(alice.sorry.give) == 0:
            Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
            Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
            Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."
            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_8
            Max_12 "А-а-ай! Алиса! Больно ведь!"
            menu:
                Alice_16 "Будешь ещё, извращенец лохматый, за мной подглядывать?"
                "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                    if RandomChance(_ch1.ch):
                        $ Skill('social', 0.2)
                        Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                        Max_14 "Ой! Понял-понял, не буду! Больше не буду..."
                        Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                        Max_08 "И какая у тебя любимая?"
                        Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                        Max_11 "Ладно! Я учту, только отпусти..."
                        Alice_02 "Вот и правильно! Гуляй..."
                    elif True:
                        $ Skill('social', 0.1)
                        Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                        Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                        Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                        Max_08 "И какая у тебя любимая?"
                        Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                        Max_11 "Ладно! Я учту, только отпусти..."
                        Alice_02 "Вот и правильно! Гуляй..."
                        $ punreason[1] = 1

        elif len(alice.sorry.give) == 1:
            if alice.sorry.give[0] == 1:
                Alice_17 "Макс, ты что, тупой?! Я тебе уже говорила, что не люблю эти конфеты! Ты меня, что, совсем не слушаешь, или у тебя помяти нет?!"
                Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
                Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_9
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                Max_08 "И какая у тебя любимая?"
                Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."
                $ punreason[1] = 1

            elif alice.sorry.give[0] == 2:
                call alice_sorry_gifts.what_disgusting from _call_alice_sorry_gifts_what_disgusting
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                Max_08 "И какая у тебя любимая?"
                Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."
                $ punreason[1] = 1

            elif alice.sorry.give[0] == 3:
                Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
                Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
                Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_10
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                            Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1

        elif len(alice.sorry.give) == 2:
            if alice.sorry.give == [1, 1]:
                Alice_17 "Макс, ты что, тупой, я тебе, уже дважды говорила, что не люблю эти конфеты?! Ты меня, что, совсем не слушаешь, или у тебя мозгов нет?!"
                Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
                Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_11
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_16 "Да тебе просто наплевать на всё то, что я тебе говорю! Так что - сам виноват..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_17 "Понял он... Катись отсюда!"
                $ alice.flags.hugs_type = 1
                $ punreason[1] = 1

            elif alice.sorry.give == [1, 2]:
                call alice_sorry_gifts.bad_again from _call_alice_sorry_gifts_bad_again

            elif alice.sorry.give == [1, 3]:
                Alice_17 "Макс, ты что, тупой?! Я тебе уже говорила, что не люблю эти конфеты! Ты меня, что, совсем не слушаешь, или у тебя помяти нет?!"
                Max_08 "Просто так уж вышло... Извини. Не смог достать другие."
                Alice_12 "Я тебе сейчас дам, не смог... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_12
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1

            elif alice.sorry.give == [2, 1]:
                call alice_sorry_gifts.bad_again from _call_alice_sorry_gifts_bad_again_1

            elif alice.sorry.give == [2, 2]:
                Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
                Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
                Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_13
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1

            elif alice.sorry.give == [2, 3]:
                call alice_sorry_gifts.what_disgusting from _call_alice_sorry_gifts_what_disgusting_1
                Alice_05 "Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_02 "Вот и молодец! Гуляй..."

            elif alice.sorry.give == [3, 1]:
                call alice_sorry_gifts.bad_again from _call_alice_sorry_gifts_bad_again_2

            elif alice.sorry.give == [3, 2]:
                Alice_12 "Ой! Какая же гадость этот кокос, не люблю его, фу-у-у! Это большая ошибка, Макс!"
                Max_10 "Я же не знал! Если ты так их не любишь, то можно было и предупредить..."
                Alice_05 "Надо было, но теперь у меня есть повод сделать вот так... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_14
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне не нравится! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1
            elif True:

                call alice_sorry_gifts.what_disgusting from _call_alice_sorry_gifts_what_disgusting_2
                Alice_05 "Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_02 "Вот и молодец! Гуляй..."

        $ alice.sorry.give.append(1)
        jump alice_sorry_gifts.end

    label alice_sorry_gifts.middle:
        $ items[_m1_alicetalk__give].use()
        $ poss['risk'].open(3)
        if len(alice.sorry.give) == 0:
            Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
            Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
            Alice_05 "Конечно, Макс, считай твои извинения приняты... А ну-ка иди сюда..."
            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_15
            Max_12 "А-а-ай! Алиса! Больно ведь!"
            Alice_16 "Будешь ещё, извращенец лохматый, за мной подглядывать?"
            Max_10 "Да я же случайно оказался около душа..."
            Alice_05 "Ответ неправильный! Наверно, нужно сильнее потянуть..."
            Max_14 "Ой! Понял-понял, не буду! Больше не буду..."
            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
            Max_08 "И какая у тебя любимая?"
            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
            Max_11 "Ладно! Я учту, только отпусти..."
            Alice_02 "Вот и правильно! Гуляй..."

        elif len(alice.sorry.give) == 1:
            if alice.sorry.give[0] == 1:
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_16
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1

            elif alice.sorry.give[0] == 2:
                Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_17
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                            Max_08 "И какая у тебя любимая?"
                            Alice_03 "Так я тебе и сказала! Но её дольше всех других нужно разворачивать..."
                            Max_11 "Я обязательно подарю тебе любимую, обещаю! Отпусти уже..."
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1
            elif True:

                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_18
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Если только это не будет моя любимая сладость..."
                Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."

        elif len(alice.sorry.give) == 2:
            if alice.sorry.give == [1, 1]:
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_12 "Я тебе сейчас дам, ничего не расскажу... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_19
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_12 "Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                Alice_05 "Не считается, если она мне неинтересна! Ты так и не подарил самую мою любимую сладость! Так что - не повезло тебе..."
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_02 "Вот и молодец! Гуляй..."
                $ alice.flags.hugs_type = 1
                $ punreason[1] = 1

            elif alice.sorry.give == [1, 2]:
                call alice_sorry_gifts.middle_again from _call_alice_sorry_gifts_middle_again

            elif alice.sorry.give == [1, 3]:
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted

            elif alice.sorry.give == [2, 1]:
                call alice_sorry_gifts.middle_again from _call_alice_sorry_gifts_middle_again_1

            elif alice.sorry.give == [2, 2]:
                Alice_13 "Вот значит как! Снова купил эти шоколадки... А ты рисковый! Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_1

            elif alice.sorry.give == [2, 3]:
                Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                menu:
                    Alice_04 "Видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                    "Хочется надеяться, что так и будет... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я сейчас более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
                            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_20
                            Max_12 "А-а-ай! Мне же больно, Алиса!"
                            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                            Max_10 "Да я же случайно оказался около душа..."
                            Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2

            elif alice.sorry.give == [3, 1]:
                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                Alice_05 "Может и не буду, только сперва сделаю вот что... А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_21
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Не считается, если она мне неинтересна! Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ punreason[1] = 1
                            $ alice.flags.hugs_type = 1

            elif alice.sorry.give == [3, 2]:
                Alice_13 "Вот значит как! Снова купил эти шоколадки... Спасибо, конечно, но не очень-то тебе хочется избежать наказания, как я вижу."
                Max_08 "Просто так уж вышло... Может, ты всё же не будешь рассказывать маме про то, что было утром?"
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_2
            elif True:

                Alice_03 "Неплохо... Не то, чтобы он мне нравился, не люблю многие начинки, но сойдёт. Спасибо!"
                Max_07 "Так значит, ты ничего не расскажешь маме об утреннем инцеденте?"
                menu:
                    Alice_04 "Видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                    "Хочется надеяться, что так и будет... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я сейчас более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
                            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_22
                            Max_12 "А-а-ай! Мне же больно, Алиса!"
                            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                            Max_10 "Да я же случайно оказался около душа..."
                            Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2

        $ alice.sorry.give.append(2)
        jump alice_sorry_gifts.end

    label alice_sorry_gifts.good:
        $ items[_m1_alicetalk__give].use()
        $ poss['risk'].open(2)
        $ items['ferrero-b'].unblock()
        $ alice.sorry.valid.add('ferrero-b')
        if len(alice.sorry.give) == 0:
            Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
            Max_03 "Никто! Просто угадал..."
            Alice_05 "Хм... Похоже, что ты, Макс, большой везунчик! Поглазел на меня голую в душе, да ещё и с конфетами угадал... Не слишком ли?"
            Max_04 "Просто благоприятное стечение обстоятельств! И я за тобой не подглядывал, просто случайность..."
            menu:
                Alice_04 "В таком случае, видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                "Именно на это я и надеюсь... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                    if RandomChance(_ch1.ch):
                        $ Skill('social', 0.2)
                        Alice_03 "[succes!t]Ладно, Макс, считай твои извинения приняты... Мама ничего не узнает, так что можешь дышать спокойно."
                        Max_07 "И даже без подвоха?!"
                        Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                        Max_01 "О, я понял, сестрёнка! Не буду мешать..."
                    elif True:
                        $ Skill('social', 0.1)
                        Alice_05 "[failed!t]Ладно, Макс, считай твои извинения приняты... А ну-ка иди сюда..."
                        call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_23
                        Max_12 "А-а-ай! Алиса! Больно ведь!"
                        Alice_16 "Будешь ещё, извращенец лохматый, за мной подглядывать?"
                        Max_10 "Да я же случайно оказался около душа..."
                        Alice_05 "Ответ неправильный! Наверно, нужно сильнее потянуть..."
                        Max_14 "Ой! Понял-понял, не буду! Больше не буду..."
                        Alice_02 "Вот и правильно! Гуляй..."
            $ AddRelMood('alice', 0, 50)

        elif len(alice.sorry.give) == 1:
            if alice.sorry.give[0] == 1:
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_05 "Хм... Похоже, что ты, Макс, большой везунчик! Поглазел на меня голую в душе, да ещё и с конфетами угадал... Не слишком ли?"
                Max_04 "Просто благоприятное стечение обстоятельств! И я за тобой не подглядывал, просто случайность..."
                Alice_04 "В таком случае, видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                Max_01 "Хочется надеяться, что так и будет..."
                Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_24
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                Max_10 "Да я же случайно оказался около душа..."
                Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                Max_14 "Ой! Я понял... Больше не буду!"
                Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Разве только это не будет большая коробка моих любимых конфет..."
                Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 50)

            elif alice.sorry.give[0] == 2:
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_05 "Хм... Похоже, что ты, Макс, большой везунчик! Поглазел на меня голую в душе, да ещё и с конфетами угадал... Не слишком ли?"
                Max_04 "Просто благоприятное стечение обстоятельств! И я за тобой не подглядывал, просто случайность..."
                menu:
                    Alice_04 "В таком случае, видимо, я должна представить, что ничего такого утром не было, а значит и маме нечего рассказывать, так?"
                    "Хочется надеяться, что так и будет... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_05 "Ладно, Макс, считай твои извинения приняты... Ого, а что это у тебя здесь..."
                            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_25
                            Max_12 "А-а-ай! Мне же больно, Алиса!"
                            Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                            Max_10 "Да я же случайно оказался около душа..."
                            Alice_05 "Видимо, ты хочешь, чтобы я ещё сильнее тебе ухо выкрутила... Я только с радостью!"
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 50)
            elif True:

                Alice_07 "Ага! Снова купил мои любимые конфеты! Большое тебе спасибо, Макс! Я удивлена, они ведь дорогие..."
                Max_03 "Почему бы не порадовать старшую сестрёнку её любимыми конфетами, если уж возможность подворачивается."
                if _m1_alicetalk__give[-1:] == 'm':
                    menu:
                        Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                        "Хочется надеяться, что так и будет... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                            if RandomChance(_ch1.ch):
                                $ Skill('social', 0.2)
                                Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                                Max_07 "Что, вот так вот просто?!"
                                Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Но, Макс, просто на будущее, знай, в следующий раз ты так легко не отделаешься! Разве только это не будет большая коробка моих любимых конфет..."
                                Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            elif True:
                                $ Skill('social', 0.1)
                                call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain
                                Alice_04 "Ну и просто на будущее, знай, в следующий раз ты так легко не отделаешься! Разве только это не будет большая коробка моих любимых конфет..."
                                Max_11 "Взято на заметку, Алиса! Отпусти уже..."
                                Alice_02 "Вот и молодец! Гуляй..."
                    $ AddRelMood('alice', 0, 100)
                elif True:
                    Alice_05 "В этот раз конфет даже больше, так что я не припоминаю, чтобы утром за мной кто-то подглядывал! Всё было в порядке..."
                    Max_01 "Ну да, меня и рядом тогда не было!"
                    menu:
                        Alice_03 "Я даже подумываю, а не обнять ли тебя, Макс? Ну так... по семейному..."
                        "Только если без последующего насилия... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                            if RandomChance(_ch1.ch):
                                call alice_sorry_gifts.you_deserve from _call_alice_sorry_gifts_you_deserve
                            elif True:
                                call alice_sorry_gifts.what_bummer from _call_alice_sorry_gifts_what_bummer
                    $ AddRelMood('alice', 5, 150, 3)

        elif len(alice.sorry.give) == 2:
            if alice.sorry.give == [1, 1]:
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_05 "Лучше поздно, чем никогда! А ну-ка иди сюда..."
                call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_26
                Max_12 "А-а-ай! Мне же больно, Алиса!"
                menu:
                    Alice_16 "Ещё подглядывать за мной будешь, подлиза ты эдакий?"
                    "Да я же случайно оказался около душа... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_05 "[succes!t]Пожалуй, на этот раз, я поверю и ничего не расскажу маме. Но, на всякий случай, за подглядывание, нужно сильнее потянуть..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 2
                        elif True:
                            $ Skill('social', 0.1)
                            Alice_12 "[failed!t]Ты всерьёз думаешь, что меня можно в этом убедить?! Нет уж, я очень хочу посмотреть, как мама тебя отшлёпает!"
                            Max_14 "Но, Алиса, я же купил вкусняшку... Ой, отпусти!"
                            Alice_05 "Слишком уж долго до тебя доходило, что я больше всего люблю... Так что - не повезло тебе..."
                            Max_14 "Ой! Я понял... Больше не буду!"
                            Alice_02 "Вот и молодец! Гуляй..."
                            $ alice.flags.hugs_type = 1
                            $ punreason[1] = 1

            elif alice.sorry.give == [1, 2]:
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_3
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [1, 3]:
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                menu:
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                    "Хочется надеяться, что так и будет... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            menu:
                                Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. Я даже подумываю, а не обнять ли тебя, Макс? Ну так... совсем немного..."
                                "Только если без последующего насилия... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                                    if RandomChance(_ch1.ch):
                                        $ Skill('social', 0.2)
                                        Alice_04 "[succes!t]Пожалуй ты заслужил это своими подарками..."
                                        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_2
                                        Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
                                        Alice_07 "Я вижу, что ты не просто хочешь избежать наказания, а ещё и мне приятно сделать стремишься. Вот я и не вредничаю..."
                                        Max_05 "Да, надо бы почаще так делать."
                                        Alice_02 "Подглядывать за мной или дарить мне сладости?!"
                                        Max_02 "Второе, конечно!"
                                        Alice_05 "Ну да, конечно... Иди давай."
                                        $ alice.flags.hugs_type = 4
                                    elif True:
                                        $ Skill('social', 0.1)
                                        Alice_05 "[failed!t]Ах, а так хотелось! Какой облом..."
                                        Max_09 "Обнять меня или придушить?"
                                        Alice_07 "Зачем останавливаться на чём-то одном, Макс? Хи-хи..."
                                        Max_01 "Я тогда лучше пойду... погуляю."
                                        Alice_02 "Ну как хочешь..."
                                        $ alice.flags.hugs_type = 3
                        elif True:
                            $ Skill('social', 0.1)
                            call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain_1
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [2, 1]:
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_4
                $ AddRelMood('alice', 0, 50)

            elif alice.sorry.give == [2, 2]:
                Alice_07 "Ничего себе! Ты даже умудрился купить мои любимые конфеты! Большое спасибо! И кто об этом проболтался?"
                Max_03 "Никто! Просто повезло, а может твоя подсказа помогла."
                menu:
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                    "Хочется надеяться, что так и будет... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        elif True:
                            $ Skill('social', 0.1)
                            call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain_2
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 50)

            elif alice.sorry.give == [2, 3]:
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                menu:
                    Alice_03 "Я даже подумываю, а не обнять ли тебя, Макс? Ну так... совсем немного..."
                    "Только если без последующего насилия... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            call alice_sorry_gifts.you_deserve from _call_alice_sorry_gifts_you_deserve_1
                        elif True:
                            call alice_sorry_gifts.what_bummer from _call_alice_sorry_gifts_what_bummer_1
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [3, 1]:
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                Max_01 "Хочется надеяться, что так и будет..."
                call alice_sorry_gifts.apology_accepted from _call_alice_sorry_gifts_apology_accepted_5
                $ AddRelMood('alice', 0, 100)

            elif alice.sorry.give == [3, 2]:
                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                menu:
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                    "Хочется надеяться, что так и будет... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                        if RandomChance(_ch1.ch):
                            $ Skill('social', 0.2)
                            Alice_03 "[succes!t]Ладно, так тому и быть, считай твои извинения приняты... Мама ничего не узнает, так что можешь не напрягаться."
                            Max_07 "Что, вот так вот просто?!"
                            Alice_05 "Ну, ты обещал мне вкусняшку и сдержал слово. А я добрая, если настроение хорошее. Более-менее добрая... Так что не искушай судьбу!"
                            Max_01 "Понял, сестрёнка! Не буду тебе мешать..."
                            $ alice.flags.hugs_type = 3
                        elif True:
                            $ Skill('social', 0.1)
                            call alice_sorry_gifts.im_in_pain from _call_alice_sorry_gifts_im_in_pain_3
                            Alice_02 "Вот и молодец! Гуляй..."
                $ AddRelMood('alice', 0, 100)
            elif True:

                Alice_07 "Ага! Снова купил мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
                Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
                if _m1_alicetalk__give[-1:] == 'm':
                    Alice_04 "Видимо, теперь я должна представить, что никто утром за мной в душе не подглядывал, да?"
                    Max_01 "Хочется надеяться, что так и будет..."
                    menu:
                        Alice_03 "Я даже подумываю, а не обнять ли тебя, Макс? Ну так... совсем немного..."
                        "Только если без последующего насилия... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                            if RandomChance(_ch1.ch):
                                call alice_sorry_gifts.you_deserve from _call_alice_sorry_gifts_you_deserve_2
                            elif True:
                                call alice_sorry_gifts.what_bummer from _call_alice_sorry_gifts_what_bummer_2
                    $ AddRelMood('alice', 0, 100)
                elif True:
                    Alice_05 "Конфет так много, что я не припоминаю, чтобы утром за мной кто-то подглядывал! Всё было в порядке..."
                    Max_01 "Ну да, меня и рядом тогда не было!"
                    Alice_04 "Я даже обниму тебя за это! Ну так... совсем немного... Иди ко мне."
                    call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_3
                    Max_03 "Вау! Это как-то очень непривычно... обнимать тебя без ущерба своему здоровью!"
                    Alice_07 "Я вижу, что ты не просто хочешь избежать наказания, а ещё и мне приятно сделать стремишься. Вот я и не вредничаю..."
                    Max_05 "Да, надо бы почаще так делать."
                    Alice_02 "Подглядывать за мной или дарить мне сладости?!"
                    Max_02 "Второе, конечно!"
                    Alice_05 "Ну да, конечно... Иди давай."
                    $ alice.flags.hugs_type = 4
                    $ AddRelMood('alice', 5, 150, 3)

        $ alice.sorry.give.append(3)
        jump alice_sorry_gifts.end

    label alice_sorry_gifts.end:
        $ spent_time += 10
        jump Waiting


label alice_about_bath:
    $ alice.flags.incident = 2
    Alice_12 "Ты о чём, Макс?"
    Max_01 "Ну, ты вернулась ночью из клуба и мы разговаривали в ванной..."
    menu:
        Alice_13 "Я не помню такого... Тебе приснилось!"
        "Ты мне кое-что показала..." if True:
            Alice_05 "Что?! Всё ты врёшь, Макс. Не было такого!"
            Max_02 "Да? Ну, думай так..."
            Alice_13 "Макс. Повторяю, ничего не было. И даже если и было, ты об этом забудешь, если хочешь жить. Ты меня понял?"
            Max_03 "Конечно..."
            Alice_16 "Я серьёзно! А теперь вали отсюда..."
            Max_01 "Хорошо..."
            $ AddRelMood('alice', 0, -50)
            jump alice_about_bath.end
        "Ты мне кое-что сделала..." if True:
            pass
        "Мы делали кое-что..." if True:
            pass
        "Да, ну извини..." if True:
            Alice_03 "Надо же, даже извинился... Вот только я правда мало что помню. Будем считать, что ничего и не было. И не напоминай мне больше об этом. Понял?"
            Max_03 "Ага..."
            $ AddRelMood('alice', 0, 50)
            jump alice_about_bath.end

    Alice_15 "Что?! Макс! Ты всё врёшь! Если это правда, я тебя убью, обещаю! А если нет, то тоже! Быстро свалил отсюда!"
    Max_01 "Хорошо..."
    $ AddRelMood('alice', 0, -100)
    jump alice_about_bath.end

    label alice_about_bath.end:
        $ spent_time += 10
        jump Waiting


label alice_about_kiss:
    $ renpy.block_rollback()
    Alice_02 "Прости, Макс, что?"
    Max_01 "Да вот спрашиваю, умеешь ты целоваться или нет?"
    Alice_05 "Да, не показалось... Тебе заняться больше нечем, Макс?"
    Max_08 "Мне срочно нужно научиться целоваться, и я не знаю кто может помочь..."
    Alice_07 "Срочно?! Бедняжка... Ты знаешь, я в каком-то фильме смотрела, там учились целоваться на помидорах. Попробуй, может получится хотя бы у тебя..."
    Max_07 "Алиса, я серьёзно же!"
    Alice_12 "Макс, отвали. Я не буду целоваться с тобой, даже не мечтай. И придумай другой способ клеиться, а то этот на уровне детского сада, серьёзно."
    Max_09 "Да я не клеился!"

    $ flags.how_to_kiss.append('alice')
    $ spent_time += 10
    return


label talkblog2:


    Alice_00 "Я тебя внимательно слушаю..."
    Max_00 "Я выяснил, какие блоги популярны..."
    Alice_02 "Открыл топ блогов и посмотрел? Или что-то более толковое удалось выяснить?"
    Max_01 "В общем, тебе нужно сделать акцент на форме, а не на содержании..."
    Alice_01 "Ты хочешь сказать, что не важно о чём мой блог, важно как я его веду? Я об этом думала... И если ты помнишь, проблема всё ещё в одежде. Я не могу в одном и том же появляться постоянно, если это бьюти-блог..."
    Max_07 "А если это не бьюти-блог?"
    Alice_05 "И что же это? Я больше ничего не умею... Или ты на что намекаешь?"
    Max_02 "Как у тебя со скромностью дела?"
    Alice_06 "Кажется, я знаю к чему ты клонишь, Макс. Наверняка, ты насмотрелся каких-нибудь девочек, которые крутят задницами перед камерами за деньги? Нет, я на это не соглашусь!"
    Max_03 "Воу... Я не думал об этом, но если ты говоришь..."
    Alice_12 "Я знаю, что на этом можно много заработать, но вдруг кто-то из моих друзей или знакомых увидит... Нет, я на это не пойду."
    Max_09 "Ты уверена в этом?"
    Alice_00 "Да, Макс! Уверена, я смогу развить свой блог и без этого."
    Max_00 "Ясно. Нет, так нет..."
    $ poss['blog'].open(3 if len(house[1].cams) else 2)
    $ spent_time += 10
    jump Waiting


label talkblog3:



    Alice_02 "Не особо? Это как? Раздеваться частично?"
    Max_07 "Ты можешь рекламировать что-то..."
    Alice_05 "Макс, да все блогеры что-то рекламируют. Ты снова не изобрёл велосипед..."
    Max_01 "Я имею в виду другое..."
    Alice_03 "Хорошо, я внимательно слушаю..."
    Max_04 "Ты можешь рекламировать нижнее бельё или игрушки для взрослых."
    Alice_05 "Макс... Это не очень отличается от той идеи с позированием перед камерами за деньги... Хотя, в этом что-то есть, конечно. И я не об игрушках для взрослых..."
    Max_03 "Значит, нижнее бельё?"
    Alice_13 "Ну можно попробовать. Однако, главная проблема остаётся в силе, у меня только один комплект белья, тот в котором я сплю, а этого мало даже чтобы просто начать... И денег на новое нет..."
    Max_07 "Ну а если я тебе его подарю?"
    menu:
        Alice_05 "Ты подаришь мне нижнее бельё? На какие деньги? И что я за это буду тебе должна?"
        "Ничего..." if True:
            Alice_02 "И давно ты в альтруисты записался?"
            Max_01 "Я просто хочу помочь..."
        "Может, попозируешь для меня..." if True:

            Alice_02 "Только и всего? Если там что-то приличное, то почему нет..."
            Max_03 "Было бы супер!"

    Alice_03 "Давай попробуем, но я не уверена и ничего не обещаю. Твои вложения могут оказаться бесполезными... Для начала мне нужно бельё просто для того, чтобы заинтересовать людей."
    Max_07 "Для начала?"
    Alice_00 "Ага. Затем, уже нужно будет найти рекламодателей, которые будут присылать бельё, которое я и буду рекламировать. Обычно это так делается... Или ты думал, что мне кто-то будет платить за моё же бельё?"
    Max_00 "Ну, если это так делается..."
    Alice_01 "Да, Макс. Причём, желающих на этом зарабатывать больше, чем желающих за это платить. И в этом главная проблема. Но как я уже сказала, я могу попробовать. Если купишь что-то, посмотрим..."
    Max_01 "Понял, с меня симпатичное бельишко..."
    $ poss['blog'].open(4)
    $ items['b.lingerie'].unblock()
    $ spent_time += 10
    jump Waiting


label gift_black_lingerie:

    if _in_replay:

        if alice.plan_name == 'sun':
            call alice_sun from _call_alice_sun_1
        elif True:
            if tm > '20:00':
                call alice_evening_closer from _call_alice_evening_closer_1
            elif True:
                call alice_morning_closer from _call_alice_morning_closer_1

    $ _ch1 = GetChance(mgg.social, 2, 900)
    Alice_02 "И что же это? Я должна угадать?"
    Max_01 "Нижнее бельё..."
    menu:
        Alice_07 "Ой. Это супер! Симпатичное? Дай посмотреть..."
        "Ну что, примеришь при мне?" if 'pajamas' in alice.gifts or _in_replay:
            $ _ch1 = Chance(1000)
            Alice_05 "Примерю при тебе? Об этом мы не договаривались. Я покажусь в нём, но... Хотя, ладно. Примерю при тебе, но ты не подглядывай! Увижу, что смотришь, получишь и пойдёшь в бассейн. Вниз головой."

        "Ну что, примеришь при мне? {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if 'pajamas' not in alice.gifts and not _in_replay:
            if not RandomChance(_ch1.ch) and not _in_replay:

                Alice_12 "[failed!t]Примерю при тебе? Об этом мы не договаривались. Я покажусь в нём и только... А если будешь и дальше упрашивать, то вообще ничего не увидишь! Понял?"
                Max_10 "Да понял... Ладно. Буду ждать за дверью."


                $ renpy.scene()
                $ renpy.show('location house aliceroom door-'+get_time_of_day())
                Max_09 "{i}( А посмотреть-то хочется! Быстренько оббежать комнаты и подглядеть в окно? Может заметить... Или пойти в комнату и подглядеть через камеру? Пока дойду и открою свой сайт она уже переоденется... Эх, вот я пролетел! ){/i}"
                Alice "{b}Алиса:{/b} Всё, Макс. Можешь заходить..."


                scene BG char Alice newpajamas
                $ renpy.show('Alice newlingerie '+'08' if '09:00' <= tm < '20:00' else '08e')
                Alice_01 "Ну, как тебе? Хорошо сидит? Вроде бы немного лифчик не того размера... Или нет... Ну, Макс, чего молчишь?"
                Max_05 "Ну, я... э..."
                Alice_05 "Контуженый что ли? Я тебя спрашиваю хорошо сидит или нет... Хотя... по тебе же всё сразу видно. Значит, всё в порядке..."
                Max_02 "Ага, полный порядок!"
                $ poss['blog'].open(5)
                jump gift_black_lingerie.final
            elif True:

                Alice_05 "[succes!t]Примерю при тебе? Об этом мы не договаривались. Я покажусь в нём, но... Хотя, ладно. Примерю при тебе, но ты не подглядывай! Увижу, что смотришь, получишь и пойдёшь в бассейн. Вниз головой."

    Max_00 "Опять угрозы..."
    $ _m1_alicetalk__suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
    if not ('09:00' <= tm < '20:00'):
        $ _m1_alicetalk__suf += 'e'
    scene BG char Alice newpajamas
    $ renpy.show('Alice newpajamas 01'+_m1_alicetalk__suf)
    Alice_03 "Макс, у тебя же есть инстинкт самосохранения, верно? Не вздумай подглядывать!"
    Max_01 "Ага..."
    if not _in_replay:
        $ SetCamsGrow(house[1], 160)


    scene BG char Alice newpajamas
    if renpy.random.randint(0, 1) > 0 and alice.dress!='c':

        $ renpy.show('Alice newpajamas 02'+_m1_alicetalk__suf)
        Alice_01 "Макс! Ты что, пялишься на мою грудь? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"
        Max_03 "Я не пялюсь..."

        $ renpy.show('Alice newlingerie 04'+_m1_alicetalk__suf)
        Alice_02 "Похоже, размер мне подходит... и удобно. ... Ну, как тебе?"
        Max_04 "Тебе идёт! Мне нравится..."

        $ _m1_alicetalk__suf = 'a' if alice.dress=='a' and alice.req.result != 'nopants' else 'an'
        $ _m1_alicetalk__suf += 'e' if not ('09:00' <= tm < '20:00') else ''
        if _m1_alicetalk__suf in ['an', 'ane'] and alice.req.result == 'nopants':

            Alice_05 "Класс! А теперь быстро отвернись, а то на мне трусиков нет, благодаря твоим уговорам! Нужно ещё новые трусики примерить."
            $ renpy.show('Alice newlingerie 06'+_m1_alicetalk__suf)
            Max_02 "Конечно, я не смотрю..."
        elif True:

            Alice_03 "Отлично! А теперь отвернись, не подглядывай! Нужно ещё трусики примерить."
            $ renpy.show('Alice newlingerie 06'+_m1_alicetalk__suf)
            if alice.req.result != 'not_nopants':
                Max_02 "Конечно, я не смотрю..."
            elif True:

                Max_08 "Конечно, я не смотрю... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"
                Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                Max_01 "Ладно, считай, я ничего не видел."
                $ alice.req.noted = True

        $ renpy.show('Alice newlingerie '+('08' if '09:00' <= tm < '20:00' else '08e'))
        Alice_07 "Размер в самый раз... ... Как тебе, Макс? Хорошо сидит?"
        Max_05 "Не то слово, всё выглядит шикарно!"
        if not _in_replay:
            $ poss['blog'].open(6)
        jump gift_black_lingerie.final
    elif True:


        $ _m1_alicetalk__suf = 's' if alice.plan_name in ['sun', 'swim'] else alice.dress
        if _m1_alicetalk__suf=='a' and alice.req.result == 'nopants':
            $ _m1_alicetalk__suf += 'n'
        if not ('09:00' <= tm < '20:00'):
            $ _m1_alicetalk__suf += 'e'
        $ renpy.show('Alice newpajamas 03'+_m1_alicetalk__suf)
        if _m1_alicetalk__suf in ['a', 'ae']:

            Alice_03 "Макс! Ты что, пялишься на мой зад? Тут же кругом зеркала и я всё вижу! Быстро отвернись!"
            if alice.req.result != 'not_nopants':

                Max_02 "Я не пялюсь..."
            elif True:

                Max_08 "Я не пялюсь... Эй! А ты же ведь не должна носить трусики! У нас ведь уговор!"
                Alice_06 "Вот чёрт! Да... я забыла, что сегодня не должна их носить! А ты сейчас не должен был этого увидеть, так что молчи... а то выпну отсюда..."
                Max_01 "Ладно, считай, я ничего не видел."
                $ alice.req.noted = True
        elif _m1_alicetalk__suf in ['an', 'ane']:

            if not _in_replay:
                $ SetCamsGrow(house[1], 180)
            Alice_05 "Макс! Ты что, пялишься на мой зад? Быстро отвернись, на мне же нет трусиков, благодаря твоим уговорам!"
            Max_02 "Я не пялюсь..."
        elif True:

            if not _in_replay:
                $ SetCamsGrow(house[1], 180)
            Alice_03 "Макс! Ты что, пялишься на мой зад? Тут же кругом зеркала и я всё вижу! Быстро отвернись, на мне же нет трусиков!"
            Max_02 "Я не пялюсь..."

        $ _m1_alicetalk__suf = 's' if alice.plan_name in ['sun', 'swim'] else 'a' if alice.dress in ['a', 'c'] else alice.dress
        if not ('09:00' <= tm < '20:00'):
            $ _m1_alicetalk__suf += 'e'
        $ renpy.show('Alice newlingerie 05'+_m1_alicetalk__suf)
        Alice_02 "Размер в самый раз... ... Как тебе, Макс? Хорошо сидят?"
        Max_04 "Не то слово, сидят прекрасно!"
        Alice_01 "Здорово! А теперь отвернись, не подглядывай! Нужно ещё лифчик примерить."

        $ renpy.show('Alice newlingerie '+('07' if '09:00' <= tm < '20:00' else '07e'))
        Max_03 "Конечно, я не смотрю..."

        $ renpy.show('Alice newlingerie '+('08' if '09:00' <= tm < '20:00' else '08e'))
        Alice_07 "Похоже, размер мне подходит... и удобно. Очень лёгонький топик. Ну, как тебе всё в целом?"
        Max_05 "Тебе идёт, всё выглядит шикарно!"
        if not _in_replay:
            $ poss['blog'].open(6)
        jump gift_black_lingerie.final

    label gift_black_lingerie.final:
        if not _in_replay:
            call alice_add_black_linderie from _call_alice_add_black_linderie

    Alice_02 "Ну, спасибо тебе. Да, в этом точно можно покрасоваться перед камерами. Не уверена, что даст эффект, но я же одета... В общем, я попробую!"
    Max_04 "Этого достаточно?"
    Alice_03 "Сомневаюсь, если честно. Ты знаешь... Давай попробуем на всякий случай ещё кое-что. Поищи что-нибудь более сексуальное. Ничего не обещаю, но вдруг поможет..."
    Max_01 "Хорошо, я что-нибудь подыщу..."
    $ renpy.end_replay()

    $ spent_time += 30
    jump Waiting


label alice_gift_sweets:

    menu:
        Alice_02 "Да ладно! Это мне нравится... И что там у тебя?"
        "Конфеты \"Ferrero Rocher\" (16 штук)" if items['ferrero-m'].have:
            $ _m1_alicetalk__give = 'ferrero-m'
        "Конфеты \"Ferrero Rocher\" (24 штуки)" if items['ferrero-b'].have:
            $ _m1_alicetalk__give = 'ferrero-b'

    $ items[_m1_alicetalk__give].use()
    Alice_07 "Ага! Мои любимые конфеты! Как здорово... Большое тебе спасибо, Макс!"
    Max_03 "Я люблю радовать старшую сестрёнку её любимыми конфетами."
    if _m1_alicetalk__give=='ferrero-m':

        $ _ch1 = GetChance(mgg.social, 3, 900)
        menu:
            Alice_03 "Я даже подумываю, а не обнять ли тебя за это, Макс? Ну так... совсем немного..."
            "Только если без последующего насилия... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                pass
        if RandomChance(_ch1.ch):
            $ Skill('social', 0.2)
            Alice_04 "[succes!t]Ладно, Макс, пожалуй ты это заслужил..."

            call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_4
            Max_03 "Хорошо, что хоть так можно взять и обнять тебя без ущерба своему здоровью!"
            Alice_07 "Я вижу, что ты действительно стремишься сделать мне приятно, вот я и не вредничаю..."
            Max_05 "Да, надо бы почаще так делать."
            Alice_13 "Ой, Макс, нет! Почаще - не надо... А то я фигуру испорчу, мне так нельзя!"
            Max_02 "Согласен, такую стройную фигуру лучше не портить... Но временами, любимыми конфетами можно и побаловаться!"
            Alice_05 "Ну да, временами... И сейчас как раз такой момент!"
            Max_01 "Наслаждайся, сластёна! Не буду мешать..."
            $ alice.flags.hugs += 1
            $ infl[alice].add_m(12)
        elif True:
            $ Skill('social', 0.2)
            Alice_05 "[failed!t]Ах, а так хотелось! Какой облом..."

            call alice_sorry_gifts.kick_ears from _call_alice_sorry_gifts_kick_ears_27
            Max_09 "Ну вот, я тебе любимые конфеты покупаю от чистого сердца, а ты..."
            Alice_07 "Не повезло тебе просто сегодня... Если бы купил большую коробку конфет, я бы чувствовала себя самой любимой сестрёнкой! А так..."
            Max_01 "Понятно всё с тобой. Я тогда лучше пойду..."
    elif True:

        Alice_04 "Я даже обниму тебя за это! Ну так... совсем немного... Иди ко мне."

        call alice_sorry_gifts.kindred_hugs from _call_alice_sorry_gifts_kindred_hugs_5
        Max_03 "Хорошо, что хоть так можно взять и обнять тебя без ущерба своему здоровью!"
        Alice_07 "Я вижу, что ты действительно стремишься сделать мне приятно, вот я и не вредничаю..."
        Max_05 "Да, надо бы почаще так делать."
        if all([alice.daily.oiled==2, mgg.dress>'b']):

            Alice_12 "Так, Макс, это что за дела? У тебя почему стоит? На меня что ли?"
            Max_02 "Даже не знаю! Здесь больше никого нет. Похоже, что на тебя..."
            Alice_03 "Ты же в курсе, что есть иные способы сказать, что я нисколько не порчу этими конфетами фигуру?"
            Max_04 "Ну, а я выдал комплимент без слов! Честнее некуда."
            Alice_05 "Ну да, я вижу... Считай, этот комплимент принят!"
            Max_01 "Наслаждайся конфетами, сластёна! Не буду мешать..."
        elif True:
            Alice_13 "Ой, Макс, нет! Почаще - не надо... А то я фигуру испорчу, мне так нельзя!"
            Max_02 "Согласен, такую стройную фигуру лучше не портить... Но временами, любимыми конфетами можно и побаловаться!"
            Alice_05 "Ну да, временами... И сейчас как раз такой момент!"
            Max_01 "Наслаждайся, сластёна! Не буду мешать..."
        $ alice.flags.hugs += 1
        $ infl[alice].add_m(20)
    $ spent_time += 10


    $ alice.dcv.sweets.set_lost(renpy.random.randint(5, 7))
    jump Waiting


label alice_about_lingerie0:
    Alice_12 "Слышал или подслушал?"
    Max_01 "Слышал. Эрик мне и сказал."
    Alice_05 "Да, мне нужно ещё одно сексуальное боди. И я показала ему, какое конкретно хочу. Решили, что купим, когда поедем на шопинг в субботу. А что?"
    Max_02 "Да так, интересно было, какое ты себе боди захотела. Покажешь?"
    if current_room == house[1]:
        jump alice_showing_lingerie1
    elif True:
        Alice_03 "Для этого компьютер нужен. Так что, если интересно, то заходи, когда я в своей комнате. Покажу..."
        Max_01 "Ага. Обязательно зайду"
        $ alice.dcv.intrusion.stage = 2

    $ spent_time += 10
    jump Waiting


label alice_showing_lingerie1:


    if tm>='20:00' and GetWeekday(day) in [3, 4]:
        $ renpy.show('Alice blog 02'+alice.dress)
        $ renpy.show('Max blog 04'+mgg.dress)
    Alice_03 "Вот, смотри... Боди, как боди, слегка прозрачное и кружевное. Всё, как вы, мальчики, любите."
    Max_03 "Ну да, мне уже не терпится увидеть его на тебе!"
    Alice_05 "Это если я ещё разрешу тебе смотреть на меня в этом боди! Вот Эрик купит - ему и можно будет смотреть, ну и тем, для кого я всё это рекламирую."
    Max_11 "А как же я?"
    Alice_02 "Интернет тебе в помощь, Макс! Там полно всяких разных девушек в любом нижнем белье. Может и меня там найдёшь, уже..."
    Max_08 "Ладно, я тебя понял."
    Max_09 "{i}( Мне ещё как можно будет на тебя смотреть, когда я куплю это боди первее Эрика! Вот только времени совсем в обрез, надо торопиться... Блин, Эрик точно будет этому не рад! Стоит ли оно того, это боди? ){/i}"

    $ alice.dcv.intrusion.stage = 3
    $ items['sexbody2'].unblock()
    $ notify_list.append(_("В интернет-магазине доступен новый товар."))
    $ spent_time += 10
    jump Waiting


label gift_lace_lingerie:


    Alice_15 "Ого! В смысле, то самое, которое я тебе показывала или какое-то другое?"
    Max_01 "Да, то самое. Ты же не против?"
    Alice_05 "Конечно не против! Давай его сюда, буду примерять... Только, если не будешь смотреть..."
    Max_03 "Конечно! Мне не терпится увидеть, как оно на тебе сидит..."


    scene BG char Alice spider-night-04
    $ renpy.show('Max newbody2 01'+mgg.dress)
    $ renpy.show('Alice newbody2 '+renpy.random.choice(['01', '02', '03'])+alice.dress)
    Alice_12 "Неплохо это ты уселся в первых рядах, Макс! Отвернись хоть для приличия или живо пойдёшь гулять..."
    Max_02 "Я глаза закрою..."


    $ renpy.show('Alice newbody2 '+renpy.random.choice(['04', '05', '06'])+alice.dress)
    Alice_14 "Эй! Макс! Ты же сказал, что закроешь глаза. Хорошо я заметила, что ты пялишься на меня, прежде чем всё с себя сняла! Отвернись, быстро! Ну или хотя бы закрой глаза руками..."
    Max_04 "Ты так красиво начала раздеваться, что я забыл не смотреть. Считай, закрыл."


    $ renpy.show('Max newbody2 02'+mgg.dress)
    Alice_05 "Смотри мне, Макс! Я ведь сразу увижу в зеркало, если ты начнёшь подглядывать сквозь пальцы. Ты же не хочешь получить с ноги за это?"
    $ _ch1 = GetChance(mgg.stealth, 1.5, 900)
    menu:
        Max_19 "Естественно, не хочу."
        "{i}подглядывать {color=[_ch1.col]}(Скрытность. Шанс: [_ch1.vis]){/color}{/i}" if True:
            show FG blog-dresses-max-03
            if RandomChance(_ch1.ch) or _in_replay:


                $ renpy.show('Alice newbody2 '+renpy.random.choice(['07', '08']))
                Max_02 "{i}( Ага, взял и закрыл! Я что, совсем святой, чтобы не рискнуть хоть одним глазком увидеть голую Алису! Да ещё так близко! Бесподобная у меня сестрёнка... ){/i}"

                $ renpy.show('Alice newbody2 '+renpy.random.choice(['09', '10']))
                Max_07 "{i}( Ухх... Алиса не спешит спрятать свои аппетитные сисечки под боди! Прямо, как мне и хочется... Хм, а может она заметила, что я всё равно подглядываю и таким образом дразнит меня?! Знать бы это наверняка... ){/i}"
            elif True:



                Alice_18 "Макс!!!"
                hide FG
                menu:
                    Max_08 "Не бей! Я просто тебя проверял. На внимательность..."
                    "{i}ждать{/i}" if True:
                        pass
        "{i}ждать{/i}" if True:
            pass



    hide FG
    $ renpy.show('Max newbody2 01'+mgg.dress)
    show Alice newbody2 11
    Alice_02 "Всё, можно смотреть... Что скажешь, тебе нравится или нет? Мне вот в нём удобно..."
    Max_04 "Алиса, на твоём чудесном теле, что угодно будет смотреться шикарно. И да, мне нравится, как это выглядит! Покрутись ещё немного для меня..."


    show Alice newbody2 12
    Alice_06 "Ну как, всё посмотрел? Ай!!! У меня ногу свело! Ой, как же сильно свело... Ой-ёй-ёй!!!"
    Max_07 "Которую? Давай её мне, я помассирую..."


    scene BG char Alice blog-mass-01
    show Alice newbody2 mass-01
    $ renpy.show("Max newbody2 mass-01"+mgg.dress)
    Alice_13 "Правую. Ой, Макс! По-моему, лучше не трогать... Очень уж тянет. А хотя... вроде лучше... Да, так намного лучше... Фух!"
    Max_09 "Многовато ты за компьютером времени проводишь. Двигаться надо побольше."
    Alice_05 "Ой, ну вторая мама появилась у меня! Просто разок свело ногу, подумаешь."
    Max_08 "Ага, скоро снова сведёт, это я тебе гарантирую. На онлайн-курсах узнал, если сводит, то нужно или двигаться больше, или массаж делать серьёзнее."


    scene BG char Alice blog-mass-02
    show Alice newbody2 mass-02
    $ renpy.show("Max newbody2 mass-02"+mgg.dress)
    Alice_03 "Двигаться больше — это спортом заниматься, ты хочешь сказать? Не люблю я это. Я люблю на солнышке понежиться, за книжкой посидеть или перед экраном ТВ или компьютера. Ты же знаешь."
    Max_07 "Знаю. Значит массаж. Надо больше внимания уделить твоим ножкам. Согласна?"
    Alice_05 "А согласна! Ты так самоотверженно мне сейчас ногу помассировал. Даже ни разу не попытался на грудь мою засмотреться или ещё куда. А боди ведь слегка прозрачное!"
    Max_02 "Да я твои сосочки наизусть знаю! Это шутка..."
    Alice_01 "Но правдивая, извращенец ты мелкий! Давай гуляй, у меня блог простаивает... И спасибо за подарок. Нужно будет Эрику не забыть сказать, что ты его опередил. Это же не станет для вас проблемой?"
    Max_01 "Разберёмся как-нибудь, не переживай."


    $ renpy.end_replay()
    $ added_mem_var('lace_ling_max1')
    $ spent_time += 40
    $ alice.dcv.intrusion.stage = 5
    $ items['sexbody2'].give()
    $ alice.gifts.append('sexbody2')
    $ setting_clothes_by_conditions()
    $ infl[alice].add_m(40)
    $ poss['blog'].open(18)
    jump Waiting


label alice_about_defend_punish0:


    Alice_12 "Эээ... Прекрасно сидится, как видишь."
    Max_02 "Ну ещё бы, ведь твою симпатичную попку никто сегодня не отшлёпал, благодаря мне."
    Alice_05 "А, вот ты о чём! Ну да, моя попка цела и невредима. Почаще бы ты меня от маминой руки ещё спасал, было бы супер!"
    Max_07 "Да как-то не очень хочется, на самом деле, вообще это делать. По крайней мере за просто так."
    Alice_13 "А что ты хочешь? Гадости какие-нибудь наверняка..."
    Max_03 "Самое правильное - это всё равно тебя наказать! Только в отличие от мамы, я сделаю это с нежностью."
    Alice_15 "Чего?! Вот ещё! Чтобы меня младший брат наказывал? Обойдёшься, Макс!"
    Max_09 "Ты уверена? Ох, не сладко тебе будет без моего вмешательства. Но дело твоё."
    Alice_05 "Вот именно."

    $ spent_time += 10
    $ alice.dcv.private.stage = 1
    jump Waiting


label alice_about_defend_punish1:


    $ alice.dcv.private.stage = 3
    Alice_13 "Так ты позлорадствовать пришёл. Нет, чтобы заступиться за сестрёнку..."
    Max_01 "Если разрешишь тебя немного пошлёпать за это, то буду заступаться."
    Alice_12 "Макс, давай иначе договоримся? Это отстой..."
    Max_09 "Иногда получать от меня легонько по попке - это значит отстой, а всегда и сурово от мамы - это класс?! Ты ведь даже не знаешь, как я буду шлёпать!"
    $ _ch1 = GetChance(mgg.social, 1.5, 900)
    menu:
        Alice_16 "Я и узнавать не хочу!"
        "Ладно, как знаешь... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
            jump alice_about_defend_punish1.convince

    label alice_about_defend_punish1.cont:
        $ _ch1 = GetChance(mgg.social, 1.5, 900)
        menu:
            Alice_12 "Чтобы меня младший брат наказывал? Обойдёшься, Макс!"
            "Ладно, как знаешь... {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                jump alice_about_defend_punish1.convince

    label alice_about_defend_punish1.convince:
        if not RandomChance(_ch1.ch):

            Alice_17 "Я лучше от мамы наказания потерплю, чем от тебя..."
            Max_07 "Ох, не завидую я тебе..."
        elif True:

            Alice_06 "А ты точно не больно будешь шлёпать?"
            Max_04 "Точно."
            Alice_05 "Ладно, можешь меня шлёпать. Конечно, если от мамы спасёшь. Тогда и поговорим."
            Max_01 "Я постараюсь."
            $ poss['ass'].open(0)
            $ alice.dcv.private.stage = 4
            $ alice.dcv.private.set_lost(0)

    $ spent_time += 10
    jump Waiting


label alice_about_private_punish:

    if tm> '19:00' and 1<GetWeekday(day)<5:

        Alice_13 "Макс, давай завтра! Днём, например. Когда мы дома одни остаёмся... Ну и всё, что выпадет на выходные дни, будем переносить на понедельник, хорошо?"
        $ alice.dcv.private.set_lost(2)
    elif True:

        Alice_13 "Макс, давай теперь уже в понедельник днём! Когда мы дома одни остаёмся..."
        $ alice.dcv.private.set_lost(2+GetWeekday(day)-5)

    Max_04 "Без проблем."
    Alice_16 "И смотри, если мне будет больно, то ты с фингалом ходить неделю будешь... Ясно?"
    Max_01 "Ага, не переживай."
    $ alice.flags.private = True
    $ spent_time += 10
    jump Waiting


label alice_private_punish_0:

    Alice_03 "Эх, Макс... Я так хорошо лежала и загорала. Ну да ладно, где это сделам?"
    jump alice_private_punish_0.pun

    menu alice_private_punish_0.smoke:
        Alice_00 "Макс, поглазеть пришёл?"
        "Пора отшлёпать одну милую попку!" if True:
            Alice_05 "Да, Макс, сейчас... Только дай докурю спокойно и я в твоём распоряжении."
            menu:
                Max_03 "Хорошо. Я подожду..."
                "{i}подождать Алису{/i}" if True:
                    pass

            scene BG punish-sun 01
            show Alice punish-sun 01-01
            $ renpy.show("Max punish-sun 01-01"+mgg.dress)
            Alice_03 "Всё, я готова. Где это сделам?"
            jump alice_private_punish_0.pun

    label alice_private_punish_0.pun:
        Max_01 "Да прямо тут, во дворе."


    scene BG punish-sun 02
    $ renpy.show("Alice punish-sun 02-01"+mgg.dress)
    Alice_05 "Ладно, давай здесь. Только не больно, хорошо? И не приставать!"
    Max_02 "Ага, раздевайся давай..."


    $ renpy.show("Alice punish-sun 02-02"+mgg.dress)
    Alice_14 "Чего?! В смысле, раздевайся? О таком мы не договаривались!"
    Max_07 "Это само собой разумеющееся, Алиса. Со всеми претензиями обращайся к маме, это ведь она установила такой порядок наказаний."
    menu:
        Alice_13 "Если ты думаешь, что я стану тут перед тобой раздеваться..."
        "{i}стянуть верх купальника{/i}" if True:
            pass

    $ renpy.show("Alice punish-sun 02-03"+mgg.dress)
    Alice_15 "Макс!!! Ты офигел так делать?! Я же тебе сейчас уши оторву..."
    menu:
        Max_09 "Сколько от тебя шума, Алиса! Да ещё и по такому пустяку. Надоели уже твои угрозы."
        "{i}стянуть низ купальника{/i}" if True:
            pass

    $ renpy.show("Alice punish-sun 02-04"+mgg.dress)
    Alice_06 "Дикарь ты и извращенец! Я тебе потом такое устрою..."
    Max_01 "Ага, обязательно. Только давай сперва тебя накажем."
    menu:
        Alice_12 "Только не вздумай глазеть на меня при этом!"
        "{i}шлёпать нежно{/i}" if True:

            scene BG punish-sun 03
            $ renpy.show("Alice punish-sun 03-01"+mgg.dress)
            menu:
                Alice_05 "А это однозначно лучше, чем когда мама шлёпает! После того, чему моя попка подвергалась, твои шлепки даже приятны..."
                "Ну вот, а ты не хотела!" if True:

                    scene BG punish-sun 02
                    $ renpy.show("Alice punish-sun 02-05"+mgg.dress)
                    Alice_06 "Ну всё, хватит. А то ты уже не шлёпаешь, а просто лапаешь мою попку. И так раздел меня бесцеремонно..."
                    Max_03 "Просто хотел ускорить процесс."

                    $ renpy.show("Alice punish-sun 02-04"+mgg.dress)
                    Alice_03 "Ты меня своим озабоченным взглядом не смущай. Вали уже, оденусь я без твоей помощи..."
                "Могу сильнее, а то это уже не наказание!" if True:

                    $ _m1_alicetalk__r1 = renpy.random.randint(1, 2)

                    scene BG punish-sun 04
                    $ renpy.show("Alice punish-sun 04-0"+str(_m1_alicetalk__r1)+mgg.dress)
                    Alice_06 "Ой, Макс! Ну ты чего? Так уже больно. Ты же говорил, что будешь с нежностью шлёпать!"
                    Max_04 "А если я немного потру, чтобы не болело... Так легче?"

                    scene BG punish-sun 05
                    $ renpy.show("Alice punish-sun 05-0"+str(_m1_alicetalk__r1)+mgg.dress)
                    Alice_12 "Да... Но этого не пришлось бы делать, если бы ты шлёпал легонько!"
                    Max_07 "Это я чисто, чтобы напомнить, что это всё равно наказание."
                    Alice_13 "А мне кажется, что это больше похоже на извращение! Давай прекращай..."
                    Max_05 "Но приятное ведь?"

                    scene BG punish-sun 04
                    $ renpy.show("Alice punish-sun 04-03"+mgg.dress)
                    Alice_05 "Ага, сложно не заметить, сколько радости от этого в твоих шортах."
                    Max_03 "На такую красотку, как ты, у любого встанет!"
                    Alice_03 "Ах... Вот это комплимент! Не ожидала я такого от тебя, Макс. Так, всё, повеселились и хватит. Убери эту свою штуку и не появляйся в таком виде рядом со мной!"
                    $ alice.flags.privpunish += 1
            menu:
                Max_02 "Хорошо, до следующего раза. А попка у тебя славная!"
                "{i}уйти{/i}" if True:
                    jump alice_private_punish_0.end
        "{i}шлёпать сильно{/i}" if True:


            scene BG punish-sun 03
            $ renpy.show("Alice punish-sun 03-01"+mgg.dress)
            Alice_18 "Ай, ай, ай! Больно же! Ну ты чего, Макс? Меня и мама могла также отшлёпать. Всё, хватит!"
            Max_07 "Это же наказание всё-таки, Алиса. Должно быть немножко больно."

            scene BG punish-sun 04
            $ renpy.show("Alice punish-sun 04-03"+mgg.dress)
            Alice_15 "Это не немножко... У тебя ещё и стоит на всё это! Я в шоке! Прикрылся бы хоть..."
            Max_03 "Ну, ты же девушка... И очень привлекательная!"
            Alice_17 "И что? Я ещё и твоя сестра! Забыл? Всё, мы закончили. И что у тебя там, вообще, в башке творится..."
            Max_02 "Хорошо, до следующего раза. А попка у тебя славная!"
            menu:
                Alice_13 "Ох, и зачем я на всё это согласилась..."
                "{i}уйти{/i}" if True:
                    jump alice_private_punish_0.end

    label alice_private_punish_0.end:
        $ spent_time += 30
        $ alice.dcv.private.stage = 5
        $ alice.dcv.private.set_lost(0)
        $ alice.dcv.prudence.set_lost(renpy.random.randint(1, 3))
        $ alice.spanked = True
        jump Waiting


label alice_private_punish_r:

    Alice_03 "Эх, Макс... Я так хорошо лежала и загорала. Ну да ладно, давай побыстрее с этим покончим..."
    jump alice_private_punish_r.pun

    label alice_private_punish_r.smoke:
        Alice_05 "Да, Макс, сейчас... Только дай докурю спокойно и я в твоём распоряжении."
        menu:
            Max_03 "Хорошо. Я подожду..."
            "{i}подождать Алису{/i}" if True:
                jump alice_private_punish_r.smoke_pun

    label alice_private_punish_r.smoke_pun:

        scene BG punish-sun 01
        show Alice punish-sun 01-01
        $ renpy.show("Max punish-sun 01-01"+mgg.dress)
        Alice_03 "Всё, я готова. Давай побыстрее с этим покончим..."
        jump alice_private_punish_r.pun

    label alice_private_punish_r.pun:
        pass


    scene BG punish-sun 02
    $ renpy.show("Alice punish-sun 02-01"+mgg.dress)
    Alice_05 "Мне же больше делать нечего, только и жду с самого утра, когда ты придёшь и накажешь меня!"
    Max_02 "Сама разденешься или помочь?"

    $ renpy.show("Alice punish-sun 02-02"+mgg.dress)
    menu:
        Alice_04 "Вот тебе надо, чтобы я была голая, так сам и раздевай! Не облегчать же тебе работу..."
        "{i}стянуть верх купальника{/i}" if True:
            pass

    $ renpy.show("Alice punish-sun 02-03"+mgg.dress)
    menu:
        Alice_15 "Ну не так же резко, Макс! Смотри, если порвёшь мой купальник, я тебе тоже мигом что-нибудь порву..."
        "{i}стянуть низ купальника{/i}" if True:
            pass

    $ renpy.show("Alice punish-sun 02-04"+mgg.dress)
    menu:
        Alice_06 "И чего глазеем? Шлёпай давай! Руки только не распускай слишком сильно."
        "{i}шлёпать нежно{/i}" if True:

            scene BG punish-sun 03
            $ renpy.show("Alice punish-sun 03-01"+mgg.dress)
            menu:
                Alice_05 "Ты там уже начал? А то мне показалось, что это больше тянет на поглаживания, а не на шлепки..."
                "И как, тебе нравится?" if True:

                    scene BG punish-sun 02
                    $ renpy.show("Alice punish-sun 02-05"+mgg.dress)
                    Alice_02 "Мне нравится, что небольно. Ну всё, потискал мою попку и хватит. А то, если тебя не остановить, ты так и будешь залипать, куда не надо..."
                    Max_03 "Просто зрелище такое... завораживающее."

                    $ renpy.show("Alice punish-sun 02-04"+mgg.dress)
                    Alice_03 "Ты меня своим озабоченным взглядом не смущай. Вали уже, оденусь я без твоей помощи..."
                "Могу сильнее, раз ты заскучала!" if True:

                    $ _m1_alicetalk__r1 = renpy.random.randint(1, 2)

                    scene BG punish-sun 04
                    $ renpy.show("Alice punish-sun 04-0"+str(_m1_alicetalk__r1)+mgg.dress)
                    Alice_06 "Ой, Макс! Ну ты чего? Так уже больно. Ты же говорил, что будешь с нежностью шлёпать!"
                    Max_04 "А я потру, чтобы не болело... Так легче?"

                    scene BG punish-sun 05
                    $ renpy.show("Alice punish-sun 05-0"+str(_m1_alicetalk__r1)+mgg.dress)
                    Alice_13 "Да, я не жалуюсь... Но можно было ведь и дальше шлёпать легонько."
                    Max_07 "Это я чисто, чтобы напомнить, что это всё равно наказание."
                    Alice_02 "Ну всё, потискал мою попку и хватит. А то, если тебя не остановить, ты так и будешь залипать, куда не надо..."
                    Max_03 "Просто зрелище такое... завораживающее."

                    scene BG punish-sun 04
                    $ renpy.show("Alice punish-sun 04-03"+mgg.dress)
                    Alice_03 "Ага, сложно не заметить, сколько радости от этого в твоих шортах. Приму это за комплимент, но хватит уже меня смущать своим озабоченным видом!"
                    $ renpy.end_replay()
                    $ poss['ass'].open(1)
                    $ alice.flags.privpunish += 1
            menu:
                Max_02 "Хорошо, до следующего раза."
                "{i}уйти{/i}" if True:
                    jump alice_private_punish_r.end
        "{i}шлёпать сильно{/i}" if True:


            scene BG punish-sun 03
            $ renpy.show("Alice punish-sun 03-01"+mgg.dress)
            Alice_18 "Ай, ай, ай! Больно же! Ну ты чего, Макс? Меня и мама могла также отшлёпать. Всё, хватит!"
            Max_07 "Это же наказание всё-таки, Алиса. Должно быть немножко больно."

            scene BG punish-sun 04
            $ renpy.show("Alice punish-sun 04-03"+mgg.dress)
            Alice_15 "Это не немножко... У тебя ещё и стоит на всё это! Я в шоке! Прикрылся бы хоть..."
            Max_03 "Ну, ты же девушка... И очень привлекательная!"
            Alice_17 "И что? Я ещё и твоя сестра! Забыл? Всё, мы закончили. И что у тебя там, вообще, в башке творится..."
            Max_02 "Хорошо, до следующего раза. А попка у тебя славная!"
            menu:
                Alice_13 "Ох, и зачем я на всё это согласилась..."
                "{i}уйти{/i}" if True:
                    jump alice_private_punish_r.end

    label alice_private_punish_r.end:
        $ spent_time += 30
        $ alice.dcv.private.set_lost(0)
        $ alice.dcv.prudence.set_lost(renpy.random.randint(1, 3))
        $ alice.spanked = True
        jump Waiting
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
