
label StartPunishment:
    $ pun_list.clear()
    $ first = True
    $ defend = False
    if tm > '18:00':

        if lisa.sorry.owe and lisa.sorry.left == 0:
            $ lisa.sorry.owe = False
            $ punreason[0] = 1
            $ poss['SoC'].open(1)
        elif all([flags.film_punish, lisa.dcv.special.enabled, lisa.dcv.special.done]):
            $ punreason[0] = 1

        if alice.sorry.owe and alice.sorry.left == 0:
            $ alice.sorry.owe = False
            $ punreason[1] = 1
            $ poss['risk'].open(1)

    if punreason[2] or punreason[3] and tm < "18:00":
        $ pun_list.append("mgg")
    elif max(punreason) and tm > "18:00":
        $ pun_list.append("mgg")

    if tm > "18:00" and 0 < GetWeekday(day) < 6:

        $ chance = GetLisaPunChance()
        if RandomChance(chance):
            $ punlisa[0][1] = 1
            $ pun_list.append("lisa")
        elif True:



            if all([
                    any([newpunishment==2, newpunishment==1 and (day >= 50 or (dcv.new_pun.stage==2 and dcv.new_pun.done))]),
                    flags.add_training, lisa.dcv.punpause.done, RandomChance(500)
                ]):
                $ punlisa[0][1] = 2
                $ pun_list.append("lisa")

    if all([tm > "18:00", alice.dcv.special.enabled, alice.dcv.special.stage > 1, 0 < GetWeekday(day) < 6]):

        $ chance = GetAlicePunChance()
        if RandomChance(chance):
            $ pun_list.append("alice")

    $ renpy.random.shuffle(pun_list)

    if len(pun_list):
        $ renpy.block_rollback()
        if tm < "14:00":
            scene BG punish-morning 00
            $ renpy.show("Ann punish-morning 00"+ann.dress)
        elif True:
            scene BG punish-evening 00
            $ renpy.show("Ann punish-evening 00"+ann.dress)

        if newpunishment == 0 and flags.dinner>=12:
            jump first_new_punishment

        if newpunishment == 1 and (day >= 50 or (dcv.new_pun.stage==2 and dcv.new_pun.done)):
            jump first_naked_punishment

        Ann_16 "Прежде, чем мы начнём, кое-кто заслуживает наказания и сейчас все на это посмотрят..."
        jump punishment
    elif tm > "14:00":
        jump dinner_after_punishment
    elif True:
        jump breakfast_after_punishment


label punishment:
    $ _i = 0
    play music punishment
    while len(pun_list) > _i:
        if pun_list[_i] == "mgg":
            if len(pun_list) > 1:
                if first:
                    $ first = False
                    Ann_18 "Итак, Макс, ты первый..."
                elif True:
                    Ann_18 "Макс, теперь твоя очередь..."
            elif True:
                Ann_18 "Макс, иди сюда..."
            call punishment_max from _call_punishment_max
        elif pun_list[_i] == "lisa":
            if len(pun_list) > 1:
                if first:
                    $ first = False
                    Ann_18 "Так, Лиза, начнём с тебя..."
                elif True:
                    Ann_18 "Теперь Лиза..."
            elif True:
                Ann_18 "Лиза, подойди-ка ко мне."
            call punishment_lisa from _call_punishment_lisa
        elif pun_list[_i] == "alice":
            if len(pun_list) > 1:
                if first:
                    $ first = False
                    Ann_18 "Алиса, начнём с тебя..."
                elif True:
                    Ann_18 "Теперь ты, Алиса..."
            elif True:
                Ann_18 "Алиса, подойди-ка сюда."
            call punishment_alice from _call_punishment_alice
        $ _i += 1

    stop music fadeout 1.0
    if tm > "14:00":
        jump dinner_after_punishment
    elif True:
        jump breakfast_after_punishment


label first_new_punishment:
    Ann_12 "Да, напоминаю всем. С сегодняшнего дня все наказания будут в обнажённом виде. Да, я понимаю, что это непедагогично, но очень эффективно."
    Max_10 "Но мам..."
    Ann_16 "Я знаю, Макс, но уговаривать и пытаться вас убедить другим способом у меня нет ни сил ни времени. Чем более унизительно наказание, тем у вас будет меньше желания нарушить правила."
    Lisa_09 "Мам, и что, нам с Алисой придётся раздеваться догола прямо перед Максом? А если он разденется, нам смотреть на этот... его... ну..."
    Max_07 "Что, страшно?"
    Ann_00 "Да, Лиза. Видишь, ты уже боишься. Значит, приложишь все усилия, чтобы тебя не наказали. Уже правила работают, а стоит один раз вам быть униженными перед всей семьёй..."
    Max_09 "А если ты накосячишь? Кто тебя будет наказывать?"
    Ann_02 "Макс, ну что за ерунда. Что я могу нарушить? Я же ваша мама и всегда даю вам пример для подражания..."
    Max_08 "Э... Ты уверена?"
    Ann_04 "Да, Макс, я уверена. Но даже если я и совершу ошибку, то меня сможет наказать, допустим, Эрик... Но этого не случится. Я соблюдаю свои же правила!"
    Max_09 "Ага, уж он то накажет..."
    Ann_12 "Макс, ты слишком много говоришь... Ладно, дам вам последнюю поблажку - в ближайший месяц можете оставаться в трусах во время наказания. Но если и это никак вас не образумит, то всё, будете раздеваться догола. И больше никаких предупреждений. Теперь всё будет строго."
    $ dcv.new_pun.stage = 2
    $ dcv.new_pun.set_lost(30)
    $ newpunishment = 1
    jump punishment


