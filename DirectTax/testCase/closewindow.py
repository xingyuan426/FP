
import time

def test_closewindow(driver):
    time.sleep(5)
    print driver.current_window_handle
    handles = driver.window_handles
    print handles
    for handle in handles:
        if handle != driver.current_window_handle:
            print 'switch to ', handle
            driver.switch_to_window(handle)
            print driver.current_window_handle
            break

    driver.close()
    driver.switch_to_window(handles[0])