define config.name = _('Твоя судьба')

define config.version = "1.0"

define gui.about = _("Created by PyTom.\n\nHigh school backgrounds by Mugenjohncel.")
define default_name = "Егор Крид"
define e = Character(default_name)

image eileen happy = "это.png" # Убедитесь, что этот файл существует
# Добавьте фоновое изображение
image bg room = "images/моксва.jpg" # Замените на путь к вашему локальному фону
image bg bathroom = "ванна2.jpg" # Определяем фон ванной
image bg cafe = "кафе2.jpg"
image bg hoho = "дом.webp" # Определяем фон дома
image shaman = "шаман.png"
image kallen = "Remove-bg.ai_1729358445143.png"
image ulit = "прогулка.jpg"
image new_character_portrait = "df4150bc68c8bef335414fd6c416598f.png"
image ужас = "страх.jpg"


label start:
    play music "Egor_Krid_-_Budilnik_31096222.mp3"
    $ renpy.music.set_volume(0.5) # Установить громкость музыки на 50%
    show bg room with fade # Показать фон с эффектом fade
    show eileen happy # Показать изображение персонажа

    e "Доброе утро, моя принцесса."
    jump choose_name

label choose_name:
    e "Как тебя зовут?"
    $ player_name = renpy.input("Введите ваше имя:") # Ввод имени игрока
    $ player_name = player_name.strip() # Удаляем лишние пробелы

    # Если имя пустое, используем имя по умолчанию
    if not player_name:
        $ player_name = default_name

    menu:
        "Посмотреть вокруг":
            player_name "Я посмотрела в его глаза. Сбылась моя мечта."

        "Встала с кровати":
            player_name "Неудобная была ночка, фух."
            jump open_door

        "Обнять Егора Крида":
            player_name "Я в шоке, я обнимаю самого Егора Крида."
            e "А что тебя удивляет?"
            player_name "Да просто жизнь дала мне тебя"
            jump look_window

    e "У тебя такое прекрасное имя."
    player_name "Спасибо, очень приятно."
    e "Как ты относишься к тому, чтобы пойти в кафе?"
    player_name "Да, давай сходим, дорогой."

label up_bed:
    menu:
        "Пойти умыться.":
            show bg bathroom with fade # Показать фон ванной с эффектом fade
            jump go_right
        "Пойти в кафе.":
            show bg cafe with fade # Показать фон кафе с эффектом fade
            jump go_left

label open_door:
    player_name "Я встал(а) и открыл(а) дверь в другуюю комнату."
    player_name "Какой прекрасный день!"
    e "Это правда, давай выйдем на улицу?"
    player_name "Я не против, только мне нужно собраться!"
    e "Конечно, я подожду тебя"



    menu:
        "Пойти в ванную.":
            jump go_right
        "Сходить до подруги.":
            jump go_left
        "Пойти к шаману.":
            stop music
            play music "Shaman_-_Mojj_bojj_76390332.mp3"
            jump go_home

label look_window:
    player_name "Егор, я думаю, нам надо поехать навестить шамана."
    e "Классная идея!!!"
    player_name "Он наверное сейчас на работе хехехе."
    e "Я тоже так думаю, но лучше давай пока полежим"

    menu:
        "Остаться в кровати.":
         player_name "Что-то лень вставать с кровати, но до ванной сходить всё же надо."
         jump go_right
        "Пойти приготовиить поесть":
         player_name "Ты хочешь чего-нибудь покушать."
         e "Да, поэтому угощу тебя в кафе"
         "Вы быстром шагом пошли до кафе"
         jump go_left

