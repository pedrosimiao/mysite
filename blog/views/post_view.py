from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Django Views - Exercício Módulo 8</title>
        </head>
        <body>
            <div style="
                margin: 0 auto;
                width: 360px; 
                height: 360px; 
                background-color: #e3e3e3; 
                opacity: 0.5; 
                border-radius: 16px; 
                border: 2px groove #e3e3e3;">
                    # <h1>Hello, World!</h1>
                    # <p>Welcome to the Django!</p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html_content, content_type="text/html")

