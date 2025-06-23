from phi.playground import Playground, serve_playground_app
from main import content_creator_system

app = Playground(
    agents=[content_creator_system]
).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
