from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, 'li[class="styles_ndsCarouselItem__dnUkr"] img')
SELECTED_COLOR = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] div')

@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/levi-s-women-s-superlow-loose-jeans/-/A-92690358?preselect=92463709#lnk=sametab')
    sleep(5)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Abraided Art', 'Blended Beauty', 'Table Talk']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        # for visibility only:
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'