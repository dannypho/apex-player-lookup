from flask import Flask, render_template, request
from utils.api_helpers import query_api, get_player_info, get_top_legends_percent, get_top_total_stats

app = Flask(__name__)

PLATFORMS = ["PC", "PS4", "X1"]

@app.route("/")
def index():
    return render_template("index.html", platforms=PLATFORMS)

@app.route("/search")
def search():
    ea_id = request.args.get("ea_id")
    platform = request.args.get("platform")
    
    # Check if input is provided
    if not ea_id and platform is not None:
        return render_template("error.html", platforms=PLATFORMS, selected_platform=platform, invalid_input=True)
    elif not ea_id:
        return render_template("error.html", platforms=PLATFORMS, invalid_input=True)
    elif platform is None:
        return render_template("error.html", platforms=PLATFORMS, ea_id=ea_id, invalid_button=True)
    
    # Query the API to see if the user does not exist
    response = query_api(ea_id, platform)
    if 'Error' in response:
        return render_template("error.html", platforms=PLATFORMS, ea_id=ea_id, selected_platform=platform, invalid_user=True)
    
    player_info = get_player_info(response)
    top_legends = get_top_legends_percent(response)
    top_stats = get_top_total_stats(response)

    return render_template("search.html", platforms=PLATFORMS, ea_id=ea_id, selected_platform=platform, player_info=player_info, top_legends=top_legends, top_stats=top_stats)

if __name__ == "__main__":
    app.run(debug=True)


