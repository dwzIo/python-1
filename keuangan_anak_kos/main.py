import flet as ft
from database import DBHelper

def main(page: ft.Page):
    db = DBHelper()
    page.title = " Keuangan Anak Kos"
    page.window_width = 400
    page.window_height = 800
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK

    def refresh_data():
        data = db.get_summary()
        budget_awal, dana_darurat, tabungan = data[1], data[2], data[3]
        
        cursor = db.conn.cursor()
        cursor.execute("SELECT SUM(jumlah) FROM transaksi WHERE tipe='Pengeluaran'")
        res = cursor.fetchone()
        total_exp = res[0] if res[0] else 0
        
        sisa = budget_awal - total_exp
        
        txt_sisa.value = "Rp {:,.0f}".format(sisa)
        txt_tabungan.value = "Rp {:,.0f}".format(tabungan)
        txt_darurat.value = "Rp {:,.0f}".format(dana_darurat)
        page.update()

    def tambah_saldo_proses(e):
        try:
            tipe_aktif = dlg_tambah.data
            if input_pop.value:
                nominal = float(input_pop.value)
                if tipe_aktif == "Budget":
                    db.update_budget(nominal)
                elif tipe_aktif == "Tabungan":
                    db.tambah_tabungan(nominal)
                elif tipe_aktif == "Dana Darurat":
                    db.tambah_darurat(nominal)
                
                input_pop.value = ""
                dlg_tambah.open = False
                refresh_data()
        except:
            pass
        page.update()

    input_pop = ft.TextField(
        label="Masukkan nominal", 
        color="#FFFFFF", 
        border_color="#444444",
        focused_border_color="#FFFF00",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    dlg_tambah = ft.AlertDialog(
        title=ft.Text("Update Saldo"),
        content=input_pop,
        actions=[
            ft.TextButton("Batal", on_click=lambda _: setattr(dlg_tambah, "open", False) or page.update()),
            ft.ElevatedButton("Simpan", on_click=tambah_saldo_proses)
        ]
    )

    def buka_dialog(tipe_nama):
        dlg_tambah.data = tipe_nama
        dlg_tambah.title.value = "Input " + tipe_nama
        page.dialog = dlg_tambah
        dlg_tambah.open = True
        page.update()

    header = ft.Container(
        content=ft.Column([
            ft.Text("SISA BUDGET LO", color="#BBBBBB", size=12, weight="bold"),
            txt_sisa := ft.Text("Rp 0", color="#FFFF00", size=45, weight="bold"),
            ft.ElevatedButton(
                "Atur Budget Bulanan LO", 
                on_click=lambda _: buka_dialog("Budget"),
                style=ft.ButtonStyle(bgcolor="#222222", color="#FFFFFF")
            )
        ], horizontal_alignment="center", spacing=10),
        padding=40,
        bgcolor="#111111",
        border_radius=ft.border_radius.only(bottom_left=40, bottom_right=40),
    )

    txt_tabungan = ft.Text("Rp 0", size=16, weight="bold", color="#FFFFFF")
    txt_darurat = ft.Text("Rp 0", size=16, weight="bold", color="#FFFFFF")

    row_cards = ft.Container(
        margin=ft.margin.only(left=20, right=20, top=-40),
        content=ft.Row([
            ft.Container(
                content=ft.Column([
                    ft.Text("TABUNGAN LO", size=11, weight="bold", color="#AAAAAA"),
                    txt_tabungan,
                    ft.ElevatedButton("Tambah", on_click=lambda _: buka_dialog("Tabungan"), style=ft.ButtonStyle(bgcolor="#333333"))
                ], horizontal_alignment="center", spacing=8),
                bgcolor="#1E1E1E", padding=20, expand=True, border_radius=20, border=ft.border.all(1, "#333333")
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("DANA DARURAT LO", size=11, weight="bold", color="#AAAAAA"),
                    txt_darurat,
                    ft.ElevatedButton("Tambah", on_click=lambda _: buka_dialog("Dana Darurat"), style=ft.ButtonStyle(bgcolor="#333333"))
                ], horizontal_alignment="center", spacing=8),
                bgcolor="#1E1E1E", padding=20, expand=True, border_radius=20, border=ft.border.all(1, "#333333")
            ),
        ], spacing=15)
    )

    txt_jumlah = ft.TextField(
        label="Input Pengeluaran", 
        border_radius=15, 
        bgcolor="#1E1E1E",
        color="#FFFFFF",
        border_color="#444444"
    )

    def simpan_pengeluaran(e):
        if txt_jumlah.value:
            try:
                db.catat_transaksi("Pengeluaran", float(txt_jumlah.value))
                txt_jumlah.value = ""
                refresh_data()
            except:
                pass
            
    page.overlay.append(dlg_tambah)
    
    page.add(
        header,
        row_cards,
        ft.Container(
            padding=35,
            content=ft.Column([
                ft.Text("Catat Transaksi Baru", weight="bold", size=16, color="#FFFFFF"),
                txt_jumlah,
                ft.ElevatedButton(
                    "Simpan Pengeluaran",
                    on_click=simpan_pengeluaran,
                    width=400,
                    height=55,
                    style=ft.ButtonStyle(bgcolor="#FFFF00", color="#000000")
                )
            ], spacing=15)
        )
    )

    refresh_data()

ft.app(target=main)