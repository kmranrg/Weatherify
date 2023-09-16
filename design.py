import flet as ft
import datetime
from weather import get_weather_details, get_forecast_details

# Get the current date
current_date = datetime.datetime.now()

# Format the date as "Wednesday, July 22"
formatted_date = current_date.strftime('%A, %B %d')

weather_data = get_weather_details('new delhi')
forecast_data = get_forecast_details('new delhi')



def hourly_items_report():
    items = []
    for k,v in forecast_data.items():
        time = k
        logo = v['logo']
        temp = v['temp_c']

        hourly_icon = ft.Image(height=50)
        hourly_time = ft.Text(font_family='Comfortaa-Medium',style='titleMedium',color=ft.colors.WHITE)
        hourly_temp = ft.Text(font_family='Comfortaa-Medium',style='titleLarge',color=ft.colors.WHITE)
        hourly_container = ft.Column([
            hourly_icon,
            hourly_time,
            hourly_temp
        ],horizontal_alignment='center')
        
        # setting the values of hourly container
        hourly_icon.src = f"weather_icons/{logo}"
        hourly_temp.value = temp
        hourly_time.value = time

        items.append(
            ft.Container(
                content=hourly_container,
                alignment=ft.alignment.center,
                width=150,
                height=150,
                blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR),
                border_radius=ft.border_radius.all(5),
            )
        )
    return items


font_dictionary = {
    'Comfortaa-Bold' : "fonts/Comfortaa-Bold.ttf",
    'Comfortaa-Light': "fonts/Comfortaa-Light.ttf",
    'Comfortaa-Medium': "fonts/Comfortaa-Medium.ttf",
    'Comfortaa-Regular': "fonts/Comfortaa-Regular.ttf",
    'Comfortaa-SemiBold': "fonts/Comfortaa-SemiBold.ttf"
}

page_data = ft.Column([
    ft.Container(height=10),
    ft.Text(value=formatted_date,font_family="Comfortaa-Light",color=ft.colors.WHITE,style='titleLarge'),
    ft.Text(value=weather_data['Location'],font_family="Comfortaa-Bold",style='titleLarge',color=ft.colors.WHITE),
    ft.Container(height=80),
    ft.Image(src=f"weather_icons/{weather_data['IconLocation']}",width=150),
    ft.Container(height=10),
    ft.Text(value=f"{weather_data['Climate']}",font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
    ft.Text(value=f"{int(round(float(weather_data['Temperature (°C)'])))}°",font_family='Comfortaa-Light',style='displayLarge',color=ft.colors.WHITE,size=100),
    ft.Container(height=60),
    ft.Divider(color=ft.colors.WHITE),
    ft.Row(spacing=1,controls=hourly_items_report(),scroll='auto')
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