import requests
import json

# Returns a dict of the top three highest topPercent values corresponding to the three legends
def get_top_legends_percent(response):
    temp_dict = {}
    top_legends = {}

    legends_dictionary = response['legends']['all']

    for legend, value in legends_dictionary.items():
        # If you haven't played a legend in a long time, the dictionary will not have the 'data' key
        if 'data' in value:
            topPercent = value['data'][0]['rank']['topPercent']
            # There is a chance the topPercent's value is a str 'NOT_CALCULATED_YET'
            if isinstance(topPercent, float):
                temp_dict[legend] = topPercent
    
    if len(temp_dict) < 3:
        error = {}
        error['Error'] = "Not enough data"
        return error
    else:
        temp_list = sorted(temp_dict.items(), key=lambda x: x[1])
        while len(temp_list) != 3:
            temp_list.pop()
    
    top_legends = dict(temp_list)
    return top_legends

# Returns a dict of the top three most important stats
def get_top_total_stats(response):
    top_total_stats = {}

    total_stats = response['total']

    if len(total_stats) == 0:
        error = {}
        error['Error'] = "Not enough data"
        return error
    elif len(total_stats) < 3:
        error = {}
        error['Error'] = "Not enough data"
        return error
    else:
        counter = 0
        for value in total_stats.values():
            if counter == 3:
                break
            temp_list = list(value.items())
            top_total_stats[temp_list[0][1]] = temp_list[1][1]
            counter = counter + 1

    return top_total_stats

# Returns a dict of the player's rank and an image of the rank
def get_player_info(response):
    player_info = {}
    player_info['level'] = response['global']['level']
    player_info['rank'] = response['global']['rank']['rankName']
    player_info['rankImg'] = response['global']['rank']['rankImg']
    return player_info

def query_api(name, platform):
    API_key = 'b8f9106490e9b1ccbdebd1a26535a231'
    return requests.get(f'https://api.mozambiquehe.re/bridge?auth={API_key}&player={name}&platform={platform}').json()

if __name__ == "__main__":
    
    response = query_api("PhoDanny", "PC")
    topPercents = get_top_legends_percent(response)
    topTotalStats = get_top_total_stats(response)
    # print(json.dumps(topTotalStats, indent=3))
    # print(json.dumps(get_player_info(response), indent=3))
    print(json.dumps(response, indent=3))

