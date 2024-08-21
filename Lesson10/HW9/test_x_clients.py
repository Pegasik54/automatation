import pytest
import allure
from Employee import Employer
from DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудниов из БД и АПИ, сравниваем их")
@allure.feature("Тест №1")
def test_get_list_of_employers():
	with allure.step("БД - Создание компании"):
		db.create_company('Alexvill', 'good_company')
	with allure.step("БД - Получаем ID созданной компании"):
		max_id = db.last_company_id()
	with allure.step("БД - Добавляем сотрудника в компанию"):
		db.create_employer(max_id, "Alex", "Morozov", 8800882211)
	with allure.step("БД - Получаем список сотрудников из созданной компании"):
		db_employer_list = db.get_list_employer(max_id)
	with allure.step("АПИ - Получаем спиосок сотрудников из созданной компании"):
		api_employer_list = api.get_list(max_id)
	with allure.step("Сравниваем списки сотрудников из БД и АПИ"):
		assert len(db_employer_list) == len(api_employer_list)
	with allure.step("БД - Удаляем созданного сотрудника"):
		response = (api.get_list(max_id))[0]
	employer_id = response["id"]
	db.delete_employer(employer_id)
	with allure.step("БД - Удаляем последнюю созданную компанию"):
		db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудников")
@allure.description("Добавляем сотрудника в БД и сравниваем с АПИ имя, статус, фамилию")
@allure.feature("Тест №2")
def test_add_new_employer():
	with allure.step("БД - Создание компании"):
		db.create_company('Alex adding new employer', 'employer')
	with allure.step("БД - Получаем ID созданной компании"):
		max_id = db.last_company_id()
	with allure.step("БД - Добавляем сотрудника в компанию"):
		db.create_employer(max_id, "Alex", "Morozov", 8800882211)
	response = (api.get_list(max_id))[0]
	employer_id = response["id"]
	with allure.step("Сравниваем ID компании"):
		assert response["companyId"] == max_id
	with allure.step("Сравниваем имя сотрудника с заданным"):
		assert response["firstName"] == "Alex"
	with allure.step("Проверяем что статус сотрудника - True"):
		assert response["isActive"] == True
	with allure.step("Сравниваем фамилию сотрудника с заданной"):
		assert response["lastName"] == "Morozov"
	with allure.step("БД - Удаляем созданного сотрудника"):
		db.delete_employer(employer_id)
	with allure.step("БД - Удаляем последнюю созданную компанию"):
		db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Сравнение информации о сотруднике из АПИ с БД")
@allure.description("Сравнение информации о сотруднике из АПИ с информацией указанной при создании сотрудника В БД ")
@allure.feature("Тест №3")	
def test_assertion_data():
	with allure.step("БД - Создание компании"):
		db.create_company('Employer get id company', 'new')
	with allure.step("БД - Получаем ID созданной компании"):
		max_id = db.last_company_id()
	with allure.step("БД - Добавляем сотрудника в компанию"):
		db.create_employer(max_id, "Alex", "Morozov", 8800882211)
	with allure.step("БД - Записываем ID сотрудника в переменную"):
		employer_id = db.get_employer_id(max_id)
	with allure.step("Сравниваем полученную информацию из АПИ с информацией при создании сотрудника из БД"):
		get_api_info = (api.get_info(employer_id)).json()
	with allure.step("Сравниваем имя сотрудника с заданным"):
		assert get_api_info["firstName"] == "Alex"
	with allure.step("Сравниваем фамилию сотрудника с заданным"):
		assert get_api_info["lastName"] == "Morozov"
	with allure.step("Сравниваем телефон сотрудника с заданным"):
		assert get_api_info["phone"] == "8800882211"
	with allure.step("БД - Удаляем созданного сотрудника"):
		db.delete_employer(employer_id)
	with allure.step("БД - Удаляем последнюю созданную компанию"):
		db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Сравнение информации из АПИ с БД измененной")
@allure.description("Сравниваем информацию о сотруднике по АПИ с измененной информацией в БД")
@allure.feature("Тест №4")
def test_update_user_info():
	with allure.step("БД - Создание компании"):
		db.create_company('New updating company', 'test')
	with allure.step("БД - Получаем ID созданной компании"):
		max_id = db.last_company_id()
	with allure.step("БД - Добавляем сотрудника в компанию"):
		db.create_employer(max_id, "Alex", "Morozov", 8800882211)
	with allure.step("БД - Записываем ID сотрудника в переменную"):
		employer_id = db.get_employer_id(max_id)
	with allure.step("БД - Изменяем именя сотрудника"):
		db.update_employer_info("Vlad", employer_id)
	with allure.step("Сравниваем полученную информацию из АПИ с информацией при создании сотрудника из БД"):
		get_api_info = (api.get_info(employer_id)).json()
	with allure.step("Сравниваем имя сотрудника с заданным"):
		assert get_api_info["firstName"] == "Vladis"
	with allure.step("Сравниваем фамилию сотрудника с заданным"):
		assert get_api_info["lastName"] == "Morozov"
	with allure.step("Проверяем что статус сотрудника - True"):
		assert get_api_info["isActive"] == True
	with allure.step("БД - Удаляем созданного сотрудника"):
		db.delete_employer(employer_id)
	with allure.step("БД - Удаляем последнюю созданную компанию"):
		db.delete(max_id)