# importing libraries
import flet as ft
import datetime
from weather import get_weather_details, get_forecast_details

# Get the current date
current_date = datetime.datetime.now()

# Format the date as "Wednesday, July 22"
formatted_date = current_date.strftime('%A, %B %d')

# setting the city
weather_data = get_weather_details('mumbai')
forecast_data = get_forecast_details('mumbai')

# main flet application
def main(page: ft.Page):

    # setting up the page
    page.title = 'Weatherify'
    page.padding = 0
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_width = 500
    page.window_height = 800
    page.theme = ft.theme.Theme(color_scheme_seed='green')
    page.window_bgcolor = '#019877'
    page.fonts = {
        'Comfortaa-Bold' : "fonts/Comfortaa-Bold.ttf",
        'Comfortaa-Light': "fonts/Comfortaa-Light.ttf",
        'Comfortaa-Medium': "fonts/Comfortaa-Medium.ttf",
        'Comfortaa-Regular': "fonts/Comfortaa-Regular.ttf",
        'Comfortaa-SemiBold': "fonts/Comfortaa-SemiBold.ttf"
    }

    # generating multiple items for containing hourly weather data
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
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    # homepage contents
    homepage_data = ft.Column([
        ft.Container(height=5),
        ft.Text(value=formatted_date,font_family="Comfortaa-Light",color=ft.colors.WHITE,style='titleLarge'),
        ft.Text(value=weather_data['Location'],font_family="Comfortaa-Bold",style='titleLarge',color=ft.colors.WHITE),
        ft.Container(height=25),
        ft.Image(src=f"weather_icons/{weather_data['IconLocation']}",width=150),
        ft.Container(height=10),
        ft.Text(value=f"{weather_data['Climate']}",font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
        ft.Text(value=f"{int(round(float(weather_data['Temperature (°C)'])))}°",font_family='Comfortaa-Light',style='displayLarge',color=ft.colors.WHITE,size=100),
        ft.Container(height=25),
        ft.Divider(color=ft.colors.WHITE),
        ft.Row(spacing=10,controls=hourly_items_report(),scroll='auto'),
        ft.Row([
            ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS,
                icon_color=ft.colors.WHITE,
                icon_size=30,
                on_click=lambda _: page.go("/")
            ),
            ft.IconButton(
                icon=ft.icons.ARROW_FORWARD_IOS,
                icon_color=ft.colors.WHITE,
                icon_size=30,
                on_click=lambda _: page.go("/homepage/weatherdetails")
            ),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        
    ],horizontal_alignment='center')

    # homepage container
    homepage_body = ft.Container(
        content=homepage_data,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=['#001a31','#019877']
        ),
        width=500,
        height=800,
        border_radius=5,
        padding=20
    )

    # splash screen contents
    splash_screen_data = ft.Column([
        ft.Text(value='Weatherify',font_family='Comfortaa-Bold',style='displaySmall',text_align='center'),
        ft.Container(height=20),
        ft.Image(src="logo/logo.svg",width=200),
        ft.Container(height=20),
        ft.IconButton(
            icon=ft.icons.ARROW_FORWARD_IOS,
            icon_color=ft.colors.WHITE,
            icon_size=30,
            on_click=lambda _: page.go("/homepage")
        ),
        ft.Container(height=20),
        ft.Container(
            content=ft.Text(' Developer: Kumar Anurag | Instagram: kmranrg ',font_family='Comfortaa-Medium',style='labelLarge'),
            bgcolor='#019877',
            border_radius=20,
            padding=10
        ),
    ],horizontal_alignment='center',alignment='center')

    # splash screen container
    splash_screen = ft.Container(
        content=splash_screen_data,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=['#001a31','#019877']
        ),
        width=500,
        height=800,
        border_radius=5,
        padding=20
    )

    # weather details content
    weather_indepth_data = ft.Column([
        ft.Container(height=5),
        ft.Text(value=formatted_date,font_family="Comfortaa-Light",color=ft.colors.WHITE,style='titleLarge'),
        ft.Text(value=weather_data['Location'],font_family="Comfortaa-Bold",style='titleLarge',color=ft.colors.WHITE),
        ft.Container(height=15),
        ft.Divider(color=ft.colors.WHITE),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Humidity',font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
            ft.Text(value=weather_data['Humidity'],font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Wind Speed',font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
            ft.Text(value=weather_data['WindSpeed'],font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Pressure',font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
            ft.Text(value=weather_data['Pressure'],font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Precipitation',font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
            ft.Text(value=weather_data['Precipitation'],font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='Gust',font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
            ft.Text(value=weather_data['Gust'],font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Row([
            ft.Text(value='UV Index',font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
            ft.Text(value=weather_data['UVIndex'],font_family="Comfortaa-Light",style='titleLarge',color=ft.colors.WHITE),
        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(height=5),
        ft.Divider(color=ft.colors.WHITE),
        ft.Container(height=15),
        ft.Row(spacing=10,controls=hourly_items_report(),scroll='auto'),
        ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS,
            icon_color=ft.colors.WHITE,
            icon_size=30,
            on_click=lambda _: page.go("/homepage")
        )
    ],horizontal_alignment='center',alignment='center')

    # weather details container
    weather_indepth_body = ft.Container(
        content=weather_indepth_data,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=['#001a31','#019877']
        ),
        width=500,
        height=800,
        border_radius=5,
        padding=20
    )

    # defining route change function
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    splash_screen
                ],
                scroll='auto',
                vertical_alignment='center',
                horizontal_alignment='center',
                padding=0
            )
        )
        if page.route == "/homepage" or page.route == "/homepage/weatherdetails":
            page.views.append(
                ft.View(
                    "/homepage",
                    [
                        homepage_body,
                    ],
                    scroll='auto',
                    vertical_alignment='center',
                    horizontal_alignment='center',
                    padding=0
                )
            )
        if page.route == "/homepage/weatherdetails":
            page.views.append(
                ft.View(
                    "/weatherdetails",
                    [
                        weather_indepth_body,
                    ],
                    scroll='auto',
                    vertical_alignment='center',
                    horizontal_alignment='center',
                    padding=0
                )
            )
    page.update()

    # defining view pop function
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # setting up the route change and view pop functions to the page
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

# calling the main function
ft.app(target=main,assets_dir='assets',view=ft.WEB_BROWSER)