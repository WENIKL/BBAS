
label cam0_kira_sleep_night:
    $ renpy.show('Kira cams sleep night '+cam_poses_manager(kira, ['01', '02', '03'])+kira.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'kira_sleep' not in cam_flag:
        $ cam_flag.append('kira_sleep')
        Max_01 "Моя очаровательная тётя Кира спит..."
    return

label cam0_kira_sleep_morning:
    $ renpy.show('Kira cams sleep morning '+cam_poses_manager(kira, ['01', '02', '03'])+kira.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'kira_sleep' not in cam_flag:
        $ cam_flag.append('kira_sleep')
        Max_01 "Моя очаровательная тётя Кира спит..."
    return

label cam0_kira_shower:
    if tm[-2:] < '20' and kira.dress_inf != '00a':
        show FG cam-shum-noact at laptop_screen
        if 'kira_not_shower' not in cam_flag:
            $ cam_flag.append('kira_not_shower')
            if len(house[3].cams)>1:
                Max_09 "Киры не видно через эту камеру... Может посмотреть через другую?"
            elif True:
                Max_09 "Киры не видно через эту камеру..."
    elif True:
        $ kira.dress_inf = '00a'
        if 'kira_shower' not in cam_flag:
            $ _m1_kira_cam__pose = cam_poses_manager(kira, [x for x in range(1,9)])
        elif True:

            $ _m1_kira_cam__pose = cam_poses_manager(kira, [x for x in range(1,7)]) if _m1_kira_cam__pose < 7 else cam_poses_manager(kira, [7,8])

        $ renpy.show('Kira cams shower 0'+str(_m1_kira_cam__pose), at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            if _m1_kira_cam__pose < 7:
                Max_04 "За такой классной тётей, принимающей душ, будет преступлением не понаблюдать..."
            elif True:
                Max_05 "О да, тётя Кира! Потереть киску на камеру будет точно не лишним... Зрители будут в восторге."
    return

label cam1_kira_shower:
    if tm[-2:] < '20' and kira.dress_inf != '00a':

        if kira.daily.shower > 1 or 'kira_bath_mirror' in cam_flag:
            $ _m1_kira_cam__r1 = {'04a':'b', '02a':'c', '00':'d', '00a':'d'}[kira.dress_inf]
        elif True:
            $ _m1_kira_cam__r1 = renpy.random.choice(['b', 'c', 'd'])
            $ kira.dress_inf = {'b':'04a', 'c':'02a', 'd':'00'}[_m1_kira_cam__r1]

        $ _m1_kira_cam__pose = cam_poses_manager(kira, ['01', '02', '03'], 1) if _m1_kira_cam__r1 != 'd' else cam_poses_manager(kira, ['01', '02', '03', '04', '05'], 1)
        $ renpy.show('Kira cams bath-mirror '+_m1_kira_cam__pose+_m1_kira_cam__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_bath_mirror' not in cam_flag:
            $ cam_flag.append('kira_bath_mirror')
            if _m1_kira_cam__pose in ['01', '02', '03']:
                Max_03 "Тётя Кира красуется перед зеркалом. Полюбуемся..."
            elif True:
                Max_05 "Ого! А ей явно не хватает секса, раз она решила пошалить перед душем... А как красиво!"
    elif True:

        show FG cam-shum-noact at laptop_screen
        if 'kira_shower1' not in cam_flag:
            $ cam_flag.append('kira_shower1')
            Max_09 "Киры не видно через эту камеру... Может посмотреть через другую?"
    return

label cam0_kira_alice_shower:

    if 'alice_sh' in cam_flag:
        $ _m1_kira_cam__var = 'alice' if tm[-2:] < '30' else 'kira'
    elif 'kira_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira' if tm[-2:] < '30' else 'alice'
    elif 'kira_alice_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira_alice'
    elif True:
        $ _m1_kira_cam__var = renpy.random.choice(['alice', 'kira_alice', 'kira', 'kira_alice'])
        if _m1_kira_cam__var == 'alice':
            $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'kira_sh')
        elif _m1_kira_cam__var == 'kira':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'alice_sh')
        elif True:
            $ cam_flag.append('kira_alice_sh')

    if _m1_kira_cam__var == 'alice':

        $ renpy.show('Alice cams shower 0'+str(cam_poses_manager(alice, [x for x in range(1, 10)])), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'alice_shower' not in cam_flag:
            $ cam_flag.append('alice_shower')
            Max_04 "Старшая сестрёнка принимает душ... Это зрелище, которое никогда мне не надоест..."
            if 'kira_mirror' not in cam_flag:

                if len(house[3].cams)>1:
                    Max_09 "Киры не видно через эту камеру... Может посмотреть через другую?"
                elif True:
                    Max_09 "Киры не видно через эту камеру..."
    elif _m1_kira_cam__var == 'kira':

        $ renpy.show('Kira cams shower 0'+str(cam_poses_manager(kira, [x for x in range(1, 7)])), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_04 "За такой классной тётей, принимающей душ, будет преступлением не понаблюдать..."

            if 'alice_mirror' not in cam_flag:

                if len(house[3].cams)>1:
                    Max_09 "Алиса, должно быть, красуется перед зеркалом... Надо взглянуть через другую камеру..."
                elif True:
                    Max_09 "Алиса, должно быть, красуется перед зеркалом, но здесь этого не увидеть..."
    elif True:

        $ kira.dress_inf != '00a'
        $ alice.dress_inf != '00aa'
        $ renpy.show('Alice cams shower 0'+str(cam_poses_manager(alice, [x for x in range(1, 9)])), at_list=[cam_shower_right])
        $ renpy.show('Kira cams shower 0'+str(cam_poses_manager(kira, [x for x in range(1, 7)])), at_list=[cam_shower_left])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_07 "Ого... Две очень плохие девочки сегодня моются вместе... тётя Кира и Алиса! Как же они хороши..."

    return

label cam1_kira_alice_shower:

    if 'alice_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira' if tm[-2:] < '30' else 'alice'
    elif 'kira_sh' in cam_flag:
        $ _m1_kira_cam__var = 'alice' if tm[-2:] < '30' else 'kira'
    elif 'kira_alice_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira_alice'
    elif True:
        $ _m1_kira_cam__var = renpy.random.choice(['alice', 'kira_alice', 'kira', 'kira_alice'])
        if _m1_kira_cam__var == 'alice':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'alice_sh')
        elif _m1_kira_cam__var == 'kira':

            $ cam_flag.append('alice_sh' if tm[-2:] < '30' else 'kira_sh')
        elif True:
            $ cam_flag.append('kira_alice_sh')

    if _m1_kira_cam__var == 'kira':

        if tm[-2:] < '10' and kira.dress_inf != '00a':
            $ _m1_kira_cam__r1 = 'b'
        elif tm[-2:] < '20' and kira.dress_inf not in ['00a', '00']:
            $ _m1_kira_cam__r1 = 'c'
        elif True:
            $ _m1_kira_cam__r1 = 'd'
        $ kira.dress_inf = {'b':'04a', 'c':'02a', 'd':'00'}[_m1_kira_cam__r1]
        $ renpy.show('Kira cams bath-mirror '+cam_poses_manager(kira, ['01', '02', '03'], 1)+_m1_kira_cam__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_mirror' not in cam_flag:
            $ cam_flag.append('kira_mirror')
            Max_03 "Тётя Кира красуется перед зеркалом. Полюбуемся..."
    elif _m1_kira_cam__var == 'alice':

        if tm[-2:] < '10' and alice.dress_inf != '00aa':
            $ _m1_kira_cam__r1 = 'a'
        elif tm[-2:] < '20' and alice.dress_inf not in ['00a', '00aa']:
            $ _m1_kira_cam__r1 = 'c'
        elif True:
            $ _m1_kira_cam__r1 = 'd'
        $ alice.dress_inf = {'a':'04ca', 'b':'04da', 'c':'02fa', 'd':'00a'}[_m1_kira_cam__r1]
        $ renpy.show('Alice cams bath-mirror '+cam_poses_manager(alice, ['01', '02', '03'], 1)+_m1_kira_cam__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'alice_mirror' not in cam_flag:
            $ cam_flag.append('alice_mirror')
            Max_05 "Ух, старшая сестрёнка просто сногсшибательна..."
    elif True:
        show FG cam-shum-noact at laptop_screen
        if 'alice_shower1' not in cam_flag:
            $ cam_flag.append('alice_shower1')
            Max_09 "Через эту камеру никого не видно... Может посмотреть через другую?"

    return

label cam0_kira_lisa_shower:

    if 'lisa_sh' in cam_flag:
        $ _m1_kira_cam__var = 'lisa' if tm[-2:] < '30' else 'kira'
    elif 'kira_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira' if tm[-2:] < '30' else 'lisa'
    elif 'kira_lisa_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira_lisa'
    elif True:
        $ _m1_kira_cam__var = renpy.random.choice(['lisa', 'kira_lisa', 'kira', 'kira_lisa'])
        if _m1_kira_cam__var == 'lisa':
            $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'kira_sh')
        elif _m1_kira_cam__var == 'kira':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'lisa_sh')
        elif True:
            $ cam_flag.append('kira_lisa_sh')

    if _m1_kira_cam__var == 'lisa':

        $ lisa.dress_inf != '00a'
        $ renpy.show('Lisa cams shower 0'+str(cam_poses_manager(lisa, [x for x in range(1, 10)])), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'lisa_shower' not in cam_flag:
            $ cam_flag.append('lisa_shower')
            Max_04 "Младшая сестрёнка принимает душ... Прекрасная Лиза - прекрасное утро!"
            if 'kira_mirror' not in cam_flag:

                if len(house[3].cams)>1:
                    Max_09 "Киры не видно через эту камеру... Может посмотреть через другую?"
                elif True:
                    Max_09 "Киры не видно через эту камеру..."
    elif _m1_kira_cam__var == 'kira':

        $ renpy.show('Kira cams shower 0'+str(cam_poses_manager(kira, [x for x in range(1, 7)])), at_list=[laptop_screen,])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen

        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_04 "За такой классной тётей, принимающей душ, будет преступлением не понаблюдать..."
            if 'lisa_mirror' not in cam_flag:

                if len(house[3].cams)>1:
                    Max_09 "Лизы не видно через эту камеру... Может посмотреть через другую?"
                elif True:
                    Max_09 "Лизы не видно через эту камеру..."
    elif True:

        $ kira.dress_inf != '00a'
        $ lisa.dress_inf != '00a'
        $ renpy.show('Lisa cams shower 0'+str(cam_poses_manager(lisa, [x for x in range(1, 9)])), at_list=[cam_shower_right])
        $ renpy.show('Kira cams shower 0'+str(cam_poses_manager(kira, [x for x in range(1, 7)])), at_list=[cam_shower_left])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_shower' not in cam_flag:
            $ cam_flag.append('kira_shower')
            Max_07 "О как... Тётя и младшая сестрёнка сегодня моются вместе! Они офигенно хороши..."

    return

label cam1_kira_lisa_shower:

    if 'lisa_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira' if tm[-2:] < '30' else 'lisa'
    elif 'kira_sh' in cam_flag:
        $ _m1_kira_cam__var = 'lisa' if tm[-2:] < '30' else 'kira'
    elif 'kira_lisa_sh' in cam_flag:
        $ _m1_kira_cam__var = 'kira_lisa'
    elif True:
        $ _m1_kira_cam__var = renpy.random.choice(['lisa', 'kira_lisa', 'kira', 'kira_lisa'])
        if _m1_kira_cam__var == 'lisa':
            $ cam_flag.append('kira_sh' if tm[-2:] < '30' else 'lisa_sh')
        elif _m1_kira_cam__var == 'kira':

            $ cam_flag.append('lisa_sh' if tm[-2:] < '30' else 'kira_sh')
        elif True:
            $ cam_flag.append('kira_lisa_sh')

    if _m1_kira_cam__var == 'kira':

        if tm[-2:] < '10' and kira.dress_inf != '00a':
            $ _m1_kira_cam__r1 = 'b'
        elif tm[-2:] < '20' and kira.dress_inf not in ['00a', '00']:
            $ _m1_kira_cam__r1 = 'c'
        elif True:
            $ _m1_kira_cam__r1 = 'd'
        $ kira.dress_inf = {'b':'04a', 'c':'02a', 'd':'00'}[_m1_kira_cam__r1]
        $ renpy.show('Kira cams bath-mirror '+cam_poses_manager(kira, ['01', '02', '03'], 1)+_m1_kira_cam__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_mirror' not in cam_flag:
            $ cam_flag.append('kira_mirror')
            Max_03 "Тётя Кира красуется перед зеркалом. Полюбуемся..."
    elif _m1_kira_cam__var == 'lisa':

        if tm[-2:] < '10' and lisa.dress_inf != '00a' and 'bathrobe' in lisa.gifts:
            $ _m1_kira_cam__r1 = 'a'
        elif tm[-2:] < '20' and lisa.dress_inf not in ['00a', '00']:
            $ _m1_kira_cam__r1 = 'c'
        elif True:
            $ _m1_kira_cam__r1 = 'd'
        $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[_m1_kira_cam__r1]
        $ renpy.show('Lisa cams bath-mirror '+cam_poses_manager(lisa, ['01', '02', '03'], 1)+_m1_kira_cam__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'lisa_mirror' not in cam_flag:
            $ cam_flag.append('lisa_mirror')
            Max_03 "Лиза любуется собой перед зеркалом. И мы этим со зрителями тоже полюбуемся..."
    elif True:
        show FG cam-shum-noact at laptop_screen
        if 'kira_shower1' not in cam_flag:
            $ cam_flag.append('kira_shower1')
            Max_09 "Через эту камеру никого не видно... Может посмотреть через другую?"

    return

label cam0_kira_sun:
    $ renpy.show('Kira cams sun '+cam_poses_manager(kira, ['01', '02', '03', '04', '05', '06']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'kira_swim1' not in cam_flag:
        $ cam_flag.append('kira_swim1')
        Max_01 "Ух, тётя Кира загорает и радует нас всех своими соблазнительными формами..."
    return

label cam1_kira_sun:
    show FG cam-shum-noact at laptop_screen
    if 'kira_sun1' not in cam_flag:
        $ cam_flag.append('kira_sun1')
        Max_09 "Через эту камеру никого не видно... Может посмотреть через другую?"
    return

label cam0_kira_swim:
    show FG cam-shum-noact at laptop_screen
    if 'kira_swim0' not in cam_flag:
        $ cam_flag.append('kira_swim0')
        if len(house[6].cams)>1:
            Max_09 "Ничего толком не видно... Стоит взглянуть через другую камеру..."
        elif True:
            Max_09 "Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн..."
    return

label cam1_kira_swim:
    show BG-cam house courtyard-1 day at laptop_screen
    $ renpy.show('Kira cams swim day '+cam_poses_manager(kira, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_01 "Всегда приятно посмотреть, как тётя Кира расслабляется во дворе..."
    return

label cam0_kira_bath:
    if tm[-2:] < '10':

        show Kira cams bath 01 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_bath0_st0' not in cam_flag:
            $ cam_flag.append('kira_bath0_st0')
            Max_01 "Тётя Кира набирает воду. После долгого рабочего дня самое то принять ванну..."
    elif tm[-2:] > '40':

        show Kira cams bath 05 at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'kira_bath0_st1' not in cam_flag:
            $ cam_flag.append('kira_bath0_st1')
            Max_04 "Эх, тётя Кира уже вытирается, самое интересное позади. Почти..."
    elif True:
        $ renpy.show('Kira cams bath '+cam_poses_manager(kira, ['02', '03', '04']), at_list=[laptop_screen,])
        show FG cam-shum-act at laptop_screen
        if 'kira_bath0_st0' not in cam_flag:
            $ cam_flag.append('kira_bath0_st0')
            Max_05 "Так, руки на стол! Можно обжечься... ведь тётя Кира - огонь!"
    return

label cam1_kira_bath:
    show FG cam-shum-noact at laptop_screen
    if 'kira_bath1' not in cam_flag:
        $ cam_flag.append('kira_bath1')
        Max_09 "Через эту камеру никого не видно... Может посмотреть через другую?"
    return

label cam0_kira_night_tv:
    if tm[-2:] < '10':
        $ renpy.show('Kira cams tv '+cam_poses_manager(kira, ['01', '02', '03']), at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'kira_tv' not in cam_flag:
            $ cam_flag.append('kira_tv')
            if kira.flags.porno:
                Max_02 "Похоже, тётя Кира смотрит какой-то сериал или кино... Может, стоит составить ей компанию?"
            elif True:
                Max_01 "Похоже, тётя Кира смотрит какой-то сериал или кино... Ну а мне приятней смотреть на тётю..."
    elif kira.flags.porno:
        if 'kira_tv1' not in cam_flag:
            $ cam_flag.append('kira_tv1')
            $ _m1_kira_cam__pose = cam_poses_manager(kira, ['01', '02', '03'])
            $ renpy.show('Kira cams tv m-'+_m1_kira_cam__pose, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            Max_05 "Ага, тётя наверняка порнушку включила! Хотя, может ей стало просто скучно... Может, ей помочь?"
        elif True:
            $ renpy.show('Kira cams tv m-'+_m1_kira_cam__pose, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
    elif True:
        $ renpy.show('Kira cams tv '+cam_poses_manager(kira, ['01', '02', '03']), at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen

    return

label cam0_kira_night_swim:
    show FG cam-shum-noact at laptop_screen
    if 'kira_swim0' not in cam_flag:
        $ cam_flag.append('kira_swim0')
        if len(house[6].cams)>1:
            Max_09 "Ничего толком не видно... Стоит взглянуть через другую камеру..."
        elif True:
            Max_09 "Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн..."
    return

label cam1_kira_night_swim:
    $ renpy.show('Kira cams swim night '+cam_poses_manager(kira, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_swim1' not in cam_flag:
        $ cam_flag.append('ann_swim1')
        Max_05 "Класс! Тётя Кира решила ночью поплавать без купальника... пока никто не видит... Ну да, никто!"
    return

label cam0_return_from_club:
    show FG cam-shum-noact at laptop_screen
    if 'kira_return' not in cam_flag:
        $ cam_flag.append('kira_return')
        if len(house[6].cams)>1:
            Max_09 "Ничего толком не видно... Стоит взглянуть через другую камеру..."
        elif True:
            Max_09 "Ничего не разглядеть... Нужно установить камеру, которая охватила бы бассейн..."
    return

label cam1_return_from_club:
    show Kira cams after-club 01 at laptop_screen
    show FG cam-shum-noact at laptop_screen
    menu:
        Max_01 "{i}( Вот и девчонки вернулись из клуба! Если перед сном хочется поискать приключений, то нужно быстро бежать и встречать их... ){/i}"
        "{i}встретить их{/i}" if True:
            $ at_comp = False
            jump return_from_club
        "{i}отправиться спать{/i}" if True:

            Max_00 "Поздно уже, пойду лучше спать..."
            jump Sleep

label cam0_kira_bath_with_eric:

    if renpy.random.randint(1, 2):
        show Eric cams bath-kira hj01 at laptop_screen
    elif True:
        show Eric cams bath-kira lick01 at laptop_screen
    show FG cam-shum-act at laptop_screen
    if kira.dcv.battle.stage > 2:
        Max_08 "Бедной тёте Кире приходится ублажать Эрика, чтобы никто о нас с ней не узнал..."
    elif True:
        Max_01 "Повезло Эрику... Тётя Кира умеет ублажать мужчин и ещё как!"


    if renpy.random.randint(1, 2):
        show Eric cams bath-kira bj01 at laptop_screen
    elif True:
        show Eric cams bath-kira bj02 at laptop_screen
    if kira.dcv.battle.stage > 2:
        Max_10 "Благо у Эрика такой член, с которым Кире не составит труда справиться! Хотя, его выдержке можно позавидовать..."
    elif True:
        Max_07 "Со стороны кажется, что для Киры это самое обыденное дело! Она так легко управляется с членом Эрика, хотя это и не сложно, после моего-то..."


    if renpy.random.randint(1, 2):
        show Eric cams bath-kira cum01 at laptop_screen
    elif True:
        show Eric cams bath-kira cum02 at laptop_screen
    if kira.dcv.battle.stage > 2:
        Max_09 "Всё! На этот раз Кира отмучалась... Но от Эрика надо скорее избавляться."
    elif True:
        Max_02 "Вот и всё! С Кирой долго не продержишься... Особенно если она нацелена доставить своим языком максимум удовольствия."

    if 'kira_bath0_st0' not in cam_flag:
        $ cam_flag.append('kira_bath0_st0')
    $ spent_time = max((30 - int(tm[-2:])), 20)
    jump Waiting

label cam1_kira_bath_with_eric:
    show FG cam-shum-noact at laptop_screen
    if 'kira_bath1' not in cam_flag:
        $ cam_flag.append('kira_bath1')
        Max_09 "Через эту камеру никого не видно... Может посмотреть через другую?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
