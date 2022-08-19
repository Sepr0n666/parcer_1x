import requests


def get_game(result):
    for game in result["Value"]:
        game_id = game['I']
        champs = game['LI']

        params = {
            'sports': '1',
            'champs': champs,
            'count': '50',
            'tf': '2200000',
            'tz': '3',
            'mode': '4',
            'subGames': game_id,
            'country': '82',
            'partner': '78',
            'getEmpty': 'true',
        }

        response = requests.get('https://1xbet.kz/LineFeed/Get1x2_VZip', params=params)
        game_result = response.json()
        print(game_result)
        break


def main():
    url = "https://1xbet.kz/line/football/96463-germany-bundesliga"
    champs = url.split('/')[-1].split('-')[0]
    # print(champs)

    params = {
        'sports': '1',
        'champs': champs,
        'count': '50',
        'tf': '2200000',
        'tz': '3',
        'mode': '4',
        'country': '82',
        'partner': '78',
        'getEmpty': 'true',
    }

    response = requests.get('https://1xbet.kz/LineFeed/Get1x2_VZip', params=params)
    result = response.json()
    # print(result)
    get_game(result)


if __name__ == '__main__':
    main()
