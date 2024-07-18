import sqlite3
import os
import sys

def get_firefox_profile_path():
    """
    Trouve le répertoire du profil Firefox sous Windows.
    """
    firefox_profile_dir = r"C:\Users\nicos\AppData\Roaming\Mozilla\Firefox\Profiles"
    profiles = [d for d in os.listdir(firefox_profile_dir) if d.endswith(".default-release") or d.endswith(".default") or "dev-edition-default" in d]
    
    if not profiles:
        print("No Firefox profiles found.")
        sys.exit(1)
    
    return os.path.join(firefox_profile_dir, profiles[0])

def show_visited_sites(profile_path):
    """
    Affiche les sites visités à partir de la base de données places.sqlite.
    """
    places_db_path = os.path.join(profile_path, "places.sqlite")
    if not os.path.exists(places_db_path):
        print(f"places.sqlite not found in {profile_path}")
        return
    
    conn = sqlite3.connect(places_db_path)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT url, title, visit_count, last_visit_date
    FROM moz_places
    WHERE visit_count > 0
    ORDER BY last_visit_date DESC
    """)

    rows = cursor.fetchall()
    print("\nVisited Sites:")
    for row in rows:
        print(f"URL: {row[0]}\nTitle: {row[1]}\nVisit Count: {row[2]}\nLast Visit Date: {row[3]}\n")

    conn.close()

def show_cookies(profile_path):
    """
    Affiche les cookies à partir de la base de données cookies.sqlite.
    """
    cookies_db_path = os.path.join(profile_path, "cookies.sqlite")
    if not os.path.exists(cookies_db_path):
        print(f"cookies.sqlite not found in {profile_path}")
        return
    
    conn = sqlite3.connect(cookies_db_path)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT host, name, value, expiry, lastAccessed
    FROM moz_cookies
    ORDER BY lastAccessed DESC
    """)

    rows = cursor.fetchall()
    print("\nCookies:")
    for row in rows:
        print(f"Host: {row[0]}\nName: {row[1]}\nValue: {row[2]}\nExpiry: {row[3]}\nLast Accessed: {row[4]}\n")

    conn.close()

def main():
    profile_path = get_firefox_profile_path()
    show_visited_sites(profile_path)
    show_cookies(profile_path)

if __name__ == "__main__":
    main()
