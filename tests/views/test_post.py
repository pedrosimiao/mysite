# import json

import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    # import pdb
    # pdb.set_trace()
    # response.content = json.loads(response.content)

    assert (response.content == b"Hello World")


    # b'\n        '
    #         b'<!DOCTYPE html>\n        '
    #         b'<html>\n        '
    #         b'<head>\n            '
    #         b'<title>Django Views - Modulo 8</title>\n        '
    #         b'</head>\n        '
    #         b'<body>\n            '
    #         b'<div style="\n                '
    #         b'margin: 64px auto;\n                p'
    #         b'adding-top: 32px;\n                '
    #         b'width: 420px; \n                '
    #         b'height: 240px; \n                '
    #         b'background-color: #e3e3e3; \n                '
    #         b'opacity: 0.5; \n                '
    #         b'border-radius: 16px; \n                '
    #         b'border: 4px groove #000;\n                '
    #         b'display: flex;\n                '
    #         b'flex-direction: column;\n                '
    #         b'align-items: center\n            '
    #         b'">\n                    '
    #         b'<h1>Hello, World!</h1>\n                    '
    #         b'<h3>Welcome to the Django!</h3>\n            '
    #         b'</div>\n        '
    #         b'</body>\n        '
    #         b'</html>\n        ')