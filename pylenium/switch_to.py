from selenium.webdriver.support import expected_conditions as ec
from pylenium.element import Element


class SwitchTo:
    def __init__(self, pylenium):
        self._py = pylenium

    def frame_by_id(self, frame_id: str, timeout: int = 0):
        """ Switch the driver's context to the new frame given the id of the element.

        Args:
            frame_id: The frame's `id` attribute value
            timeout: The number of seconds to wait for the frame to be switched to

        Examples:
            py.switch_to.frame_by_id('iframe-id')
        """
        self._py.log.info(f'[STEP] py.switch_to.frame_by_id() - Switch to frame using id: ``{frame_id}``')
        frame = self._py.get(f'#{frame_id}', timeout=timeout)
        self._py.wait(timeout).until(ec.frame_to_be_available_and_switch_to_it(frame.webelement))
        return self._py

    def frame_by_name(self, name: str, timeout: int = 0):
        """ Switch the driver's context to the new frame given the name of the element.

        Args:
            name: The frame's `name` attribute value
            timeout: The number of seconds to wait for the frame to be switched to

        Examples:
            py.switch_to.frame_by_name('iframe-name')
        """
        self._py.log.info(f'[STEP] py.switch_to.frame_by_name() - Switch to frame using name: ``{name}``')
        frame = self._py.get(f'[name="{name}"]', timeout=timeout)
        self._py.wait(timeout).until(ec.frame_to_be_available_and_switch_to_it(frame.webelement))
        return self._py

    def frame_by_element(self, element: Element, timeout: int = 0):
        """ Switch the driver's context to the given frame element.

        Args:
            element (Element): The frame element to switch to
            timeout: The number of seconds to wait for the frame to be switched to.

        Examples:
            iframe = py.get('iframe')
            py.switch_to.frame_by_element(iframe)
        """
        self._py.log.info('[STEP] py.switch_to.frame_by_element() - Switch to frame using an Element.')
        self._py.wait(timeout).until(ec.frame_to_be_available_and_switch_to_it(element.webelement))
        return self._py

    def parent_frame(self):
        """ Switch the driver's context to the parent frame.

        If the parent frame is the current context, nothing happens.
        """
        self._py.log.info('[STEP] py.switch_to.parent_frame() - Switch to the parent frame')
        self._py.webdriver.switch_to.parent_frame()
        return self._py

    def default_content(self):
        """ Switch the driver's context to the default content. """
        self._py.log.info('[STEP] py.switch_to.default_content() - Switch to default content of this browser session')
        self._py.webdriver.switch_to.default_content()
        return self._py

    def window(self, name_or_handle='', index: int = None):
        """ Switch the driver's context to the specified Window or Browser Tab.

        Args:
            name_or_handle: The name or window handle of the Window to switch to.
            index: The index position of the Window Handle.

        * `index=0` would be the default content.

        Examples:
            # Switch to a Window by handle
            windows = py.window_handles
            py.switch_to.window(name_or_handle=windows[1])

            # Switch to a newly opened Browser Tab by index
            py.switch_to.window(index=1)
        """
        if index is not None:
            handle = self._py.webdriver.window_handles[index]
            self._py.log.info(f'[STEP] py.switch_to.window() - Switch to a Tab or Window by index: ``{index}``')
            self._py.webdriver.switch_to.window(handle)
            return self._py
        elif name_or_handle:
            self._py.log.info(
                f'[STEP] py.switch_to.window() - Switch to Tab or Window by name or handle: ``{name_or_handle}``')
            self._py.webdriver.switch_to.window(name_or_handle)
            return self._py
        else:
            # context unchanged
            return self._py