label go_right: # Исправлено: добавлено двоеточие
    player_name "Вы встали и пошли до ванной."
    player_name "Нужно привести себя в порядок я думаю."
    player_name "Перед вами стоит выбор?"

    menu:
        "Продолжать умываться.":
            player_name "Вы продолжили заниматься делами!"
            player_name "Сначала приду в себя и осмыслю всё сделаннное"
            e "Ты там долго ещё?"
            player_name "Сейчас выхожу"
            jump end_game

        "Позвонить подруге в ванной и похвастаться Егором Кридом":
            hide bg room
            show bg bathroom with fade
            player_name "БРОООО, Я ТУТ С КРИДОМ"
            define new_name= Character("Подруга")
            new_name"Чего, как ты там оказалась?"
            player_name "Я сама этого не понмю, но мне это нравится"
            new_name "Можно я приеду с сфоткаюсь с ним?"
            player_name "Лучше не надо разглашать"
            jump go_game

label go_game:
    menu:
        "Выйти из ванной и пойти в кафе.":
            hide bathroom
            show bg room with fade
            player_name "Я всё, теперь можно полежать!"
            e "Пошли лучше в кафе??"
            player_name "Ну давай думаю"
            jump end_game

        "Остаться дома и посмотреть фильм ":
            hide bathroom
            show ужас with fade
            player_name "Какой фильм посмотрим?"
            e "Какой хочешь, но я больше люблю страшилки.."
            player_name "Давай Проклятье Аннабель?"
            e "АХХАХАХ, хорошо, только вот он вобще не страшный"
            player_name "Ты потом возьмёшь свои слова обратно"
            stop music
            play music "sekret-strashnye-zvuki.mp3"
            e "Чето реально страшно, пошли в кафе"
            jump go_left

label go_left:
    stop music
    play music "Egor_Krid_-_Samaya-samaya_47834988 (mp3cut.net).mp3"
    hide ужас
    show bg cafe with fade
    e "Вы вместе собрались и пошли в кафе."
    hide eileen happy
    show kallen with fade
    player_name "Я вижу Эдварда Каллина, стоп, а кто это с ним?!"
    e "Это его жена - Бэлла, она прекрасна, не будем на них зацикливаться."
    player_name "Ты прав, пошли дальше"
    show eileen happy with fade
    e "Давай закажу нам кофе)"
    jump go_choice

label go_choice:
    menu:
        "Заказать кофе за свой счёт.":
            player_name "Блин, скоро так обонкрочусь!"
            show eileen happy with fade
            e "Пошли погуляем?"
            player_name "Конечно"
            jump end_game

        "Дождаться пока оплатит он":
            player_name "Спасибо, очень приятно)"
            show eileen happy with fade
            e "Пошли погуляем?"
            player_name "Конечно"
        "Выйти на улицу":
            jump go_street

label go_street:
    hide kallen
    show ulit with fade
    player_name "Такая классная погода"
    show eileen happy with fade
    e "Согласен, такая романтика"
    player_name "Конечно"
    show eileen happy with fade
    e "Давай по пути заскочим к шаману"
    player_name "Давай попробуем"
    jump go_home

label go_home:
    stop music
    play music "Shaman_-_Mojj_bojj_76390332.mp3"
    hide ulit
    show bg hoho with fade # Добавьте эту строку
    show shaman with fade
    player_name "Я вижу его в жизни, омайгад!"
    define new_character = Character("Шаман")
    hide shaman
    define new_leps = Character("Григорий Лепс")
    new_character "Привет! Я лучший исполнитель в мире!"
    show это with fade
    e "Что-то ты немного перепутал"
    show shaman with fade
    new_character "В каком смысле?!"
    show это with fade
    e "Послушай мои треки и узнаешь"
    player_name "Мальчики, не ругайтесь!!"
    show new_character_portrait with fade
    play music "Grigorijj_Leps_-_YA_podnimayu_ruki_73041063 (mp3cut.net).mp3"
    new_leps "Замолкните малявки!"
    show new_character_portrait
    menu:
        "Пожать руку.":
            e "Здравствуйте, вы очень классный исполнитель!!"
            play music "Я согласшусь с Кридом"
            new_character "Ойойойо, ну и идите к своему Лепсу, я ушел"
            jump end_game

        "Сказать насколько классные у него песни.":
            e "Мне нравится ваше творчество."
            jump end_game


label end_game:
    return
