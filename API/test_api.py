import allure
from APIPage import APIPage
import pytest


api = APIPage()


@allure.epic("API tests")
@allure.feature("Позитивные проверки")
@allure.title("Поиск по названию фильма")
@pytest.mark.test_api
def test_search_film_by_title():

    new_title = "The Beekeeper"
    response = api.search_film_by_title(new_title)
    assert response.status_code == 200
    assert response.json()["docs"][0]["alternativeName"] == new_title

@allure.epic("API tests")
@allure.feature("Позитивные проверки")
@allure.title("Поиск по имени актера")
@pytest.mark.test_api
def test_search_name_person():
    name_person = "Johnny Depp"
    response = api.search_name_person(name_person)
    assert response.json()["docs"][0]["enName"] == name_person
    assert response.status_code == 200


@allure.epic("API tests")
@allure.feature("Позитивные проверки")
@allure.title("Поиск фильма по id актера")
@pytest.mark.test_api
def test_search_film_person_id():
    person_id = 6245
    response = api.search_film_person_id(person_id)
    print(response)
    assert response.json()["docs"][0]["id"] == 6461896
    assert response.status_code == 200


@allure.epic("API tests")
@allure.feature("Негативные проверки")
@allure.title("Поиск по неверному id")
@pytest.mark.test_api
def test_search_wrong_id():
    wrong_id = "249"
    response = api.search_wrong_id(wrong_id)
    assert response.status_code == 400
    assert response.json()["error"] == "Bad Request"


@allure.epic("API tests")
@allure.feature("Негативные проверки")
@allure.title("Поиск несуществующего жанра")
@pytest.mark.test_api
def test_search_wrong_category():
    wrong_category = "небылица"
    response = api.search_wrong_category(wrong_category)
    assert response.status_code == 200
    assert response.json()["total"] == 0

