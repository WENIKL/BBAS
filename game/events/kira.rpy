

label kira_swim:
    scene expression 'Kira swim '+pose3_4+kira.dress
    $ persone_button1 = 'Kira swim '+pose3_4+kira.dress+'b'
    return


label kira_sun:
    scene expression 'BG char Alice sun'
    $ renpy.show('Kira sun '+pose3_4+kira.dress)
    $ persone_button1 = 'Kira sun '+pose3_4+kira.dress+'b'
    return


label kira_bath:
    scene location house bathroom door-evening
    if kira.daily.bath != 0:
        return

    $ renpy.dynamic('ch_catch', 'catch', 'r1')
    $ kira.daily.bath = 1
    menu:
        Max_01 "Только один человек может в это время не спать и плескаться в ванне. И человек этот - Кира!"
        "{i}постучаться{/i}" if not kira.flags.m_foot:
            Kira "{b}Кира:{/b} Кто там? Я принимаю ванну и абсолютно голая... Так что не входите, дайте отдохнуть!"
            if flags.ladder < 1:
                Max_09 "Нужно найти способ как-то подглядеть за девчонками в ванной. Может, попробовать вечером со двора?!"
            elif flags.ladder < 2:
                Max_09 "Нужно найти способ как-то подглядеть за девчонками в ванной. Может, стоит осмотреться изнутри?!"
            elif flags.ladder < 3:
                Max_09 "Нужно уже наконец купить стремянку, чтобы подглядывать за тем, что происходит в ванной..."
            elif True:
                Max_09 "В следующий раз лучше заглянуть со стремянки..."
            jump kira_bath.end

        "{i}войти{/i}" if kira.flags.m_foot > 0:

            if wcv.catch_Kira.stage==1:


                if kira.dcv.battle.stage == 2:
                    Max_09 "Пусть лучше тётя Кира отдохнёт, а вернее отмоется от Эрика... А то как-то не очень хочется что-то делать в ванне сразу после него!"
                elif True:
                    Max_09 "Пусть лучше тётя Кира отдохнёт и отмоется от Эрика... Можно было бы всё же зайти, но вдруг Эрик этого и ждёт. Лучше не рисковать!"

                jump kira_bath.end

            jump kira_bath.mass_bath

        "{i}установить стремянку{/i}" if items['ladder'].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
            Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."
            $ flags.ladder = 3
            $ items['ladder'].give()


            jump kira_bath.ladder

        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2 and not kira.flags.m_foot:
            jump kira_bath.ladder
        "{i}уйти{/i}" if True:

            jump kira_bath.end

    label kira_bath.ladder:
        $ renpy.scene()
        show Max bathroom-window-evening 02c
        Max_04 "Посмотрим, что у нас тут..."

        scene BG bath-00
        show Kira bath-window 01
        show FG bath-00
        $ Skill('hide', 0.03)

        Max_02 "Ох, чёрт! Какая аппетитная попка у неё... Это я удачно решил дождаться её возвращения! Давай, тётя Кира, этой попке пора стать мокренькой..."
        if _in_replay or all([kira.flags.porno, lisa.flags.m_foot>0]):

            show Kira bath-window 02
            Max_05 "Ого! Да она сперва решила поиграть со своей киской... Вот это классно! Только почему бы не делать это лёжа в ванной? Такое ощущение, что она это специально..."
            show Kira bath-window 03
            Max_10 "Блин! Она меня видела! Вот это уже не круто... Хотя, это же тётя Кира... она же не станет меня сдавать маме? Или нет?!"
            show Kira bath-window 04
            menu:
                Max_08 "Что? Она зовёт меня к себе?! Да ладно! Как-то мне это не очень нравится..."
                "{i}идти к Кире{/i}" if True:
                    $ kira.flags.m_foot = 1
                    jump kira_bath.kira_mass_bath_first
        elif True:

            $ r1 = renpy.random.choice(['05', '06'])
            $ renpy.show('Kira bath-window '+r1)
            Max_04 "Да-а-а, у неё просто обалденная грудь! Сосочки прямо там, где надо... Ох, я бы с ней ванну попринимал! Надеюсь, мне это приснится. Пора идти спать..."
            jump kira_bath.end_sleep

    label kira_bath.kira_mass_bath_first:
        scene BG bath-talk-00
        $ r1 = renpy.random.choice(['01', '02'])
        $ renpy.show('Kira bath-talk '+r1)
        Kira_04 "А мне было интересно, осмелишься ли ты зайти... Значит, Макс, любишь подглядывать?"
        Max_07 "Ну, немного..."
        Kira_05 "Немного? Это сколько? Раз в неделю? Или раз в день?"
        Max_09 "Ты сдашь меня маме?"
        Kira_02 "Ох, конечно нет, Макс! Я и сама большая любительница за чем-нибудь... интересным понаблюдать."
        Max_01 "Фух... хорошо."
        Kira_07 "Хотя, всё будет зависеть от тебя!"
        Max_08 "В каком это смысле?"

        scene BG bath-talk-02
        $ renpy.show('Kira bath-talk 2-'+r1)
        show Max bath-talk 2-01
        Kira_01 "Я слышала, ты неплохо так массируешь ножки то одной сестре, то другой..."
        Max_01 "Ну да, бывает такое."
        Kira_02 "Я сегодня очень устала... И если бы нашёлся тот, кто помог бы снять усталость с моих ног, то может быть, в качестве благодарности, я бы и не стала рассказывать своей сестре, какой у неё испорченный сын."
        Max_07 "Э-э-э... Что, прямо здесь?"
        Kira_05 "Ой, а я разве тебя смущаю, Макс?! Ты разве не за этим подглядывал? Чтобы как можно больше всего увидеть безнаказанно..."
        Max_08 "Да, но... прямо здесь... в ванне?!"
        Kira_08 "Что ты, нет! Ты сядешь здесь, рядом с ванной, а я свешу тебе свои ноги... Ха! Конечно, в ванне! Я же вижу с каким трудом ты прикрываешь свой... энтузиазм... Расслабься уже и залезай в ванну. Или, может, хочешь уйти?"
        Max_02 "Конечно, нет! Это я мигом..."

        scene BG bath-talk-03
        show Kira bath-talk 3-01
        Kira_07 "Ну и как, Макс, доволен видом? Удобно устроился?"
        Max_05 "Ага, у меня просто невероятная тётя!"
        menu:
            Kira_02 "Да, я такая... Понимаю, ты был бы не прочь так всю ночь просидеть, но не пора ли сделать своей любимой тёте приятно?"
            "{i}начать массаж{/i}" if True:
                pass
        $ r1 = renpy.random.choice(['01', '02'])
        $ renpy.show('Kira bath-mass 1-'+r1)
        Max_04 "{i}( Я и мечтать о таком не мог! Что буду сидеть с совершенно голой тётей в одной ванне и массировать её ножки... А как изящно она прикрывает ими свою киску! ){/i}"
        Kira_04 "Да, Макс, это очень приятно! Ты молодец... Кто тебя научил этому?"
        Max_01 "Курсы на компьютере... Ну и на Алисе с Лизой тренировался."
        Kira_05 "Думаю, тебе нужно это развивать... Уверена, твои нежные, но сильные пальчики могут принести невероятное наслаждение!"

        scene BG char Kira bath-mass-02
        $ renpy.show('Kira bath-mass 2-'+r1)
        Max_07 "И как мне это развивать?"
        Kira_01 "У меня здесь есть одна бывшая одноклассница и, как я помню, она с мужем как раз занимается массажем и йогой. Я попробую с ней встретиться и договориться, чтобы они тебя поднатаскали в этом... Если, конечно, хочешь?"
        Max_03 "Конечно, да! Я сейчас понял, насколько это классно, делать массаж голой женщине!"
        Kira_09 "Ты только не останавливайся, от твоих прикосновений мне становится так жарко..."

        $ renpy.show('Kira bath-mass 3-'+r1)
        Max_07 "Ухх, тётя Кира, ты..."
        Kira_07 "Ой! А во что это там такое твёрдое и большое упёрлась моя нога?"
        Max_02 "А то ты не знаешь?!"
        menu:
            Kira_09 "Ну конечно знаю... Видимо, мне стало уже слишком хорошо, чтобы просто лежать без дела. Так что давай-ка закругляться, Макс. Уже так поздно..."
            "{i}закончить массаж{/i}" if True:
                pass

        scene BG bath-talk-00
        $ r1 = renpy.random.choice(['01', '02'])
        $ renpy.show('Kira bath-talk '+r1)
        Max_04 "Ладно, тётя Кира. Я тогда пошёл. Спокойной ночи. Было очень классно побыть с тобой!"
        Kira_04 "Приятных снов, Макс. И да, пожалуй, в следующий раз, ты можешь просто заходить без стука. Если ещё не будешь спать..."
        Max_05 "С радостью."
        if not _in_replay:
            $ added_mem_var('kira_mass_bath_first')
            $ added_mem_var('kira.bath.mass')
            $ mgg.cleanness = 100
            $ SetCamsGrow(house[3], 150)
        jump kira_bath.end_sleep

    label kira_bath.mass_bath:
        if not _in_replay and 'kira_bath.mass_bath' not in persistent.memories:
            $ persistent.memories['kira_bath.mass_bath'] = 0
            $ SetCamsGrow(house[3], 180)
        if not _in_replay:
            $ added_mem_var('kira.bath.mass')


        if _in_replay or not wcv.catch_Kira.enabled:
            $ ch_catch = 0
        elif flags.eric_jerk:
            $ ch_catch = 0
        elif all([wcv.catch_Kira.enabled, not wcv.catch_Kira.done, wcv.catch_Kira.stage<1]):
            $ ch_catch = 1000 - 250 * wcv.catch_Kira.lost
        elif True:
            $ ch_catch = 1000

        scene BG bath-talk-00
        $ r1 = renpy.random.choice(['01', '02', '03'])
        $ renpy.show('Kira bath-talk '+r1)
        Kira_01 "А, Макс, это ты! Всё полуночничаешь... А я вот хотела немного поваляться в ванне, перед тем, как идти спать. Присоединишься?"
        menu:
            Max_02 "Конечно, тётя Кира! Тебя я и дожидался."
            "{i}снять шорты{/i}" if True:
                pass
        scene BG bath-talk-02
        $ renpy.show('Kira bath-talk 2-'+r1)
        show Max bath-talk 2-02
        menu:
            Kira_02 "О да, я вижу, как ты меня ждал! Залезай скорее..."
            "{i}присоединиться к тёте{/i}" if True:
                pass
        scene BG bath-talk-03
        show Kira bath-talk 3-01
        Kira_07 "Ну и как, Макс, доволен видом? Удобно устроился?"
        Max_05 "Ага, у меня самая красивая тётя на свете!"
        menu:
            Kira_02 "Да, я такая... Понимаю, ты был бы не прочь так всю ночь просидеть, но не пора ли сделать своей любимой тёте приятно?"
            "{i}начать массаж{/i}" if True:
                pass
        $ kira.flags.m_foot += 1
        $ r1 = renpy.random.choice(['01', '02'])
        $ renpy.show('Kira bath-mass 1-'+r1)
        Max_04 "{i}( А ведь мечты сбываются, если очень захотеть! Сидим с тётей голые в ванне и я массирую её гладкие и стройные ножки. А как изящно она прикрывает ими свою киску! ){/i}"
        Kira_04 "Как хорошо... Это то, что мне так сейчас нужно! Хочется, чтобы это продолжалось как можно дольше..."
        scene BG char Kira bath-mass-02
        $ renpy.show('Kira bath-mass 2-'+r1)
        Max_03 "{i}( Она так прекрасна... а мокренькая так вообще огонь! Её шикарная грудь так классно вздымается, когда она начинает глубоко дышать от моего массажа... ){/i}"
        if lisa.dcv.seduce.stage<2:
            Kira_07 "Ты только не останавливайся, от твоих прикосновений мне становится так жарко! Напряжения, как не бывало..."
            menu:
                Max_01 "Это потому что я уже скоро закончу."
                "{i}закончить массаж{/i}" if True:
                    pass
            scene BG bath-talk-03
            show Kira bath-talk 3-01
            Kira_08 "Ты молодец, Макс. Мне было очень приятно, а как легко моим ножкам стало! Спасибо тебе и давай-ка закругляться. Уже так поздно..."
            Max_04 "Ладно, тётя Кира. Я тогда пошёл. Спокойной ночи. Было очень классно побыть с тобой!"
            Kira_04 "Приятных снов, Макс."
            jump kira_bath.end_sleep
        elif True:
            $ _ch1 = GetChance(mgg.social, 2, 900)
            menu:
                Kira_07 "Ты только не останавливайся, от твоих прикосновений мне становится так жарко! Напряжения, как не бывало..."
                "А моё напряжение только растёт, тётя Кира! Может поможешь? \n{color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if kira.flags.m_breast<2:
                    if not RandomChance(_ch1.ch) and not _in_replay:
                        $ Skill('social', 0.2)
                        Kira_09 "Макс, уже так поздно... и меня настолько расслабила ванна и твой массаж, что я засыпаю. Так что давай закругляться."
                        scene BG bath-talk-03
                        show Kira bath-talk 3-01
                        Max_04 "Ладно, тётя Кира. Я тогда пошёл. Спокойной ночи. Было очень классно побыть с тобой!"
                        Kira_04 "Приятных снов, Макс."
                        jump kira_bath.end_sleep
                    elif True:
                        $ Skill('social', 0.1)
                "А моё напряжение только растёт, тётя Кира! Может поможешь?" if kira.flags.m_breast>1:
                    pass
            $ renpy.show('Kira bath-mass 3-'+r1)
            Kira_05 "О, ты прав, Макс! Думаю, очень непросто высидеть со мной в одной ванне и ограничиться лишь массажем..."
            Max_05 "Ухх... от твоих прикосновений мне становится уже немного лучше!"
            if kira.flags.promise:
                jump kira_bath.promise_cuni
            scene BG bath-talk-03
            show Kira bath-mass fj1-01
            Kira_02 "Раз уж ты снял усталость с моих ножек, то может они, в качестве благодарности, смогут помочь и тебе..."
            Max_03 "{i}( Ох... Определённо смогут! Не зря я так хорошо размял её пальчики, они начинают такое вытворять... Ого! Тётя так возбудилась, что раздвинула ножки и начала ласкать свою киску... ){/i}"
            Kira_07 "Ну как, Макс? Тебе нравится то, что твоя тётя умеет вытворять ногами?"
            Max_20 "Да-а-а... Это очень приятно! Только не прекращай, тётя Кира!"
            $ r1 = renpy.random.randint(1,2)
            if r1== 1:
                show Kira bath-mass fj1-02
            elif True:
                scene BG bath-cun-01
                show Kira bath-mass fj2-01
            $ _ch1 = GetChance(mgg.sex+10, 4, 900)
            menu:
                Kira_09 "Ох, Макс, как же меня заводит твой огромный член! Ты так жадно смотришь, как я ласкаю себя, свою грудь... Ах, моя киска вся горит, не отводи от неё глаз..."
                "{i}подтянуть её к себе и ласкать пальцами{/i}" if kira.stat.blowjob or (_in_replay and memes>1):
                    jump kira_bath.cuni_bj
                "{i}пытаться не кончить{/i} \n{color=[_ch1.col]}(Сексуальный опыт. Шанс: [_ch1.vis]){/color}" if not _in_replay or (_in_replay and memes<2):
                    pass
            if not RandomChance(_ch1.ch) and not _in_replay:
                scene BG char Kira bath-fj-03
                show Kira bath-mass fj3-01
                $ Skill('sex', 0.1)
                Kira_06 "[norestrain!t]Ухх, Макс! Ты кончил раньше, чем мне хотелось..."
            elif True:
                scene BG bath-cun-01
                show Kira bath-mass fj2-02
                $ Skill('sex', 0.2)
                menu:
                    Kira_10 "[restrain!t]Тебе нравится, как я ввожу пальчики в свою киску? Это так приятно и сладко, что я уже вот-вот кончу! Ох... давай, не сдерживайся..."
                    "{i}кончить{/i}" if True:
                        pass
                scene BG char Kira bath-fj-03
                show Kira bath-mass fj3-01
                Kira_08 "Фух, Макс, ну мы и выдали с тобой..."
            Max_02 "Да, тётя Кира, это было что-то нереальное!"
            Kira_01 "Давай уже быстренько разбегаться, а то вдруг наши с тобой стоны кто-то услышал."
            Max_01 "Ага. Спокойной ночи, тётя Кира. С тобой очень здорово!"
            Kira_04 "Приятных снов, Макс."
            $ kira.stat.footjob += 1
            if not _in_replay:
                $ SetCamsGrow(house[3], 200)
                $ persistent.memories['kira_bath.mass_bath'] = 1
            jump kira_bath.end_sleep

    label kira_bath.promise_cuni:

        Kira_02 "Раз уж ты снял усталость с моих ножек, то может порадуешь свою тётю, как обещал? Или ты уже забыл!?"
        menu:
            Max_03 "Конечно помню! И хочу порадовать тебя ещё..."
            "{i}подтянуть её к себе и ласкать пальцами{/i}" if True:
                scene BG bath-cun-01
                show Kira bath-mass cun-01
        menu:
            Kira_05 "Оу... Ты тот ещё шалунишка! У тебя такие нежные пальчики... Да... Поиграй с ней!"
            "{i}поработать языком{/i}" if True:
                show Kira bath-mass cun-02
                Kira_09 "Ухх... Как же ловко твой горячий язычок скользит там внизу... Это такие сладкие ощущения! Ещё быстрее... Ммм..." nointeract
            "{i}проникнуть в неё пальцами{/i}" if kira.stat.handjob:
                show Kira bath-mass cun-04
                Kira_09 "Ухх... Да, ещё... Входи своими пальчиками поглубже... Это такие сладкие ощущения! Ещё быстрее... Ммм..." nointeract
        $ rez = renpy.display_menu([(_("{i}работать языком быстрее{/i}"), 0)])
        scene BG bath-cun-02
        show Kira bath-mass cun-03


        if RandomChance(ch_catch):
            $ catch = 'cun'
            jump kira_bath.caught

        Kira_11 "Макс... О да... продолжай вот так, я уже не могу сдерживаться... Сожми мою попку покрепче! Уже так близко... Да! Я кончаю... Ахх..."
        Max_03 "Похоже, и здесь я всё помассировал как надо!"

        scene BG bath-talk-03
        show Kira bath-talk 3-01

        Kira_06 "Ещё как... Мне очень понравилось... Ты очень способный... племянник..."
        Max_05 "И ты очень классная, тётя Кира! С тобой здорово!"
        Kira_01 "Спасибо, Макс, приятно такое слышать... Давай уже быстренько разбегаться, а то вдруг наши с тобой стоны кто-то услышал."
        Max_01 "Ага. Спокойной ночи, тётя Кира."
        Kira_04 "Приятных снов, Макс."

        if not _in_replay:
            $ SetCamsGrow(house[3], 200)
        $ kira.flags.promise = False
        jump kira_bath.end_sleep

    label kira_bath.cuni_bj:
        if not _in_replay:
            $ SetCamsGrow(house[3], 200)
            if GetRelMax('kira')[0]<3:
                $ AttitudeChange('kira', 1)
        scene BG bath-cun-01
        show Kira bath-mass cun-01
        menu:
            Kira_05 "Оу... Макс, не выдержал и сам захотел поласкать мою киску? У тебя такие нежные пальчики... Да... Поиграй с ней!"
            "{i}поработать языком{/i}" if True:
                show Kira bath-mass cun-02
                if kira.dcv.photo.stage>1:

                    Kira_09 "Ухх... Как же ловко твой горячий язычок скользит там внизу... Это такие сладкие ощущения! Ммм... Но я бы не отказалась от кое-чего большого и у тебя это есть... Что скажешь?" nointeract
                elif True:
                    Kira_09 "Ухх... Как же ловко твой горячий язычок скользит там внизу... Это такие сладкие ощущения! Ещё быстрее... Ммм..." nointeract
            "{i}проникнуть в неё пальцами{/i}" if kira.stat.handjob:
                show Kira bath-mass cun-04
                if kira.dcv.photo.stage>1:
                    Kira_09 "Ухх... Да, ещё... Входи своими пальчиками поглубже... Это такие сладкие ощущения! Ммм... Не хочешь проникнуть в свою тётю чем-нибудь ещё?" nointeract
                elif True:
                    Kira_09 "Ухх... Да, ещё... Входи своими пальчиками поглубже... Это такие сладкие ощущения! Ещё быстрее... Ммм..." nointeract
        if kira.dcv.photo.stage > 1:

            $ rez = renpy.display_menu([(_("{i}работать языком быстрее{/i}"), 0), (_("Садись на меня, тётя Кира!"), 1), (_("Давай-ка сюда свою шикарную попку!"), 2)])
            if rez == 1:
                jump kira_bath.horsewoman
            elif rez == 2:
                jump kira_bath.dogstyle
        elif True:
            $ rez = renpy.display_menu([(_("{i}работать языком быстрее{/i}"), 0)])
        scene BG bath-cun-02
        show Kira bath-mass cun-03


        if RandomChance(ch_catch * .75):
            $ catch = 'cun'
            jump kira_bath.caught

        Kira_11 "Макс... О да... продолжай вот так, я уже не могу сдерживаться... Сожми мою попку покрепче! Уже так близко... Да! Я кончаю... Ахх..."
        Max_03 "Похоже, и здесь я всё помассировал как надо!"
        menu:
            Kira_06 "Да... Ты у меня способный племянник... и я хочу твой член! Хочу почувствовать его у себя во рту..."
            "{i}приблизиться членом к её лицу{/i}" if True:
                show Kira bath-mass hj-01


        if RandomChance(ch_catch):
            $ catch = 'hj'
            jump kira_bath.caught

        Kira_02 "О, Макс... Он такой твёрдый и горячий... Я чувствую, как сильно ты хочешь проникнуть им поглубже мне в рот!"
        Max_04 "Да... Я очень этого хочу!"
        if renpy.random.randint(1, 2)>1:
            scene BG char Kira bath-bj-02
            show Kira bath-mass bj-02
        elif True:
            scene BG char Kira bath-bj-01
            show Kira bath-mass bj-01
        $ _ch3 = GetChance(mgg.sex+10, 3, 900)
        menu:
            Kira_05 "Сначала, я хочу приласкать его своим язычком... Вот так... Я знаю, что тебе это нравится..."
            "Ох, тётя Кира... Ты слишком ловко меня дразнишь! Я могу не выдержать... \n{color=[_ch3.col]}(Сексуальный опыт. Шанс: [_ch3.vis]){/color}" if True:
                if not RandomChance(_ch3.ch) and not _in_replay:

                    jump kira_bath.not_restrain


        $ Skill('sex', 0.2)

        if renpy.random.randint(1, 2)>1:
            scene BG char Kira bath-bj-02
            show Kira bath-mass bj-04
        elif True:
            scene BG bath-cun-01
            show Kira bath-mass bj-03

        $ _ch2 = GetChance(mgg.sex+10, 2, 900)
        menu:
            Max_21 "{i}( Ухх... Как нежно она посасывает своими губами мой член. И язычком орудует с такой страстью... Просто бесподобно! ){/i}"
            "Да, давай ещё тётя Кира! Какие же горячие и ненасытные у тебя губки... Да... \n{color=[_ch2.col]}(Сексуальный опыт. Шанс: [_ch2.vis]){/color}" if True:
                if not RandomChance(_ch3.ch) and not _in_replay:

                    jump kira_bath.not_restrain


        $ Skill('sex', 0.2)
        scene BG char Kira bath-bj-02
        show Kira bath-mass bj-05
        menu:
            Max_22 "{i}( Вот чёрт! Она так глубоко насаживает на него свой ротик... Ещё чуть-чуть и я взорвусь! А она сосёт всё быстрее... ){/i}"
            "Тётя Кира, я больше не могу... сейчас кончу! Да-а-а..." if True:
                Max_06 "{i}( Да... Она принимает всю мою сперму не вынимая член изо рта! О боже... Кажется, я её люблю! Хотя, что я болтаю... Но как же это приятно! ){/i}"
        scene BG char Kira bath-cum-01
        show Kira bath-mass cum-02
        Kira_08 "Вот и твоё напряжение мы сняли! Какие мы сегодня молодцы... Мне очень это всё понравилось!"
        Max_05 "И мне тоже! Было очень классно!"
        Kira_01 "Давай уже быстренько разбегаться, а то вдруг наши с тобой стоны кто-то услышал."
        Max_01 "Ага. Спокойной ночи, тётя Кира. С тобой очень здорово!"
        Kira_04 "Приятных снов, Макс."
        if not _in_replay:
            $ added_mem_var('bath_cuni_bj')
        jump kira_bath.end_sleep

    label kira_bath.not_restrain:

        $ Skill('sex', 0.1)
        scene BG bath-cun-02
        show Kira bath-mass hj-02
        Kira_08 "[norestrain!t]Ого! Кто-то у нас тут слишком перевозбудился... А я ведь только начала..."
        Max_20 "Фух... Я уже просто не мог... Принимать с тобой ванну - очень горячо, тётя Кира."
        scene BG char Kira bath-cum-01
        show Kira bath-mass cum-01
        Kira_05 "Да, Макс, такая вот у тебя тётя! Но мне всё равно очень понравилось!"
        Max_05 "И мне тоже! Было очень классно!"
        Kira_01 "Давай уже быстренько разбегаться, а то вдруг наши с тобой стоны кто-то услышал."
        Max_01 "Ага. Спокойной ночи, тётя Кира. С тобой очень здорово!"
        Kira_04 "Приятных снов, Макс."
        jump kira_bath.end_sleep

    label kira_bath.caught:

        scene BG char Eric catch-bath-00
        $ renpy.show('Kira catch bath '+catch)
        show Eric catch bath 00

        Eric_12 "Ох нифига себе, Макс!!! Это я удачно зашёл..."
        Max_13 "Это не то, чем кажется! Мы просто..."
        Eric_06 "Неужели вы тут на самом деле на лыжах катаетесь?! А так сразу и не скажешь!"
        Max_14 "Нет, просто так получилось..."


        scene BG char Eric catch-bath-01
        show Eric catch bath 01

        Eric_04 "Да не переживай, Макс. Вам повезло, что это я, а не кто-нибудь из твоих сестёр или твоя мама. Вы бы могли спокойно вылететь из этого дома со скандалом!"
        Kira_15 "Мне думается, что нам не так уж и повезло, видя то, как ты злорадствуешь!"
        Eric_05 "Это как посмотреть. Думаю, всем здесь понятно, что держать этот секрет в тайне от всех остальных я за просто так не стану..."
        Kira_13 "И что ты хочешь?"


        scene BG char Kira bath-bj-01
        show Eric catch bath 02
        Eric_03 "Сомневаюсь, что это Макс тебя совратил, а значит отдуваться тебе, Кира! Мне должно быть {b}приятно{/b} хранить этот секрет! Если понимаешь, о чём я..."
        Kira_16 "По-видимому, секс за молчание?!"
        Eric_08 "Приятно вести дела со взрослыми людьми. Правда, если я оттрахаю тебя, то криков ты точно не сдержишь, так что пока будет достаточно просто обалденного минета от тебя, Кира. Как ты на это смотришь?"
        Kira_14 "Мы тут слишком застигнуты врасплох. Нужно время, чтобы подумать."
        Eric_02 "Только не тяните с этим, а то я заскучаю... Ещё увидимся, если вы примете верное решение."


        scene BG char Kira bath-mass-02
        show Eric catch bath 03
        if GetRelMax('eric')[0]>0 and kira.dcv.battle.stage == 1:

            Max_08 "Ты правда собираешься по ночам отсасывать Эрику?!"
            Kira_13 "Похоже, придётся... Иначе, ты отправишься прямиком в летний лагерь, а я... Меня, скорее всего, тоже выгонят и боюсь отношения с твоей мамой у меня будут испорчены навсегда... А я этого очень не хочу..."
            Max_09 "Может быть, у меня получится как-то \"смягчить\" условия Эрика..."
            Kira_14 "Да они и так довольно мягкие, Макс. Может быть даже так, что от твоих попыток смягчить эти условия, ты сделаешь только обратное. Я буду делать то, что могу... и умею... Хотя бы ради тебя, потому что и правда, это ведь я тебя соблазнила. За всё приходится платить..."
            Max_07 "Я всё равно постараюсь тебе как-то помочь!"
            Kira_10 "Только осторожно, Макс! Потому что пока, всё не так уж и плохо..."
            $ kira.dcv.battle.stage = 2
        elif True:

            Max_08 "Тётя Кира, ты же не собираешься по ночам отсасывать Эрику, правда?!"
            Kira_13 "Похоже, придётся... Иначе, ты отправишься прямиком в летний лагерь, а я... Меня, скорее всего, тоже выгонят и боюсь отношения с твоей мамой у меня будут испорчены навсегда... А я этого очень не хочу..."
            Max_09 "Надо что-нибудь придумать, потому что для меня это не вариант!"
            Kira_14 "Ну, я буду делать то, что могу... и умею... Хотя бы ради тебя, потому что и правда, это ведь я тебя соблазнила. За всё приходится платить..."
            Max_11 "Мне это всё не нравится..."
            Kira_13 "Тогда, только ты сможешь с ним договориться о чём-то другом. Ну а мне придётся согласиться на это... Так что, вся надежда на тебя, Макс..."
            $ kira.dcv.battle.stage = 3
        menu:
            Max_10 "Ладно, я понял..."
            "{i}отправиться спать{/i}" if True:
                $ wcv.catch_Kira.set_lost(0)
                $ wcv.catch_Kira.stage = 1
                jump kira_bath.end_sleep

    label kira_bath.horsewoman:
        $ renpy.dynamic('ch3', 'ch2')
        $ ch3 = GetChance(mgg.sex+10, 2, 900)
        $ ch2 = GetChance(mgg.sex, 33, 900)


        scene BG char Kira bath-sex-03
        show Kira bath-sex 01-01
        menu:
            Kira_09 "Ах, Макс... Д-а-а... Вот так... Хватит уже дразнить мою киску... Дай мне уже сесть на него! Какой он твёрдый... Ммм..."
            "{i}Наслаждаться{/i} {color=[ch3.col]}(Сексуальный опыт. Шанс: [ch3.vis]){/color}" if True:
                pass
        if RandomChance(ch3.ch) or _in_replay:

            $ Skill('sex', 0.2)
            $ kira.stat.sex += 1

            if renpy.random.randint(0, 1):
                scene BG char Kira bath-sex-04
                show Kira bath-sex 01-02a
            elif True:
                scene BG char Kira bath-sex-05
                show Kira bath-sex 01-02b
            Kira_11 "[restrain!t]Охх... Да... Обожаю, когда можно попрыгать на чём-то весьма ощутимом! Д-а-а... Только не кончи раньше меня... Ммм... Я уже скоро! Как хорошо..."
            Max_20 "Ты обалденная, тётя Кира! Давай ещё быстрее..."
            menu:
                Kira_12 "О да! Я больше не могу, Макс... Ммм... Ох, как хорошо! Да, я кончаю... Ахх..."
                "{i}кончить в неё{/i}" if True:

                    scene BG char Kira bath-sex-03
                    show Kira bath-sex 01-01
                    show FG Kira bath-sex 01-cum01
                    Kira_07 "Вот так... Нравится кончать в свою тётю, а Макс? Мне вот понравилось!"
                    Max_05 "И мне тоже! Было очень классно!"
                    jump kira_bath.end_sex
                "{i}кончить ей на ноги{/i}" if True:


                    scene BG char Kira bath-fj-03
                    show Kira bath-mass fj3-01
                    Kira_08 "Фух, Макс, ну мы и выдали с тобой..."
                    Max_02 "Да, тётя Кира, это было что-то нереальное!"
                    jump kira_bath.end_sex
                "{i}кончить ей в рот{/i} {color=[ch2.col]}(Сексуальный опыт. Шанс: [ch2.vis]){/color}" if True:

                    jump kira_bath.cum_in_her_mouth
        elif True:



            scene BG char Kira bath-sex-03
            show Kira bath-sex 01-01
            show FG Kira bath-sex 01-cum01
            Kira_08 "[norestrain!t]Ого! Кто-то у нас тут слишком перевозбудился... А я ведь только начала..."
            Max_20 "Фух... Я уже просто не мог... Принимать с тобой ванну - очень горячо, тётя Кира."
            $ Skill('sex', 0.1)
            Kira_05 "Да, Макс, такая вот у тебя тётя! Давай уже быстренько разбегаться, а то вдруг наши с тобой стоны кто-то услышал."
            menu:
                Max_01 "Ага. Спокойной ночи, тётя Кира. С тобой очень здорово!"
                "{i}уйти{/i}" if True:
                    jump kira_bath.end_sleep

    label kira_bath.dogstyle:
        $ renpy.dynamic('ch3', 'ch2')
        $ ch3 = GetChance(mgg.sex+10, 2, 900)
        $ ch2 = GetChance(mgg.sex, 33, 900)


        scene BG char Kira bath-sex-01
        show Kira bath-sex 02-01
        menu:
            Kira_09 "Вот, держи... Д-а-а... Вот так... Вводи его не спеша... Ох, Макс... Он с таким трудом входит в меня, даже когда я такая мокренькая... Ммм..."
            "{i}трахать её{/i} {color=[ch3.col]}(Сексуальный опыт. Шанс: [ch3.vis]){/color}" if True:
                pass
        if RandomChance(ch3.ch) or _in_replay:


            if renpy.random.randint(0, 1):
                scene BG bath-cun-02
                show Kira bath-sex 02-02a
            elif True:
                scene BG char Kira bath-sex-02
                show Kira bath-sex 02-02b
            Kira_11 "[restrain!t]Охх... Да... Вот так, Макс! Трахай меня... Ещё... Ещё сильнее! Как же чертовски приятно чувствовать твой член! Д-а-а... Ещё... Я уже близко!"
            $ Skill('sex', 0.2)
            $ kira.stat.sex += 1
            Max_20 "Нравится, как я тебя трахаю, тётя Кира? Получай ещё..."
            menu:
                Kira_12 "О да! Трахай меня ещё быстрее! Я еле сдерживаюсь... Ох, как хорошо! Ещё! Да, вот так... Ммм... Да, я кончаю... Ахх..."
                "{i}кончить в неё{/i}" if True:

                    scene BG char Kira bath-sex-01
                    show Kira bath-sex 02-01
                    show FG Kira bath-sex 02-cum01
                    Kira_07 "Вот так... Нравится кончать в свою тётю, а Макс? Мне вот понравилось!"
                    Max_05 "И мне тоже! Было очень классно!"
                    jump kira_bath.end_sex
                "{i}кончить ей на попку{/i}" if True:


                    scene BG bath-cun-01
                    show Kira bath-sex 02-03
                    if renpy.random.randint(0, 1):
                        show FG Kira bath-sex 02-cum02a
                    elif True:
                        show FG Kira bath-sex 02-cum02b
                    Kira_05 "Ого, всю попку со спиной мне забрызгал, Макс! Приятно развлеклись перед сном, да?"
                    Max_02 "Да, тётя Кира, это было что-то нереальное!"
                    jump kira_bath.end_sex
                "{i}кончить ей в рот{/i} {color=[ch2.col]}(Сексуальный опыт. Шанс: [ch2.vis]){/color}" if True:

                    jump kira_bath.cum_in_her_mouth
        elif True:


            scene BG char Kira bath-sex-01
            show Kira bath-sex 02-01
            show FG Kira bath-sex 02-cum01
            Kira_08 "[norestrain!t]Ого! Ты уже всё! Кто-то у нас тут слишком перевозбудился... Тебе ещё привыкать и привыкать к нашим шалостям..."
            Max_20 "Фух... Я уже просто не мог... Принимать с тобой ванну - очень горячо, тётя Кира."
            $ Skill('sex', 0.1)
            Kira_05 "Да, Макс, такая вот у тебя тётя! Давай уже быстренько разбегаться, а то вдруг наши с тобой стоны кто-то услышал."
            menu:
                Max_01 "Ага. Спокойной ночи, тётя Кира. С тобой очень здорово!"
                "{i}уйти{/i}" if True:
                    jump kira_bath.end_sleep

    label kira_bath.cum_in_her_mouth:
        if RandomChance(ch2.ch) or _in_replay:


            if renpy.random.randint(0, 1):
                scene BG bath-cun-01
                show Kira bath-mass bj-03
            elif True:
                scene BG char Kira bath-bj-02
                show Kira bath-mass bj-04
            menu:
                Max_21 "[restrain!t]Ухх... Какие же горячие и ненасытные у тебя губки... Ты просто бесподобно сосёшь, тётя Кира! Да..."
                "{i}кончить{/i}" if True:
                    pass

            scene BG char Kira bath-bj-02
            show Kira bath-mass bj-05
            Max_06 "{i}( Да... Она принимает всю мою сперму не вынимая член изо рта! О боже... Кажется, я её люблю! Хотя, что я болтаю... Но как же это приятно! ){/i}"

            scene BG bath-cun-01
            show Kira bath-mass cum-02
            Kira_08 "Вот и твоё напряжение мы сняли! Какие мы сегодня молодцы... Мне очень это всё понравилось!"
            Max_05 "И мне тоже! Было очень классно!"
            $ Skill('sex', 0.2)
            jump kira_bath.end_sex
        elif True:


            scene BG bath-cun-02
            show Kira bath-mass hj-02
            Kira_08 "[norestrain!t]Ого! Кто-то у нас тут слишком перевозбудился... Я даже не успела ничего сделать..."
            Max_20 "Фух... Я уже просто не мог... Принимать с тобой ванну - очень горячо, тётя Кира."

            scene BG char Kira bath-cum-01
            show Kira bath-mass cum-01
            Kira_05 "Да, Макс, такая вот у тебя тётя! Но мне всё равно очень понравилось!"
            Max_05 "И мне тоже! Было очень классно!"
            $ Skill('sex', 0.1)
            jump kira_bath.end_sex

    label kira_bath.end_sex:
        Kira_01 "Давай уже быстренько разбегаться, а то вдруг наши с тобой стоны кто-то услышал."
        menu:
            Max_01 "Ага. Спокойной ночи, тётя Кира. С тобой очень здорово!"
            "{i}уйти{/i}" if True:
                jump kira_bath.end_sleep

    label kira_bath.end_sleep:
        $ renpy.end_replay()
        $ spent_time += 30
        $ current_room = house[0]
        $ mgg.cleanness = 100
        jump Sleep

    label kira_bath.end:
        $ spent_time += 10
        jump Waiting


