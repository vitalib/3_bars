import json
import haversine
import argparse

def load_data_from_json_file(filepath):
    with open(filepath) as json_file:
        return json.load(json_file)

def fetch_bars_from_json(json_dict):
    return json_dict['features']

def sorting_by_seats_criteria(bar):
    return bar['properties']['Attributes']['SeatsCount']

def get_biggest_bar(bars):
    return max(bars, key=sorting_by_seats_criteria)

def get_smallest_bar(bars):
    return min(bars, key=sorting_by_seats_criteria) 

def get_closest_bar(bars, longitude, latitude):
    from_point = (longitude, latitude)
    get_dest_point = lambda bar: bar['geometry']['coordinates']
    closest_bar = min (
			    	bars, 
			    	key=lambda bar: haversine.haversine(
                                            from_point,
                                            get_dest_point(bar)
			    							)
    )
    return closest_bar

def print_bar_info(bar, additional_info=''):
    print(additional_info)
    for attr in ('Name', 'Address', 'PublicPhone', 'SeatsCount'):
        print(attr, ':', bar['properties']['Attributes'][attr])
    print()


def get_filepath():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args().filepath
    

def main():
    filename = get_filepath()
    bars_raw = load_data_from_json_file(filename)
    bars_list = fetch_bars_from_json(bars_raw)
    smallest_bar = get_smallest_bar(bars_list)
    biggest_bar = get_biggest_bar(bars_list)
    print_bar_info(smallest_bar, 'Smallest bar:')
    print_bar_info(biggest_bar, 'Biggest bar:')
    user_gps = (float(num) for num in 
                    input('Please input yr gps coordinates: ').split())
    closest = get_closest_bar(bars_list, *user_gps)
    print_bar_info(closest, 'The closest bar for you is: ')

if __name__ == '__main__':
    main()
