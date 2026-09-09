from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

USERNAME = 'abdul2'
EMAIL = 'abdul2@gmail.com'
PASSWORD = 'September2024...#'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/login")


email_input = driver.find_element(By.ID, value="email-input")
password_input = driver.find_element(By.ID,value='password-input')
button = driver.find_element(By.ID,value="submit-button")

email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
button.send_keys(Keys.ENTER)
time.sleep(3)
#class_cards = driver.find_elements(By.CSS_SELECTOR,value="div[id^='class-card-']"
class_cards = driver.find_elements(
    By.CSS_SELECTOR,
    "div[id^='class-card-']"
)


new_bookings = 0
new_waitlists = 0
already_booked_or_waitlisted = 0
total_processed = 0

class_details = []

for card in class_cards:

    class_time = card.find_element(
        By.CSS_SELECTOR,
        "p[id^='class-time-']"
    ).text.strip()

    day_group = card.find_element(
        By.XPATH,
        "./ancestor::div[starts-with(@id, 'day-group-')][1]"
    )

    class_day = day_group.find_element(
        By.CSS_SELECTOR,
        "h2[id^='day-title-']"
    ).text.strip()

    is_target_day = (
        "Tue," in class_day
        or "Thu," in class_day
    )

    is_six_pm = "6:00 PM" in class_time.upper()

    if is_target_day and is_six_pm:

        total_processed += 1

        class_name = card.find_element(
            By.CSS_SELECTOR,
            "h3[id^='class-name-']"
        ).text.strip()

        booking_button = card.find_element(
            By.CSS_SELECTOR,
            "button[id^='book-button-']"
        )

        button_text = booking_button.text.strip()

        if button_text == "Booked":
            already_booked_or_waitlisted += 1

            message = (
                f"✓ Already booked: "
                f"{class_name} on {class_day}"
            )

            detail = (
                f"[Already Booked] "
                f"{class_name} on {class_day}"
            )

            print(message)
            class_details.append(detail)

        elif button_text == "Waitlisted":
            already_booked_or_waitlisted += 1

            message = (
                f"✓ Already on waitlist: "
                f"{class_name} on {class_day}"
            )

            detail = (
                f"[Already Waitlisted] "
                f"{class_name} on {class_day}"
            )

            print(message)
            class_details.append(detail)

        elif button_text == "Join Waitlist":
            booking_button.click()
            new_waitlists += 1

            message = (
                f"✓ Joined waitlist for: "
                f"{class_name} on {class_day}"
            )

            detail = (
                f"[New Waitlist] "
                f"{class_name} on {class_day}"
            )

            print(message)
            class_details.append(detail)

        elif button_text == "Book Class":
            booking_button.click()
            new_bookings += 1

            message = (
                f"✓ Successfully booked: "
                f"{class_name} on {class_day}"
            )

            detail = (
                f"[New Booking] "
                f"{class_name} on {class_day}"
            )

            print(message)
            class_details.append(detail)

        else:
            message = (
                f"⚠ Unexpected state '{button_text}': "
                f"{class_name} on {class_day}"
            )

            print(message)
            class_details.append(
                f"[Unexpected State] {class_name} on {class_day}"
            )


print("\n--- BOOKING SUMMARY ---")
print(f"New bookings: {new_bookings}")
print(f"New waitlist entries: {new_waitlists}")
print(
    f"Already booked/waitlisted: "
    f"{already_booked_or_waitlisted}"
)
print(
    f"Total Tuesday & Thursday 6pm classes: "
    f"{total_processed}"
)

print("\n--- DETAILED CLASS LIST ---")

if class_details:
    for detail in class_details:
        print(f"• {detail}")
else:
    print("• No Tuesday or Thursday 6pm classes found")