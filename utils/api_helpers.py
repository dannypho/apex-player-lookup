import requests
import json

# Returns a dict of the top three highest topPercent values corresponding to the three legends
def get_top_legends_percent(legends_dictionary):
    temp_dict = {}
    top_legends = {}

    for legend, value in legends_dictionary.items():
        # If you haven't played a legend in a long time, the dictionary will not have the 'data' key
        if 'data' in value:
            topPercent = value['data'][0]['rank']['topPercent']
            # There is a chance the topPercent's value is a str 'NOT_CALCULATED_YET'
            if isinstance(topPercent, float):
                temp_dict[legend] = topPercent
    
    if len(temp_dict) < 3:
        return 'Not enough data'
    else:
        temp_list = sorted(temp_dict.items(), key=lambda x: x[1])
        while len(temp_list) != 3:
            temp_list.pop()
    
    top_legends = dict(temp_list)
    return top_legends

# Returns a dict of the top three most important stats
def get_top_total_stats(total_stats):
    top_total_stats = {}

    if len(total_stats) == 0:
        return 'Not enough data'
    elif len(total_stats) < 3:
        return 'Not enough data'
    else:
        counter = 0
        for value in total_stats.values():
            if counter == 3:
                break
            temp_list = list(value.items())
            top_total_stats[temp_list[0][1]] = temp_list[1][1]
            counter = counter + 1

    return top_total_stats

def query_api(name, platform):
    API_key = 'b8f9106490e9b1ccbdebd1a26535a231'
    return requests.get(f'https://api.mozambiquehe.re/bridge?auth={API_key}&player={name}&platform={platform}').json()

if __name__ == "__main__":
    
    response = query_api("PhoDanny", "PC")

    # all_legends = response['legends']['all']
    # parsed_legends = (json.dumps(all_legends, indent=3))

    # total_stats = response['total']
    # parsed_total_stats = (json.dumps(total_stats, indent=3))

    if 'Error' in response:
        print("Error, player not found")
    else:
        print(response)

