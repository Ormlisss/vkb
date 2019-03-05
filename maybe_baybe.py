import time

import vk_api

vk_session = vk_api.VkApi(
    token='38919655ffd62bcb2c98656c47e945cfc9f22194059caa3325cf1fb73adb6e5bc2b11351a5d41a76535f4')
vk = vk_session.get_api()


def comment_last_group_post(message='', group=1, count=1):
    last_post_id = vk.wall.get(owner_id=-group, count=1, offset=1)['items'][0]['id']
    for i in range(count):
        while True:
            post = vk.wall.get(owner_id=-group, count=1, offset=1)['items'][0]
            if post['id'] != last_post_id:
                vk.wall.createComment(owner_id=-group, post_id=post['id'], message=message)
                print(f'Оставил комментарий: "{message}" посту {id}'
                      f'Осталось оставить {count - i - 1} комментариев', sep='\n')
                break
            last_post_id = post['id']
            time.sleep(1)


if __name__ == '__main__':
    comment_last_group_post(message='упс', group=98699940)
