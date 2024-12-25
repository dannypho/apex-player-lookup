import requests
import json

# Returns a dict of the top three highest topPercent values corresponding to the three legends along with their icon
def get_top_legends(response):
    legends_dictionary = response['legends']['all']
    temp_list = []

    for legend, value in legends_dictionary.items():
        # Check if the legend has data and valid topPercent
        if 'data' in value and isinstance(value['data'][0]['rank']['topPercent'], (float, int)):
            topPercent = value['data'][0]['rank']['topPercent']
            temp_list.append({
                'legend': legend,
                'topPercent': topPercent,
                'icon': value['ImgAssets']['icon']
            })

    # Sort legends by topPercent in ascending order
    temp_list = sorted(temp_list, key=lambda x: x['topPercent'])

    if len(temp_list) < 3:
        return {"Error": "Not enough data"}
    
    # Extract top three legends
    top_legends = temp_list[:3]
    return {legend['legend']: {'topPercent': legend['topPercent'], 'icon': legend['icon']} for legend in top_legends}

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

# Returns a dict of the player's name, rank and an image of the rank
def get_player_info(response):
    player_info = {}
    player_info['name'] = response['global']['name']
    player_info['level'] = response['global']['level']
    player_info['rank'] = response['global']['rank']['rankName']
    player_info['rankImg'] = response['global']['rank']['rankImg']
    return player_info

# Returns a str of the player's selected legend's banner
def get_selected_banner(response):
    selected_banner = response['legends']['selected']['ImgAssets']['banner']
    return selected_banner

# Returns a dict with the player's selected legend's name and correpsonding icon
def get_selected_legend(response):
    selected_legend = {}
    selected_legend['LegendName'] = response['legends']['selected']['LegendName']
    selected_legend['icon'] = response['legends']['selected']['ImgAssets']['icon']
    return selected_legend

# Returns a dict of player data
def query_api(name, platform):
    API_key = 'b8f9106490e9b1ccbdebd1a26535a231'
    return requests.get(f'https://api.mozambiquehe.re/bridge?auth={API_key}&player={name}&platform={platform}').json()

if __name__ == "__main__":
    
    response = query_api("awysz", "PC")
    topLegends = get_top_legends(response)
    topTotalStats = get_top_total_stats(response)
    playerInfo = get_player_info(response)
    selectedLegend = get_selected_legend(response)
    print(json.dumps(selectedLegend, indent=3))

