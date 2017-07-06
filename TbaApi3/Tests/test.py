import TbaApi3
import time
from unittest import TestCase

TEAMS = ['frc263', 'frc254', 'frc469']
EVENTS = {'frc263' : ['2017flwp', '2017nyli'], 'frc254' :['2017casf', '2017dal'], 'frc469' : ['2017micen', '2017micmp2']}
API_KEY = 'MauDxOjjHL3V2TS6LAQJt0dtpMlTeM2IWVuirihlfyikvVGkFrQsFKL6xqcZ1HF3'


class TestObject(TestCase):
    def test(self):
        """
        ------------------------------------------------
        |                 OBJECT TESTS                 |
        ------------------------------------------------
        """
        test_object = TbaApi3.ApiObject(API_KEY)
        test_status = test_object.status()

class TestTeams(TestCase):
    def test(self):
        """
        ------------------------------------------------
        |                  TEAM TESTS                  |
        ------------------------------------------------
        """
        test_object = TbaApi3.ApiObject(API_KEY)
        for i in range(5):
            test_object.teams_page(i)
            test_object.teams_page_simple(i)
            test_object.teams_page_keys(i)
            test_object.teams_page_year(i, year=2015)
            test_object.teams_page_year_simple(i, year=2015)
            test_object.teams_page_year_keys(i, year=2015)
            time.sleep(15)
        for team in TEAMS:
            test_object.get_team(team)
            test_object.get_team_simple(team)
            test_object.years_participated(team)
            test_object.team_districts(team)
            test_object.team_robots(team)
            test_object.team_events(team)
            test_object.team_events_simple(team)
            test_object.team_events_keys(team)
            test_object.team_events_year(team, year=2016)
            test_object.team_events_year_simple(team, year=2016)
            test_object.team_events_year_keys(team, year=2016)
            time.sleep(15)
            test_object.team_awards(team)
            test_object.team_awards_year(team, year=2013)
            test_object.team_matches_year(team)
            test_object.team_matches_year_simple(team)
            test_object.team_matches_year_keys(team)
            test_object.team_matches_year(team, year=2014)
            test_object.team_matches_year_simple(team, year=2014)
            test_object.team_matches_year_keys(team, year=2014)
            test_object.team_media_year(team)
            test_object.team_media_year(team, year=2011)
            test_object.team_social_media(team)
            time.sleep(15)
        for team, events in EVENTS.items():
            for event in events:
                test_object.team_event_matches(team, event)
                test_object.team_event_matches_simple(team, event)
                test_object.team_event_matches_keys(team, event)
                test_object.team_event_status(team, event)
                time.sleep(15)

class TestFunctions(TestCase):
    def test(self):
        """
        ------------------------------------------------
        |                FUNCTION TESTS                |
        ------------------------------------------------
        """
        test_object = TbaApi3.ApiObject(API_KEY)
        test_object.get_all_teams()