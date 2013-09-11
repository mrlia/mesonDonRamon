import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium import webdriver

class MesonTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_meson_site(self):
        # User opens web browser, and goes to the meson page
        self.browser.get(self.live_server_url + '/meson/')

        # Sees the main page with the restaurant name
        title = self.browser.find_element_by_tag_name('body')
        self.assertIn('Meson Don Ramon', title.text)

    def test_can_see_menu_via_meson_site(self):
        # Goes to the menu page and check the menu links exist
        self.browser.get(self.live_server_url + '/meson/menu/')
        menuPermanent = self.browser.find_element_by_id('menuPermanentTab')
        self.assertIn('Variety', menuPermanent.text)
        menuDaily = self.browser.find_element_by_id('menuDailyTab')
        self.assertIn('Daily Menu', menuDaily.text)

    def test_can_see_permanent_menu_page(self):
        # Goes to the permanent menu page and check the menu links exist
        # And checks there's no error without any menu in the BD
        self.browser.get(self.live_server_url + '/meson/menuPermanent/')
        menuPermanent = self.browser.find_element_by_id('permanentMenuContent')
        self.assertIn('Menu del Meson Don Ramon', menuPermanent.text)

    def test_can_see_daily_menu_page(self):
        # Goes to the daily menu page and check the menu links exist
        # And checks there's no error without any menu in the BD
        self.browser.get(self.live_server_url + '/meson/menuDaily/')
        menuDaily = self.browser.find_element_by_id('dailyMenuContent')
        dateMenu = "Menu del "+datetime.date.today().isoformat()
        self.assertIn(dateMenu, menuDaily.text)
