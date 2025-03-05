# Демо проект по автоматизации сайта магазина товаров для животных "Petshop"
[![Лого](https://github.com/dfeoktistova/petshop_ru/blob/master/data/images/1.png)](https://www.petshop.ru/)

  
## Технологии и инструменты

<p align="center">
<a href="https://www.jetbrains.com/idea/"><img src="images/logo/Idea.svg" width="50" height="50"  alt="IDEA"/></a>
<a href="https://www.java.com/"><img src="images/logo/Java.svg" width="50" height="50"  alt="Java"/></a>
<a href="https://github.com/"><img src="images/logo/GitHub.svg" width="50" height="50"  alt="Github"/></a>
<a href="https://junit.org/junit5/"><img src="images/logo/Junit5.svg" width="50" height="50"  alt="JUnit 5"/></a>
<a href="https://gradle.org/"><img src="images/logo/Gradle.svg" width="50" height="50"  alt="Gradle"/></a>
<a href="https://selenide.org/"><img src="images/logo/Selenide.svg" width="50" height="50"  alt="Selenide"/></a>
<a href="https://aerokube.com/selenoid/"><img src="images/logo/Selenoid.svg" width="50" height="50"  alt="Selenoid"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="images/logo/Allure.svg" width="50" height="50"  alt="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="images/logo/Jenkins.svg" width="50" height="50"  alt="Jenkins"/></a>
<a href="https://qameta.io/"><img src="images/logo/Allure_TO.svg" width="50" height="50"  alt="Allure TestOps"/></a>  
<a href="https://www.atlassian.com/ru/software/jira/"><img src="images/logo/Jira.svg" width="50" height="50"  alt="Jira"/></a>  
</p>
В данном проекте содержатся UI, API и MOBILE автотесты, написанные на <code>Python</code>.

>
> <code>Selenoid</code> выполняет запуск браузеров в контейнерах <code>Docker</code>. Также проект предполагает возможность запуска тестов локально.
>
> Запуск автотестов выполняется или на своей локальной машине после копирования репозитория, или на сервере непрерывной интеграции <code>Jenkins</code>, который 
> развернут в облаке.
>
> После завершения прогона <code>Allure Report</code> формирует отчеты о запуске тестов.

## Покрытый функционал
### API

- [x] Добавление различных товаров в корзину
- [x] Удаление товаров из корзины
- [x] Запрос содержимого корзины
- [x] Запрос акционных предложений
- [x] Поиск по сайту

### UI

- [x] Тестирование информационных страниц сайта (информация о доставке, магазинах, акциях и программе лояльности)
- [x] Тестирование категорий товаров для собак
- [x] Тестирование категорий товаров для кошек

### MOBILE

- Тестирование начального экрана приложения "Petshop Выгул":
- [x] Пролистывание экранов с начальной информацией о возможностях приложения
- [x] Открытие контактов











## Содержание

<details>
<summary>Установка</summary>

### Клонирование репозитория

Для начала работы, клонируйте репозиторий и перейдите в директорию проекта:

   ```sh
    git clone https://github.com/dfeoktistova/petshop_ru.git # Клонировать репозиторий
    cd petshop_ru # Перейти в папку проекта
   ```

### Создание и запуск виртуального окружения

   ```sh
    python -m venv venv # Создать виртуальное окружение
    .\venv\Scripts\activate # Активировать созданное виртуальное окружение
   ```

### Установка зависимостей

   ```sh
     pip install -r requirements.txt  # Установить зависимости из файла requirements.txt
   ```
</details>



<details>
<summary>Запуск тестов</summary>

### Возможности

Тесты находятся в папке "tests" и разделены по следующим директориям, а также предполагают различный
способ запуска:
- api_tests (локально)
- mobile_tests (на локальном эмуляторе или в browserstack)
- ui_tests (локально или в контейнере selenoid)

Ключи для запуска тестов возможны следующие:
- browser_name (браузер, на котором будут запущены тесты)
- browser_version (версия браузера)
- context (среда для запуска мобильных тестов (browserstack/локальный эмулятор))
- ui_env (среда для запуска UI тестов (локальный запуск/selenoid))

```commandline
def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        choices=['chrome', 'firefox'],
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        choices=['99.0', '100.0', '113.0', '114.0', '120.0', '121.0', '122.0', '123.0', '124.0', '125.0', '126.0'],
        default='126.0'
    )
    parser.addoption(
        '--context',
        choices=['bstack', 'local_emulator'],
        default='local_emulator'
    )
    parser.addoption(
        '--ui_env',
        choices=['local', 'selenoid'],
        default='local'
    )
```

### Локальный запуск

Для локального запуска используется команда:

   ```sh
     pytest # Запуск всех тестов проекта
   ```

Если параметры запуска, рассмотренные в предыдущем разделе, не указаны, то тесты будут запущены
с дефолтными настройками (задаются в файле "conftest").

</details>


<details>
<summary>Allure отчеты</summary>

После тестового прогона сырые данные для отчета формируются в директории "alluredir", которая задается
в файле "pytest.ini".

Для формирования отчета необходимо использовать команду:
   ```sh
      allure serve allure-results # Сформировать отчет по результатам тестирования
   ```
где allure-results - заданная директория.

После этого в браузере будет открыт Allure отчет.

В каждом тесте есть необходимая информация для того, чтобы можно было сделать вывод о возникшей ошибке.
Запрос с параметрами/ответ, скриншоты, лог, видео и HTML страница:


![Allure](https://github.com/dfeoktistova/petshop_ru/blob/master/data/images/2.png))

Пример видео с прохождением UI-теста:

![Видео](https://github.com/dfeoktistova/petshop_ru/blob/master/data/images/allure_video.gif)


Пример видео с прохождением MOBILE-теста:

![Видео](https://github.com/dfeoktistova/petshop_ru/blob/master/data/images/mobile_video.gif)


</details>