import tkinter as tk


class ScreenHint:
    @staticmethod
    def showCaptureRegion(region: tuple[int, int, int, int]) -> None:

        left, top, width, height = region
        transparent_color = "#010203"
        overlay = tk.Tk()
        overlay.overrideredirect(True)
        overlay.attributes("-topmost", True)
        overlay.wm_attributes("-transparentcolor", transparent_color)
        overlay.configure(bg=transparent_color)
        overlay.geometry(f"{width}x{height}{left:+d}{top:+d}")

        canvas = tk.Canvas(
            overlay,
            bg=transparent_color,
            highlightthickness=0
        )
        canvas.pack(fill="both", expand=True)
        canvas.create_rectangle(
            1, 1, width - 2, height - 2,
            outline="#A0A0A0",
            width=1
        )

        overlay.after(200, overlay.destroy)
        overlay.mainloop()