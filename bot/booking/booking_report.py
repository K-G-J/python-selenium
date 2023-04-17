# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self, boxes_selection_element: WebElement):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements(By.CLASS_NAME, 'sr_property_block')

    def pull_title(self):
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                By.CLASS_NAME, 'sr-hotel_name').get_attribute('innerHTML').strip()
            print(hotel_name)
