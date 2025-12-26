import arcade
import arcade.gui
from resources import resources

class GameView(arcade.View):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background = resources.backgrounds["cyber_room"]
        
        # Камера
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.camera_target_x = self.window.width / 2
        self.camera_target_y = self.window.height / 2
        self.camera_speed = 0.1  # Скорость следования (0.1 = медленно, 0.5 = быстрее)
        
        # UI-менеджер
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.chat_input = arcade.gui.UITextEntry(x=200, y=50, width=400, height=40, text="",
                                                font_name="VCR OSD Mono", font_size=14,
                                                text_color=arcade.color.WHITE,
                                                background_color=arcade.color.DARK_GRAY)
        self.ui_manager.add(self.chat_input)
        self.chat_messages = []
        self.chat_display = arcade.Text("", 200, 150, arcade.color.WHITE,
                                      font_name="VCR OSD Mono", font_size=14)

    def on_draw(self):
        self.clear()
        # Активируем камеру
        self.camera.use()
        # Рисуем фон с учётом смещения камеры
        arcade.draw_texture_rectangle(self.window.width / 2, self.window.height / 2,
                                    800, 600, self.background)
        # UI рисуем отдельно (без камеры)
        self.window.use()
        self.ui_manager.draw()
        self.chat_display.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        # Обновляем цель камеры на основе позиции мыши
        # Смещаем относительно центра, но ограничиваем (например, ±50 пикселей)
        self.camera_target_x = self.window.width / 2 + (x - self.window.width / 2) * 0.2
        self.camera_target_y = self.window.height / 2 + (y - self.window.height / 2) * 0.2
        # Ограничиваем смещение
        self.camera_target_x = max(350, min(450, self.camera_target_x))
        self.camera_target_y = max(250, min(350, self.camera_target_y))

    def on_update(self, delta_time):
        # Плавное движение камеры к цели (lerp)
        current_x, current_y = self.camera.position
        new_x = current_x + (self.camera_target_x - current_x) * self.camera_speed
        new_y = current_y + (self.camera_target_y - current_y) * self.camera_speed
        self.camera.move_to((new_x, new_y), 1.0)

    def on_mouse_press(self, x, y, button, modifiers):
        self.ui_manager.on_mouse_press(x, y, button, modifiers)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER and self.chat_input.text:
            self.chat_messages.append(f"Hunter: {self.chat_input.text}")
            self.chat_display.text = "\n".join(self.chat_messages[-3:])
            self.chat_input.text = ""
        self.ui_manager.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.ui_manager.on_key_release(key, modifiers)