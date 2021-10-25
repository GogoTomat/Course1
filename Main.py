import requests, json, time, os

VK_USER_ID = 187510320
VK_TOKEN = '81427859f64a01b9f0c3eeafa27ed72191b8746f08f10e434166416976eabd03e7bf7662079961061f536'


def get_foto_data(offset=0, count=50):
    api = requests.get("https://api.vk.com/method/photos.getAll", params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'offset': offset,
        'count': count,
        'photo_sizes': 0,
        'v': 5.103
    })
    return json.loads(api.text)


def get_foto():
    data = get_foto_data()
    count_foto = data["response"]["count"]
    i = 0
    count = 50
    fotos = []
    while i <= count_foto:
        if i != 0:
            data = get_foto_data(offset=i, count=count)
        for files in data["response"]["items"]:
            file_url = files["sizes"][-1]["url"]
            filename = file_url.split("/")[-1]
            fotos.append(filename)
            time.sleep(0.1)
            api = requests.get(file_url)

            with open("images/%s" % filename, "wb") as file:
                file.write(api.content)
        print(i)
        i += count
    print(len(fotos))


def main():
    get_foto()


if __name__ == "__main__":
    main()



