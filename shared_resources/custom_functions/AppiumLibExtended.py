
import robot
from AppiumLibrary import *
import sys, time, re, os
#from _global_element_functions import select_dropdown_menu_answer


#reload(sys)
#sys.setdefaultencoding('utf8')

#set default timeout
TIMEOUT=15

class AppiumLibExtended(AppiumLibrary):

    ROBOT_LIBRARY_SCOPE = 'Global'
    localTime = time.strftime("%Y-%m-%d", time.localtime())

    def __init__(self):
        AppiumLibrary.__init__(self)


    #added by CM 1/28/2018
    def wait_until_element_is_not_visible(self, locator, timeout=None, error=None):
        """Waits until element specified with `locator` is not visible.

        Fails if `timeout` expires before the element is not visible. See
        `introduction` for more information about `timeout` and its
        default value.

        `error` can be used to override the default error message.

        See also `Wait Until Page Contains`, `Wait Until Page Contains 
        Element`, `Wait For Condition` and BuiltIn keyword `Wait Until Keyword
        Succeeds`.
        """
        def check_no_visibility():
            visible = self._is_visible(locator)
            if not(visible):
                return
            elif not(visible) is None:
                return error or "Element locator '%s' still matched elements after %s" % (locator, self._format_timeout(timeout))
            else:
                return error or "Element '%s' was still visible in %s" % (locator, self._format_timeout(timeout))
        self._wait_until_no_error(timeout, check_no_visibility)

        

    def get_matching_sizzle_count(self, element):
        """Returns number of elements matching ``sizzle`` or ``css`` or ``jquery``
		
		As noted above, this should work with sizzle, jquery or css locators.

        One should not use the `jquery=` or 'css=' prefix for 'jquery'. Sizzle/jquery is assumed.

        | *Correct:* |
        | ${count}  | Get Matching Sizzle Count | [text='Test'] |
        | Incorrect:  |
        | ${count}  | Get Matching Sizzle Count | jquery=[text='Test'] |

        """
        count = len(self._element_find("jquery=" + element, False, False))
        return str(count)



    def element_should_not_be_visible(self, locator, loglevel='INFO'):
        """Verifies that element identified with locator is not visible.
        
        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        
        New in AppiumLibrary 1.4.5
        """
        if self._element_find(locator, True, True).is_displayed():
            self.log_source(loglevel)
            raise AssertionError("Element '%s' should not be visible "
                                 "but it is" % locator)



    def go_to(self, url):
        self.go_to_url(url)
        print("opening '%s'" % url)

        
    def select_from_list(self, menu_element, submenu_element):
        self.select_dropdown_menu_answer(menu_element, submenu_element)
        
        
        
        
        
    #def log_location(self):
    #    """Logs and returns the current URL."""
    #    url = self._current_application().get_location()  #this line is not correct.
    #    self.info(url)
    #    return url