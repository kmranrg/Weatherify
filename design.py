import flet as ft
import datetime
from weather import get_weather_details

# Get the current date
current_date = datetime.datetime.now()

# Format the date as "Wednesday, July 22"
formatted_date = current_date.strftime('%A, %B %d')

weather_data = get_weather_details('Houston')
print(f"https:{weather_data['Icon']}")

font_dictionary = {
    'Comfortaa-Bold' : "fonts/Comfortaa-Bold.ttf",
    'Comfortaa-Light': "fonts/Comfortaa-Light.ttf",
    'Comfortaa-Medium': "fonts/Comfortaa-Medium.ttf",
    'Comfortaa-Regular': "fonts/Comfortaa-Regular.ttf",
    'Comfortaa-SemiBold': "fonts/Comfortaa-SemiBold.ttf"
}

page_data = ft.Column([
    ft.Text(value=formatted_date,font_family="Comfortaa-Light",color=ft.colors.WHITE,style='titleLarge'),
    ft.Text(value=weather_data['Location'],font_family="Comfortaa-Bold",style='titleLarge',color=ft.colors.WHITE),
    ft.Image(src=f"https:{weather_data['Icon']}",width=600,height=600),
],horizontal_alignment='center')

body = ft.Container(
    content=page_data,
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        colors=['#001a31','#019877']
    ),
    width=500,
    height=1000,
    border_radius=5,
    padding=20
)

def main(page: ft.Page):
    page.title = 'Weatherify'
    page.padding = 0
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_width = 500
    page.window_height = 800
    page.theme = ft.theme.Theme(color_scheme_seed='green')
    page.window_bgcolor = '#019877'
    page.fonts = font_dictionary

    page.add(
        body
    )

ft.app(target=main,assets_dir='assets')