label kira_night_swim:
    $ renpy.dynamic('r1')
    $ renpy.scene()
    $ renpy.show('Kira night-swim '+renpy.random.choice(['01', '02', '03']))

    if kira.flags.promise or not kira.stat.blowjob:
        Max_03 "Ого... Купаешься голой, тётя Кира?! Классно смотришься!"
        Kira_01 "А, Макс... Я думала, что все уже спят. Хотела немного поплавать... А ты чего не спишь?"
        Max_01 "Да, что-то не спится... К тебе можно?"
        Kira_02 "Ну, бассейн большой. К тому же, это ваш дом. Кому как не тебе решать? Но, давай не сегодня. Я очень устала и собиралась уже идти спать..."
        Max_04 "Тогда и я пойду спать... Спокойной ночи, тётя Кира."
        Kira_05 "Ага. Приятных снов, Макс."
        jump kira_night_swim.end
    elif True:
        $ added_mem_var('hj_in_pool')
        Max_03 "Ого... Купаешься голой, тётя Кира?! Классно смотришься!"
        menu:
            Kira_01 "А, Макс... Я думала, что все уже спят. Хотела немного поплавать... А ты чего не спишь?"
            "Да, что-то не спится... К тебе можно?" if kira.stat.handjob < 1:
                if not _in_replay:
                    $ SetCamsGrow(house[6], 200)
                scene BG char Kira pool-night-01
                show Max pool-night 01
                $ renpy.show('Kira pool-night '+renpy.random.choice(['01', '02', '03']))

                Kira_02 "Ну, бассейн большой. К тому же, это ваш дом. Кому как не тебе решать, с таким-то большим членом?"
                Max_03 "А, ну да. Это просто ты голая, вот у меня и стоит."
                menu:
                    Kira_05 "Абсолютно голая! Ладно, спускайся, а то я не могу спокойно на это смотреть..."
                    "{i}снять шорты{/i}" if True:
                        scene Kira pool-night 04

                Kira_04 "Да, теперь мне очень хорошо видно, насколько тебе нравится то, что скрывается под этой прозрачной водой..."
                Max_04 "Да и над водой тут нисколько картина не хуже!"

                scene Kira pool-night 05a

                Kira_07 "А тебя, похоже, заводит, что кто-то может увидеть, как твоя обнажённая тётя крепко сжимает и дрочит твой огромный член, да Макс?"
                Max_02 "О да!"

                scene Kira pool-night 06

                Kira_06 "Значит, любишь, когда за тобой наблюдают?"
                Max_07 "Ну, смотря кто..."

                scene Kira pool-night 07

                Kira_04 "Представь, что за тем, что я вытворяю своим языком с твоим членом, кто-то подглядывает... Может это Алиса... или Лиза... а может, даже твоя мама!"
                Max_20 "Ох, от таких мыслей я сейчас кончу, тётя Кира!"
                menu:
                    Kira_02 "Какой же ты испорченный мальчик! Но не переживай, бассейн мы не испачкаем. Я чувствую, ты уже совсем близко... Давай..."
                    "{i}кончить ей в рот!{/i}" if True:
                        scene Kira pool-night 08
                        show other Kira pool-night 08

                Max_05 "Ух, тётя Кира, как хорошо... Тебя я всё же немного испачкал."
                Kira_05 "Это разве испачкал, Макс? Конечно нет... Главное, что в воду ничего не попало."
                Max_03 "Ага, как будто ничего и не было."
                Kira_03 "Ладно, Макс, беги спать. Уже поздно. А то если нас заметят тут, будет много вопросов..."

                scene BG char Kira pool-night-10
                show Kira pool-night 10

                Max_04 "Только после тебя..."
                Kira_05 "О, спасибо, Макс! Приятно, что ты решил немного поухаживать за мной. Спокойной ночи! И шорты не забудь..."
                Max_01 "Не забуду... Спокойной ночи!"

                $ kira.stat.handjob = 1
                jump kira_night_swim.end

            "Не могу уснуть, слишком напряжён! {i}(снять шорты){/i}" if kira.stat.handjob > 0:
                if not _in_replay:
                    $ SetCamsGrow(house[6], 200)
                scene BG char Kira pool-night-01
                show Max pool-night 02
                $ renpy.show('Kira pool-night '+renpy.random.choice(['01', '02', '03']))

                menu:
                    Kira_06 "Ухх, впечатлил! Спускайся, тебе нужно немного охладиться. И как знать, может даже ты встретишь приключение на свой член!"
                    "{i}спуститься к Кире{/i}" if True:
                        scene Kira pool-night 04

                Max_04 "Приключения - это я люблю..."
                Kira_05 "А я, как раз кстати, могу тебе их обеспечить..."

                $ r1 = renpy.random.choice([1, 2])
                if r1 < 2:
                    scene BG char Kira pool-night-05
                    show Kira pool-night 05
                elif True:
                    scene Kira pool-night 05a

                Kira_04 "Я уже собиралась отправляться спать, устала. Но так уж и быть, немного помогу тебе, а заканчивать будешь сам..."
                Max_07 "Ну, так не интересно..."

                scene Kira pool-night 06

                Kira_02 "Не интересно? Ну да, согласна... Тогда давай сделаем так, утром я буду принимать душ одна, но не откажусь от твоей компании!"
                Max_03 "Так это я с радостью, тётя Кира!"
                Kira_07 "И если в душе ты меня порадуешь, то я порадую тебя сейчас, договорились?"
                Max_05 "Конечно!"

                scene Kira pool-night 07

                Kira_04 "Тогда, я пожалуй поиграю с тобой своим язычком. Тебе же нравится, когда я ласкаю им твой член?"
                Max_20 "О да, ты делаешь это великолепно! Продолжай тётя Кира..."

                $ r1 = renpy.random.choice(['08', '09'])
                $ renpy.scene()
                $ renpy.show('Kira pool-night '+r1)

                $ renpy.dynamic('sex2', 'sex4')
                $ sex2 = GetChance(mgg.sex+5, 2, 900)
                $ sex4 = GetChance(mgg.sex+10, 4, 900)

                $ kira.stat.handjob += 1
                menu:
                    Kira_02 "Какой же ты испорченный мальчик! Всё время называешь меня тётей... Это так пикантно! Давай, кончи мне в рот, я этого очень хочу..."
                    "{i}кончить!{/i}" if True:

                        $ renpy.show('other Kira pool-night '+r1)

                        Max_05 "Ух, тётя Кира, как хорошо... Тебя я всё же немного испачкал."
                        Kira_05 "Это разве испачкал, Макс? Конечно нет... Главное, что в воду ничего не попало."
                        Max_03 "Ага, как будто ничего и не было."
                        jump kira_night_swim.end_cum
                    "{i}сдерживаться{/i} {color=[sex4.col]}(Сексуальный опыт. Шанс: [sex4.vis]){/color}" if kira.stat.sex > 4:

                        if RandomChance(sex4.ch):

                            $ Skill('sex', 0.2)
                            Kira_07 "[restrain!t]Похоже, против таких приёмов, ты просто так сдаваться не собираешься... Как думаешь, долго ли ты продержишься, если твой дружок окажется у меня во рту?"
                            Max_02 "Давай проверим..."

                            scene Kira pool-night 11
                            Max_20 "{i}( Д-а-а... Она сосёт просто потрясающе! Так смачно и жадно... Как же приятно, когда мой член проскальзывает сквозь её нежные губки прямо в рот! ){/i}"
                            menu:
                                Max_19 "Охх... тётя Кира... Обожаю, когда ты так делаешь..."
                                "{i}получать удовольствие{/i} {color=[sex2.col]}(Сексуальный опыт. Шанс: [sex2.vis]){/color}" if True:
                                    if RandomChance(sex2.ch):

                                        $ Skill('sex', 0.2)
                                        $ added_mem_var('bj_in_pool')

                                        scene Kira pool-night 12
                                        Max_21 "[restrain!t]{i}( Вот чёрт! Я двигаюсь ей навстречу, а она всё глубже берёт его в рот! И всё больше и больше ускоряется... Такое я долго не выдержу! Я уже на грани... ){/i}"
                                        Max_22 "Тётя Кира, да... Я сейчас кончу... Давай ещё глубже! А-а-а..."

                                        $ r1 = renpy.random.choice(['08', '09'])
                                        $ renpy.scene()
                                        $ renpy.show('Kira pool-night '+r1)
                                        $ renpy.show('other Kira pool-night '+r1)
                                        Max_05 "{i}( О да... Прямо ей в рот! Хотя, нет, и мимо немного попало... О боже... Как же это приятно! ){/i}"
                                        Kira_05 "Понравилось, Макс? Как же я увлеклась... Надеюсь, мы никого не разбудили!"
                                        Max_03 "Вроде, нет... Всё тихо. Ты лучшая, тётя Кира!"
                                        $ kira.stat.blowjob += 1
                                        jump kira_night_swim.end_cum
                                    elif True:

                                        $ Skill('sex', 0.1)
                                        jump kira_night_swim.no_restrain
                        elif True:

                            $ Skill('sex', 0.1)
                            jump kira_night_swim.no_restrain

            "Я просто прогуливался перед сном. Пойду, уже поздно..." if not _in_replay:
                Kira_05 "Я тоже уже собираюсь идти спать... Приятных тебе снов, Макс."
                Max_04 "Спокойной ночи, тётя Кира."
                jump kira_night_swim.end

    label kira_night_swim.no_restrain:
        $ renpy.scene()
        $ renpy.show('Kira pool-night '+r1)
        $ renpy.show('other Kira pool-night '+r1)

        Max_05 "[norestrain!t]Ух, тётя Кира, как хорошо... Тебя я всё же немного испачкал."
        Kira_05 "Это разве испачкал, Макс? Конечно нет... Главное, что в воду ничего не попало."
        Max_03 "Ага, как будто ничего и не было."
        jump kira_night_swim.end_cum

    label kira_night_swim.end_cum:
        Kira_03 "Ладно, Макс, беги спать. Уже поздно. А то если нас заметят тут, будет много вопросов..."

        scene BG char Kira pool-night-10
        show Kira pool-night 10

        Max_04 "Только после тебя..."
        Kira_05 "О, спасибо, Макс! Приятно, что ты решил немного поухаживать за мной. Утром буду тебя ждать... Спокойной ночи! И шорты не забудь..."
        Max_01 "Не забуду... Спокойной ночи!"

        $ kira.flags.promise = True

    label kira_night_swim.end:
        $ renpy.end_replay()
        $ current_room = house[0]
        jump Sleep


