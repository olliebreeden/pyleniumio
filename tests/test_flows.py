from pylenium.driver import Pylenium


def test_add_to_cart(py: Pylenium):
    py.visit('https://jane.com')
    py.get('[data-testid="deal-image"]').click()

    for dropdown in py.find('select'):
        dropdown.select(1)

    py.get('[data-testid="add-to-bag"]', timeout=1).click()
    assert py.get("[href='/bag']").should().be_visible()


def test_add_to_cart_xpath(py: Pylenium):
    py.visit('https://jane.com')
    py.getx('//*[@data-testid="deal-image"]').click()

    for dropdown in py.findx('//select'):
        dropdown.select(1)

    py.getx('//*[@data-testid="add-to-bag"]', timeout=1).click()
    assert py.getx("//*[@href='/bag']").should().be_visible()
