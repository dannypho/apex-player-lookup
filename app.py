from flask import Flask, render_template, request

app = Flask(__name__)

PLATFORMS = ["PC", "PS4", "Xbox"]

@app.route("/")
def index():
    return render_template("index.html", platforms=PLATFORMS)

@app.route("/search")
def search():
    ea_id = request.args.get("ea_id", )
    platform = request.args.get("platform")

    if not ea_id and platform is not None:
        return render_template("error.html", platforms=PLATFORMS, invalid_input=True, selected_platform=platform)
    elif not ea_id:
        return render_template("error.html", platforms=PLATFORMS, invalid_input=True)
    elif platform is None:
        return render_template("error.html", platforms=PLATFORMS, ea_id=ea_id, invalid_button=True)

    return render_template("search.html", platforms=PLATFORMS, ea_id=ea_id, selected_platform=platform)

if __name__ == "__main__":
    app.run(debug=True)

# import requests
# import json

# # Returns a dict of the top three highest topPercent values corresponding to the three legends
# def get_top_legends_percent(legends_dictionary):
#     temp_dict = {}
#     top_legends = {}

#     for legend, value in legends_dictionary.items():
#         # If you haven't played a legend in a long time, the dictionary will not have the 'data' key
#         if 'data' in value:
#             topPercent = value['data'][0]['rank']['topPercent']
#             # There is a chance the topPercent's value is a str 'NOT_CALCULATED_YET'
#             if isinstance(topPercent, float):
#                 temp_dict[legend] = topPercent
    
#     if len(temp_dict) < 3:
#         return 'Not enough data'
#     else:
#         temp_list = sorted(temp_dict.items(), key=lambda x: x[1])
#         while len(temp_list) != 3:
#             temp_list.pop()
    
#     top_legends = dict(temp_list)
#     return top_legends

# # Returns a dict of the top three most important stats
# def get_top_total_stats(total_stats):
#     top_total_stats = {}

#     if len(total_stats) == 0:
#         return 'Not enough data'
#     elif len(total_stats) < 3:
#         return 'Not enough data'
#     else:
#         counter = 0
#         for value in total_stats.values():
#             if counter == 3:
#                 break
#             temp_list = list(value.items())
#             top_total_stats[temp_list[0][1]] = temp_list[1][1]
#             counter = counter + 1

#     return top_total_stats

# API_key = 'b8f9106490e9b1ccbdebd1a26535a231'

# response = requests.get(f'https://api.mozambiquehe.re/bridge?auth={API_key}&player=PhoDanny&platform=PC').json()
# parsed_response = json.dumps(response, indent=3)

# all_legends = response['legends']['all']
# parsed_legends = (json.dumps(all_legends, indent=3))

# total_stats = response['total']
# parsed_total_stats = (json.dumps(total_stats, indent=3))

# print(parsed_response)