label kira_sleep_night:
    scene BG char Kira lounge-night-01
    $ renpy.show('Kira sleep night '+pose3_4+kira.dress)
    if kira.hourly.sleep != 0:
        return

    $ kira.hourly.sleep = 1
    menu:
        Max_04 "Ага! Тётя Кира спит. Хорошо, что её ночнушка слегка просвечивает... Ухх, как она хороша..."
        "{i}подойти поближе{/i}" if True:
            scene BG char Kira lounge-night-02
            $ renpy.show('Kira sleep-closer night '+pose3_4+kira.dress)
            if pose3_4=='01':
                Max_02 "Класс! Какая сладкая попка у моей тёти... Хочется любоваться бесконечно. И не только любоваться..."
            elif pose3_4=='02':
                Max_03 "О, да! К этой шикарной попке я бы с удовольствием прижался... Как и к этим соблазнительным сисечкам. Ммм, очаровательна, как ни крути..."
            elif True:
                Max_05 "Чёрт, от вида этих раздвинутых и стройных ножек в шортах становится слишком тесно... Ещё бы, такая горячая красотка!"
        "{i}уйти{/i}" if True:
            pass

    return


label kira_sleep_morning:

    scene BG char Kira lounge-morning-01
    $ renpy.show('Kira sleep morning '+pose3_4+kira.dress)
    if kira.hourly.sleep != 0:
        return

    $ kira.hourly.sleep = 1

    if kira.sleepnaked:
        $ txt = _("Тёте Кире очень идёт быть голой! Может быть, это потому что я привык видеть её голой? В такие округлости просто нельзя не влюбиться...")
    elif True:
        $ txt = _("Ага! Тётя Кира ещё спит. Хорошо, что её ночнушка слегка просвечивает... Ухх, как она хороша...")
    menu:
        Max_04 "[txt!t]"
        "{i}подойти поближе{/i}" if True:
            scene BG char Kira lounge-morning-02
            $ renpy.show('Kira sleep-closer morning '+pose3_4+kira.dress)
            if pose3_4=='01':
                Max_02 "Класс! Какая сладкая попка у моей тёти... Хочется любоваться бесконечно. И не только любоваться..."
            elif pose3_4=='02':
                Max_03 "О, да! К этой шикарной попке я бы с удовольствием прижался... Как и к этим соблазнительным сисечкам. Ммм, очаровательна, как ни крути..."
            elif True:
                Max_05 "Чёрт, от вида этих раздвинутых и стройных ножек в шортах становится слишком тесно... Ещё бы, такая горячая красотка!"
        "{i}уйти{/i}" if True:
            pass

    return


