import json
import haversine
import argparse


def load_data_from_json_file(filepath):
    with open(filepath) as json_file:
        return json.load(json_file)


def get_seats_in_bar(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_biggest_bar(bars):
    return max(bars, key=get_seats_in_bar)


def get_smallest_bar(bars):
    return min(bars, key=get_seats_in_bar)


def get_closest_bar(bars, longitude, latitude):
    from_point = (longitude, latitude)
    closest_bar = min(
        bars,
        key=lambda bar: haversine.haversine(
                                from_point,
                                bar['geometry']['coordinates']
                                )
        )
    return closest_bar


def print_bar_info(bar, additional_info=''):
    print(additional_info)
    for attr in ('Name', 'Address', 'SeatsCount'):
        print(attr, ':', bar['properties']['Attributes'][attr])
    print(
        'Phone', ':',
        bar['properties']['Attributes']['PublicPhone'][0]['PublicPhone']
        )
    print()


def get_filepath():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args().filepath


def main():
    filename = get_filepath()
    bars_raw = load_data_from_json_file(filename)
    bars_list = bars_raw['features']
    smallest_bar = get_smallest_bar(bars_list)
    biggest_bar = get_biggest_bar(bars_list)
    print_bar_info(smallest_bar, 'Smallest bar:')
    print_bar_info(biggest_bar, 'Biggest bar:')
    user_gps = map(float, input('Please input yr gps coordinates: ').split())
    closest_bar = get_closest_bar(bars_list, *user_gps)
    print_bar_info(closest_bar, 'The closest bar for you is: ')

if __name__ == '__main__':
    main()
