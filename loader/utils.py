# сохранение картинки в папку uploads PyCharm
def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path
