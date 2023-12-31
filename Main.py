import csv
import re
import cfbd
import json
import os
from dotenv import load_dotenv
load_dotenv()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = os.getenv("CFBD_API_KEY")
configuration.api_key_prefix['Authorization'] = 'Bearer'

offensive_positions = ["QB", "RB", "WR", "PK", "P", "TE"]

# Setup admin access to FB Storage bucket
cred = credentials.Certificate("/Users/coltenglover/Downloads/b1g-fantasy-football-firebase-adminsdk-yg8ju-73d5d2b292.json")
firebase_admin.initialize_app(cred, {
    "storageBucket": "b1g-fantasy-football.appspot.com"
})

bucket = storage.bucket()


def main():
    blob = bucket.blob('2023-images/purdue-roster-photos/picture.jpeg')
    blob.upload_from_filename(filename="/Users/coltenglover/Downloads/crop.jpeg")

if __name__ == "__main__":
    main()
