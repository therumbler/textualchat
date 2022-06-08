"""Entrypoint for Chat app"""
from textual.app import App
from rich.panel import Panel
from textual.reactive import Reactive
from textual.widgets import Placeholder
from textual.widget import Widget


class Messages(Widget):
    messages = Reactive([])

    def render(self) -> Panel:
        """Render the Messages Panel"""
        return Panel(f"Messages: {self._message_string()}")

    def _message_string(self):
        return "m: ".join([f"message: {message}" for message in self.messages])


class TextInput(Widget):
    """A TextInput Textual widget"""
    text = Reactive("")

    def render(self) -> Panel:
        """render the TextInput"""
        return Panel(f"[b]text:[/b] {self.text}", style=(""))

    # async def on_key(self, event):
    #     """fires when a key is pressed"""
    #     self._handle_key(event.key)

    # def _handle_key(self, key):
    #     if key == 'ctrl+h':
    #         if len(self.text) > 0:
    #             self.text = self.text[:-1]
    #     elif key == 'enter':
    #         self.text = ""
    #     else:
    #         self.text += str(key)


class ChatApp(App):
    text = ""
    messages = None
    text_input = None

    async def on_mount(self) -> None:
        self.messages = Messages()
        self.text_input = TextInput()
        await self.view.dock(self.messages, size=28, edge="top")
        await self.view.dock(self.text_input, size=4)

    async def on_key(self, event):
        """fires when a key is pressed"""
        self._handle_key(event.key)

    def _handle_key(self, key):
        if key == 'ctrl+h':  # delete
            if len(self.text) > 0:
                self.text = self.text[:-1]
        elif key == 'enter':  # enter
            self.messages.messages.append(self.text)
            self.text = ""

        else:
            self.text += str(key)
        self.text_input.text = self.text


ChatApp.run(log="logs.txt")
