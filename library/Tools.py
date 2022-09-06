class Tools:
    def get_not_archived_thread(self, response):
        i = 0
        while response.json()['data']['children'][i]['data']['archived']:
            i = i + 1
        return response.json()['data']['children'][i]['data']['name']

    def get_fullname_post(self, response):
        url = response.json()['jquery'][10][3][0]
        fullname_post = 't3_' + url.rsplit('/')[6]
        return fullname_post
