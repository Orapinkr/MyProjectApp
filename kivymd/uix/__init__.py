  
from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from kivymd.uix.behaviors import SpecificBackgroundColorBehavior


class MDAdaptiveWidget(SpecificBackgroundColorBehavior):
    adaptive_height = BooleanProperty(False)
    """
    If `True`, the following properties will be applied to the widget:
    .. code-block:: kv
        size_hint_y: None
        height: self.minimum_height
    :attr:`adaptive_height` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    adaptive_width = BooleanProperty(False)
    """
    If `True`, the following properties will be applied to the widget:
    .. code-block:: kv
        size_hint_x: None
        width: self.minimum_width
    :attr:`adaptive_width` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    adaptive_size = BooleanProperty(False)
    """
    If `True`, the following properties will be applied to the widget:
    .. code-block:: kv
        size_hint: None, None
        size: self.minimum_size
    :attr:`adaptive_size` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    def on_adaptive_height(self, instance, value):
        if not isinstance(self, (FloatLayout, Screen)):
            self.size_hint_y = None
            self.bind(minimum_height=self.setter("height"))

    def on_adaptive_width(self, instance, value):
        if not isinstance(self, (FloatLayout, Screen)):
            self.size_hint_x = None
            self.bind(minimum_width=self.setter("width"))

    def on_adaptive_size(self, instance, value):
        if not isinstance(self, (FloatLayout, Screen)):
            self.size_hint = (None, None)
            self.bind(minimum_size=self.setter("size"))