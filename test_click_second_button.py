from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def test_click_second_button():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # Відкрити сайт
        driver.get("https://editorial.link/")

        # Знайти та клацнути кнопку "Decline all" за класом
        decline_button = wait.until(
            ec.element_to_be_clickable((By.CLASS_NAME, "coi-banner__decline"))
        )
        decline_button.click()
        print("Cookies declined using class 'coi-banner__decline'.")

        # Альтернативний спосіб - якщо перший не спрацює
        # decline_button = wait.until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.coi-banner__decline"))
        # )

        # Дочекатися зникнення cookie банера (опціонально)
        try:
            wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "coi-banner")))
            print("Cookie banner disappeared.")
        except TimeoutException:
            print("Cookie banner still visible, continuing...")

        # Знайти кнопку "See Client Results" за класом
        target_button = wait.until(
            ec.element_to_be_clickable((By.CLASS_NAME, "btn-main-block"))
        )
        target_button.click()
        print("Clicked the 'See Client Results' button.")

        # Дочекатися переходу на `/case/`
        wait.until(ec.url_contains("/case/"))
        assert "/case/" in driver.current_url, f"Expected '/case/' in URL, but got {driver.current_url}"
        print(f"Test passed! Successfully navigated to: {driver.current_url}")

    except TimeoutException as e:
        print(f"Timeout error: {e}")
        print("Element not found within the specified time limit.")
        print(f"Current URL: {driver.current_url}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Current URL: {driver.current_url}")
    finally:
        print("\n" + "=" * 50)
        print("TEST RESULTS:")
        print("=" * 50)
        print(f"Final URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        print("Browser remains open for manual inspection.")
        print("=" * 50)
        print("\nPress Ctrl+C to close the browser or close it manually.")


# Запустити тест
if __name__ == "__main__":
    test_click_second_button()