label first_naked_punishment:
    Ann_12 "А так как месяц прошёл, а вы всё так же не взялись за ум, то с этого момента наказывать я вас буду полностью голых! Как и обещала..."
    Lisa_11 "Ой, нет! Не надо, мам!"
    Alice_16 "Это беспредел какой-то!"
    Ann_19 "Тихо! У вас был шанс этого избежать. Если вам не стыдно за свою безалаберность, то, надеюсь, станет стыдно получать по голому заду на глазах у всех!"
    $ newpunishment = 2
    jump punishment


label punishment_max:
    $ renpy.block_rollback()

    if tm < "14:00":
        scene BG punish-morning 01
        $ renpy.show("Ann punish-morning 01"+ann.dress)
        $ renpy.show("Max punish-morning 01"+mgg.dress)
    elif True:
        scene BG punish-evening 01
        $ renpy.show("Ann punish-evening 01"+ann.dress)
        $ renpy.show("Max punish-evening 01"+mgg.dress)

    if warning < 2 and newpunishment == 0:
        $ warning += 1
        Ann_19 "Макс! Я вынуждена отчитать тебя перед всеми, так как у нас в семье не должно быть никаких секретов."
        if warning > 0:
            Max_10 "Я снова не виноват!"
            Ann_17 "Не виноват, значит? Снова? Кажется, ты не осознаёшь, что это последнее предупреждение и в следующий раз я тебя выпорю на глазах у сестёр. Ты меня понял? А теперь рассказывай, что натворил, чтобы все были в курсе!" nointeract
        elif True:
            Max_10 "Я не виноват!"
            Ann_17 "Не виноват, значит? А я думаю, что ещё как виноват. В этот раз тебе повезло, это всего лишь первое предупреждение. Надеюсь, второго не потребуется... Кстати, можешь всем рассказать, что ты натворил..." nointeract
        $ _m1_punishment__list = []
        label punishment_max.pun_reson:
            $ _m1_punishment__list.clear()
            if punreason[0]:
                $ _m1_punishment__list.append((_("Ну, я случайно оказался рядом с душем, когда там была Лиза..."), 0))
            if punreason[1]:
                $ _m1_punishment__list.append((_("Ну, я оказался случайно рядом с душем, где мылась Алиса..."), 1))
            if punreason[2]:
                $ _m1_punishment__list.append((_("Ну, я подглядывал за тобой, мам..."), 2))
            if punreason[3]:
                $ _m1_punishment__list.append((_("Ну, я подглядывал за вами с Эриком..."), 3))
            if punreason[4]:
                $ _m1_punishment__list.append((_("Ну, я плохо себя вёл..."), 4))
            if punreason[5]:
                $ _m1_punishment__list.append((_("Ну, я оказался случайно рядом с душем, где мылась Алиса..."), 5))
            $ rez = renpy.display_menu(_m1_punishment__list)
            if rez == 0:
                Lisa_12 "Он видел меня голой, мам! Накажи его! Почему он отделывается только предупреждением? Пусть получит, что заслужил!"
                $ punreason[0] = 0
                $ lisa.daily.shower = 0
                Max_11 "Да ничего я не заслужил!"
            if rez == 1:
                Alice_16 "Случайно? Врёт он всё, мам! Он стоял и пялился на меня!"
                $ punreason[1] = 0
                $ alice.daily.shower = 0
                Max_11 "Да, я мимо проходил!"
            if rez == 2:
                Ann_14 "Очень хочу надеяться, что это было случайно. Тем не менее, ты пойман и как я уже сказала, получаешь предупреждение."
                $ ann.daily.shower = 0
                $ punreason[2] = 0
                Max_10 "Больше это не повторится!"
            if rez == 3:
                Ann_14 "Очень хочу надеяться, что ты это сделал не специально и просто проходил мимо. Тем не менее, ты пойман и как я уже сказала, получаешь предупреждение."
                $ punreason[3] = 0
                Max_10 "Да, я мимо проходил!"
            if rez == 4:
                Ann_14 "У тебя есть ещё время подумать над своим поведением. Надеюсь, следующего раза не будет!"
                $ punreason[4] = 0
                Max_10 "Да, мам..."
            if rez == 5:
                Alice_16 "Случайно? Мам! Он всё врёт! Он подглядывал и, может быть, даже паука подбросил! А ты знаешь, как я боюсь пауков..."
                $ alice.daily.shower = 0
                $ punreason[5] = 0
                Max_09 "Трусиха!"
            if max(punreason):
                $ _r1 = renpy.random.randint(1, 3)
                if _r1 == 1:
                    Ann_18 "Ты не закончил, Макс. Продолжай..." nointeract
                elif _r1 == 2:
                    Ann_18 "Дальше, Макс, мы тебя внимательно слушаем..." nointeract
                elif True:
                    Ann_18 "А ты про кое-что ещё не забыл?" nointeract
                jump punishment_max.pun_reson
        Ann_16 "У тебя есть ещё время подумать над своим поведением. Надеюсь, следующего раза не будет!"
        Max_14 "Да, мам..."
        Ann_12 "В общем, на этот раз вопрос уладили. Все сделали выводы, а кое-кто и серьёзно задумается. Да, Макс? Можешь не отвечать."
    elif newpunishment == 0:
        $ _ch1 = GetChance(mgg.social, 2, 900)
        menu:
            Ann_16 "Макс! Сейчас ты будешь наказан, сам знаешь за что!"
            "Я же не виноват! {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if True:
                pass
        if RandomChance(_ch1.ch):
            $ Skill('social', 0.2)
            Ann_14 "[succes!t]Ты знаешь, Макс, всё говорит о том, что ты виноват и должен быть наказан. Но поверю тебе на слово, что это была какая-то ошибка. Надеюсь, я не пожалею о своём решении..."
            Max_08 "Спасибо, мам!"
            python:
                for d in range(len(punreason)):
                    punreason[d] = 0
            return
        elif True:
            $ Skill('social', 0.1)
            if mgg.dress == "a":
                $ _text = _("штаны")
            elif True:
                $ _text = _("шорты")
            menu:
                Ann_19 "[failed!t]Вот так просто? \"Я не виноват\" и всё забудем? Нет, Макс, со мной эти шуточки не прокатят. Давай, снимай [_text!t] и ложись на мои колени. Надеюсь, ты сегодня в трусах..."
                "{i}снять штаны{/i}" if True:
                    pass
        if tm < "14:00":
            $ renpy.show("Max punish-morning 02"+mgg.dress)
        elif True:
            $ renpy.show("Max punish-evening 02"+mgg.dress)

        Ann_18 "Ну и долго я буду ждать?! Давай ложись..."

        if tm < "14:00":
            scene BG punish-morning 02
            $ renpy.show("Ann punish-morning max-01"+ann.dress+mgg.dress)
        elif True:
            scene BG punish-evening 02
            $ renpy.show("Ann punish-evening max-01"+ann.dress+mgg.dress)


        if punreason.count(1) > 1:
            Ann_16 "У Макса несколько провинностей... Он их прекрасно знает и перечислять я их не стану. Сейчас он получит за все сразу!"
        elif True:
            $ _text = {
                0 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Лизой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                1 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                2 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                3 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной... с Эриком. Я уже предупреждала, что такое недопустимо!"),
                4 : _("Если вы не в курсе, Макс будет наказан за своё отвратительное поведение. Надеюсь, теперь ты будешь хорошенько думать о том, что делаешь и что говоришь!"),
                5 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой в душе и, возможно, даже подбросил туда паука. Ты знаешь, что такое я не потерплю!"),
                }[punreason.index(1)]
            Ann_16 "[_text!t]"

        if tm < "14:00":
            $ renpy.show("Ann punish-morning max-02"+ann.dress+mgg.dress)
        elif True:
            $ renpy.show("Ann punish-evening max-02"+ann.dress+mgg.dress)
        Max_14 "{i}Мама наказывает меня прямо перед сёстрами... Это так унизительно...{/i}\n\n{color=[orange]}{b}Внимание:{/b} Ваше влияние на присутствующих понизилось!{/color}"

        call max_consequences from _call_max_consequences

        if tm < "14:00":
            scene BG punish-morning 01
            $ renpy.show("Ann punish-morning 01"+ann.dress)
            $ renpy.show("Max punish-morning 03"+mgg.dress)
        elif True:
            scene BG punish-evening 01
            $ renpy.show("Ann punish-evening 01"+ann.dress)
            $ renpy.show("Max punish-evening 03"+mgg.dress)

        Ann_12 "Ну вот. Теперь все всё поняли? Ведите себя хорошо и вас не ждёт эта участь..."
    elif newpunishment in [1, 2]:

        if newpunishment == 1:
            if mgg.dress=='b':
                menu:
                    Ann_12 "Ну, Макс, раздевайся до трусов. Остальные просто посмотрят, что бывает, когда кто-то косячит..."
                    "{i}раздеться{/i}" if True:
                        pass
            elif True:
                menu:
                    Ann_12 "Ну, Макс, снимай шорты. Остальные просто посмотрят, что бывает, когда кто-то косячит..."
                    "{i}снять шорты{/i}" if True:
                        pass
        elif True:
            menu:
                Ann_12 "Ну, Макс, раздевайся. Остальные просто посмотрят, что бывает, когда кто-то косячит..."
                "{i}раздеться{/i}" if True:
                    pass
        if tm < "14:00":
            $ renpy.show("Max punish-morning 02"+('c' if newpunishment == 1 else 'ca'))
        elif True:
            $ renpy.show("Max punish-evening 02"+('c' if newpunishment == 1 else 'ca'))
        Ann_14 "Хорошо. А теперь, ложись на мои колени и приступим, а то все голодные сидят..."
        if tm < "14:00":
            scene BG punish-morning 02
            $ renpy.show("Ann punish-morning max-01"+ann.dress+('c' if newpunishment == 1 else 'ca'))
        elif True:
            scene BG punish-evening 02
            $ renpy.show("Ann punish-evening max-01"+ann.dress+('c' if newpunishment == 1 else 'ca'))

        if punreason.count(1) > 1:
            Ann_16 "У Макса несколько провинностей... Он их прекрасно знает и перечислять я их не стану. Сейчас он получит за все сразу!"
        elif True:
            $ _text = {
                0 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Лизой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                1 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                2 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                3 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной... с Эриком. Я уже предупреждала, что такое недопустимо!"),
                4 : _("Если вы не в курсе, Макс будет наказан за своё отвратительное поведение. Надеюсь, теперь ты будешь хорошенько думать о том, что делаешь и что говоришь!"),
                5 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой в душе и, возможно, даже подбросил туда паука. Ты знаешь, что такое я не потерплю!"),
                }[punreason.index(1)]
            Ann_16 "[_text!t]"

        if tm < "14:00":
            $ renpy.show("Ann punish-morning max-02"+ann.dress+('c' if newpunishment == 1 else 'ca'))
        elif True:
            $ renpy.show("Ann punish-evening max-02"+ann.dress+('c' if newpunishment == 1 else 'ca'))
        Max_14 "{i}Блин... Все с таким интересом смотрят, как меня наказывают... Это так унизительно...{/i}\n\n{color=[orange]}{b}Внимание:{/b} Ваше влияние на присутствующих понизилось!{/color}"

        call max_consequences from _call_max_consequences_1

        if tm < "14:00":
            scene BG punish-morning 01
            $ renpy.show("Ann punish-morning 01"+ann.dress)
            $ renpy.show("Max punish-morning 03"+('c' if newpunishment == 1 else 'ca'))
        elif True:
            scene BG punish-evening 01
            $ renpy.show("Ann punish-evening 01"+ann.dress)
            $ renpy.show("Max punish-evening 03"+('c' if newpunishment == 1 else 'ca'))

        $ SetCamsGrow(house[5], 150)

        Ann_12 "Ну всё, Макс, одевайся. Надеюсь, ты сделал выводы и постараешься больше не попадать в такую унизительную ситуацию..."

    if newpunishment==2:
        $ mgg.flags.nakedpunish = True

    return


