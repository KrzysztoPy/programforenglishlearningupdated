from tkinter import Tk, ttk

from all_setting_for_gui.main_window_setting import main_window_name_text, rules_for_determining_the_size_of_the_main_window, \
    set_middle_position_for_main_window
from decorators.mian_window_decorators import resctriction_for_minimal_screen_resolution, \
    checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum


def set_title(root):
    root.title(main_window_name_text())


@checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum
def get_screen_result(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    return screen_width, screen_height


def set_geometry_main_window(root, width_screen_resolution, height_screen_resolution):
    width_window_size, height_window_size = rules_for_determining_the_size_of_the_main_window(width_screen_resolution,
                                                                                              height_screen_resolution)

    horizontal_position, vertical_position = set_middle_position_for_main_window(width_screen_resolution,
                                                                                 height_screen_resolution,
                                                                                 width_window_size, height_window_size)

    root.geometry(f"{width_window_size}x{height_window_size}+{horizontal_position}+{vertical_position}")


def main_loop(root):
    root.mainloop()