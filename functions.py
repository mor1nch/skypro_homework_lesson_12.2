import json


# загрузка json файла
def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


# поиск постов по слову
def get_posts_by_word(word: str) -> list[dict]:
    result = []
    posts = load_posts()
    for post in posts:
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


# добавление нового поста
def add_post(post: dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