label max_consequences:

    python:
        if flags.voy_stage==0 and punreason[3]:
            flags.voy_stage=1 

        for cr in current_room.cur_char:
            if chars[cr].infmax is not None:
                chars[cr].infmax = clip(chars[cr].infmax - 5.0, 0.0, 100.0)


        for d in range(len(punreason)):
            punreason[d] = 0

        if flags.film_punish:
            
            lisa.dcv.special.enabled = False

        mgg.flags.pun +=1

    return


label punishment_lisa:
    $ renpy.block_rollback()

    scene BG punish-evening 01
    $ renpy.show("Lisa punish-evening 01"+lisa.dress)
    $ renpy.show("Ann punish-evening 01"+ann.dress)

    $ _m1_punishment__mood = 0

    $ lisa.dcv.punpause.set_lost(renpy.random.randint(5, 12))
    $ lisa.weekly.punished += 1
    if newpunishment==0:

        if lisa.dress == "a":
            $ _text = _("Ближе подходи, Лиза. И да, снимай штаны, ты заслужила!")
        elif True:
            $ _text = _("Ближе подходи, Лиза. И да, снимай свой халат, ты заслужила!")
        if defend:
            Ann_16 "[_text!t]"
        elif True:
            $ _ch1 = GetChance(mgg.social, 2, 900)
            menu:
                Ann_16 "[_text!t]"
                "{i}Заступиться за Лизу {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}{/i}" if True:
                    $ defend = True
                    Max_08 "Мам, не нужно наказывать Лизу. Она правда старалась, я сам видел. Ну и я помогу ей подтянуть оценки."
                    if "mgg" in pun_list:
                        Ann_12 "Нет, Макс, и даже не пытайся меня уговорить. Ты и сам накосячил... А ты, Лиза, не стой столбом, шевелись давай..."
                    elif RandomChance(_ch1.ch):
                        $ Skill('social', 0.2)
                        Ann_00 "[succes!t]Хорошо, Макс, в этот раз я не стану её наказывать. Надеюсь, я не пожалею о своём решении... А ты, Лиза, благодари брата, да учись давай, а то в следующий раз не помилую..."
                        Lisa_02 "Спасибо тебе, Макс!"
                        $ lisa.flags.defend += 1
                        $ lisa.weekly.protected += 1
                        $ punlisa[0][2] = 2
                        return
                    elif True:
                        $ Skill('social', 0.1)
                        Ann_12 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит то, что заслужила. А ты, Лиза, не стой столбом, шевелись давай..."
                        $ punlisa[0][2] = 1
                "{i}далее{/i}" if True:
                    pass
        Lisa_10 "Мам... Я не специально... Просто, задание было сложное..."
        if lisa.dress == "a":
            $ _text = _("Быстро снимай штаны!")
        elif True:
            $ _text = _("Быстро снимай халат!")
        Ann_14 "Сложное? У тебя была куча времени, чтобы подготовиться! Сидишь в своём телефоне вечно вместо того, чтобы учиться. [_text!t]"

    elif newpunishment==1:
        Ann_12 "Лиза. Мне нужно всем объяснять за что ты сейчас будешь наказана? Молчишь? Значит, знаешь... Всё, давай раздевайся до трусов и быстро, без разговоров!"
    elif newpunishment==2:
        if punlisa[0][1] == 2:
            Ann_12 "Лиза. Твой классный руководитель говорит, ты плохо себя ведёшь в школе! Молчишь? Значит, это правда... Всё, давай раздевайся догола и быстро, без разговоров!"
        elif True:
            Ann_12 "Лиза. Мне нужно всем объяснять за что ты сейчас будешь наказана? Молчишь? Значит, знаешь... Всё, давай раздевайся и быстро, без разговоров!"


    $ _lisa_dress = 'b' if newpunishment==1 else 'ca' if newpunishment==2 else lisa.dress
    $ renpy.show("Lisa punish-evening 02"+_lisa_dress)
    if newpunishment==0:
        $ _text = _("Теперь ложись, и побыстрее, все есть хотят...")
        $ SetCamsGrow(house[5], 130)
    elif True:
        $ _text = _("Что прикрываешься, Лиза? Стесняешься? Стыдно? Вот и хорошо... А теперь ложись на мои колени. Быстро!")
        $ SetCamsGrow(house[5], 150)

    if defend:
        Ann_18 "[_text!t]"
    elif True:
        menu:
            Ann_18 "[_text!t]"
            "{i}Заступиться за Лизу {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}{/i}" if True:
                $ defend = True
                if punlisa[0][1] == 2:
                    Max_08 "Мам, не нужно наказывать Лизу. Обещаю, что бы там ни было, я поработаю с ней над поведением, честно. Вот увидишь, проблем больше не будет!"
                elif True:
                    Max_08 "Мам, не нужно наказывать Лизу. Она правда старалась, я сам видел. Ну и я помогу ей подтянуть оценки."
                if "mgg" in pun_list:
                    Ann_12 "Нет, Макс, и даже не пытайся меня уговорить. Ты и сам накосячил... А ты, Лиза, не стой столбом, шевелись давай..."
                elif RandomChance(_ch1.ch):
                    $ Skill('social', 0.2)
                    Ann_00 "[succes!t]Хорошо, Макс, в этот раз я не стану её наказывать. Надеюсь, я не пожалею о своём решении... А ты, Лиза, можешь одеваться. Скажи спасибо Максу, что сегодня осталась безнаказанной. Но не думай, что я всегда буду такой доброй..."
                    Lisa_02 "Спасибо тебе, Макс!"
                    if newpunishment==2:
                        $ lisa.flags.defend += 1

                        if lisa.flags.defend >= 5:
                            if lisa.flags.topless and not lisa.dcv.other.enabled:
                                Max_07 "{i}( На одних \"спасибо\" далеко не уедешь... Нужно придумать и для себя что-то хорошее. Думаю, Лизу удастся уговорить смотреть ужастики без маечки. Это точно лучше, чем получать по голой заднице от мамы у всех на глазах! И поговорить с ней лучше, пока моя доброта свежа в её памяти... ){/i}"
                            $ lisa.dcv.other.set_lost(1)

                    $ lisa.weekly.protected += 1
                    $ punlisa[0][2] = 2
                    return
                elif True:
                    $ Skill('social', 0.1)
                    Ann_12 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит то, что заслужила. А ты, Лиза, не стой столбом, шевелись давай..."
                    $ punlisa[0][2] = 1
            "{i}далее{/i}" if True:
                pass


    scene BG punish-evening 02
    $ renpy.show("Ann punish-evening lisa-01"+ann.dress+_lisa_dress)

    $ _m1_punishment__mood -= 100
    $ lisa.flags.pun += 1

    if newpunishment==1:
        $ SetCamsGrow(house[5], 200)
        Max_04 "{i}( А вот это мне уже нравится... Сестрёнка сверкает своими классными сиськами... Можно смотреть и ничего за это не будет! Красота! ){/i}"
    elif newpunishment==2:
        $ SetCamsGrow(house[5], 250)
        Max_04 "{i}( Хоть Лиза и получает сейчас по своей миленькой попке, но зато можно полюбоваться и всем остальным... А видно много чего интересного! ){/i}"
    elif True:
        $ SetCamsGrow(house[5], 150)
        Lisa_09 "Ма-ам, я больше не буду... Ай... В смысле, буду лучше учиться. Извини..."
    $ renpy.show("Ann punish-evening lisa-02"+ann.dress+_lisa_dress)

    if newpunishment==0:
        $ _text = _("Говоришь тебе, говоришь, все как об стенку горох...")


        python:
            for i in range(min(5, len(punlisa))):
                if punlisa[i][0] == 1 or punlisa[i][0] > 2:
                    _text = _("Поразительно! Тебе даже Макс помогает, а ты двойки хватаешь!") 
                    break

        Ann_00 "Конечно, будешь. [_text!t] Совсем расслабилась."
    elif True:
        Lisa_10 "Ой... Мам! Больно!"
        if punlisa[0][1] == 2:
            Ann_16 "Давай терпи! Плохо вела себя в школе - получила по голой заднице у всех на глазах."
        elif True:
            Ann_16 "Давай терпи! Получила двойку - получила по голой заднице у всех на глазах."

    $ punlisa[0][3] = 1
    if punlisa[0][0] == 1:
        $ punlisa[0][4] = renpy.random.randint(50, 300)


    scene BG punish-evening 01
    $ renpy.show("Lisa punish-evening 03"+_lisa_dress)
    $ renpy.show("Ann punish-evening 01"+ann.dress)
    if newpunishment==0:
        Ann_12 "Лиза, надеюсь, ты извлекла урок из этого наказания и больше это не повторится. А теперь одевайся!"
    elif True:
        Ann_12 "Лиза, надеюсь, ты извлекла урок из этого наказания. Да, тебе было стыдно и неприятно, что все пялились на тебя, но надеюсь, ты всё поняла и больше это не повторится. А теперь одевайся!"

    if newpunishment==2:
        $ lisa.flags.nakedpunish = True

    $ AddRelMood('lisa', 0, _m1_punishment__mood)
    return


