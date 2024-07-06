import flet as ft
from flet import *
import time

def main(page: ft.Page):
    # title
    page.title = "Jadon Forman Portfolio"

    # animate social
    def _animate_social(e):
        if e.data == "true":
            _icon_text_.offset, _icon_text_.opacity=transform.Offset(0, 0.05), 0
            _icon_text_.update()
            for btn in _social_button.controls[:]:
                btn.offset, btn.opacity=transform.Offset(0, 0.15), 1
                btn.update()
                time.sleep(0.1)
        else:
            for btn in _social_button.controls[:]:
                btn.offset, btn.opacity=transform.Offset(0, -0.9), 0
                btn.update()
                time.sleep(0.1)
            _icon_text_.offset, _icon_text_.opacity=transform.Offset(0, -1.1), 1
            _icon_text_.update()
            

    # resize function
    def on_resized(e):
        if page.width <= 730:
            _nav.controls[0].visible = False
            _nav.update()
            _min_nav.visible = True
            _min_nav.update()
        else:
            _nav.controls[0].visible = True
            _nav.update()
            _min_nav.visible = False
            _min_nav.update()
                

    # text color function
    def _change_text_color(e):
        if e.control.content.color == "white":
            e.control.content.color = "#475569" # dark blue
            e.control.content.update()
        else:
            e.control.content.color = "white"
            e.control.content.update()

    # navbar
    _nav = Row(
        alignment="end",
        controls=[
            Container(
                padding=padding.only(right=20),
                # bgcolor="pink",
                height=64,
                content=Row(
                    controls=[
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text("About Me",
                                weight="w600",
                                color="white",),
                        
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text("Contact",
                                weight="w600",
                                color="white",),
                        
                        ),
                        Container(
                            on_hover=lambda e: _change_text_color(e),
                            content=Text("Services",
                                weight="w600",
                                color="white",),
                        
                        ),
                    ],
                )
            ),
        ],
    )

    # minimized navbar
    _min_nav = Row(
        visible=False,
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="About Me"),
                    PopupMenuItem(text="Contact"),
                    PopupMenuItem(text="Services"),
                ]
            )
        ]
    )

    # titles
    _title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={'xs': 12, 'sm': 12, 'md': 10, 'lg': 10, 'xl': 12},
                alignment=alignment.top_center,
                padding=20,
                content=Text(
                    "Jadon Forman Portfolio",
                    size=45,
                    weight="w600",
                    text_align="center",
                    color="white",
                )
            )
        ],
    )

    # subtitles
    _sub_title = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={'xs': 12, 'sm': 12, 'md': 12, 'lg': 12, 'xl': 12},
                alignment=alignment.top_center,
                padding=20,
                content=Text(
                    "Welcome to my personal webpage! Have a look around and contact me if you find anything interesting.",
                    text_align="center",
                    size=16,
                    weight="w500",
                    color="white",
                )
            )
        ]
    )

    # social media button
    _icon_list_ = [
        icons.EMAIL_SHARP,
        icons.SHARE_SHARP
    ]

    _social_button = Row(
        alignment="center",
        vertical_alignment="center",
    )

    _icon_text_ = Text(
        "Connect!",
        size=16,
        color="white",
        weight="w800",
        animate_opacity=50,
        offset=transform.Offset(0, -1.1),
        animate_offset=animation.Animation(duration=1000, curve="elasticOut"),
            
    )

    for icon in _icon_list_:
        _icon = IconButton(
            icon=icon,
            icon_size=22,
            icon_color="white",
            offset=transform.Offset(0, -0.9),
            animate_offset=animation.Animation(duration=1000, curve="elasticOut"),
            animate_opacity=200,
            opacity=0,
        )

        _social_button.controls.append(_icon)

    _icon_container = Container(
        width=145,
        height=50,
        bgcolor="blue",
        border_radius=8, #
        alignment=alignment.center,
        on_hover=lambda e: _animate_social(e),
        content=Column(
            spacing=0,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                _social_button,
                Row(
                    alignment="center",
                    controls=[
                        _icon_text_,
                    ]
                )
            ]
        ),
    )

    # portfolio grid responsive
    _items = ["ITEM ONE", "ITEM TWO", "ITEM THREE", "ITEM FOUR", "ITEM FIVE", "ITEM SIX"]
    _item_row = ResponsiveRow(alignment='start')
    _container_item = Container(
        padding=20,
        content=_item_row,
    )

    for item in _items:
        _item_container = Container(
            width=300,
            height=300,
            aspect_ratio=1,
            bgcolor="white",
            padding=35,
            border_radius=12,
            alignment=alignment.center,
            col={'xs': 10, 'sm': 5, 'md': 4, 'lg': 6, 'xl': 3},
            content=Container(
                aspect_ratio=1,
                border_radius=8,
                bgcolor="black",
                alignment=alignment.center,
                content=Text(
                    f'{item}',
                    size=21,
                    color="white",
                )
            )
        )

        _item_row.controls.append(_item_container)

    # main column
    _main_col = Column(horizontal_alignment="center", scroll="auto")
    _main_col.controls.append(_nav)
    _main_col.controls.append(_min_nav)
    _main_col.controls.append(_title)
    _main_col.controls.append(_sub_title)
    _main_col.controls.append(Container(padding=padding.only(top=10)))
    _main_col.controls.append(_icon_container)
    _main_col.controls.append(Container(padding=padding.only(bottom=40)))
    _main_col.controls.append(_container_item)



    # background
    _background = Container(
        height=page.height,
        expand=True,
        margin=10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                "#13547a",
                "#0f172a", # blue gradient
            ],
        ),
        
        content=_main_col,
    )
    # app
    page.add(_background)
    # resize
    page.on_resized = on_resized

ft.app(main)