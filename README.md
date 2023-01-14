<h1 align="center">Проект по тестированию приложения Wikipedia</h1>

&#8287;&#8287;&#8287;&#8287;&#8287;
## :open_book: Содержание:
- [Технологии и инструменты](#gear-проект-реализован-с-использованием)
- [Что проверяем](#heavy_check_mark-описание)
- [Запуск тестов из Jenkins](#-запуск-тестов-из-jenkins)
- [Запуск тестов из терминала](#computer-запуск-тестов-из-терминала)
- [Тестовые артефакты](#movie_camera-тестовые-артефакты)

&#8287;&#8287;&#8287;&#8287;&#8287;
## :gear: Проект реализован с использованием
  <p align="center">
    <img src="/README/icons/python.svg" title="Python" width="50" height="50"  alt="python"/>
    <img src="/README/icons/pycharm.svg" title="Pycharm" width="50" height="50"  alt="pycharm"/>
    <img src="/README/icons/pytest.svg" title="Pytest" width="50" height="50"  alt="pytest"/>
    <img src="/README/icons/selene.png" title="Selene" width="50" height="50"  alt="selene"/>
    <img src="/README/icons/appium.svg" title="Appium" width="50" height="50"  alt="appium"/>
    <img src="/README/icons/browserstack.svg" title="Browserstack" width="50" height="50"  alt="browserstack"/>
    <img src="/README/icons/selenoid.svg" title="selenoid" width="50" height="50"  alt="selenoid"/>
    <img src="/README/icons/jenkins.svg" title="Jenkins" width="50" height="50"  alt="jenkins"/>
    <img src="/README/icons/github.svg" title="Github" width="50" height="50"  alt="github"/>
 </p>


&#8287;&#8287;&#8287;&#8287;&#8287;
## :heavy_check_mark: Описание
Реализованы простые проверки функционала приложения. Запуск тестов осуществляется в Jenkins. По выбору можно запустить либо через browserstack либо в эмуляторе. 
Выбор осуществляется с помошью переменных окружения.


&#8287;&#8287;&#8287;&#8287;&#8287;
## <img src="/README/icons/jenkins.svg" width="50" height="50"  alt="jenkins"/> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/002_Clorhexidinum_diploma_python/)
  
  Для запуска тестов из Jenkins

  <p>1. Необходимо нажать кнопку "Собрать с параметрами".</p>
  
  <p>2. Выбрать параметры.</p>
  
  <p>3. Нажать кнопку "Собрать"</p>
  
&#8287;&#8287;&#8287;&#8287;&#8287;
## :computer: Запуск тестов из терминала

Для локального запуска необходимо выполнить команду:
```
pytest *test_folder*
```
  
&#8287;&#8287;&#8287;&#8287;&#8287;
## :movie_camera: Тестовые артефакты

В результате прохождения тестов собираются следующие артефакты:
  
  <p>Скриншот страницы</p>

  <p>Дамп страницы</p>

  <p>Видео прохождения</p>
  
