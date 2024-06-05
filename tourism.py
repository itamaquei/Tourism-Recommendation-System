import flet as ft

# Importing the recommendation function
from recommend import generate_recommendations2

generate_recommendations = generate_recommendations2


def main(page: ft.Page):
    page.title = "Osogbo Tourism Recommendation System"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Applying styles to the page
    page.theme = ft.Theme(
        font_family="Montserrat",
        use_material3=True,
        color_scheme_seed=ft.colors.BLUE_GREY_200,
    )
    page.fonts = {"Montserrat": "/Montserrat-Regular.ttf"}
    page.bgcolor = ft.colors.BLUE_GREY_100
    page.padding = 50
    page.scroll = "AUTO"
    page.update()

    def on_submit(event):
        interests = interests_input.value
        budget = budget_input.value
        duration = duration_input.value
        previous_experiences = experiences_input.value

       # Generate recommendations using the imported function
        if interests and budget and duration and previous_experiences:
            recommendations = generate_recommendations(
                interests, budget, duration, previous_experiences)
            

        else:
            recommendations = "PLEASE ENTER THE NECESSARY VALUES"

        interests_input.value = ""
        budget_input.value = ""
        duration_input.value = ""
        experiences_input.value = ""
        recommendations_output.value = recommendations
        page.update()

    # UI Controls
    interests_input = ft.TextField(
        adaptive=True,
        label="Interests",
        hint_text="e.g., History, Art, Nature",
        border_color=ft.colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=ft.TextStyle(font_family="Montserrat"),
    )
    budget_input = ft.TextField(
        adaptive=True,
        label="Budget",
        hint_text="e.g., #500, #1000",
        border_color=ft.colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=ft.TextStyle(font_family="Montserrat"),
    )
    duration_input = ft.TextField(
        adaptive=True,
        label="Duration of Stay (days)",
        hint_text="e.g., 3, 7",
        border_color=ft.colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=ft.TextStyle(font_family="Montserrat"),
    )
    experiences_input = ft.TextField(
        adaptive=True,
        label="Previous Travel Experiences",
        hint_text="e.g., Beach, Mountains",
        border_color=ft.colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=ft.TextStyle(font_family="Montserrat"),
    )
    submit_button = ft.ElevatedButton(
        text="Get Recommendations",
        on_click=on_submit,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_GREY_500,
            color=ft.colors.WHITE,
            elevation=4,
            padding=ft.padding.only(top=10, bottom=10, left=20, right=20),
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    # Retrieve user inputs

    img = ft.Image(
        src=f"https://picsum.photos/200/200",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    recommendations_output = ft.TextField(
        adaptive=True,
        label="Recommendations",
        multiline=True,
        read_only=True,
        height=150,
        border_color=ft.colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=ft.TextStyle(font_family="Montserrat"),
    )

    # Adding controls to the page
    page.add(
        ft.Column(
            [
                ft.Text(
                    value="Welcome to Osogbo Tourism Recommendation System", style="headlineMedium"),
                interests_input,
                budget_input,
                duration_input,
                experiences_input,
                submit_button,
                #recommendations_output,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=True
        )
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
