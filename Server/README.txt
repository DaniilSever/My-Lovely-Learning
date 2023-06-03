
Даниил: FrontEnd Developers
Николай: BackEnd Developers


Обозначение папок:

main_zone - Бек основных страниц
conditions_zone - Бек условий пользования и кофиденциальности
settings_zone - Бек настроек пользователя
my_course_zone - Бек страницы "мои курсы"
teachers_zone - Бек страницы "преподавателям"
edit_course_zone - Бек создания курсов

Server - Настройки сервака
api - Апишка сайта
compiler - компилятор


Логика сайта: 

	loading folders:

		main_zone
		
		Выбрали условия пользования и конфедициальности:
			conditions_zone
		Выбрали настройки:
			settings_zone
		Выбрали мои курсы:
			my_course_zone
		Выбрали преподавание:
			teachers_zone
			
			Выбрали создаение курсов
				edit_course_zone

	loading backends:
		
		Server
		compiler
		api
		

Изменять папки: 
	
	Можно: 
		Server
		settings_zone
		my_course_zone
		edit_course_zone
		compiler
		api

	Лучше не стоит без надобности:
		
		main_zone
		teachers_zone
		conditions_zone



			
