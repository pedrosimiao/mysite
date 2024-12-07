#import json

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

    assert response.content == b'\n        <!DOCTYPE html>\n        <html>\n        <head>\n            <title>Django Views - Exerc\xc3\xadcio M\xc3\xb3dulo 8</title>\n        </head>\n        <body>\n            <div style="\n                margin: 0 auto;\n                width: 360px; \n                height: 360px; \n                background-color: #e3e3e3; \n                opacity: 0.5; \n                border-radius: 16px; \n                border: 2px groove #e3e3e3;">\n                    # <h1>Hello, World!</h1>\n                    # <p>Welcome to the Django!</p>\n            </div>\n        </body>\n        </html>\n        '