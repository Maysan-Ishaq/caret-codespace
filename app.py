from textual.app import App, ComposeResult
from textual.containers import Container, Vertical, Horizontal, Right
from textual.reactive import reactive
from textual.widgets import Header, Footer, Input, Static

class Application(App):

    def __init__(self):
        super().__init__()
        self.userInput = ""
        self.discussion = []

    CSS_PATH = "tcss/app.tcss"

    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Container(
                Static("par ici ya un fichier"),
                Static("par ici ya un fichier"),
                Static("par ici ya un fichier"),
                Static("par ici ya un fichier"),
                Static("par ici ya un fichier"),

                classes="explorer"
            ),

            Static(classes="horizontal-separator"),

            Vertical(
                Container(
                    Vertical(

                        Vertical(id="discussion"),

                        Input(placeholder="Ask something..."),
                    ),

                    classes="page"
                ),

                Container(
                    classes="logs"
                ),

                classes="vertical-divider"
            ),

            classes="horizontal-divider"
        )

        yield Footer()

    def on_input_submitted(self, event: Input.Submitted):
        self.userInput = event.value
        if self.userInput.strip():
            container = self.query_one("#discussion", Vertical)

            container.mount(Right(Container(
                Static(self.userInput),
                classes="userMessage"
            )))

            container.mount(Container(
                Static("BOB, bob, BOBY BOB"),
                classes="modelMessage"
            ))

            event.control.value = ""

            container.scroll_end()

if __name__ == "__main__":
    app = Application()
    app.run()