# Тестовое задание по созданию сайта с тестами

Требования по функциональный части сервиса:
- Регистрация пользователей;
- Аутентификация пользователей;
- Зарегистрированные пользователи могут проходить любой из тестовых наборов;
- Последовательный ответ на все вопросы;
- После завершения тестирования возможность просмотра результатов, где указано количество правильных/неправильных ответов, а также процент правильных ответов.

Требования по админке:
- Стандартный раздел пользователей;
- Раздел с наборами тестов;
- Возможность на странице набора тестов добавлять вопросы/ответы к вопросам/отмечать правильные ответы;
- Валидация на то, что должен быть хотябы 1 правильный вариант, а также на то, что все варианты не могут быть правильными;
- Удаление вопросов/вариантов ответов/изменение правильных решений при редактировании тестового набора.

--------------------

  Для того, чобы удовлетворить требование вложенности, т.е. чтобы можно было редактировать не только название/содержание теста, но и вопросов и ответов была использована библиотека django-nested-admin, все необходимые библотеки указаны в файле requirements.txt. 
  Для обработки указываемых ответов в вопросах использовался js.
