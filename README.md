# Анимированное окно с отскакивающими объектами

Этот проект представляет собой простую программу на Python, которая создает анимированное графическое окно с использованием библиотеки `tkinter`. Программа отображает два движущихся объекта, которые отскакивают от краев окна, создавая динамичный визуальный эффект.

## Описание

Программа использует объектно-ориентированный подход для создания структурированного и легко расширяемого кода. Основные компоненты программы включают:

*   **Базовый класс движущихся объектов:**
    *   Этот класс обеспечивает общую функциональность для любого объекта, который должен перемещаться на экране.
    *   Он отвечает за загрузку изображения объекта, его отображение и перемещение.

*   **Класс отскакивающих объектов:**
    *   Этот класс наследует функциональность от базового класса и добавляет логику отскока от краев окна.
    *   Он определяет, когда объект достигает границы экрана, и меняет направление его движения.

*   **Основной класс приложения:**
    *   Этот класс управляет всем приложением, включая создание окна, установку фона, создание объектов и запуск анимационного цикла.

## Логика работы

1.  Программа создает окно заданного размера и устанавливает фоновое изображение.
2.  На фоне окна создаются два объекта, которые начинают движение.
3.  Программа циклически обновляет положение объектов, вызывая метод, который:
    *   Перемещает объект.
    *   Проверяет, не достиг ли объект границ экрана.
    *   При достижении границы меняет направление движения объекта.
4.  Циклический вызов метода обновления обеспечивает анимацию движения.

## Ключевые идеи

*   **Наследование:** Класс отскакивающих объектов расширяет возможности базового класса, повторно используя существующий код.
*   **Анимация:** Анимация достигается путем циклического обновления положения объектов на экране.
*   **Объектно-ориентированное программирование:** Использование классов делает код более организованным и легким для понимания и расширения.

## Как запустить

1.  Убедитесь, что у вас установлен Python и библиотека `tkinter`.
2.  Скопируйте код в файл с расширением `.py`.
3.  Запустите файл через командную строку или IDE.

## Заключение

Эта программа является примером простой анимации, которая демонстрирует, как можно создавать динамичные визуальные эффекты в Python, используя `tkinter` и принципы ООП. Она может служить отправной точкой для более сложных проектов анимации и игр. 

## Идеи для танков:
1. Создать новый класс танков которые например будут быстрее, маленькие, но хрупкие. Или громоздкие, малоподвижные, но бронебойные и тд.
2. Создать пару пользовательских карт имеющих свои механики и особенности.
3. Создать мультиплеер для игры с друзьями.
4. Создать меню, для преукрашивания игры.

