import flet as ft

def cal_suma(txtnum1,txtnum2,lblResultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        result=num1+num2
        lblResultado.value="resultado:{result}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"

def cal_resta(txtnum1,txtnum2,lblResultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        result=num1-num2
        lblResultado.value="resultado:{result}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"

def cal_mult(txtnum1,txtnum2,lblResultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        result=num1+num2
        lblResultado.value="resultado:{result}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"




def main(page: ft.Page):
    page.title= "Calculadora"
    page.bgcolor="green"
    
    txtnum1=ft.TextField(label="ingresa tu primer numero",color="white")
    txtnum2=ft.TextField(label="ingresa tu segundo numero",color="white")
    lblResultado=ft.Text("Resultado:",color="white")
    
    btnSuma=ft.ElevatedButton(text="+",on_click=on_cal_suma)
    btnResta=ft.ElevatedButton(text="-",onclick=on_cal_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",onclick=on_cal_mult)
    btnDivicion=ft.ElevatedButton(text="/",onclick=on_cal_div)
    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtnum1,
                txtnum2
            ],alignment="center"),
        ]),
            ft.Row(controls=[
                lblResultado
            ],alignment="center"),
            ft.Row(controls=[
                btnSuma,
                btnResta,
                btnMultiplicacion,
                btnDivicion
            ],alignment="center")
            
        
    )
    
    

ft.app(main)
