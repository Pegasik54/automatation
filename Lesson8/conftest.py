import pytest
import requests
from constants import X_client_URL

@pytest.fixture()
def get_token(username='musa', password='music-fairy'):
	log_pass = {'username': username, 'password': password}
	resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
	token = resp_token.json()['userToken']
	return token