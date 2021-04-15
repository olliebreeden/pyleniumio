from pylenium import jquery
from pylenium.driver import Pylenium


THE_INTERNET = 'https://the-internet.herokuapp.com'


def test_check_single_box(py: Pylenium):
    py.visit(f'{THE_INTERNET}/checkboxes')
    box = py.get('[type="checkbox"]')
    assert box.check().should().be_checked()
    assert box.uncheck().is_checked() is False


def test_check_many_boxes(py: Pylenium):
    py.visit(f'{THE_INTERNET}/checkboxes')
    assert py.find('[type="checkbox"]').check(allow_selected=True).are_checked()


def test_select_dropdown(py: Pylenium):
    py.visit(f'{THE_INTERNET}/dropdown')
    option = py.get('#dropdown').select('2')
    assert option.is_selected()


def test_drag_to_with_selector(py: Pylenium):
    py.visit(f'{THE_INTERNET}/drag_and_drop')
    py.get('#column-a').drag_to('#column-b')
    assert py.get('#column-b > header').should().have_text('A')


def test_drag_to_with_element(py: Pylenium):
    py.visit(f'{THE_INTERNET}/drag_and_drop')
    column_b = py.get('#column-b')
    py.get('#column-a').drag_to_element(column_b)
    assert column_b.get('header').should().have_text('A')


def test_jquery(py: Pylenium):
    py.visit('https://amazon.com')
    jquery.inject(py.webdriver, version='3.5.1')
    assert py.execute_script('return jQuery.expando;') is not None
    assert py.execute_script('return $.expando;') is not None
    assert jquery.exists(py.webdriver) == '3.5.1'


def test_hover(py: Pylenium):
    py.visit(f'{THE_INTERNET}/hovers')
    py.get('.figure').hover()
    assert py.contains('View profile').should().be_visible()


def test_radio_buttons(py: Pylenium):
    py.visit('http://test.rubywatir.com/radios.php')
    radio = py.get('#radioId')
    assert radio.check().should().be_checked()

    py.get('[value="Radio1"]').check()
    assert not radio.is_checked()


def test_checkbox_buttons(py: Pylenium):
    py.visit('http://test.rubywatir.com/checkboxes.php')
    checkbox = py.get('input[name=sports][value=soccer]')
    assert checkbox.should().be_checked()

    checkbox.uncheck()
    assert not checkbox.is_checked()
