<h1 align="center">Инструкция по запуску тестов</h1>

* Перед дальнейшими действиями проверьте, установлены ли gimp, vlc, vim в системе. Если нет, то их необходимо заинсталлировать.
* Шаг 1
    ```bash
    # Установка дополнительного пакета
    su - 
    echo "rpm [p8] http://ftp.altlinux.org/pub/distributions/ALTLinux/ p8/branch/x86_64 classic" >> /etc/apt/sources.list.d/altsp.list
    apt-get update
    apt-get install xorg-xvfb
    exit (or) su - officer
    ```
* Шаг 2
    * Если officer и root имеют права sudo, то переходим к следующему пункту. Иначе:
    ```bash
    su - 
    vim /etc/sudoers
    # Далее в редакторе добавляем следующие строчки
    officer ALL=(ALL) ALL
    root ALL=(ALL) ALL
    # Сохраняем изменения в файла и переходим обратно к сессии пользователя officer
    exit (or) su - officer
    ```
* Шаг 3
    * Переходим по [ссылке](https://bootstrap.pypa.io/get-pip.py) и сохраняем файл.
    * Открываем терминал и переходим при помощи команды cd в раздел с сохраненным файлом get-pip.py
    ```bash
    python3 get-pip.py
    # После успешной установки удаляем файл
    sudo rm get-pip.py
    ```
    * [Скачиваем архив](https://ngit.ivk.ru/mnaumov/system-testing) нашего репозитория и разархивируем его.
    * В терминале переходим в папку разархивированного репозитория.
    * Прописываем следующие команды:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```
* Шаг 4
    ```bash
    # Открываем необходимый файл
    vim testSuite_1_1/testCases/TestCase_1419.py
    ```
    * Изменяем 7-ю строчку: вместо PUT HERE SUDO PASSWORD FOR OFFICER прописываем свой пароль от officer (например, 'qwerty' ). 
        Кавычки необходимо оставить!
    * Запускаем все тесты одной командой. Будьте внимательны, после ключа --html необходимо указать свой путь для сохранения отчета о выполнении теста.
    ```bash
    sudo venv/bin/python3 -m pytest -q --tb=no --html=/your/path/makehtml.html testSuite_1_1/testCases/TestCase*.py
    ```
    * В итоге будет сгенерирован html документ с результатами прогона тестов.
    
