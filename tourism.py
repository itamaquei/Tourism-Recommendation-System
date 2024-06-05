from flet import *

# Importing the recommendation function
from recommend import generate_recommendations2

generate_recommendations = generate_recommendations2


def main(page: Page):
    page.title = "Osogbo Tourism Recommendation System"
    page.theme_mode = ThemeMode.LIGHT

    # Applying styles to the page
    page.theme = Theme(
        font_family="Montserrat",
        use_material3=True,
        color_scheme_seed=colors.BLUE_GREY_200,
    )
    page.fonts = {"Montserrat": "/Montserrat-Regular.ttf"}
    page.bgcolor = colors.BLUE_GREY_100
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
            _controls.controls.append(recommendations_output)
                       

        else:
            recommendations = "PLEASE ENTER THE NECESSARY VALUES"

        interests_input.value = ""
        budget_input.value = ""
        duration_input.value = ""
        experiences_input.value = ""
        recommendations_output.value = recommendations
        page.update()

    # UI Controls
    interests_input = TextField(
        adaptive=True,
        label="Interests",
        hint_text="e.g., History, Art, Nature",
        border_color=colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=TextStyle(font_family="Montserrat"),
    )
    budget_input = TextField(
        adaptive=True,
        label="Budget",
        hint_text="e.g., #500, #1000",
        border_color=colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=TextStyle(font_family="Montserrat"),
    )
    duration_input = TextField(
        adaptive=True,
        label="Duration of Stay (days)",
        hint_text="e.g., 3, 7",
        border_color=colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=TextStyle(font_family="Montserrat"),
    )
    experiences_input = TextField(
        adaptive=True,
        label="Previous Travel Experiences",
        hint_text="e.g., Beach, Mountains",
        border_color=colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=TextStyle(font_family="Montserrat"),
    )
    submit_button = ElevatedButton(
        text="Get Recommendations",
        on_click=on_submit,
        style=ButtonStyle(
            bgcolor=colors.BLUE_GREY_500,
            color=colors.WHITE,
            elevation=4,
            padding=padding.only(top=10, bottom=10, left=20, right=20),
            shape=RoundedRectangleBorder(radius=10),
        ),
    )
    # Retrieve user inputs

    img = Image(
        src=f"https://picsum.photos/200/200",
        width=100,
        height=100,
        fit=ImageFit.CONTAIN,
    )

    recommendations_output = TextField(
        adaptive=True,
        label="Recommendations",
        multiline=True,
        read_only=True,
        height=150,
        border_color=colors.BLUE_GREY_400,
        border_width=2,
        border_radius=10,
        text_style=TextStyle(font_family="Montserrat"),
    )

    _controls = Column(
            [
                Text(
                    value="Welcome to Osogbo Tourism Recommendation System", style="headlineMedium"),
                interests_input,
                budget_input,
                duration_input,
                experiences_input,
                submit_button,
                #recommendations_output,
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll=True
        )

    # Adding controls to the page
    page.add(_controls)


app(target=main, view=AppView.WEB_BROWSER)


