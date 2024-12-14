from django.views import generic

from blog.models.post import Post



class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"





# class PostView(generic.View):
#     def get(self, request, *args, **kwargs):
#         html_content = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>Django Views - Modulo 8</title>
#         </head>
#         <body>
#             <div style="
#                 margin: 64px auto;
#                 padding-top: 32px;
#                 width: 420px; 
#                 height: 240px; 
#                 background-color: #e3e3e3; 
#                 opacity: 0.5; 
#                 border-radius: 16px; 
#                 border: 4px groove #000;
#                 display: flex;
#                 flex-direction: column;
#                 align-items: center
#             ">
#                     <h1>Hello, World!</h1>
#                     <h3>Welcome to the Django!</h3>
#             </div>
#         </body>
#         </html>
#         """
#         return HttpResponse(html_content, content_type="text/html")