label kira_night_tv:
    $ renpy.block_rollback()
    $ renpy.dynamic('lst', 'film', 'naked', 'suf', 'r1')
    scene BG tv-watch-01
    $ lst = []
    python:
        for i in range(1, 6):
            for j in range(3, 4):
                lst.append('porn-0'+str(i)+' 0'+str(j))
        if not _in_replay:
            for j in range(1, 7):
                lst.append('serial 0'+str(j)+'-0'+str(renpy.random.randint(1, 3)))
    $ film = renpy.random.choice(lst)
    $ naked = False
    $ renpy.show('tv '+film, at_list=[tv_screen,])
    $ renpy.show('Kira tv-watch 01'+kira.dress)
    if 'kira_night_tv.porn_view' not in persistent.memories:
        $ persistent.memories['kira_night_tv.porn_view'] = 0

    if 'serial' in film:

        menu:
            Max_01 "Тётя Кира ещё не легла спать... смотрит сериалы. Может, стоит задержаться?"
            "{i}подойти ближе{/i}" if True:
                pass
        scene BG lounge-tv-00
        $ renpy.show('Kira tv '+pose3_4+kira.dress)
        menu:
            Max_04 "Да-а-а, кто-то залипает на сериалы, а я вот залипаю на свою тётю..."
            "Тётя Кира?" if True:
                scene BG lounge-tv-01
                $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                show Max tv 00c

                menu:
                    Kira_01 "А? Макс? Как ты подкрался незаметно... Я думала, уже все спят давно... А меня тут один сериальчик зацепил, решила досмотреть..."
                    "Мне что-то не спится. Можно тоже телек с тобой посмотреть?" if True:
                        menu:
                            Kira_04 "Да без проблем, садись рядом. Будем досматривать сериал или найдём какой-нибудь боевик, фантастику?"
                            "Может быть, эротику?" if not kira.flags.porno:
                                Kira_08 "Макс, а ты не слишком юн для этого? Я не думаю, что это хорошая идея."
                                Max_09 "Ты прямо как моя мама! Я уже взрослый, а в этом доме не то что посмотреть эротику не выйдет, так даже просто произнести это нельзя."
                                Kira_14 "Вообще, я думаю, что тебе уже пора спать. Три часа ночи... Давай в другой раз поговорим об этом..."
                                Max_08 "Вот так всегда..."
                                jump kira_night_tv.end
                            "Давай смотреть порно?!" if kira.flags.porno:
                                jump kira_night_tv.porn
                    "Я насчёт уроков поцелуев, если момент подходящий..." if 'kira' in flags.how_to_kiss and learned_hand_massage():
                        jump kira_night_tv.teachkiss
                    "Я просто хотел пожелать спокойной ночи!" if True:
                        Kira_00 "Хорошо, Макс. Спокойной ночи! Я тоже уже скоро ложусь спать, только серию досмотрю..."
                        Max_00 "Ага, приятных снов..."
                        jump kira_night_tv.end
            "{i}посмотреть, что будет дальше{/i}" if True:
                scene BG lounge-tv-00
                $ renpy.show('Kira tv m-'+pose3_4+kira.dress)
                menu:
                    Max_05 "Ухх... Она начала ласкать свою киску... Вот это уже горячо!"
                    "Тётя Кира?" if True:
                        scene BG lounge-tv-01
                        $ renpy.show('Kira tv-closer m-'+pose3_4+kira.dress)
                        show Max tv 00c

                        menu:
                            Kira_07 "А? Макс? Как ты подкрался незаметно... Я думала, уже все спят давно... А я тут... отдыхаю, как видишь. Я тебя не смущаю таким своим видом?"
                            "Ни капли!" if True:
                                $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                                Kira_04 "Если твоя мама узнает, то нам обоим влетит. Так что... Пусть этот инцидент останется тайной..."
                                Max_03 "Конечно, тётя Кира. Мне что-то не спится. Можно тоже телек с тобой посмотреть?"
                                jump kira_night_tv.porn
                            "Да ты продолжай, я посижу, посмотрю..." if True:
                                $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                                Kira_04 "Ну что ты, Макс. Я просто не ожидала, что кто-то увидит. Так неловко... Мы ведь сохраним этот инцидент в тайне?"
                                Max_03 "Конечно, тётя Кира. Мне что-то не спится. Можно тоже телек с тобой посмотреть?"
                                jump kira_night_tv.porn
                            "Я насчёт уроков поцелуев, если момент подходящий..." if 'kira' in flags.how_to_kiss and learned_hand_massage():
                                $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                                jump kira_night_tv.teachkiss
                            "Я просто хотел пожелать спокойной ночи!" if True:
                                $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                                jump kira_night_tv.good_night
                    "{i}уже поздно, пора спать...{/i}" if True:
                        jump kira_night_tv.end
            "{i}уже поздно, пора спать...{/i}" if True:


                jump kira_night_tv.end
    elif True:

        pass
    if not _in_replay:
        $ SetCamsGrow(house[4], 150)

    menu:
        Max_01 "Тётя Кира ещё не легла спать... смотрит порнушку. Может, стоит задержаться?"
        "{i}подойти ближе{/i}" if True:
            pass
    scene BG lounge-tv-00
    $ renpy.show('Kira tv m-'+pose3_4+kira.dress)
    menu:
        Max_05 "Ухх... Она начала ласкать свою киску... Вот это уже горячо! От такой компании я не откажусь..."
        "Тётя Кира?" if True:
            scene BG lounge-tv-01
            $ renpy.show('Kira tv-closer m-'+pose3_4+kira.dress)
            show Max tv 00c

            if kira.flags.porno:
                menu:
                    Kira_07 "А? Макс? Как ты подкрался незаметно... Я думала, уже все спят давно... А я тут... отдыхаю, как видишь. Присоединишься?"
                    "Конечно, да!" if True:
                        jump kira_night_tv.porn
                    "Я насчёт уроков поцелуев, если момент подходящий..." if 'kira' in flags.how_to_kiss and learned_hand_massage():
                        jump kira_night_tv.teachkiss
                    "Я просто хотел пожелать спокойной ночи!" if True:
                        jump kira_night_tv.good_night
            elif True:
                menu:
                    Kira_07 "А? Макс? Как ты подкрался незаметно... Я думала, уже все спят давно... А я тут... отдыхаю, как видишь. Я тебя не смущаю таким своим видом?"
                    "Ни капли!" if True:
                        $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                        Kira_04 "Если твоя мама узнает, то нам обоим влетит. Так что... Пусть этот инцидент останется тайной..."
                        Max_03 "Конечно, тётя Кира. А мне можно тоже... посмотреть этот фильм?"
                        jump kira_night_tv.porn
                    "Да ты продолжай, я посижу, посмотрю..." if True:
                        $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                        Kira_04 "Ну что ты, Макс. Я просто не ожидала, что кто-то увидит. Так неловко... Мы ведь сохраним этот инцидент в тайне?"
                        Max_03 "Конечно, тётя Кира. А мне можно тоже... посмотреть этот фильм?"
                        jump kira_night_tv.porn
                    "Я насчёт уроков поцелуев, если момент подходящий..." if 'kira' in flags.how_to_kiss and learned_hand_massage():
                        $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                        jump kira_night_tv.teachkiss
                    "Я просто хотел пожелать спокойной ночи!" if True:
                        $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
                        jump kira_night_tv.good_night
        "{i}уже поздно, пора спать...{/i}" if True:
            jump kira_night_tv.end

    label kira_night_tv.porn:
        if kira.flags.porno:
            jump kira_night_tv.porn_view
        Kira_08 "Макс, а не рано тебе такое смотреть? Если эротику, то ещё куда ни шло... но это самое настоящее порно! Хотя, и эротику тебе не стоит смотреть. Во всяком случае, со мной..."
        Max_07 "Как будто я порно не видел... Мама с Эриком всё время тут порно смотрят, прежде чем уходят к себе наверх."
        if online_cources[0].cources[1].less > 0:
            $ _ch1 = GetChance(mgg.social, 2, 900)
        menu:
            Kira_07 "Ага. И ты не придумал ничего лучше, чем попробовать посмотреть со своей тётей порно среди ночи?"
            "Вообще-то, с лучшей тётей на свете! \n{color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if online_cources[0].cources[1].less > 0:
                if RandomChance(_ch1.ch):
                    $ Skill('social', 0.1)
                    Kira_02 "[succes!t]Очень приятно это слышать, Макс. Порно, значит... Ну давай, присаживайся. Только руки не распускать. И не смущайся - я иногда... к себе прикасаюсь, так ощущения от фильма более... интересные, если ты меня понимаешь..."
                    Max_04 "Да без проблем! Давай уже смотреть..."
                elif True:
                    jump kira_night_tv.failed
            "Вообще-то, с лучшей тётей на свете!" if not online_cources[0].cources[1].less > 0:
                jump kira_night_tv.failed

    label kira_night_tv.porn_view:

        if not _in_replay and 'kira_night_tv.porn_view' not in persistent.memories:
            $ persistent.memories['kira_night_tv.porn_view'] = 0
        if not _in_replay:
            $ SetCamsGrow(house[4], 180)
            if GetRelMax('kira')[0] < 2:
                $ AttitudeChange('kira', 1)
        scene BG tv-watch-01
        $ kira.flags.porno+=1
        if kira.flags.porno==1:
            show tv kira-porn-00 01 at tv_screen
            $ renpy.show('Kira tv-watch 01'+kira.dress)
            show Max tv-watch 01c

            Kira_04 "Давай. Хорошо, что я привезла с собой такие фильмы, а то с запретами вашей мамы здесь легко с ума сойти можно..."
            Max_10 "И не говори, тётя Кира. Сам изо дня в день мучаюсь... Столько девчонок красивых в доме, а если заметят стояк, так сразу извращенцем и ненормальным называют."
            show tv kira-porn-00 02 at tv_screen
            Kira_05 "Так нужно донести до каждой из них, что это нормальная реакция! Хоть это и твоя мама с сёстрами, но они так же ещё и девочки."
            Max_09 "Да я пытаюсь, нужно время..."
            show tv kira-porn-00 03 at tv_screen
            Kira_03 "Так, мы порно собирались смотреть или что? Всё, тихо... всё внимание на экран."
            Max_02 "{i}( О да, так классно смотреть такое со своей тётей... Она ведь та ещё проказница! А в шортах-то как тесно... ){/i}"

            scene BG tv-mass-01
            show Kira tv-closer max-01

            Max_03 "{i}( Ого, она трогает свою грудь! Блин, мне повезло с тётей. Она такая классная! ){/i}"
            Kira_07 "Макс, тебе тесно в твоих шортах? Я же ведь уже всё видела. Стесняешься меня? Мы с тобой сидим, смотрим порно, а ты прикрываешься?"

            show Kira tv-closer max-02

            Kira_05 "В общем, если хочешь, можешь себя трогать. Как я уже говорила, фильм от этого становится интереснее..."
            Max_04 "Да для меня ты уже интереснее фильма..."
            menu:
                Kira_02 "Спасибо, Макс... Это приятно слышать... Но ты так всё пропустишь самое интересное на экране..."
                "{i}начать дрочить{/i}" if True:
                    pass

            scene BG tv-mass-05
            show Kira tv-closer max-03

            Max_05 "{i}( С ума сойти... Я дрочу на глазах у своей тёти перед огромным экраном, на котором показывают порно... А она продолжает трогать свою грудь... и даже раздвинула ножки... И не стесняясь ласкает свою киску через трусики! ){/i}"
            Kira_10 "Ох, он у тебя такой большой, Макс... Это всё так возбуждает... Ммм..."
            menu:
                Max_20 "{i}( Да, Кира... Твоя помощь бы мне не помешала... Хотя... похоже, я сейчас кончу! ){/i}"
                "{i}кончить{/i}" if True:
                    pass

            scene BG tv-kiss-03
            show Kira tv-closer max-04
            Kira_09 "Ох, ты уже? Так быстро... Ну, иди приведи себя в порядок и ложись спать. Тебе уже пора. Я тоже скоро... заканчиваю..."
            Max_04 "Хорошо. Спокойной ночи, тётя Кира."
            jump kira_night_tv.end
        elif True:
            if _in_replay:
                scene BG tv-watch-01
            elif persistent.memories['kira_night_tv.porn_view'] < 1:
                $ persistent.memories['kira_night_tv.porn_view'] = 1
            $ renpy.show('tv kira-porn-00 '+renpy.random.choice(['01', '02', '03']), at_list=[tv_screen,])
            $ renpy.show('Kira tv-watch 01'+kira.dress)
            show Max tv-watch 01c

            Kira_04 "Давай. Благо, у меня большая коллекция таких фильмов..."
            Max_03 "Супер! Хотя я больше рад тому, с кем я это смотрю."

            scene BG tv-mass-01
            show Kira tv-closer max-02

            Kira_07 "Не стесняйся, Макс... Вижу, тебе уже очень тесно в шортах, доставай свой член! На экране уже давно это сделали... Ты отстаёшь..."
            Max_04 "Меня уговаривать не надо..."

            scene BG tv-mass-05
            show Kira tv-closer max-03
            $ suf = ''
            if kira.flags.m_foot:
                Kira_05 "Если хочешь, можешь даже снять шорты, чтобы резинка ничего не передавливала..."
                Max_02 "Только если ты тоже разденешься..."
                menu:
                    Kira_02 "Как же без этого, Макс. Но только немножко... чтобы ты не кончил уж очень быстро..."
                    "{i}снять шорты{/i}" if not kira.stat.blowjob and not kira.flags.promise:
                        $ suf = 'a'
                        show Kira tv-closer max-03a
                    "{i}снять шорты{/i}" if kira.stat.blowjob and not kira.flags.promise:
                        jump kira_night_tv.tv_cuni
                    "{i}снять шорты{/i}" if kira.flags.promise:
                        jump kira_night_tv.promise_cuni
            Kira_05 "Да, Макс, так уже лучше... С тобой просмотр порно становится куда интереснее. Похоже, тебе совершенно не стыдно дрочить прямо перед своей тётей?"
            Max_01 "Ни капли не стыдно! Особенно, если ей самой это нравится..."
            Kira_09 "О да, мне это очень нравится! От этого я становлюсь такой мокренькой... Ой, какая же я грязная девчонка..."
            Max_05 "{i}( Да, тётя Кира, ты очень плохая девочка... Мы смотрим порно, а ты раздвинула ножки и с таким жаром ласкаешь свою киску, пока я дрочу... ){/i}"
            Kira_10 "Ох, он у тебя такой большой, Макс... Это всё так возбуждает... Как хорошо... Делай это быстрее..."
            menu:
                Max_20 "{i}( Да, Кира... Твоя помощь бы мне не помешала... Хотя... похоже, я сейчас кончу и без этого! ){/i}"
                "{i}кончить{/i}" if True:
                    scene BG tv-kiss-03
                    $ renpy.show('Kira tv-closer max-04'+suf)

            Kira_09 "Ох, ты всё? Ну, тогда иди приведи себя в порядок и ложись спать. Тебе уже пора. Я тоже уже близка к тому... чтобы закончить..."
            Max_04 "Хорошо. Спокойной ночи, тётя Кира."
            jump kira_night_tv.end

    label kira_night_tv.promise_cuni:
        scene BG tv-mass-05
        show Kira tv-closer max-03b
        if not _in_replay:
            $ SetCamsGrow(house[4], 200)

        Kira_05 "Да, Макс, так уже лучше... С тобой просмотр порно становится куда интереснее. Но, мы же не будем просто сидеть, смотреть на экран и ласкать себя! Может порадуешь свою тётю, как обещал? Или ты уже забыл!?"
        menu:
            Max_03 "Конечно помню! Сейчас развлечёмся..."
            "{i}начать ласкать её киску языком{/i}" if True:
                scene BG tv-mass-03
                show Kira tv-game cun-01ab
        menu:
            Kira_02 "Макс... Если тебе мешают мои трусики, я их сниму... Или сними их сам."
            "{i}раздеть её и повернуть{/i}" if True:
                $ r1 = renpy.random.choice([1, 2])
        if r1<2:
            scene BG lounge-tv-01
            show Kira tv-game cun-04-1
        elif True:
            scene BG tv-cun-01
            show Kira tv-game cun-04-2

        menu:
            Kira_07 "Оу... Решил поиграть со мной так, Макс... Моя киска так скучала по твоим ласкам... Не останавливайся, я это обожаю! А ты способный... племянник..."
            "{i}проникнуть в неё пальцами{/i}" if True:
                if r1<2:
                    scene BG tv-cun-01
                    show Kira tv-game cun-05-1
                elif True:
                    scene BG tv-kiss-03
                    show Kira tv-game cun-05-2
        menu:
            Kira_10 "Ухх... Чёрт! Как хорошо... Ещё... глубже и быстрее... Да, вот так... Ммм..."
            "{i}продолжить языком{/i}" if True:
                $ r1 = renpy.random.choice([1, 2, 3])
        if r1<2:
            scene BG lounge-tv-01
            show Kira tv-game cun-06-1
        elif r1<3:
            scene BG tv-kiss-03
            show Kira tv-game cun-06-2
        elif True:
            scene BG char Alice tv-mass-11
            show Kira tv-game cun-06-3

        Kira_12 "Ох, Макс, не останавливайся! Сожми мою попку покрепче! Я уже так близко... Да! Я кончаю... Ахх..."
        Max_02 "Какая у тебя сочная попка, тётя Кира..."

        scene BG tv-mass-03
        show Kira tv-game cun-00bb

        Kira_06 "Да, Макс, она у меня такая... Я в восторге! Но лучше нам закругляться, а то я вполне могла кого-нибудь разбудить своими стонами."
        Max_01 "Конечно, тётя Кира. Ты лучшая! Спокойной ночи!"

        $ kira.flags.promise = False
        jump kira_night_tv.end

    menu kira_night_tv.teachkiss:
        Kira_00 "Да, да... Момент вполне подходящий... Ну что же, давай приступим."
        "С чего начнём?" if lisa.dcv.seduce.stage == 1:
            jump kira_night_tv.first_lesson

        "Как в прошлый раз?" if 1 < lisa.dcv.seduce.stage < 4:
            jump kira_night_tv.second_lesson

        "Отлично!" if lisa.dcv.seduce.stage > 3:
            jump kira_night_tv.repeat_lesson

    label kira_night_tv.first_lesson:

        $ renpy.block_rollback()
        scene BG lounge-tv-01
        show Kira tv-closer 01a
        show Max tv-closer 04c
        Kira_01 "Очень важная часть поцелуя - это прелюдия. Если ты накинешься на девушку в первый раз и начнёшь целовать, пусть даже и хорошо, то скорее всего, получишь отказ..."
        Max_00 "И что делать?"
        Kira_02 "Ну, с прелюдиями я тебе не помогу, тут всё индивидуально. Просто, поймай нужный момент и попробуй меня поцеловать как умеешь, для начала..."
        Max_02 "Да это легко!"
        scene BG char Kira tv-kiss-01
        show Kira tv-kiss 1-01
        Kira_04 "А вот и нет. Излишняя самоуверенность на многих действует, но скромных девушек может отпугнуть. Ты должен чувствовать ту, с которой планируешь... что ты там планируешь..."
        Max_04 "Тётя Кира, хватит меня дразнить, я всё это и так знаю!"
        menu:
            Kira_05 "Ну хорошо. Давай приступим..."
            "{i}поцеловать её{/i}" if True:
                pass
        $ r1 = renpy.random.choice(['02', '03'])
        $ renpy.show('Kira tv-kiss 1-'+r1)
        menu:
            Max_03 "{i}( Ого... Какой горячий ротик... И она так ловко орудует язычком... Так... И что мне, как... Эх, учиться мне ещё и учиться... А что, я очень даже не против такому учиться! ){/i}"
            "{i}продолжить целоваться{/i}" if True:
                $ renpy.block_rollback()
                $ r1 = {'02':'03', '03':'02'}[r1]
                $ renpy.show('Kira tv-kiss 1-'+r1)
                Max_05 "{i}( Ухх, она такая классная, что даже не хочется это прекращать! Так бы и целовал её вечно... ){/i}"
                show Kira tv-kiss 1-01
                Kira_01 "Ну всё, на сегодня хватит. Конечно, получается у тебя пока не очень, но это нормально. И ты знаешь, где меня найти, если захочешь потренироваться ещё... А теперь марш спать!"
                $ mgg.kissing = 1.1
            "{i}прикоснуться к её груди{/i}" if True:
                $ renpy.block_rollback()
                show Kira tv-kiss 1-04
                Kira_03 "Так, Макс, а вот это уже лишнее! Разве я позволяла тебе распускать руки?"
                Max_07 "Нет... Рука просто сама потянулась."
                show Kira tv-kiss 1-01
                Kira_04 "Что я тебе говорила про излишнюю самоуверенность? Спешка хороша для другого дела... и то, только по настроению. Понял меня?"
                Max_03 "Ага... Я учту это."
                Kira_01 "Тогда, на сегодня мы закончили. Конечно, получается у тебя пока не очень, но это нормально. И ты знаешь, где меня найти, если захочешь потренироваться ещё... А теперь марш спать!"
                $ mgg.kissing = 0.9
        Max_01 "Конечно! Спасибо, тётя Кира!"
        $ renpy.end_replay()
        $ persistent.memories['kira_night_tv.first_lesson'] = 1
        $ poss['seduction'].open(7)
        if GetRelMax('kira')[0] < 2:
            $ AttitudeChange('kira', 1)
        $ lisa.dcv.seduce.stage = 2
        $ SetCamsGrow(house[4], 150)

        jump kira_night_tv.end

    label kira_night_tv.second_lesson:

        $ renpy.block_rollback()
        if not _in_replay and 'kira_night_tv.second_lesson' not in persistent.memories:
            $ persistent.memories['kira_night_tv.second_lesson'] = 0
        if not _in_replay:
            $ SetCamsGrow(house[4], 180)
        scene BG char Kira tv-kiss-01
        show Kira tv-kiss 1-01
        Kira_01 "В прошлый раз я тебе рассказала про прелюдии, но с ними мы разобрались. Так что, давай просто будем повышать твою технику опытным путём..."
        menu:
            Max_02 "Да я только за!"
            "{i}поцеловать её{/i}" if True:
                pass
        if lisa.dcv.seduce.stage < 3:
            $ r1 = renpy.random.choice(['02', '03'])
            $ renpy.show('Kira tv-kiss 1-'+r1)
            Max_04 "{i}( Как же это приятно... Она такая... и такое делает язычком... Ух... Это просто невероятно... ){/i}"
            show Kira tv-kiss 1-01
            Kira_02 "Ну, уже лучше... Возвращаясь к прелюдии, кроме самих поцелуев важную роль играют так же и обоюдные ласки, которыми обмениваются партнёры во время поцелуев."
            Max_07 "Ласки, это в смысле..."
            Kira_07 "Прикосновения, Макс. Как и во время поцелуя, важно поймать нужный момент, чтобы не отпугнуть свою девушку твоим натиском, а наоборот - разжечь в ней страсть! Нужно чувствовать её и чего она хочет, понимаешь?"
            Max_01 "Не особо. Надо пробовать, тётя Кира."
            menu:
                Kira_05 "Ты прав. Когда вы оба уже во всю будете увлечены поцелуем, начни с лёгких прикосновений к талии, ножкам... Поверь мне, ты почувствуешь, нравится ли ей это... Ну что, попробуем?"
                "{i}поцеловать её{/i}" if True:
                    pass

        $ lisa.dcv.seduce.stage = 3
        $ r1 = renpy.random.choice(['02', '03'])
        $ renpy.show('Kira tv-kiss 1-'+r1)
        menu:
            Max_03 "{i}( О да! Кажется, мне никогда не надоест такая практика... Она так увлечённо целуется... Что она там говорила, про нужный момент? Может быть, это как раз он? ){/i}"
            "{i}прикоснуться к её груди{/i}" if not _in_replay:
                $ renpy.block_rollback()
                show Kira tv-kiss 1-04
                Kira_03 "Макс, это уже слишком! Зачем же так сразу? Как мне кажется, ты так ничего и не понял..."
                Max_07 "Просто решил начать с этого."
                show Kira tv-kiss 1-01
                Kira_04 "Что я тебе говорила про излишнюю самоуверенность? Спешка хороша для другого дела... и то, только по настроению. Понял меня?"
                Max_03 "Ага... Я учту это."
                Kira_01 "Тогда, на сегодня мы закончили. Конечно, получается у тебя пока не очень, но это нормально. И ты знаешь, где меня найти, если захочешь потренироваться ещё... А теперь марш спать!"
                Max_01 "Конечно! Спасибо, тётя Кира!"
                $ Skill('kissing', 0.2, 3.0)
                jump kira_night_tv.end

            "{i}прикоснуться к её попке{/i}" if not _in_replay:
                $ renpy.block_rollback()
                show Kira tv-kiss 1-01
                Kira_03 "Макс, ты немного спешишь! Зачем же так сразу? Как мне кажется, ты так ничего и не понял..."
                Max_07 "Просто решил начать с этого."
                Kira_04 "Что я тебе говорила про излишнюю самоуверенность? Спешка хороша для другого дела... и то, только по настроению. Понял меня?"
                Max_03 "Ага... Я учту это."
                Kira_01 "Тогда, на сегодня мы закончили. Конечно, получается у тебя пока не очень, но это нормально. И ты знаешь, где меня найти, если захочешь потренироваться ещё... А теперь марш спать!"
                Max_01 "Конечно! Спасибо, тётя Кира!"
                $ Skill('kissing', 0.2, 3.0)
                jump kira_night_tv.end
            "{i}подтянуть её ближе к себе{/i}" if True:

                $ renpy.block_rollback()
                scene BG tv-mass-05
                show Kira tv-kiss 2-01
                $ Skill('kissing', 0.1, 3.0)
                menu:
                    Max_02 "{i}( Ничего себе! Кира меня не оттолкнула! Похоже, я всё делаю верно... и, наверно, можно двигаться дальше? Боже мой, какая же у неё гладкая кожа, просто шёлк! ){/i}"
                    "{i}прикоснуться к её груди{/i}" if not _in_replay:
                        $ renpy.block_rollback()
                        scene BG char Kira tv-kiss-01
                        show Kira tv-kiss 1-04
                        Kira_03 "Макс, ты немного спешишь! Зачем же так сразу? Как мне кажется, ты так ничего и не понял..."
                        Max_07 "Ну поспешил немного, подумаешь!"
                        show Kira tv-kiss 1-01
                        Kira_04 "Что я тебе говорила про излишнюю самоуверенность? Спешка хороша для другого дела... и то, только по настроению. Понял меня?"
                        Max_03 "Ага... Я учту это."
                        Kira_01 "Тогда, на сегодня мы закончили. Конечно, получается у тебя пока не очень, но это нормально. И ты знаешь, где меня найти, если захочешь потренироваться ещё... А теперь марш спать!"
                        Max_01 "Конечно! Спасибо, тётя Кира!"
                        $ Skill('kissing', 0.2, 3.0)
                        jump kira_night_tv.end
                    "{i}прикоснуться к её попке{/i}" if True:

                        $ renpy.block_rollback()
                        scene BG tv-mass-01
                        show Kira tv-kiss 2-02
                        $ Skill('kissing', 0.2, 3.0)
                        menu:
                            Max_03 "{i}( Обалденно! Неужели это не сон и я действительно трогаю её суперскую попку?! Ну и что, что это попка моей тёти... На ощупь она просто восхитительна - нежная и упругая! Но пора двигаться выше. Охх... Кажется, я начинаю возбуждаться... ){/i}"
                            "{i}прикоснуться к её груди{/i}" if True:
                                pass

                scene BG tv-kiss-03
                show Kira tv-kiss 3-01
                Max_04 "{i}( Отлично! Кажется, ей действительно нравится, что я делаю... Она целует меня с такой жадностью, пока я мну её обалденную грудь... Она прикасается всё ниже и ниже, класс! ){/i}"
                if not _in_replay:
                    $ persistent.memories['kira_night_tv.second_lesson'] = 1
                    $ lisa.dcv.seduce.stage = 4
                if not kira.flags.m_foot:

                    Kira_07 "Ммм... Макс... думаю... нам надо заканчивать. Уже ведь так поздно."
                    scene BG char Kira tv-kiss-01
                    show Kira tv-kiss 1-04
                    Kira_04 "Уже значительно лучше. С сегодняшним уроком ты справился очень хорошо, но хорошего помаленьку. А то у тебя будет мозоль на языке... А теперь бегом спать! Я тут планирую ещё немного телек посмотреть..."
                    $ kira.flags.m_breast = 1
                    $ Skill('kissing', 0.3, 3.0)
                elif True:

                    $ _ch2 = GetChance(mgg.social, 2, 900)
                    menu:
                        Kira_07 "Ммм... Макс... думаю... нам надо заканчивать. Уже ведь так поздно."
                        "Давай ещё немного, тётя Кира... У меня ведь неплохо получается? \n{color=[_ch2.col]}(Убеждение. Шанс: [_ch2.vis]){/color}" if True:
                            pass
                    if not RandomChance(_ch2.ch) and not _in_replay:
                        $ Skill('social', 0.1)
                        $ Skill('kissing', 0.3, 3.0)
                        Kira_04 "[failed!t]Уже значительно лучше. С сегодняшним уроком ты справился очень хорошо, но хорошего помаленьку. А то у тебя будет мозоль на языке... А теперь бегом спать! Я тут планирую ещё немного телек посмотреть..."
                    elif True:
                        $ Skill('social', 0.2)
                        $ Skill('kissing', 0.5, 3.0)
                        menu:
                            Kira_09 "[succes!t]О да... уже значительно лучше... Ты быстро схватываешь... Ммм..."
                            "{i}развязать её ночнушку{/i}" if True:
                                if not _in_replay:
                                    $ kira.flags.m_breast = 2
                                scene BG tv-kiss-03
                                show Kira tv-kiss 3-02
                                Max_05 "{i}( Да! Я сделал это! Наконец-то я могу насладиться нежностью её обнажённой груди... Обалдеть можно, какая же она классная! Похоже, Кире тоже это нравится, я уже чувствую, как набухли её сосочки. Ухх, чёрт... она начала поглаживать мой член... ){/i}"
                                Kira_05 "О боже, Макс... Какой же ты развратник, забрался мне под ночнушку... Охх... Это очень мило, что я вызываю такое влечение у своего племянника, но нам надо остановиться..."
                                Max_07 "Почему?"
                                scene BG char Kira tv-kiss-01
                                show Kira tv-kiss 1-04a
                                Kira_04 "Потому что с сегодняшним уроком ты справился очень хорошо, но хорошего помаленьку. А то у тебя будет мозоль на языке... А теперь бегом спать! А мне ещё нужно придти немного в себя после этого..."
                Max_01 "Конечно! Спасибо, тётя Кира! Спокойной ночи!"
                jump kira_night_tv.end

    label kira_night_tv.repeat_lesson:

        if not _in_replay:
            $ persistent.memories['kira_night_tv.second_lesson'] = 1
            if 'kira_night_tv.repeat_lesson' not in persistent.memories:
                $ persistent.memories['kira_night_tv.repeat_lesson'] = 0
            if 'kira_tv_bj' not in persistent.memories:
                $ persistent.memories['kira_tv_bj'] = 0
        if not _in_replay:
            $ SetCamsGrow(house[4], 200)

        scene BG char Kira tv-kiss-01
        show Kira tv-kiss 1-01
        Kira_01 "Столько энтузиазма... Меня начинают посещать мысли, что делаешь ты это уже даже не ради обучения поцелуям..."
        menu:
            Max_02 "Не отвлекайся!"
            "{i}поцеловать её{/i}" if True:
                $ renpy.show('Kira tv-kiss 1-'+renpy.random.choice(['02', '03']))
        menu:
            Max_04 "{i}( Кажется, мне никогда не надоест это делать с такой женщиной... Ну и что, что она моя тётя... Но она так классно целуется! ){/i}"
            "{i}подтянуть её ближе к себе{/i}" if True:
                scene BG tv-mass-05
                show Kira tv-kiss 2-01
        Max_01 "{i}( Класс! Она и без моей помощи норовит страстно прижаться ко мне. Её нежная грудь слегка трётся об меня от чего мы начинаем целоваться ещё более страстно... ){/i}"
        scene BG tv-mass-01
        show Kira tv-kiss 2-02
        Max_03 "{i}( А от жара её мягкой попки под моей рукой можно потерять весь контроль... Но пора двигаться выше. Охх... Кажется, я начинаю возбуждаться... ){/i}"
        scene BG tv-kiss-03
        show Kira tv-kiss 3-01
        menu:
            Max_02 "{i}( О да! Как же это приятно, ощущать в руке упругость груди тёти Киры и наслаждаться её жаркими поцелуями... О таких уроках я и мечтать раньше не мог! ){/i}"
            "{i}развязать её ночнушку{/i}" if True:
                show Kira tv-kiss 3-02
        Max_05 "{i}( У неё такая большая и шелковистая грудь, а сосочки твёрдые и набухшие... И ей это всё очень нравится, она дышит так жарко... Её рука так приятно и легко поглаживает головку моего члена! ){/i}"
        $ Skill('kissing', 0.5 if mgg.kissing < 5 else 0.2, 6.5)
        if not kira.stat.footjob:
            $ kira.flags.m_breast = 2
            Kira_05 "О боже, Макс... Какой же ты развратник, забрался мне под ночнушку... Охх... Остановись, Макс..."
            Max_07 "Почему?"
            scene BG char Kira tv-kiss-01
            show Kira tv-kiss 1-04a
            Kira_04 "Хорошего помаленьку. У тебя уже получается гораздо лучше, чем раньше. И если захочешь попрактиковаться ещё, то ты знаешь куда и когда приходить... Но сейчас пора спать."
            Max_01 "Конечно! Спасибо, тётя Кира! Спокойной ночи!"
            jump kira_night_tv.end



        if kira.stat.blowjob:

            jump kira_night_tv.teach_cuni

        menu:
            Kira_05 "Ох... Макс, мои сосочки уже изнывают от желания, чтобы ты прикоснулся к ним своими губами и языком... Давай, не стесняйся!"
            "{i}ласкать её грудь и киску{/i}" if True:
                $ kira.flags.m_breast += 1
                if renpy.random.randint(1, 2)>1:
                    scene BG tv-mass-05
                    show Kira tv-kiss 3-04
                elif True:
                    show Kira tv-kiss 3-03
        menu:
            Kira_06 "Д-а-а... Вот так, Макс... Поиграй со мной! Как же я уже хочу, чтобы ты опускался своим шустрым язычком всё ниже и ниже... прямо туда... Оххх..."
            "{i}ласкать её киску языком{/i}" if True:
                scene BG tv-mass-03
                show Kira tv-game cun-01aa
        Kira_02 "Макс... Если тебе мешают мои трусики, я их сниму... Или сними их сам."
        Max_01 "В другой раз..."
        scene BG tv-cun-01
        show Kira tv-game cun-02aa
        menu:
            Kira_07 "Оу... Макс, ты где такому научился? В порнушке подсмотрел? Не останавливайся, я это обожаю! А ты способный... племянник..."
            "{i}продолжить{/i}" if True:
                pass
        menu:
            Kira_09 "Да... Ещё чуть-чуть и я кончу... Проникни в мою киску своими ловкими пальчиками... Она уже такая мокренькая..."
            "{i}продолжить пальцами и языком{/i}" if True:
                show Kira tv-game cun-03aa

        Kira_10 "Ухх... Чёрт! Как хорошо... Ещё... глубже и быстрее... Да, вот так... Ох, я кончаю... Д-а-а..."
        Max_02 "Вау, тётя Кира! Это было классно! Какая ты плохая девчонка..."
        Kira_05 "Ты даже не представляеешь, насколько я испорченная девчонка! Долой ночнушку... Стало уж слишком жарко..."
        Max_04 "Это точно!"
        scene BG tv-mass-07
        show Kira tv-game bj-01aa
        menu:
            Kira_07 "А ты, Макс, намного способнее, чем мне казалось... и заслужил кое-что особенное... Давай снимай шорты!"
            "{i}снять шорты{/i}" if True:
                scene BG char Kira tv-bj-01
                show Kira tv-game bj-02
        Kira_02 "Тебя ожидают незабываемые ощущения, Макс! Тебе будет очень непросто это сделать, но постарайся продержаться как можно дольше... потому что я очень хороша в том, что сейчас будет!"
        Max_03 "Думаю, я выдержу что угодно..."
        if renpy.random.randint(1, 2)>1:
            show Kira tv-game bj-04
        elif True:
            scene BG tv-mass-03
            show Kira tv-game bj-03ab
        Max_07 "Охх... тётя Кира, как приятно... чёрт, это и правда будет непросто выдержать..."
        $ _ch3 = GetChance(mgg.sex+10, 3, 900)
        menu:
            Kira_09 "Просто наслаждайся..."
            "Как бы мне не кончить уже сейчас! Какой у тебя игривый язычок... Ммм... \n{color=[_ch3.col]}(Сексуальный опыт. Шанс: [_ch3.vis]){/color}" if True:
                if not RandomChance(_ch3.ch) and not _in_replay:

                    jump kira_night_tv.not_restrain


        $ Skill('sex', 0.2)
        $ kira.stat.blowjob += 1
        if GetRelMax('kira')[0]<3:
            $ AttitudeChange('kira', 1)
        if renpy.random.randint(1, 2)>1:
            scene BG tv-mass-07
            show Kira tv-game bj-05ab
        elif True:
            scene BG char Kira tv-bj-01
            show Kira tv-game bj-06ab
        $ _ch2 = GetChance(mgg.sex+10, 2, 900)
        menu:
            Max_20 "[restrain!t]{i}Ухх, она так нежно посасывает головку моего члена... Видно, что это не так-то просто... ей еле хватает рта, чтобы это сделать.{/i}"
            "Да, вот так тётя Кира, твои губки творят чудеса! Охх... \n{color=[_ch2.col]}(Сексуальный опыт. Шанс: [_ch2.vis]){/color}" if True:
                if not RandomChance(_ch2.ch) and not _in_replay:

                    jump kira_night_tv.not_restrain


        $ Skill('sex', 0.2)
        if renpy.random.randint(1, 2)>1:
            scene BG char Kira tv-bj-01
            show Kira tv-game bj-08ab
        elif True:
            scene BG lounge-tv-01
            show Kira tv-game bj-07ab
        menu:
            Max_21 "[restrain!t]{i}Обалдеть! Как глубоко она берёт его в рот! Блин, я уже на грани... Вот-вот и кончу... А она ускоряет темп!{/i}"
            "Тётя Кира, ещё быстрее... Да... Я сейчас кончу... А-а-а..." if True:
                Max_05 "{i}( Фух... О да... Прямо туда... Неужели, она всё проглотила? Во даёт!!! ){/i}"
        scene BG char Kira tv-bj-01
        show Kira tv-game bj-02a
        Kira_08 "Макс, ты же понимаешь, что только что кончил прямо в рот своей родной тёте? Не стыдно?"
        Max_03 "Ни капли!"
        Kira_07 "Вот и правильно! Мне очень понравилось... А тебе?"
        Max_05 "Да как такое может не понравиться! Это вообще самое офигенное, что было в моей жизни!"
        scene BG tv-mass-01
        show Kira tv-game bj-09ab
        Kira_05 "О, Макс... У тебя ещё не было почти ничего..."
        Max_02 "Но, надеюсь, ведь ещё будет, тётя Кира?"
        Kira_04 "Со мной?! Очень может быть... А теперь бегом спать! А мне ещё нужно придти немного в себя после всего этого..."
        Max_01 "Конечно, тётя Кира. Ты лучшая! Спокойной ночи!"
        if not _in_replay:
            $ persistent.memories['kira_tv_bj'] = 1
            $ persistent.memories['kira_night_tv.repeat_lesson'] = 1
        jump kira_night_tv.end

    label kira_night_tv.not_restrain:

        $ Skill('sex', 0.1)
        scene BG char Kira tv-bj-01
        show Kira tv-game bj-04a
        Kira_08 "[norestrain!t]Ого! Ты уже всё! И не стыдно тебе, забрызгать всё лицо своей тёте спермой?"
        Max_05 "Ни капли!"
        Kira_05 "Вот и правильно! Со временем, когда привыкнешь к этому, тебе будет проще сдерживаться."
        Max_02 "Значит, будет следующий раз?!"
        scene BG tv-mass-01
        show Kira tv-game bj-09ab
        Kira_04 "Очень может быть... А теперь бегом спать! А мне ещё нужно придти немного в себя после всего этого..."
        Max_01 "Конечно, тётя Кира. Ты лучшая! Спокойной ночи!"
        jump kira_night_tv.end

    label kira_night_tv.not_restrain2:

        $ Skill('sex', 0.1)
        scene BG char Kira tv-bj-01
        show Kira tv-game bj-04a
        Kira_08 "[norestrain!t]Ого! Ты уже всё! Похоже, тебе ещё привыкать и привыкать к тому, что может вытворять мой ротик, потому что это было только начало..."
        Max_02 "Значит, до следующего раза?!"
        scene BG tv-mass-01
        show Kira tv-game bj-09bb
        jump kira_night_tv.end_sex

    label kira_night_tv.teach_cuni:
        if not _in_replay:
            $ persistent.memories['kira_night_tv.repeat_lesson'] = 1
            $ SetCamsGrow(house[4], 200)
            if GetRelMax('kira')[0]<3:
                $ AttitudeChange('kira', 1)
        menu:
            Kira_05 "Ох... Макс, мои сосочки уже изнывают от желания, чтобы ты прикоснулся к ним своими губами и языком..."
            "{i}ласкать её грудь и киску{/i}" if True:
                $ kira.flags.m_breast += 1
                if renpy.random.randint(1, 2)>1:
                    scene BG tv-mass-05
                    show Kira tv-kiss 3-04
                elif True:
                    show Kira tv-kiss 3-03
        menu:
            Kira_06 "Д-а-а... Вот так, Макс... Поиграй со мной! Как же я уже хочу, чтобы ты опускался своим шустрым язычком всё ниже и ниже... прямо туда... Оххх..."
            "{i}ласкать её киску языком{/i}" if True:
                scene BG tv-mass-03
                show Kira tv-game cun-01aa
        menu:
            Kira_02 "Макс... Если тебе мешают мои трусики, я их сниму... Или сними их сам."
            "{i}раздеть её{/i}" if True:
                scene BG tv-cun-01
                show Kira tv-game cun-02ba
                menu:
                    Kira_07 "Оу... Макс, моя киска так скучала по твоим ласкам... Не останавливайся, я это обожаю! А ты способный... племянник..."
                    "{i}продолжить{/i}" if True:
                        pass
                menu:
                    Kira_09 "Да... Ещё чуть-чуть и я кончу... Проникни в мою киску своими ловкими пальчиками... Она уже такая мокренькая..."
                    "{i}продолжить пальцами и языком{/i}" if True:
                        show Kira tv-game cun-03ba

                if kira.dcv.photo.stage>1:


                    jump kira_night_tv.tv_sex1


                Kira_10 "Ухх... Чёрт! Как хорошо... Ещё... глубже и быстрее... Да, вот так... Ох, я кончаю... Д-а-а..."
                Max_02 "Какая ты испорченная девчонка, тётя Кира..."
                scene BG tv-mass-07
                show Kira tv-game bj-01ba
                menu:
                    Kira_07 "Да, я очень испорченная... а ты, Макс, заслужил кое-что особенное... Давай снимай шорты! Твой член так и напрашивается на то, чтобы его хорошенько приласкали..."
                    "{i}снять шорты{/i}" if True:
                        pass

            "{i}раздеться вместе{/i}" if kira.stat.handjob:
                call kira_night_tv.cuni_var2 from _call_kira_night_tv_cuni_var2
        scene BG char Kira tv-bj-01
        show Kira tv-game bj-02
        jump kira_night_tv.bj

    label kira_night_tv.cuni_var2:
        if not _in_replay:
            $ SetCamsGrow(house[4], 200)
        $ r1 = renpy.random.choice([1, 2])
        if r1<2:
            scene BG lounge-tv-01
            show Kira tv-game cun-04-1
        elif True:
            scene BG tv-cun-01
            show Kira tv-game cun-04-2
        menu:
            Kira_07 "Оу... Решил поиграть со мной так, Макс... Моя киска так скучала по твоим ласкам... Не останавливайся, я это обожаю! А ты способный... племянник..."
            "{i}проникнуть в неё пальцами{/i}" if True:
                if r1<2:
                    scene BG tv-cun-01
                    show Kira tv-game cun-05-1
                elif True:
                    scene BG tv-kiss-03
                    show Kira tv-game cun-05-2
        menu:
            Kira_10 "Ухх... Чёрт! Как хорошо... Ещё... глубже и быстрее... Да, вот так... Ммм..."
            "{i}продолжить языком{/i}" if True:
                $ r1 = renpy.random.choice([1, 2, 3])
        if r1<2:
            scene BG lounge-tv-01
            show Kira tv-game cun-06-1
        elif r1<3:
            scene BG tv-kiss-03
            show Kira tv-game cun-06-2
        elif True:
            scene BG char Alice tv-mass-11
            show Kira tv-game cun-06-3

        if kira.dcv.photo.stage>1:

            Kira_12 "Ох, Макс, не останавливайся! Сожми мою попку покрепче! Я уже так близко... Моя киска так хочет кое-чего большого и твёрдого!"
            jump kira_night_tv.tv_sex2


        Kira_12 "Ох, Макс, не останавливайся! Сожми мою попку покрепче! Я уже так близко... Да! Я кончаю... Ахх..."
        Max_02 "Какая у тебя сочная попка, тётя Кира..."

        scene BG tv-mass-07
        show Kira tv-game bj-01bb

        Kira_07 "Да... а ты, Макс, заслужил кое-что особенное... Твой член так и напрашивается на то, чтобы его хорошенько приласкали..."
        Max_04 "Да... Я очень этого хочу!"
        return

    label kira_night_tv.bj:
        if not _in_replay:
            $ SetCamsGrow(house[4], 200)
        menu:
            Kira_02 "Тебя ожидают незабываемые ощущения, Макс! Посмотрим, как долго ты сможешь продержаться на этот раз..."
            "{i}получать удовольствие{/i}" if True:
                if renpy.random.randint(1, 2)>1:
                    show Kira tv-game bj-04
                elif True:
                    scene BG tv-mass-03
                    show Kira tv-game bj-03bb
        Max_07 "Охх... тётя Кира, как приятно..."
        $ _ch3 = GetChance(mgg.sex+10, 3, 900)
        menu:
            Kira_09 "Просто наслаждайся..."
            "Как бы мне не кончить уже сейчас! Какой у тебя игривый язычок... Ммм... \n{color=[_ch3.col]}(Сексуальный опыт. Шанс: [_ch3.vis]){/color}" if True:
                if _in_replay:
                    if persistent.memories['kira_night_tv.porn_view'] < 3:
                        jump kira_night_tv.not_restrain2
                elif not RandomChance(_ch3.ch):

                    jump kira_night_tv.not_restrain2


        if not _in_replay and persistent.memories['kira_night_tv.porn_view'] < 3:
            $ persistent.memories['kira_night_tv.porn_view'] = 3
        $ added_mem_var('tv_bj1')
        $ Skill('sex', 0.2)
        if renpy.random.randint(1, 2)>1:
            scene BG tv-mass-07
            show Kira tv-game bj-05bb
        elif True:
            scene BG char Kira tv-bj-01
            show Kira tv-game bj-06bb
        $ _ch2 = GetChance(mgg.sex+10, 2, 900)
        menu:
            Max_20 "[restrain!t]{i}Ухх, она так нежно посасывает головку моего члена... Не представляю, как ей удаётся поместить её в рот!{/i}"
            "Да, вот так тётя Кира, твои губки творят чудеса! Охх... \n{color=[_ch2.col]}(Сексуальный опыт. Шанс: [_ch2.vis]){/color}" if True:
                if _in_replay:
                    if persistent.memories['kira_night_tv.porn_view'] < 4:
                        jump kira_night_tv.not_restrain2
                elif not RandomChance(_ch2.ch):

                    jump kira_night_tv.not_restrain2


        if not _in_replay and persistent.memories['kira_night_tv.porn_view'] < 4:
            $ persistent.memories['kira_night_tv.porn_view'] = 4
        $ Skill('sex', 0.2)
        $ added_mem_var('tv_bj2')
        if renpy.random.randint(1, 2)>1:
            scene BG char Kira tv-bj-01
            show Kira tv-game bj-08bb
        elif True:
            scene BG lounge-tv-01
            show Kira tv-game bj-07bb
        menu:
            Max_21 "[restrain!t]{i}Обалдеть! Как глубоко она берёт его в рот! Блин, я уже на грани... Вот-вот и кончу... А она ускоряет темп!{/i}"
            "Тётя Кира, ещё быстрее... Да... Я сейчас кончу... А-а-а..." if True:
                Max_05 "{i}( Фух... О да... Прямо ей в рот! Она всё глотает! О боже... Как же это приятно! ){/i}"
                $ kira.stat.blowjob += 1
        scene BG char Kira tv-bj-01
        show Kira tv-game bj-02a
        Kira_07 "Ну вот. Понравилось? И ни капли мимо... ну, почти."
        Max_05 "Ты потрясающая, тётя Кира! До следующего раза?!"
        scene BG tv-mass-01
        show Kira tv-game bj-09bb
        if not _in_replay:
            $ persistent.memories['kira_tv_bj'] = 1
        jump kira_night_tv.end_sex

    label kira_night_tv.tv_cuni:
        if _in_replay:
            scene BG tv-mass-05
        if not _in_replay:
            $ SetCamsGrow(house[4], 200)
        show Kira tv-closer max-03b
        Kira_05 "Да, Макс, так уже лучше... С тобой просмотр порно становится куда интереснее. Но, мы же не будем просто сидеть, смотреть на экран и ласкать себя! Верно?"
        menu:
            Max_01 "Мне нравится, к чему ты клонишь, тётя Кира..."
            "{i}начать ласкать её киску языком{/i}" if True:
                scene BG tv-mass-03
                show Kira tv-game cun-01ab
        menu:
            Kira_02 "Макс... Если тебе мешают мои трусики, я их сниму... Или сними их сам."
            "{i}раздеть её{/i}" if True:
                scene BG tv-cun-01
                show Kira tv-game cun-02bb
                menu:
                    Kira_07 "Оу... Макс, моя киска так скучала по твоим ласкам... Не останавливайся, я это обожаю! А ты способный... племянник..."
                    "{i}продолжить{/i}" if True:
                        pass
                menu:
                    Kira_09 "Да... Ещё чуть-чуть и я кончу... Проникни в мою киску своими ловкими пальчиками... Она уже такая мокренькая..."
                    "{i}продолжить пальцами и языком{/i}" if True:
                        show Kira tv-game cun-03bb

                if kira.dcv.photo.stage>1:

                    $ naked = True
                    jump kira_night_tv.tv_sex1


                Kira_10 "Ухх... Чёрт! Как хорошо... Ещё... глубже и быстрее... Да, вот так... Ох, я кончаю... Д-а-а..."
                Max_02 "Какая ты испорченная девчонка, тётя Кира..."
                scene BG tv-mass-07
                show Kira tv-game bj-01bb
                Kira_07 "Да, я очень испорченная... а ты, Макс, заслужил кое-что особенное... Твой член так и напрашивается на то, чтобы его хорошенько приласкали..."
                Max_04 "Да... Я очень этого хочу!"
            "{i}раздеть её и повернуть{/i}" if kira.stat.handjob:
                call kira_night_tv.cuni_var2 from _call_kira_night_tv_cuni_var2_1

        scene BG char Kira tv-bj-01
        show Kira tv-game bj-02
        if persistent.memories['kira_night_tv.porn_view']<2 and not _in_replay:
            $ persistent.memories['kira_night_tv.porn_view'] = 2
        jump kira_night_tv.bj

    label kira_night_tv.tv_sex1:

        scene BG tv-cun-01
        if naked:
            show Kira tv-game cun-03bb
        elif True:
            show Kira tv-game cun-03ba

        menu:
            Kira_10 "Ухх... Чёрт! Как хорошо... Ещё... глубже и быстрее... Ещё чуть-чуть и я кончу... Может быть, ты воспользуешься чем-то потолще пальчиков и язычка?"
            "{i}трахнуть тётю Киру{/i} (миссионерская поза)" if naked:
                jump kira_night_tv.missionary

            "{i}снять шорты и трахнуть тётю Киру{/i} (миссионерская поза)" if not naked:
                jump kira_night_tv.missionary

            "{i}трахнуть тётю Киру{/i} (поза на боку)" if False:
                pass

    label kira_night_tv.tv_sex2:
        $ _ch_sex2 = GetChance(mgg.sex+5, 2, 900)
        $ _ch_sex4 = GetChance(mgg.sex+10, 4, 900)

        menu:
            Kira_12 "Ох, Макс, не останавливайся! Сожми мою попку покрепче! Я уже так близко... Моя киска так хочет кое-чего большого и твёрдого!"
            "{i}трахнуть тётю Киру (догги-стайл){/i}" if True:
                pass

        scene BG char Kira tv-sex02-01
        show Kira tv-sex 02-01
        menu:
            Kira_09 "Ох, Макс... Я обожаю этот момент! Д-а-а... Вот так... Вводи его не спеша... хочу немного привыкнуть к его размерам... Ммм..."
            "{i}трахать её{/i} {color=[_ch_sex4.col]}(Сексуальный опыт. Шанс: [_ch_sex4.vis]){/color}" if True:
                pass
        if RandomChance(_ch_sex4.ch):

            $ r1 = renpy.random.randint(1, 3)
            if r1 < 2:

                scene BG char Kira tv-sex02-01
                show Kira tv-sex 02-02a
            elif r1 < 3:

                scene BG tv-mass-03
                show Kira tv-sex 02-02b
            elif True:

                scene BG char Kira after-club-s09a-f
                show Kira tv-sex 02-02c

            Kira_11 "[restrain!t]Как приятно чувствовать твой член, Макс! Охх... Да... Вгоняй его в мою киску сильнее... Ещё! Оттрахай меня пожёстче... Д-а-а... Ещё..."
            $ Skill('sex', 0.2)
            $ kira.stat.sex += 1
            Max_20 "Какая у тебя сочная попка, тётя Кира..."
            menu:
                Kira_12 "О да! Ещё... ещё, Макс... Да, вот так... Ммм... Трахай меня ещё быстрее! Я еле сдерживаюсь... Ох, как хорошо! Ещё! Да, я кончаю... Ахх..."
                "{i}кончить в неё{/i}" if True:

                    scene BG char Kira tv-sex02-01
                    show Kira tv-sex 02-01
                    show FG Kira tv-sex 02-cum01
                    Kira_07 "Должно быть блаженно, кончать в свою тётю, да Макс? Я к этому готова всегда, но за других женщин говорить не могу, так что лучше быть осторожнее..."
                    Max_07 "Да, тётя Кира! Значит, до следующего раза?!"
                    jump kira_night_tv.end_sex
                "{i}кончить ей на попку{/i}" if True:


                    scene BG tv-sex03-01
                    show Kira tv-sex 02-03
                    $ renpy.show('FG Kira tv-sex 02-cum02'+('a' if renpy.random.randint(1, 2)<2 else 'b'))
                    Kira_05 "Ого, сколько её в тебе, Макс! Всю попку мне залил, безобразник... Это я любя! Славно развлеклись, правда?"
                    Max_02 "Да, тётя Кира! Значит, до следующего раза?!"
                    jump kira_night_tv.end_sex
                "{i}кончить ей в рот{/i} {color=[_ch_sex4.col]}(Сексуальный опыт. Шанс: [_ch_sex4.vis]){/color}" if True:

                    if RandomChance(_ch_sex4.ch):

                        jump kira_night_tv.cum_in_mouth
                "Порадуешь меня минетом, тётя Кира? {color=[_ch_sex2.col]}(Сексуальный опыт. Шанс: [_ch_sex2.vis]){/color}" if True:

                    if RandomChance(_ch_sex2.ch):


                        scene BG tv-sex03-01
                        show Kira tv-sex 02-03
                        jump kira_night_tv.minet_after_sex



            scene BG tv-sex03-01
            show Kira tv-sex 02-03
            $ renpy.show('FG Kira tv-sex 02-cum02'+('a' if renpy.random.randint(1, 2)<2 else 'b'))
            Kira_05 "[norestrain!t]Ого, сколько её в тебе, Макс! Всю попку мне залил, безобразник... Это я любя! Славно развлеклись, правда?"
            $ Skill('sex', 0.1)
            Max_02 "Да, тётя Кира! Значит, до следующего раза?!"
            jump kira_night_tv.end_sex



        scene BG char Kira tv-sex02-01
        show Kira tv-sex 02-01
        show FG Kira tv-sex 02-cum01
        Kira_08 "[norestrain!t]Ого! Ты уже всё! Похоже, тебе ещё привыкать и привыкать к тому наслаждению, которое нас ждало дальше..."
        $ Skill('sex', 0.1)
        Max_07 "Да, тётя Кира, извини! Не сдержался... Значит, до следующего раза?!"
        jump kira_night_tv.end_sex

    label kira_night_tv.missionary:
        $ _ch_sex2 = GetChance(mgg.sex+5, 2, 900)
        $ _ch_sex4 = GetChance(mgg.sex+10, 4, 900)

        scene BG tv-sex03-01
        show Kira tv-sex 03-01
        menu:
            Kira_09 "Ох, Макс... Какой же это классный момент! Д-а-а... Вот так... Вводи его не спеша... чтобы я привыкла... Ммм..."
            "{i}трахать её{/i} {color=[_ch_sex4.col]}(Сексуальный опыт. Шанс: [_ch_sex4.vis]){/color}" if True:
                pass
        if RandomChance(_ch_sex4.ch):


            if renpy.random.randint(1, 2) < 2:
                scene BG tv-sex03-01
                show Kira tv-sex 03-02a
            elif True:
                scene BG tv-mass-03
                show Kira tv-sex 03-02b

            Kira_11 "[restrain!t]Как приятно чувствовать твой член, Макс! Охх... Да... Вгоняй его в меня сильнее... Ещё! Оттрахай меня как следует... Д-а-а... Ещё..."
            $ Skill('sex', 0.2)
            $ kira.stat.sex += 1
            Max_20 "Какая ты испорченная девчонка, тётя Кира..."
            menu:
                Kira_12 "О да! Ещё... ещё, Макс... Да, вот так... Ммм... Трахай меня ещё сильнее! Я еле сдерживаюсь... Ох, как хорошо! Ещё! Да, я кончаю... Ахх..."
                "{i}кончить в неё{/i}" if True:

                    scene BG tv-sex03-01
                    show Kira tv-sex 03-01
                    show FG Kira tv-sex 03-cum01
                    Kira_07 "Должно быть блаженно, кончать в свою тётю, да Макс? Я к этому готова всегда, но за других женщин говорить не могу, так что лучше быть осторожнее..."
                    Max_07 "Да, тётя Кира! Значит, до следующего раза?!"
                    jump kira_night_tv.end_sex
                "{i}кончить ей на живот{/i}" if True:


                    scene BG tv-mass-07
                    show Kira tv-sex 03-03
                    $ renpy.show('FG Kira tv-sex 03-cum02'+('a' if renpy.random.randint(1, 2)<2 else 'b'))
                    Kira_05 "Ого, сколько её в тебе, Макс! Весь живот мне залил, безобразник... Это я любя! Славно развлеклись, правда?"
                    Max_02 "Да, тётя Кира! Значит, до следующего раза?!"
                    jump kira_night_tv.end_sex
                "{i}кончить ей в рот{/i} {color=[_ch_sex4.col]}(Сексуальный опыт. Шанс: [_ch_sex4.vis]){/color}" if True:

                    if RandomChance(_ch_sex4.ch):

                        jump kira_night_tv.cum_in_mouth
                "Порадуешь меня минетом, тётя Кира? {color=[_ch_sex2.col]}(Сексуальный опыт. Шанс: [_ch_sex2.vis]){/color}" if True:

                    if RandomChance(_ch_sex2.ch):


                        scene BG tv-mass-07
                        show Kira tv-sex 03-03
                        jump kira_night_tv.minet_after_sex



            scene BG tv-mass-07
            show Kira tv-sex 03-03
            $ renpy.show('FG Kira tv-sex 03-cum02'+('a' if renpy.random.randint(1, 2)<2 else 'b'))
            Kira_05 "[norestrain!t]Ого, сколько её в тебе, Макс! Весь живот мне залил, безобразник... Это я любя! Славно развлеклись, правда?"
            $ Skill('sex', 0.1)
            Max_02 "Да, тётя Кира! Значит, до следующего раза?!"
            jump kira_night_tv.end_sex



        scene BG tv-sex03-01
        show Kira tv-sex 03-01
        show FG Kira tv-sex 03-cum01
        Kira_08 "[norestrain!t]Ого! Ты уже всё! Похоже, тебе ещё привыкать и привыкать к тому наслаждению, которое нас ждало дальше..."
        $ Skill('sex', 0.1)
        Max_07 "Да, тётя Кира, извини! Не сдержался... Значит, до следующего раза?!"
        jump kira_night_tv.end_sex

    label kira_night_tv.cum_in_mouth:

        $ r1 = renpy.random.randint(1, 3)
        if r1 < 2:

            scene BG lounge-tv-01
            show Kira tv-game bj-02-01a
        elif r1 < 3:

            scene BG char Kira after-club-s08a-f
            show Kira tv-game bj-02-01b
        elif True:

            scene BG char Kira after-club-s04-f
            show Kira tv-game bj-02-01c

        Max_20 "[restrain!t]{i}Ухх, как же смачно она посасывает головку моего члена... Не представляю, как ей удаётся поместить её в рот, но она справляется! А я кончаю... Д-а-а...{/i}"
        $ Skill('sex', 0.2)

        scene BG tv-mass-07
        show Kira tv-game bj-02-02
        show FG Kira tv-sex 02-cum03
        Max_05 "{i}Фух... О да... Прямо ей в рот! Она всё глотает! О боже... Как же это приятно!{/i}"
        Kira_07 "Ну вот. Понравилось? И ни капли мимо... ну, почти."
        Max_05 "Ты потрясающая, тётя Кира! До следующего раза?!"

        scene BG tv-mass-03
        show Kira tv-game cun-00bb
        jump kira_night_tv.end_sex

    label kira_night_tv.minet_after_sex:

        Kira_07 "[restrain!t]Фух, удивляюсь, как ты ещё не кончил, Макс! Твой член так и напрашивается на то, чтобы его хорошенько приласкали..."
        $ Skill('sex', 0.2)
        Max_04 "Да... Я очень этого хочу!"

        scene BG char Kira tv-bj-01
        show Kira tv-game bj-02
        Kira_02 "Устраивайся поудобнее... А я позабочусь о том, чтобы ты сладко-сладко кончил мне в рот! Если конечно выдержишь то, что я буду делать языком..."
        Max_03 "О да, ты им такое вытворяешь!"
        $ r1 = renpy.random.randint(1, 2)
        if r1 < 2:

            scene BG char Kira tv-bj-01
            show Kira tv-game bj-04
        elif True:

            scene BG tv-mass-03
            show Kira tv-game bj-03bb

        Max_07 "Охх... тётя Кира, как приятно..."
        menu:
            Kira_09 "Просто наслаждайся..."
            "{i}получать удовольствие{/i} {color=[_ch_sex2.col]}(Сексуальный опыт. Шанс: [_ch_sex2.vis]){/color}" if True:
                if RandomChance(_ch_sex2.ch):

                    if r1 < 2:

                        scene BG char Kira tv-bj-01
                        show Kira tv-game bj-06bb
                    elif True:

                        scene BG tv-mass-07
                        show Kira tv-game bj-05bb

                    Max_20 "[restrain!t]{i}Ухх, она так нежно посасывает головку моего члена... Не представляю, как ей удаётся поместить её в рот!{/i}"
                    $ Skill('sex', 0.2)
                    menu:
                        Max_19 "Да, вот так тётя Кира, твои губки творят чудеса! Охх..."
                        "{i}получать удовольствие{/i} {color=[_ch_sex2.col]}(Сексуальный опыт. Шанс: [_ch_sex2.vis]){/color}" if True:
                            if RandomChance(_ch_sex2.ch):

                                if r1 < 2:

                                    scene BG char Kira tv-bj-01
                                    show Kira tv-game bj-08bb
                                elif True:

                                    scene BG lounge-tv-01
                                    show Kira tv-game bj-07bb
                                Max_21 "[restrain!t]{i}Обалдеть! Как глубоко она берёт его в рот! Блин, я уже на грани... Вот-вот и кончу... А она ускоряет темп!{/i}"
                                $ Skill('sex', 0.2)
                                Max_22 "Тётя Кира, ещё быстрее... Да... Я сейчас кончу... А-а-а..."
                                Max_05 "{i}Фух... О да... Прямо ей в рот! Она всё глотает! О боже... Как же это приятно!{/i}"

                                scene BG char Kira tv-bj-01
                                show Kira tv-game bj-02a

                                Kira_07 "Ну вот. Понравилось? И ни капли мимо... ну, почти."
                                Max_05 "Ты потрясающая, тётя Кира! До следующего раза?!"

                                scene BG tv-mass-01
                                show Kira tv-game bj-09bb
                                jump kira_night_tv.end_sex



        scene BG char Kira tv-bj-01
        show Kira tv-game bj-04a
        Kira_08 "[norestrain!t]Ого! Ты уже всё! Похоже, тебе ещё привыкать и привыкать к тому, что может вытворять мой ротик, потому что это было только начало..."
        $ Skill('sex', 0.1)
        Max_02 "Значит, до следующего раза?!"

        scene BG tv-mass-01
        show Kira tv-game bj-09bb
        jump kira_night_tv.end_sex

    label kira_night_tv.end_sex:
        Kira_04 "Да, я буду ждать... А теперь бегом спать! А мне ещё нужно придти немного в себя после всего этого..."
        menu:
            Max_01 "Конечно, тётя Кира. Ты лучшая! Спокойной ночи!"
            "{i}уйти{/i}" if True:
                jump kira_night_tv.end

    label kira_night_tv.good_night:
        Kira_02 "Хорошо, Макс. Спокойной ночи! Я тоже уже ложусь спать... скоро."
        Max_01 "Ага, приятных снов..."
        jump kira_night_tv.end

    label kira_night_tv.failed:
        $ Skill('social', 0.05)
        Kira_14 "[failed!t]Приятно слышать, Макс, но тебе пора спать! Три часа ночи... Мне уже и самой пора ложиться спать."
        Max_08 "Вот так всегда..."
        if online_cources[0].current < 3 and not flags.hint_cources:
            $ flags.hint_cources = True
            Max_09 "{i}( Тётю Киру довольно трудно в чём-то убедить... Возможно, онлайн-курсы мне с этим помогут. ){/i}"

    label kira_night_tv.end:
        $ renpy.end_replay()
        $ spent_time += 30
        $ current_room = house[0]
        jump Sleep


