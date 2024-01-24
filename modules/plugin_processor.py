import os
import zipfile
import io
import requests

def process_plugin(plugin, active_install_min, active_install_max, last_updated_year_min, output_folder):
    active_installs = int(plugin.get('active_installs', 0))
    last_updated_year = int(plugin.get('last_updated', '1970')[:4])

    if active_installs > active_install_max:
        return

    if last_updated_year < last_updated_year_min:
        return

    if active_installs < active_install_min:
        return

    print(f"[ + ] Processing {plugin['slug']}...")

    response = requests.get(plugin['download_link'])
    archive = zipfile.ZipFile(io.BytesIO(response.content))

    plugin_name = plugin['slug']
    output_path = os.path.join(output_folder, plugin_name)
    os.makedirs(output_path, exist_ok=True)

    for file in archive.namelist():
        if file.startswith(f"{plugin_name}/"):
            archive.extract(file, path=output_path)

    print(f"[ - ] {plugin_name} extracted successfully.")