label punishment_alice:
    $ renpy.block_rollback()

    scene BG punish-evening 01
    $ renpy.show("Alice punish-evening 01"+alice.dress)
    $ renpy.show("Ann punish-evening 01"+ann.dress)

    $ _m1_punishment__mood = 0
    $ alice.dcv.special.set_lost(3)
    $ alice.dcv.punpause.set_lost(renpy.random.randint(5, 14))

    $ alice.nopants = (alice.dress=="a" and alice.req.result=='nopants') or alice.dress=='b'
    $ alice.weekly.punished += 1
    $ _ch1 = GetChance(mgg.social, 2, 900)
    if newpunishment==0:

        if alice.dress == "a":
            Ann_16 "Подходи, подходи, Алиса, чего ты там мнешься. Штаны снимай, есть разговор!"
        elif True:
            Ann_16 "Подходи, подходи, Алиса, чего ты там мнешься. Снимай шорты, есть разговор!"
        Alice_12 "Мам, за что? Что я такого сделала?"
        if alice.dress == "a":
            $ _text = _("Алиса, ты издеваешься? Я нашла сигареты у тебя в комнате! Ты опять куришь! Быстро сняла штаны и легла на мои колени, кому сказала!")
        elif True:
            $ _text = _("Алиса, ты издеваешься? Я нашла сигареты у тебя в комнате! Ты опять куришь! Быстро сняла шорты и легла на мои колени, кому сказала!")
        if defend:
            Ann_18 "[_text!t]"
        elif True:
            menu:
                Ann_18 "[_text!t]"
                "{i}Заступиться за Алису {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}{/i}" if True:
                    $ defend = True
                    Max_08 "Мам, не нужно наказывать Алису. Это не её сигареты, к ней сегодня подружка приходила, наверное, она забыла."
                    if "mgg" in pun_list:
                        Ann_12 "Нет, Макс, даже не пытайся её оправдывать. Ты и сам накосячил... Алиса, пошевеливайся..."
                    elif RandomChance(_ch1.ch):
                        $ Skill('social', 0.2)
                        Ann_14 "[succes!t]Хорошо, Макс, сегодня я не стану её наказывать. Надеюсь, я не пожалею об этом... Скажи брату спасибо, Алиса, что заступился, и не приглашай больше сюда таких подружек, хорошему они не научат..."
                        Alice_13 "Хорошо, мам. Спасибо, Макс, я этого не забуду."
                        $ punalice[0][2] = 2
                        $ alice.weekly.protected += 1
                        return
                    elif True:
                        $ Skill('social', 0.1)
                        Ann_16 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит в любом случае, не за себя, так за подружку. Не будет водится с такими, до добра они не доведут..."
                        $ punalice[0][2] = 1
                "{i}далее{/i}" if True:
                    pass

        Alice_13 "Мам... Это не мои сигареты... Я не курю, честно..."
        if alice.dress == "a":
            Ann_14 "Не твои? А чьи они тогда? Быстро снимай штаны!"
            if alice.nopants:
                Alice_06 "Мам, но я сегодня без трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
                Ann_20 "Ты ещё и без трусов?! Сейчас ещё и за это получишь! Макс пусть смотрит, а тебе будет стыдно. Может тогда за ум возьмёшься!"
                show Alice punish-evening 02aa
            elif True:
                show Alice punish-evening 02a
                if alice.req.result == 'not_nopants':
                    $ alice.req.noted = True
                    $ added_mem_var('alice_not_nopants')
                    Max_09 "{i}( Ничего себе! А что это на Алисе делают трусики?! Мы же с ней договорились... Ну всё, сестрёнка, считай ты попала... и куда больше, чем есть сейчас! ){/i}"
        elif True:
            Ann_14 "Не твои? А чьи они тогда? Быстро шорты снимай!"
            Alice_06 "Мам, но под ними нет трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
            Ann_00 "А вот нечего целый день в пижаме по дому шарахаться... Совсем разленилась! Макс пусть смотрит, а тебе будет стыдно. Может тогда за ум возьмёшься!"
            show Alice punish-evening 02ba
    elif newpunishment==1:
        Ann_12 "Так, Алиса, раздевайся до трусов. Надеюсь, не надо объяснять, за что я тебя сейчас буду наказывать и сама всё понимаешь..."
        if alice.dress == "a" and alice.nopants:
            Alice_06 "Мам, но я сегодня без трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
        elif alice.dress == "b":
            Alice_06 "Мам, но под шортами нет трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
        if (alice.dress == "a" and alice.nopants) or alice.dress == "b":
            Ann_16 "Тогда раздевайся догола, так наказание даже эффективней будет. А Макс пусть смотрит, как и все остальные..."
            show Alice punish-evening 02ca
            $ SetCamsGrow(house[5], 200)
        elif alice.dress == "a":
            show Alice punish-evening 02c
        elif True:
            show Alice punish-evening 02d
    elif newpunishment==2:
        Ann_12 "Так, Алиса, раздевайся. Надеюсь, не надо объяснять, за что я тебя сейчас буду наказывать и сама всё понимаешь..."
        show Alice punish-evening 02ca

    if newpunishment==0:
        $ SetCamsGrow(house[5], 130)
        $ _text = _("Теперь ложись побыстрее, ужин стынет...")
    elif True:
        $ SetCamsGrow(house[5], 150 if newpunishment==1 else 250)
        $ _text = _("Ну как, Алиса, стыдно тебе? Молчишь? Вот подумай о своём поступке, пока я буду наказывать тебя на глазах у всех... Ложись на мои колени!")

    if defend or 0<alice.dcv.private.stage<4:
        if alice.dcv.private.stage==1:

            Max_07 "{i}Посмотрим, станет ли Алиса посговорчивей, если я перестану вмешиваться... Главное, успеть поговорить с ней, пока ей будет ещё больно сидеть!{/i}"
            $ alice.dcv.private.stage = 2
            $ alice.dcv.private.set_lost((2 if GetWeekday(day)!=5 else 3))
        elif alice.dcv.private.stage==2:
            $ alice.dcv.private.set_lost(2)
        Ann_18 "[_text!t]"
    elif True:
        menu:
            Ann_18 "[_text!t]"
            "{i}Заступиться за Алису {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}{/i}" if True:
                $ defend = True
                Max_08 "Мам, не нужно наказывать Алису. Это не её сигареты, к ней сегодня подружка приходила, наверное, она забыла."
                if "mgg" in pun_list:
                    Ann_12 "Нет, Макс, даже не пытайся её оправдывать. Ты и сам накосячил... Алиса, пошевеливайся..."
                elif RandomChance(_ch1.ch):
                    $ Skill('social', 0.2)
                    Ann_14 "[succes!t]Хорошо, Макс, сегодня я не стану её наказывать. Надеюсь, я не пожалею об этом... Можешь одеваться, Алиса, да скажи брату спасибо, что заступился. И не приглашай сюда больше таких подружек, хорошему они не научат..."
                    Alice_13 "Хорошо, мам. Спасибо, Макс, я этого не забуду."
                    if newpunishment==2:
                        $ alice.flags.defend += 1

                        if alice.flags.defend >= 5:
                            if not alice.dcv.private.enabled:
                                Max_09 "{i}Ага, как же, не забудет она... Хм... Может, стоит попросить у неё что-нибудь, чтобы она не думала, что моя доброта безвозмездна?! И сделать это нужно сегодня, пока она ещё под впечатлением...{/i}"
                            $ alice.dcv.private.set_lost((2 if GetWeekday(day)!=5 else 4))

                    $ punalice[0][2] = 2
                    $ alice.weekly.protected += 1
                    return
                elif True:
                    $ Skill('social', 0.1)
                    Ann_16 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит в любом случае, не за себя, так за подружку. Не будет водится с такими, до добра они не доведут..."
                    $ punalice[0][2] = 1
            "{i}далее{/i}" if True:
                pass

    $ poss['smoke'].open(3)


    scene BG punish-evening 02
    if newpunishment==0:
        $ SetCamsGrow(house[5], 150)
        $ _m1_punishment__suf = alice.dress + ('a' if alice.req.result == "nopants" or alice.dress=='b' else '')
        $ renpy.show("Ann punish-evening alice-01"+ann.dress+_m1_punishment__suf)
    elif True:
        if alice.req.result == "nopants" or alice.dress=='b' or newpunishment==2:
            $ SetCamsGrow(house[5], 250)
            $ _m1_punishment__suf = 'ba'
        elif True:
            $ SetCamsGrow(house[5], 220)
            $ _m1_punishment__suf = alice.dress
        $ renpy.show('Ann punish-evening alice-03'+ann.dress+_m1_punishment__suf)

    $ _m1_punishment__mood -= 50
    $ alice.flags.pun += 1

    if newpunishment==0:
        Alice_15 "Ай, больно же! Мам, я больше не буду!!!"
        $ renpy.show("Ann punish-evening alice-02"+ann.dress+_m1_punishment__suf)
    elif True:
        if newpunishment==1:
            Max_04 "{i}( Вот в такие моменты я не жалею, что нас наказывают практически голыми на глазах друг у друга! Даже порно не надо, когда такое шоу в паре метров от меня! ){/i}"
        elif True:
            Max_04 "{i}( Люблю, когда Алису наказывают... Стервозинка она та ещё, но без последствий полюбоваться её голыми прелестями в других ситуациях опасно для жизни! ){/i}"
        $ renpy.show('Ann punish-evening alice-04'+ann.dress+_m1_punishment__suf)

    if newpunishment==0:
        Ann_17 "Я знаю, что не будешь. Заслужила наказание, терпи!"
    elif True:
        Alice_15 "Ай! Ма-ам! Больно же! Мам, я больше не буду!!!"
        Ann_16 "Давай не мамкай тут! Я знаю, что не будешь. Заслужила наказание, терпи!"

    $ punalice[0][3] = 1
    if punalice[0][0] > 0 and punalice[0][1] == 1:
        $ punalice[0][4] = renpy.random.randint(50, 300)


    scene BG punish-evening 01
    $ renpy.show("Ann punish-evening 01"+ann.dress)
    if newpunishment==0:
        $ _m1_punishment__suf = alice.dress+('a' if alice.req.result == 'nopants' or alice.dress=='b' else '')
    elif True:
        $ _m1_punishment__suf = 'ca' if alice.req.result == 'nopants' or alice.dress=='b' or newpunishment == 2 else 'c' if alice.dress<'d' else 'd'

    $ renpy.show('Alice punish-evening 03'+_m1_punishment__suf)
    if newpunishment==0:
        if alice.dress == "a":
            Ann_12 "Так, всё, надевай свои джинсы. Надеюсь, ты осознала свои поступки и следующего раза не будет..."
        elif True:
            Ann_12 "Так, всё, надевай свои шорты. Надеюсь, ты осознала свои поступки и следующего раза не будет..."
    elif True:
        Ann_12 "Ну что, получила урок? Стыдно? Правильно. Должно быть стыдно. Надеюсь, это больше не повторится. А теперь, одевайся..."

    if newpunishment==2:
        $ alice.flags.nakedpunish = True

    $ AddRelMood('alice', 0, _m1_punishment__mood)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
