import argparse
from modules.wordpress_api import fetch_plugin_data
from modules.plugin_processor import process_plugin

def parse_arguments():
    parser = argparse.ArgumentParser(description='WordPress Plugin Data Fetcher')
    parser.add_argument('--active-install-min', type=int, default=999, help='Minimum active installs')
    parser.add_argument('--active-install-max', type=int, default=199999, help='Maximum active installs')
    parser.add_argument('--last-updated-year-min', type=int, default=2022, help='Minimum last updated year')
    parser.add_argument('-o', '--output-folder', default='output', help='Output folder for extracted plugin files')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    page = 1
    total_pages = None

    while total_pages is None or page <= total_pages:
        plugin_data = fetch_plugin_data(page)
        if total_pages is None:
            total_pages = int(plugin_data['info']['pages'])

        plugins = plugin_data.get('plugins', [])
        for plugin in plugins:
            process_plugin(plugin, args.active_install_min, args.active_install_max, args.last_updated_year_min, args.output_folder)

        page += 1
