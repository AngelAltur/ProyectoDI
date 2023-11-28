import flet as ft
from datetime import date

def main(page: ft.Page):
    def book_appointment(e):
        appointments_view.controls.append(ft.Text(f"Cita reservada: {name_field.value} con el Dr. {doctor_choice.value} el {date_picker.value}"))
        view.update()

    name_field = ft.TextField(hint_text="Ingresa tu nombre")
    doctor_choice = ft.Dropdown(options=["Médico A", "Médico B", "Médico C"], hint_text="Selecciona un médico")
    date_picker = ft.DatePicker(min_date=date.today(), hint_text="Selecciona una fecha")
    appointments_view = ft.Column()

    view = ft.Column(
        width=600,
        controls=[
            name_field,
            doctor_choice,
            date_picker,
            ft.Button(text="Reservar cita", on_click=book_appointment),
            appointments_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

ft.app(target=main)