label kira_shower:
    $ renpy.dynamic('r1')

    scene location house bathroom door-morning
    if kira.daily.shower > 0:
        menu:
            Max_00 "Кира сейчас принимает душ, не стоит ей мешать..."
            "{i}уйти{/i}" if True:
                return
    $ kira.daily.shower = 1
    menu:
        Max_01 "Интересно, кто сейчас в душе?"
        "{i}заглянуть со двора{/i}" if True:
            jump kira_shower.start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump kira_shower.ladder
        "{i}уйти{/i}" if True:
            return

    label kira_shower.ladder:
        $ Skill('hide', 0.03)
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        $ kira.flags.ladder += 1
        scene BG bathroom-morning-00
        $ kira.daily.shower = 2
        $ r1 = renpy.random.choice(['b', 'c', 'd'])
        $ renpy.show('Kira bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1)
        show FG bathroom-morning-00
        if r1 == 'b':
            Max_07 "Странно, что тётя Кира в полотенце... Она же любит везде посверкать своими почти голыми прелестями! Наверно, не проснулась ещё толком..."
        elif r1=='c':
            Max_03 "Здорово, тётя Кира в одних трусиках любуется собой! Отпадные у неё сиськи, люблю эти аппетитные сосочки..."
        elif True:
            Max_06 "Голая тётя Кира - это шикарно! Ей нужно в кино играть роковых красоток, с такой-то внешностью и фигурой..."
        if looked_ladder():
            $ house[3].max_cam = 2
            Max_07 "Мои зрители явно пропускают много всего интересного! Мне однозначно стоит установить сюда ещё одну камеру..."
        Max_00 "Хоть и не хочется, но пока меня не заметили, лучше уходить..."
        jump kira_shower.end

    label kira_shower.start_peeping:
        $ Skill('hide', 0.03)

        $ renpy.scene()
        $ kira.daily.shower = 2
        $ r1 = renpy.random.choice(['01', '02', '03', '04'])
        $ renpy.show('Kira shower '+r1)
        $ renpy.show('FG shower 00'+mgg.dress)
        if r1 == '04':
            $ r1 = renpy.random.randint(7, 8)
            menu:
                Max_05 "Ага! Тётя Кира сегодня одна... и похоже, решила немножко себя развлечь принимая водные процедуры... Это я удачно зашёл!"
                "К тебе можно, тётя Кира?" if kira.flags.promise:
                    jump kira_shower.promise_cuni
                "{i}продолжить смотреть{/i}" if True:
                    pass
                "{i}взглянуть со стороны{/i}" if True:
                    jump kira_shower.alt_peepeng
                "{i}уйти{/i}" if True:
                    jump kira_shower.end
        elif True:
            $ r1 = renpy.random.randint(1, 6)
            menu:
                Max_07 "Супер! Тётя Кира в душе... и совсем одна... такая голая и мокренькая... Вот это зрелище!"
                "К тебе можно, тётя Кира?" if kira.flags.promise:
                    jump kira_shower.promise_cuni
                "{i}продолжить смотреть{/i}" if True:
                    pass
                "{i}взглянуть со стороны{/i}" if True:
                    jump kira_shower.alt_peepeng
                "{i}уйти{/i}" if True:
                    jump kira_shower.end

        $ spent_time += 10

        scene BG shower-closer
        $ renpy.show('Kira shower-closer 0'+str(r1))
        show FG shower-closer
        if kira.flags.promise:
            if r1 < 7:
                Max_03 "Ухх... Наблюдать за моей тётей просто загляденье! Её округлости и изящность движений очень возбуждают..." nointeract
            elif True:
                Max_05 "За этим можно долго смотреть, а лучше присоединиться... Не зря же меня тётя Кира пригласила!" nointeract
            $ rez = renpy.display_menu([(_("К тебе можно, тётя Кира?"), 1), (_("{i}уйти{/i}"), 0)])
            if rez > 0:
                jump kira_shower.promise_cuni
            elif True:
                jump kira_shower.end
        elif True:
            if r1 < 7:
                Max_03 "Ухх... Наблюдать за моей тётей просто загляденье! Её округлости и изящность движений очень возбуждают..."
            elif True:
                Max_05 "Вот так, тётя Кира... Хорошенько поласкай свою киску для меня! Ох, как же она этим наслаждается... Вот будет неловко, если она меня увидит! Хотя, ей уж точно не будет..."
        jump kira_shower.end

    label kira_shower.alt_peepeng:
        $ spent_time += 10
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Kira shower-alt 0'+str(r1), at_list=[left_shift,])
        show FG shower-closer
        if kira.flags.promise:
            if r1 < 7:
                Max_03 "Ухх... Наблюдать за моей тётей просто загляденье! Её округлости и изящность движений очень возбуждают..." nointeract
            elif True:
                Max_05 "За этим можно долго смотреть, а лучше присоединиться... Не зря же меня тётя Кира пригласила!" nointeract
            $ rez = renpy.display_menu([(_("К тебе можно, тётя Кира?"), 1), (_("{i}уйти{/i}"), 0)])
            if rez > 0:
                jump kira_shower.promise_cuni
            elif True:
                jump kira_shower.end
        elif True:
            if r1 < 7:
                Max_03 "Ухх... Наблюдать за моей тётей просто загляденье! Её округлости и изящность движений очень возбуждают..."
            elif True:
                Max_05 "Вот так, тётя Кира... Хорошенько поласкай свою киску для меня! Ох, как же она этим наслаждается... Вот будет неловко, если она меня увидит! Хотя, ей уж точно не будет..."
        jump kira_shower.end

    label kira_shower.promise_cuni:
        if not _in_replay:
            $ SetCamsGrow(house[3], 200)
            $ mgg.cleanness = 100
        scene BG shower-closer
        show Kira shower-closer 03
        show FG shower-closer

        menu:
            Kira_02 "А, Макс, конечно можно! Тебя и дожидаюсь. Присоединяйся..."
            "{i}раздеться и присоединиться к Кире{/i}" if True:
                $ renpy.show('Kira shower-Max '+renpy.random.choice(['01','02']))

        Kira_05 "А я тут стою, вся такая мокренькая и думаю - забыл обо мне мой племянничек или нет."
        menu:
            Max_03 "Как о тебе можно забыть, тётя Кира? Тебя нужно как следует порадовать за вчерашнее..."
            "{i}ласкать её грудь{/i}" if True:
                $ r1 = renpy.random.choice(['07', '08'])
                $ renpy.scene()
                $ renpy.show('BG char Kira shower-'+r1)
                $ renpy.show('Kira shower-Max '+r1+'-01')
        menu:
            Kira_04 "Ох... Ты тот ещё шалунишка! Я обожаю, когда ласкают мою грудь и особенно мои сосочки... Ммм..."
            "{i}ласкать её киску пальцами{/i}" if True:
                $ renpy.show('Kira shower-Max '+r1+'-02')
        menu:
            Kira_10 "Да, Макс... Продолжай вот так и я уже не смогу сдержаться... У тебя такие ловкие пальчики... Да..."
            "{i}ласкать её киску языком{/i}" if True:
                $ renpy.show('Kira shower-Max '+r1+'-03')
        menu:
            Kira_11 "О да... Ещё, Макс... Я уже близко... Так приятно..."
            "{i}проникнуть в неё пальцами{/i}" if True:
                scene BG char Kira shower-08
                show Kira shower-Max 08-04

        Kira_12 "Ухх... Да, ещё... быстрее и глубже... Ммм, ещё чуть-чуть и я кончу... Ах!"
        Max_04 "Ну как, тётя Кира? Хорошо я тебя порадовал?"
        Kira_06 "Ещё как... Мне очень понравилось... Ты очень способный... племянник..."

        $ renpy.show('Kira shower-Max '+renpy.random.choice(['01','02']))

        Max_07 "Скоро уже, должно быть, завтрак будет готов, так что надо тихонько расходиться, а то нас кто-нибудь увидит."
        Kira_07 "Да, Макс, я как раз должна немного... успеть отойти..."

        $ renpy.end_replay()
        $ kira.flags.promise = False
        $ spent_time += 20
        jump kira_shower.end

    label kira_shower.end:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time += 10
        jump Waiting


label kira_lisa_shower:
    $ renpy.dynamic('r0', 'r1')

    scene location house bathroom door-morning
    if lisa.daily.shower > 0:
        menu:
            Max_00 "Лиза и Кира принимают душ, не стоит им мешать..."
            "{i}уйти{/i}" if True:
                return
    $ lisa.daily.shower = 1
    menu:
        Max_01 "Интересно, кто сейчас в душе?"
        "{i}заглянуть со двора{/i}" if True:
            jump kira_lisa_shower.start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump kira_lisa_shower.ladder
        "{i}уйти{/i}" if True:
            return

    label kira_lisa_shower.ladder:
        $ Skill('hide', 0.03)
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        if 'lisa_sh' in cam_flag:
            $ r0 = 1 if tm[-2:] < '30' else 2
            $ kira.flags.ladder += 1
        elif 'kira_sh' in cam_flag:
            $ r0 = 2 if tm[-2:] < '30' else 1
            $ lisa.flags.ladder += 1
        elif 'kira_lisa_sh' in cam_flag:
            $ r0 = 0
            $ kira.flags.ladder += 1
            $ lisa.flags.ladder += 1
        elif True:
            $ r0 = renpy.random.randint(1, 4)
            if r0 < 3:
                $ _m1_kira__var = 'kira' if r0 == 1 else 'lisa'
                if _m1_kira__var == 'lisa':
                    $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'lisa_sh')
                elif _m1_kira__var == 'kira':

                    $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'kira_sh')



        scene BG bathroom-morning-00
        $ r1 = renpy.random.choice(['c', 'd', 'c', 'd', 'c', 'd'])
        if r0 == 1:
            if 'kira_sh' in cam_flag:
                $ r1 = {'04a':'b', '04b':'c', '00':'d', '00a':'d'}[kira.dress_inf]
            elif True:
                if tm[-2:] < '10':
                    $ r1 = 'b'
                elif tm[-2:] < '20':
                    $ r1 = 'c'
                elif True:
                    $ r1 = 'd'
                $ kira.dress_inf = {'b':'04a', 'c':'04b', 'd':'00'}[r1]
            $ renpy.show('Kira bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1)
            show FG bathroom-morning-00
            if r1=='b':
                Max_07 "Странно, что тётя Кира в полотенце... Она же любит везде посверкать своими почти голыми прелестями! Наверно, не проснулась ещё толком, а за кадром ещё и Лиза принимает душ!"
            elif r1=='c':
                Max_03 "Здорово, тётя Кира в одних трусиках любуется собой, а за кадром ещё и Лиза принимает душ! Отпадные у неё сиськи, люблю эти аппетитные сосочки..."
            elif True:
                Max_06 "Голая тётя Кира - это шикарно, а за кадром ещё и Лиза принимает душ! Ей нужно в кино играть роковых красоток, с такой-то внешностью и фигурой..."

        elif r0 == 2:

            if lisa.dress_inf != '04a':
                $ r1 = {'04c':'a', '02c':'c', '00':'d', '00a':'d'}[lisa.dress_inf]
            elif True:
                if tm[-2:] < '10'  and 'bathrobe' in lisa.gifts:
                    $ r1 = 'a'
                elif tm[-2:] < '20':
                    $ r1 = 'c'
                elif True:
                    $ r1 = 'd'
                $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[r1]

            $ renpy.show('Lisa bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1)
            show FG bathroom-morning-00
            if r1 == 'a':
                Max_03 "Лиза смотрится в подаренном мною халатике очень соблазнительно... Особенно когда так хорошо видно её упругие сисечки, а за кадром ещё и тётя Кира принимает душ!"
            elif r1=='c':
                Max_07 "Моя обворожительная сестрёнка в одних трусиках... Так и хочется зайти и стянуть их с её прекрасной попки, а за кадром ещё и тётя Кира принимает душ!"
            elif True:
                Max_06 "Утро может быть действительно очень добрым, если удаётся полюбоваться совершенно голенькой Лизой, а за кадром ещё и тётя Кира принимает душ!"
        elif True:

            $ renpy.show('Lisa bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1, at_list=[ladder_left_shift,])
            $ renpy.show('Kira bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1, at_list=[ladder_right_shift,])
            show FG bathroom-morning-00
            if r1=='c':
                Max_05 "Отлично, сегодня Лиза с тётей Кирой вместе! Красуются перед зеркалом в одних трусиках... Это просто заглядение!"
            elif True:
                Max_06 "Ухх, невероятно горячие и голенькие тётя с моей младшей сестрёнкой! Любовался бы бесконечно, как они красуются перед зеркалом..."

        if looked_ladder():
            $ house[3].max_cam = 2
            Max_07 "Мои зрители явно пропускают много всего интересного! Мне однозначно стоит установить сюда ещё одну камеру..."
        Max_00 "Ладно, хорошего понемногу, а то ещё заметит меня здесь кто-нибудь..."
        jump kira_lisa_shower.end

    label kira_lisa_shower.start_peeping:
        $ Skill('hide', 0.03)

        scene Kira shower-Lisa 01
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Отлично! Лиза вместе с тётей Кирой сегодня оказались в одно и то же время в душе... Очень соблазнительно!"
            "{i}продолжить смотреть{/i}" if True:
                pass
            "{i}взглянуть со стороны{/i}" if True:
                jump kira_lisa_shower.alt_peepeng
            "{i}уйти{/i}" if True:
                jump kira_lisa_shower.end

        $ spent_time += 10
        $ r1 = renpy.random.randint(1, 6)
        $ _m1_kira__r2 = renpy.random.randint(1, 6)
        scene BG shower-closer
        $ renpy.show('Kira shower-closer 0'+str(_m1_kira__r2), at_list=[left_shift,])
        $ renpy.show('Lisa shower-closer 0'+str(r1), at_list=[right_shift,])
        show FG shower-closer
        Max_04 "Эти две киски такие мокрые... Глаз не оторвать! Ну и как в этом доме не быть извращенцем?!"
        jump kira_lisa_shower.end

    label kira_lisa_shower.alt_peepeng:
        $ spent_time += 10
        $ lisa.dress_inf = '00aa'
        $ kira.dress_inf = '00a'
        $ r1 = renpy.random.randint(1, 6)
        $ _m1_kira__r2 = renpy.random.randint(1, 6)
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Lisa shower-alt 0'+str(_m1_kira__r2), at_list=[alt_left_shift,])
        $ renpy.show('Kira shower-alt 0'+str(r1), at_list=[alt_right_shift,])
        show FG shower-water
        Max_04 "Эти две киски такие мокрые... Глаз не оторвать! Ну и как в этом доме не быть извращенцем?!"
        jump kira_lisa_shower.end

    label kira_lisa_shower.end:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time += 10
        jump Waiting


label kira_alice_shower:
    $ renpy.dynamic('r0', 'r1')
    scene location house bathroom door-morning
    if alice.daily.shower > 0:
        menu:
            Max_00 "Кира и Алиса принимают душ, не стоит им мешать..."
            "{i}уйти{/i}" if True:
                return
    $ alice.daily.shower = 1
    menu:
        Max_01 "Интересно, кто сейчас в душе?"
        "{i}заглянуть со двора{/i}" if True:
            jump kira_alice_shower.start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump kira_alice_shower.ladder
        "{i}уйти{/i}" if True:
            return

    label kira_alice_shower.ladder:
        $ Skill('hide', 0.03)
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."

        if 'alice_sh' in cam_flag:
            $ r0 = 1 if tm[-2:] < '30' else 2
            $ kira.flags.ladder += 1
        elif 'kira_sh' in cam_flag:
            $ r0 = 2 if tm[-2:] < '30' else 1
            $ alice.flags.ladder += 1
        elif 'kira_alice_sh' in cam_flag:
            $ r0 = 0
            $ kira.flags.ladder += 1
            $ alice.flags.ladder += 1
        elif True:
            $ r0 = renpy.random.randint(1, 4)
            if r0 < 3:
                $ _m1_kira__var = 'alice' if r0 == 1 else 'kira'
                if _m1_kira__var == 'alice':
                    $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'alice_sh')
                elif True:
                    $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'kira_sh')
            elif True:
                $ _m1_kira__var = 'kira_alice'
        scene BG bathroom-morning-00
        if r0 == 1:
            if 'kira_sh' in cam_flag:
                $ r1 = {'04a':'b', '04b':'c', '00':'d', '00a':'d'}[kira.dress_inf]
            elif True:
                if tm[-2:] < '10':
                    $ r1 = 'b'
                elif tm[-2:] < '20':
                    $ r1 = 'c'
                elif True:
                    $ r1 = 'd'
                $ kira.dress_inf = {'b':'04a', 'c':'04b', 'd':'00'}[r1]

            $ renpy.show('Kira bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1)
            show FG bathroom-morning-00
            if r1=='b':
                Max_07 "Странно, что тётя Кира в полотенце... Она же любит везде посверкать своими почти голыми прелестями! Наверно, не проснулась ещё толком, а за кадром ещё и Алиса принимает душ!"
            elif r1=='c':
                Max_03 "Здорово, тётя Кира в одних трусиках любуется собой, а за кадром ещё и Алиса принимает душ! Отпадные у неё сиськи, люблю эти аппетитные сосочки..."
            elif True:
                Max_06 "Голая тётя Кира - это шикарно, а за кадром ещё и Алиса принимает душ! Ей нужно в кино играть роковых красоток, с такой-то внешностью и фигурой..."

        elif r0 == 2:
            if alice.dress_inf != '04aa':
                $ r1 = {'04ca':'a', '04da':'b', '02fa':'c', '00a':'d'}[alice.dress_inf]
            elif True:
                if tm[-2:] < '10':
                    $ r1 = 'a'
                elif tm[-2:] < '20':
                    $ r1 = 'c'
                elif True:
                    $ r1 = 'd'
                $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[r1]
            $ renpy.show('Alice bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1)
            show FG bathroom-morning-00
            if r1=='a':
                Max_02 "Может Алиса и в халатике, но сиськи её видны просто замечательно, а за кадром ещё и тётя Кира принимает душ!"
            elif r1=='c':
                Max_04 "Алиса сегодня без халатика... в одних трусиках... Гдядя на эту красоту, можно мечтать лишь об одном, а за кадром ещё и тётя Кира принимает душ!"
            elif True:
                Max_06 "Алиса сегодня совершенно голая! И даже не представляет, что тем самым дарит мне возможность любоваться всеми её прелестями, а за кадром ещё и тётя Кира принимает душ!"
        elif True:

            $ r1 = renpy.random.choice(['c', 'd', 'c', 'd', 'c', 'd'])
            $ renpy.show('Alice bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1, at_list=[ladder_left_shift,])
            $ renpy.show('Kira bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1, at_list=[ladder_right_shift,])
            show FG bathroom-morning-00
            if r1=='c':
                Max_05 "Класс, две самые непослушные девчонки этого дома вместе! Так изящно позируют перед зеркалом... Глаза аж разбегаются!"
            elif True:
                Max_06 "О да, сегодня тётя Кира и Алиса зажигают своими голыми попками перед зеркалом! Это можно прировнять к новому чуду света..."

        if looked_ladder():
            $ house[3].max_cam = 2
            Max_07 "Мои зрители явно пропускают много всего интересного! Мне однозначно стоит установить сюда ещё одну камеру..."
        Max_00 "Ладно, хорошего понемногу, а то ещё заметит меня здесь кто-нибудь..."
        jump kira_alice_shower.end

    label kira_alice_shower.start_peeping:
        $ Skill('hide', 0.03)

        scene Kira shower-Alice 01
        $ renpy.show('FG shower 00'+mgg.dress)
        menu:
            Max_07 "Ого... Две очень плохие девочки сегодня моются вместе... тётя Кира и Алиса! Как же они хороши..."
            "{i}продолжить смотреть{/i}" if True:
                pass
            "{i}взглянуть со стороны{/i}" if True:
                jump kira_alice_shower.alt_peepeng
            "{i}уйти{/i}" if True:
                jump kira_alice_shower.end

        $ spent_time += 10
        $ r1 = renpy.random.randint(1, 6)
        $ _m1_kira__r2 = renpy.random.randint(1, 6)
        scene BG shower-closer
        $ renpy.show('Kira shower-closer 0'+str(_m1_kira__r2), at_list=[left_shift,])
        $ renpy.show('Alice shower-closer 0'+str(r1), at_list=[right_shift,])
        show FG shower-closer
        Max_02 "О, да... Поскользить чем-нибудь между их сисечками было бы невероятно круто!"
        jump kira_alice_shower.end

    label kira_alice_shower.alt_peepeng:
        $ spent_time += 10
        $ alice.dress_inf = '00aa'
        $ kira.dress_inf = '00a'
        $ r1 = renpy.random.randint(1, 6)
        $ _m1_kira__r2 = renpy.random.randint(1, 6)
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Alice shower-alt 0'+str(_m1_kira__r2), at_list=[alt_left_shift,])
        $ renpy.show('Kira shower-alt 0'+str(r1), at_list=[alt_right_shift,])
        show FG shower-water
        Max_03 "Да-а-а... Вот бы оказаться между двумя этими мокрыми попками... Я бы уж их помылил!"
        jump kira_alice_shower.end

    label kira_alice_shower.end:
        $ current_room, prev_room = prev_room, current_room
        $ spent_time += 10
        jump Waiting


label return_from_club:


    scene BG char Kira after-club-pull
    show Kira after-club 00

    Kira_03 "Алиса, тише... Все уже спят! Нужно тихо, тихо, тихо... О... Макс? А ты почему не спишь?!"
    Max_02 "Да что-то не спится..."

    if not alice.daily.drink:

        Kira_05 "Это зря... Надо спать... Мы вот с Алисой тоже собираемся спать... Конечно, не вместе... Хотя... Она такая классная!"
        Max_07 "Кажется, кто-то пьян..."
        Alice_02 "Ага, еле дотащила её. А ведь она сильная. Ещё и сопротивляется! Хотела в какой-то другой ночной клуб пойти, продолжить тусить... Еле отговорила!"
        Max_08 "А ты трезва?"
        Alice_05 "Конечно, Макс! Ты же знаешь, что я не пью. Да и нужно было кому-то приглядывать за тётей Кирой. Она очень любит развлекаться, да так, что стыдно рассказать..."
        Max_07 "И что было?"
        Kira_07 "Ой, Макс... Чего только не было... И стриптизёры, и стриптиз... И я даже..."
        Max_08 "Что?"
        Alice_06 "А вот это уже не обязательно рассказывать. Я как вспомню, краснеть от стыда начинаю. Скажу лишь, что стриптиз танцевала тётя Кира, а остальное совсем не для твоих ушей..."
        Max_03 "Ого... Я всё пропустил!"
        Kira_06 "Точно! Нужно будет взять Макса с собой в следующий раз!"
        Max_04 "Я только за!"
        menu:
            Alice_03 "Не сомневаюсь, Макс. Но всё, хватит разговоров. Я пойду переодену и уложу тётю Киру в гостиной, а ты иди в свою комнату и ложись спать. Пока!"
            "Давай лучше я уложу тётю Киру!" if kira.stat.blowjob:
                Alice_05 "Наверняка из-за момента, что её нужно переодеть, да? Какой же ты испорченный мальчишка, Макс!"
                Max_09 "Мне теперь и тёте любимой нельзя помочь без упрёков?! Может, это вы тут все испорченные, а я один адекватный. Тётя Кира, ты ведь не против, если я тебе помогу?"
                Kira_05 "Ой, Макс... Я просто не могу отказать такому галантному вниманию. Алиса, можешь гулять... Макс обо мне позаботится."
                Alice_12 "Ну как знаете! Мне и без этого есть чем заняться. Доброй ночи."
                menu:
                    Max_01 "Ага, доброй. Пойдём, тётя Кира, я тебя провожу..."
                    "{i}отвести тётю в гостиную{/i}" if True:
                        pass


                scene BG char Kira after-club-s01-f
                show Kira after-club s01

                Kira_02 "Должна сказать, Макс, я довольно неплохо иду... если учесть, сколько я выпила..."
                Max_02 "Да, но я тебя всё равно немного придержу, чтобы никаких казусов не вышло. Приятное платьице... на ощупь."
                Kira_05 "Да, я его обожаю... Оно так классно облегает мои формы! Никто не остаётся равнодушным... к моей попке... за которую ты меня так мило придерживаешь."
                Max_04 "Так удобнее всего тебя направлять... А может расскажешь сейчас, что там ты за стриптиз устроила?"


                scene BG char Kira after-club-s02-f
                show Kira after-club s02

                Kira_07 "Зачем рассказывать, Макс, когда можно показать?! Присаживайся, если хочешь посмотреть это шоу..."
                Max_05 "Ого! Такого поворота событий я не ожидал!"
                jump return_from_club.striptease

            "Ну, ладно... Пока!" if not _in_replay:
                jump Sleep
    elif True:

        Kira_05 "И правильно! Такая ночь, как тут спать... Мы вот с Алисой отлично провели время. Оказывается, твоя старшая сестрёнка умеет зажигать!"
        Max_03 "Ого. Рассказывайте, что было?"


        show Kira after-club 00a

        Kira_07 "Скажу по секрету... Это касается трусиков Алисы! Но это секрет, так ведь?"
        Alice_05 "Именно! И Макса мы в это посвящать не будем... К тому же даже сама тётя Кира сейчас без трусиков!"
        Max_04 "Какие пикантные секреты!"
        Kira_02 "Так, Макс, я отправляюсь спать. Проводишь меня до дивана?"
        Alice_06 "Эй, а как же я?! Я хочу принять ванну перед сном, а у меня полотенце наверху! Вдруг я упаду, пока буду подниматься..."
        Max_07 "Я принесу тебе полотенце, как только уложу тётю Киру спать. Идёт?"
        menu:
            Alice_12 "Только давай быстрее!"
            "{i}Дать Алисе конфету и отвести тётю в гостиную{/i}" if _in_replay or kol_choco > 0:
                $ alice.daily.drink = 2
                $ give_choco()
                Max_01 "Вот, держи конфетку, чтобы не скучать, пока я с тётей..."
                Alice_02 "Ой, спасибо, это я люблю, Макс. На ночь лучше, конечно, сладости не есть, но разок можно. Ничего плохого не случится. Всё, жду полотенце..."


                scene BG char Kira after-club-s01-f
                show Kira after-club s01

                Kira_02 "Должна сказать, Макс, я довольно неплохо иду... если учесть, сколько я выпила..."
                Max_02 "Да, но я тебя всё равно немного придержу, чтобы никаких казусов не вышло. Приятное платьице... на ощупь."
                Kira_05 "Да, я его обожаю... Оно так классно облегает мои формы! Никто не остаётся равнодушным... к моей попке... за которую ты меня так мило придерживаешь."
                Max_04 "Так удобнее всего тебя направлять... А может расскажешь сейчас, что там ты за стриптиз устроила?"


                scene BG char Kira after-club-s02-f
                show Kira after-club s02

                menu:
                    Kira_07 "Зачем рассказывать, Макс, когда можно показать?! Присаживайся, если хочешь посмотреть это шоу..."
                    "Такого поворота событий я не ожидал! Можно и задержаться..." if True:
                        jump return_from_club.striptease
                    "Я бы задержался, но нужно проверить, как там Алиса..." if not _in_replay:

                        jump alice_after_club.knock
            "{i}Отвести тётю в гостиную{/i}" if True:


                scene BG char Kira after-club-s01-f
                show Kira after-club s01

                Kira_02 "Должна сказать, Макс, я довольно неплохо иду... если учесть, сколько я выпила..."
                Max_02 "Да, но я тебя всё равно немного придержу, чтобы никаких казусов не вышло. Приятное платьице... на ощупь."
                Kira_05 "Да, я его обожаю... Оно так классно облегает мои формы! Никто не остаётся равнодушным... к моей попке... за которую ты меня так мило придерживаешь."
                Max_04 "Так удобнее всего тебя направлять... А может расскажешь сейчас, что там ты за стриптиз устроила?"


                scene BG char Kira after-club-s02-f
                show Kira after-club s02

                menu:
                    Kira_07 "Зачем рассказывать, Макс, когда можно показать?! Присаживайся, если хочешь посмотреть это шоу..."
                    "Такого поворота событий я не ожидал! Можно и задержаться..." if True:
                        jump return_from_club.striptease
                    "Я бы задержался, но нужно проверить, как там Алиса..." if not _in_replay:

                        jump alice_after_club.knock

    label return_from_club.striptease:


        scene BG char Kira after-club-s03-f
        show Max after-club s03
        $ renpy.show("Kira after-club s03-"+renpy.random.choice(['01', '02', '03']))

        Kira_02 "А вот твой дружок уже отреагировал на то, как я приспустила платье... Я постараюсь, чтобы ты наслаждался каждой секундой этого стриптиза."
        Max_06 "Я просто нереально рад, что у меня такая потрясающая тётя!"


        scene BG char Kira after-club-s04-f
        show Max after-club s04
        $ renpy.show("Kira after-club s04-"+renpy.random.choice(['01', '02', '03']))

        Kira_04 "Ох! Кажется, я забыла надеть трусики, когда отправилась в клуб... И как же такое могло со мной произойти?!"
        Max_02 "Всё, что не делается - делается к лучшему! Забыла и забыла, я совсем не против..."


        scene BG char Kira after-club-s05-f
        show Max after-club s05
        $ renpy.show("Kira after-club s05-"+renpy.random.choice(['01', '02', '03']))

        Kira_07 "Тебе нравится, как я двигаюсь? Уверена, ты уже представил, как эта попка с жаром прыгает на твоём огромном члене! Ухх, я и сама начинаю намокать от этих мыслей..."
        Max_03 "Так может стоит в самом деле немного попрыгать перед сном?"

        if kira.dcv.feature.stage < 6:


            $ renpy.show("Kira after-club s05-"+renpy.random.choice(['04', '05']))

            Kira_10 "О да, звучит очень заманчиво, Макс! Но у меня так сильно начала кружиться голова! Похоже, я сегодня немного перебрала с алкоголем... Мне лучше прилечь."
            Max_07 "Конечно, тётя Кира, ложись... Значит, никакого продолжения не будет?"


            scene BG tv-mass-03
            show Kira tv-game cun-00bb

            Kira_14 "Боюсь, это не закончится ничем хорошим! Может быть в следующий раз..."
            Max_08 "Вот облом! Ладно, отдыхай и в следующий раз так много не пей. Доброй ночи, тётя Кира."
            menu:
                Kira_02 "Я постараюсь. Приятных снов, Макс."
                "{i}отправиться спать{/i}" if True:
                    $ renpy.end_replay()
                    $ current_room = house[0]
                    jump Sleep
                "{i}принести Алисе полотенце{/i}" if alice.daily.drink and not _in_replay:
                    jump alice_towel_after_club



        $ kira.sleepnaked = True
        $ added_mem_var('strip.show')


        scene BG char Kira after-club-s05-f
        show Max after-club s05
        $ renpy.show("Kira after-club s05-"+renpy.random.choice(['04', '05']))

        Kira_05 "О да, звучит очень заманчиво, Макс! Но этой ночью я хочу дать тебе выбор... как закончится мой стриптиз... И это будет сложный выбор! Ты же не против, если мы снимем твои шорты?"
        Max_04 "Конечно! Мне уже нравится, к чему всё идёт..."


        scene BG char Kira after-club-s06-f
        show Kira after-club s06

        menu:
            Kira_07 "Выбирай с умом, Макс, потому что ты получишь лишь что-то одно! Я могу обласкать твой член либо грудью, либо попкой. Как ты хочешь, чтобы я это сделала?"
            "Хочу грудью!" if True:


                scene BG char Kira after-club-s07b-f
                show Kira after-club s07b

                Kira_02 "Ты уверен, что хочешь именно так? Может, мне стоит немного покрутить этой роскошной попкой, чтобы ты понял, что теряешь сегодня?"
                menu:
                    Max_07 "Ухх, чёрт! Тётя Кира, когда ты так красиво это делаешь, выбор и правда становится очень сложным!"
                    "Но я всё равно хочу твою грудь!" if True:

                        scene BG char Kira after-club-s07a-f
                        show Kira after-club s07a

                        Kira_05 "Значит, всё-таки хочешь эти сисечки, да, большой мальчик? И я не могу тебя за это винить! Я знаю, какой это был непростой для тебя выбор. Надеюсь, тебе понравится..."
                        Max_05 "Мне с самого начала это нравится всё больше и больше!"


                        scene BG char Kira after-club-s08a-f
                        show Kira after-club s08a

                        jump return_from_club.boobs
                    "Я не могу устоять перед твоей попкой. Хочу её!" if True:


                        scene BG char Kira after-club-s07a-f
                        show Kira after-club s08b
                        Kira_05 "Значит, всё-таки хочешь эту попку, да, большой мальчик? И я не могу тебя за это винить! Я знаю, какой это был непростой для тебя выбор. Надеюсь, тебе понравится..."
                        Max_05 "Мне не переставало это нравится самого начала. И чем дальше, тем больше!"
                        jump return_from_club.ass
            "Хочу попкой!" if True:



                scene BG char Kira after-club-s07a-f
                show Kira after-club s07a

                Kira_02 "Ты уверен, что хочешь именно так? Может, мне стоит немного покрутить этой роскошной грудью перед твоим лицом, чтобы ты понял, что теряешь сегодня?"
                menu:
                    Max_07 "Ухх, чёрт! Тётя Кира, когда ты так красиво это делаешь, выбор и правда становится очень сложным!"
                    "Но я всё равно хочу твою попку!" if True:


                        scene BG char Kira after-club-s07b-f
                        show Kira after-club s07b

                        Kira_05 "Значит, всё-таки хочешь эту попку, да, большой мальчик? И я не могу тебя за это винить! Я знаю, какой это был непростой для тебя выбор. Надеюсь, тебе понравится..."
                        Max_05 "Мне не переставало это нравится самого начала. И чем дальше, тем больше!"


                        scene BG char Kira after-club-s07a-f
                        show Kira after-club s08b

                        jump return_from_club.ass
                    "Я не могу устоять перед твоей грудью. Хочу её!" if True:


                        scene BG char Kira after-club-s08a-f
                        show Kira after-club s08a
                        Kira_05 "Значит, всё-таки хочешь эти сисечки, да, большой мальчик? И я не могу тебя за это винить! Я знаю, какой это был непростой для тебя выбор. Надеюсь, тебе понравится..."
                        Max_05 "Мне с самого начала это нравится всё больше и больше!"
                        jump return_from_club.boobs

    label return_from_club.boobs:
        Kira_06 "Ого! Похоже, наши с тобой размеры идеально совпали! Ну как, тебе нравятся ощущения, Макс? Нравится, как я это делаю? Или хочешь быстрее?"
        Max_06 "Да-а-а, у тебя такая большая и нежная грудь! Обалденные ощущения! Главное, не останавливайся и продолжай..."


        scene BG char Kira after-club-s09a-f
        show Kira after-club s09a

        Kira_09 "Ох, я чувствую, что твоему дружку очень приятно находится в такой тесной компании моих девочек! Он пульсирует всё горячее..."
        Max_20 "{i}( Я без ума от этих сисек! Такие мягкие и большие... Она двигается всё быстрее и мне хочется начать хорошенько трахать её между них... Но что-то не так... ){/i}"


        scene BG char Kira after-club-s08a-f
        show Kira after-club s10a

        Kira_10 "Ой, Макс, у меня так сильно начала кружиться голова! Похоже, я сегодня немного перебрала с алкоголем... Мне нужно немного передохнуть и мы продолжим, хорошо?"
        Max_08 "Ну ладно. А ты уверена, что сможешь? Эээ... Тётя Кира? Заснула... И похоже, что крепко. Ну какой же это облом! Нужно уложить её на диван, пусть отдыхает."


        $ kira.dress = 'b'
        scene BG char Kira lounge-night-02
        $ renpy.show('Kira sleep-closer night '+pose3_4+kira.dress)

        menu:
            Max_01 "{i}Надеюсь, мама не будет сильно её осуждать за то, что она легла спать голая... С кем не бывает! А хороша тётя, так и гипнотизирует своей красотой. Но пора и мне спать...{/i}"
            "{i}отправиться спать{/i}" if True:
                $ renpy.end_replay()
                $ current_room = house[0]
                jump Sleep

            "{i}принести Алисе полотенце{/i}" if alice.daily.drink>1 and not _in_replay:
                jump alice_towel_after_club

    label return_from_club.ass:
        Kira_06 "О да! Твой член так плотно там поместился! Ну как, тебе нравятся ощущения, Макс? Нравится, как я это делаю? Или хочешь быстрее?"
        Max_06 "Да-а-а, у тебя такая шикарная и упругая попка! Непередаваемые ощущения! Главное, не останавливайся и продолжай..."


        scene BG char Kira after-club-s09b-f
        show Kira after-club s09b

        Kira_09 "Ох, я чувствую, что твоему дружку очень приятно находится в такой тесной компании моих ягодиц! Он пульсирует всё горячее..."
        Max_20 "{i}( Эта попка просто чумовая! Как же приятно она трётся... двигается всё быстрее! Мне хочется взять и хорошенько оттрахать её сзади... Но что-то не так... ){/i}"


        scene BG char Kira after-club-s04-f
        show Kira after-club s10b

        Kira_10 "Ой, Макс, у меня так сильно начала кружиться голова! Похоже, я сегодня немного перебрала с алкоголем... Мне нужно немного передохнуть и мы продолжим, хорошо?"
        Max_08 "Ну ладно. А ты уверена, что сможешь? Эээ... Тётя Кира? Заснула... И похоже, что крепко. Ну какой же это облом! Нужно уложить её на диван, пусть отдыхает."


        $ kira.dress = 'b'
        scene BG char Kira lounge-night-02
        $ renpy.show('Kira sleep-closer night '+pose3_4+kira.dress)

        menu:
            Max_01 "Надеюсь, мама не будет сильно её ругать за то, что она легла спать голая... Со всеми может случиться! А хороша тётя, так и гипнотизирует своей красотой. Но пора и мне спать..."
            "{i}отправиться спать{/i}" if True:
                $ renpy.end_replay()
                $ current_room = house[0]
                jump Sleep

            "{i}принести Алисе полотенце{/i}" if alice.daily.drink and not _in_replay:
                jump alice_towel_after_club


label kira_bath_with_eric:
    scene location house bathroom door-evening
    if kira.daily.bath != 0:
        return

    $ kira.daily.bath = 1
    menu:
        Max_01 "Только один человек может в это время не спать и плескаться в ванне. И человек этот - Кира!"
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            scene BG bath-00

            if renpy.random.randint(1, 2):
                show Eric bath-kira hj01
            elif True:
                show Eric bath-kira lick01
            show FG bath-00

            if kira.dcv.battle.stage > 2:
                Max_08 "Конечно, почему бы среди ночи не сходить в ванную, когда тебя там будет ждать шикарная тётя Кира, чтобы отсосать..."
            elif True:
                Max_01 "Наверно, тётя Кира хотела прийти с работы и отдохнуть, а тут ещё и Эрику нужно отсосать сперва..."


            $ spent_time += 10


            if renpy.random.randint(1, 2):
                show Eric bath-kira bj01
            elif True:
                show Eric bath-kira bj02
            if kira.dcv.battle.stage > 2:
                Max_10 "Хватит уже трахать её в рот, как какую-то порнозвезду! Она конечно порнозвезда, но не круглые же сутки..."
            elif True:
                Max_07 "Неплохо так Эрик её голову на свой член напяливает! Как будто так и надо..."


            $ spent_time += 10


            show Eric bath-kira cum01
            if kira.dcv.battle.stage > 2:
                menu:
                    Max_09 "Вот же сволочь! Спустил всё до последней капли Кире прямо в рот! Ну Эрик, ты у меня сполна получишь рано или поздно..."
                    "{i}уйти{/i}" if True:
                        pass
            elif True:
                menu:
                    Max_02 "Кира не упустила ни единой капли мимо! И как будто никто ни у кого только что смачно не отсасывал... Чистая работа!"
                    "{i}уйти{/i}" if True:
                        pass
        "{i}уйти{/i}" if True:

            pass


    $ spent_time += 10
    jump Waiting
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
