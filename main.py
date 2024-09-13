#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import transmissionrpc
import json
import time
import os

links = []

# Construct the full path to shows.json
script_dir = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(script_dir, 'shows.json')

def fetch_magnet_link(show_name, season, episode):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome WebDriver with headless options
    driver = webdriver.Chrome(options=chrome_options)
    search_url = f"https://notapiracywebsite.org/search.php?q={show_name}+s{season}e{episode}&video=on&search=Pirate+Search&page=0&orderby="
    
    # Open the search page
    driver.get(search_url)
    time.sleep(5) 

    # Find and get the 'Magnet Download' link
    magnet_button = driver.find_element(By.XPATH, "//a[contains(@href, 'magnet:')]")
    magnet_link = magnet_button.get_attribute("href")
    print(f"{show_name} link found")
    links.append(magnet_link)

    # Close the browser
    driver.quit()


def process_int(int):
    if int < 10:
        return f"0{int}"
    else:
        return int
    

def process_name(name):
    return name.replace(' ', '+')


def process_shows():
    # Read the shows.json file
    with open(json_file_path, 'r') as f:
        shows = json.load(f)

    # Iterate through the shows and fetch magnet links
    for show, details in shows.items():
        season = process_int(details['season'])
        episode = process_int(details['episode'])
        season_length = details['seasonLength']

        print(f"Fetching {show} - Season {season}, Episode {episode}")

        # Call the fetch magnet link for the current show, season, and episode
        fetch_magnet_link(process_name(show), season, episode)

        # Increment the episode number after downloading
        next_episode = int(episode) + 1

        # Check if we've reached the end of the season
        if next_episode > season_length:
            print(f"All episodes of {show} season {season} downloaded.")
            shows[show]['season'] = int(season)+1
            shows[show]['episode'] = 1
            continue

        # Update the episode in the dictionary
        shows[show]['episode'] = next_episode

    # Write the updated data back to the JSON file
    with open('shows.json', 'w') as f:
        json.dump(shows, f, indent=4)


process_shows()

# Add all the torrents to transmission
if len(links) > 0:
    for magnet_link in links:
        tc = transmissionrpc.Client('localhost', port=9091)  
        tc.add_torrent(magnet_link)
        print(f"Magnet link added to Transmission for downloading.")

