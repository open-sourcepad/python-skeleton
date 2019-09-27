from .crud import Crud

class PostsApi(Crud):
    ROUTES = [
        { 'url': '/posts', 'function': 'index' },
        { 'url': '/posts', 'function': 'create' },
        { 'url': '/posts/<id>', 'function': 'show' },
        { 'url': '/posts/<id>', 'function': 'update' },
        { 'url': '/posts/<id>', 'function': 'delete' }
        ]
