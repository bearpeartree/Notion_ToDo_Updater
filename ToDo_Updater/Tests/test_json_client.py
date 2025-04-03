import pytest
from unittest.mock import patch
import sys
import os
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Infrastructure import notion_client
from Infrastructure import json_builder
from Appservice import todo_service

@patch('requests.patch')
@patch.dict(os.environ, {'NOTION_PAGE_ID': '1234'})
def test_post_new_week_success_200(mock_patch, mocker):
    # arrange
    response = mock_patch.return_value
    response.status_code = 200

    fake_service = mocker.patch("Appservice.todo_service")
    fake_jb = mocker.patch("Infrastructure.json_builder")
    fake_week = mocker.patch("Domain.Week")
    fake_json = mocker.patch("json.dumps")

    fake_service.create_new_week(6, 12, 2021).return_value = fake_week
    fake_json.return_value = "some_json"

    client = notion_client.notion_client(fake_service, fake_jb)
    
    # act
    result = client.post_new_week(1, 12, 2022)

    # assert
    assert result.status_code == 200
