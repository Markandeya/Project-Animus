from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import wolframalpha
import re
import pytz
from datetime import datetime

class Calendar:
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Calendar API Python Quickstart'
    
    def __init__(self):
        pass

    @staticmethod
    def datetime_to_utc(timedate):
        app_id = 'L3J57Q-TWXW7R75RT'
        client = wolframalpha.Client(app_id)
        res =   client.query('timestamp of '+timedate)

        answer = next(res.results).text
        unix = int(re.sub('\(.*?\)', '', answer))

        utc = pytz.utc
        a_date = datetime.utcfromtimestamp(unix)
        utc_date = utc.localize(a_date).isoformat()
        return utc_date
    
    @staticmethod
    def get_credentials():
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                    'calendar-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(Calendar.CLIENT_SECRET_FILE, Calendar.SCOPES)
            flow.user_agent = Calendar.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    @staticmethod
    def get_events():
        credentials = Calendar.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        eventsResult = service.events().list(
            calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    @staticmethod
    def create_event(title, eventdesc, timedate):

        credentials = Calendar.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        utc_date = Calendar.datetime_to_utc(timedate)
        
        #create event
        event = {
        'summary': title,
        'description': eventdesc,
        'start': {
            'dateTime': utc_date,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': utc_date,
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: {}'.format(event.get('htmlLink')))