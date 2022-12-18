import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from hw_12.loader.utils import save_picture
from hw_12.functions import add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# отображение страницы добавления поста
@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


# страница добавления поста
@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return "Ошибка. Нет картинки или текста"

    if picture.filename.split('.')[-1] not in ['jpeg', 'png', 'jpg']:
        logging.info('Загруженный файл не картинка')
        return 'Ошибка. Неверное расширение файла'

    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Ошибка. Файл не найден'
    except JSONDecodeError:
        return 'Ошибка. Невалидный файл'
    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
