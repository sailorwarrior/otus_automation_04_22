def amount_of_elements(locator, amount):
    def __predicate(driver):
        elements = driver.find_elements(*locator)
        if len(elements) == amount:
            if len(elements) == 0:
                return True
            return elements if amount > 1 else elements[0]
        else:
            raise AssertionError(f"Error while loading of {amount} elements with locator '{locator}'")

    return __predicate
